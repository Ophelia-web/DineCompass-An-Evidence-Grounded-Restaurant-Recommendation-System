# DineCompass: An Evidence-Grounded Restaurant Recommendation System

A runnable LLM + RAG + VLM demo that accepts dining preferences and returns transparent Top-3 recommendations with evidence.

## LLM + RAG + VLM Pipeline

1. **Google Places retrieval** finds nearby candidates with ratings, reviews, photos, and metadata.
2. **Lightweight review RAG** turns each review into an evidence chunk and retrieves the most relevant snippets using keyword overlap (no vector DB).
3. **Gemini review analysis** analyzes only retrieved review evidence and produces strict JSON.
4. **Gemini VLM image analysis** analyzes restaurant photos with multimodal prompting.
5. **Dossier generation** merges place metadata + review evidence + image evidence into a structured recommendation dossier.
6. **Rule-based ranking** scores candidates with an explicit score breakdown and returns Top-3 results.

## Folder tree

```text
app/
  main.py
  models/
    schemas.py
  prompts/
    dossier_prompt.txt
    image_prompt.txt
    review_prompt.txt
  routes/
    search.py
  services/
    dossier_generator.py
    geocode_zip.py
    image_analyzer.py
    llm_client.py
    photo_fetcher.py
    places_retriever.py
    ranker.py
    report_writer.py
    review_analyzer.py
    review_rag.py
  static/
    app.js
    styles.css
  templates/
    index.html

scripts/
  test_vlm_image.py

tests/
  test_api_health.py
  test_models_fallback.py
  test_error_handling_readme.py

user_study/
  Restaurant Recommendation Web App Feedback Survey (Responses).xlsx
  Stat 5293 survey analyze.ipynb

docs/
  AI_USAGE.md
  GENAI_PROMPTS.md

README.md
requirements.txt
5293 DineCompass - report.pdf
stat5293demo.mp4
```

## Installation

```bash
cd project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## API keys

The app accepts API keys from the browser form and sends them with each search request.

- `googleMapsApiKey`: used for Google Places retrieval and photo URL generation
- `geminiApiKey`: used for Gemini text and multimodal analysis

The backend uses these keys only during request processing. The response does not return the keys.

## Run locally

```bash
cd project
uvicorn app.main:app --reload --port 8000
```

Open: `http://localhost:8000`

Health check: `GET /health`

## Request/response shape

### Request (`POST /api/search`)

```json
{
  "googleMapsApiKey": "YOUR_GOOGLE_MAPS_API_KEY",
  "geminiApiKey": "YOUR_GEMINI_API_KEY",
  "zipCode": "94103",
  "cuisine": "japanese",
  "partySize": 4,
  "budget": "medium"
}
```

> API keys are supplied through the browser form and sent with each request.
> They are used for API calls only and are not included in the backend response.

### Response (truncated)

```json
{
  "query": {
    "zipCode": "94103",
    "cuisine": "japanese",
    "partySize": 4,
    "budget": "medium"
  },
  "total_candidates": 10,
  "top_results": [
    {
      "score": {
        "cuisine_match": 30,
        "budget_match": 20,
        "rating": 18,
        "review_value_match": 10,
        "vibe_fit": 7,
        "visual_vibe_fit": 8,
        "evidence_quality": 10,
        "wait_penalty": -4,
        "total": 79
      },
      "dossier": {
        "restaurant_name": "Example Restaurant",
        "rating": 4.5,
        "price_level": 2,
        "address": "123 Example St",
        "signature_dishes": ["ramen", "karaage"],
        "service": "Friendly and attentive.",
        "value": "Good portions for the price.",
        "wait_impression": "Moderate waits during peak hours.",
        "vibe": "Casual and energetic.",
        "photo_urls": ["https://maps.googleapis.com/maps/api/place/photo?..."],
        "review_evidence": [
          {
            "text": "Great service and cozy seating for small groups.",
            "rating": 5,
            "author_name": "Alex",
            "relative_time_description": "3 months ago",
            "source": "Google Places review",
            "matched_terms": ["service", "cozy", "groups"]
          }
        ],
        "image_analysis": {
          "visual_vibe": "casual and cozy",
          "space_impression": "small but comfortable",
          "food_visual_cues": ["simple plating"],
          "group_suitability": "better for small groups",
          "visual_confidence": "medium",
          "image_evidence_summary": "Photos show close table spacing and casual decor."
        },
        "reservable": true,
        "reservation_link": "https://maps.google.com/?cid=...",
        "why_recommended": "Matches your cuisine and budget with strong ratings."
      }
    }
  ],
  "notes": ["..."]
}
```

## API limitations

- Google Places results depend on location density, API quota, and detail availability.
- Review evidence retrieval is lexical keyword overlap, so semantic misses are possible.
- Gemini outputs may vary by model availability and provider-side behavior.
- Image analysis quality depends on photo quality and whether photo URLs are retrievable.

## Fallback behavior

The app is built to continue gracefully:

- no reviews -> empty review evidence + `Unknown` review analysis fields
- no photos -> empty `photo_urls`, image-analysis fallback values
- Gemini review failure on one candidate -> fallback analysis for that candidate
- VLM failure on one candidate -> fallback image analysis for that candidate
- partial Google Places records -> best-effort normalized place metadata

If one candidate fails during module processing, the route continues processing remaining candidates and still returns valid JSON.

## Isolated VLM test helper

Use the helper script to validate image analysis on one image before a full search run:

```bash
cd project
python3 scripts/test_vlm_image.py \
  --gemini-key "YOUR_GEMINI_API_KEY" \
  --name "Test Restaurant" \
  --cuisine "japanese" \
  --image-url "https://maps.googleapis.com/maps/api/place/photo?..."
```

What it does:
- logs image fetch status and content type
- sends the image as Gemini `inline_data` (base64)
- prints parsed JSON output from VLM analysis

## Demo

1. Enter ZIP, cuisine, party size, and budget.
2. Show that results include evidence-backed rationale, not only ratings.
3. Open **Review RAG Evidence** to show retrieved snippets.
4. Open **VLM Image Analysis** to show visual cues and confidence.
5. Open **Score Breakdown** to explain transparent ranking logic.
6. Mention fallback behavior for missing reviews/photos and module failures.

<video width="600" controls>
  <source src="stat5293_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Troubleshooting Guide

### 1. The app starts but search returns no restaurants
Possible causes:
- The Google Maps API key is missing or invalid.
- The ZIP code has limited restaurant results.
- The Google Places API quota has been exceeded.

Suggested fix:
- Check that the Google Maps API key is active.
- Try a dense ZIP code such as `10018`, `10025`, or `10027`.
- Check Google Cloud API quota and billing settings.

### 2. Gemini returns an invalid or unexpected format
Possible causes:
- Gemini model output may vary.
- The response may not follow the expected JSON structure.

Suggested fix:
- The app uses fallback values when Gemini output cannot be parsed.
- Check the prompt files in `app/prompts/`.
- Re-run the same query or try a simpler cuisine/preference input.

### 3. No review evidence appears
Possible causes:
- Google Places returned few or no reviews.
- The lightweight RAG step did not find strong keyword matches.

Suggested fix:
- Try another restaurant-dense ZIP code.
- Use broader cuisine terms such as `Italian`, `Korean`, or `Japanese`.

### 4. No image analysis appears
Possible causes:
- The restaurant has no available photos.
- The photo URL could not be retrieved.
- Gemini VLM request failed.

Suggested fix:
- The app will continue with fallback image-analysis values.
- Use `scripts/test_vlm_image.py` to test one image URL separately.

### 5. Tests do not run
Suggested fix:
Run from the root project folder:

```bash
pip install -r requirements.txt
pytest -v

## Notes

- Async `httpx` calls are used for external APIs.
- LLM calls are centralized in `services/llm_client.py`.
- Prompts are versioned in `app/prompts/`.
- The pipeline is modular for easy extension (vector retrieval, deeper ranking rules, etc.).
