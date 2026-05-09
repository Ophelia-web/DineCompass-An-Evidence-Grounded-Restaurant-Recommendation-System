# GenAI Prompt Log

This file records exact prompts used for final-stage GenAI-assisted review and refinement for **DineCompass: An Evidence-Grounded Restaurant Recommendation System**.

Early exploratory GenAI interactions were not fully retained. To avoid fabricating exact prompts, those uses are disclosed generally in `docs/AI_USAGE.md`. The prompts below were used for final-stage review, debugging support, prompt refinement, documentation editing, and presentation preparation.

---

## Prompt 1: Review Analysis Prompt Refinement

**Tool**: ChatGPT  
**Model / Settings**: ChatGPT web interface, default settings  
**Purpose**: Review the existing review-analysis prompt for clarity and structured output reliability.

**Exact prompt used**:

We are building DineCompass, an evidence-grounded restaurant recommendation system. The system retrieves restaurant candidates from Google Places, selects relevant review snippets, and uses Gemini to extract structured dining signals.

Please review the following existing prompt file for clarity, consistency, and JSON-output reliability. Do not redesign the whole system. Only suggest minimal wording improvements that make the prompt more stable and easier for the model to follow.

**File**: app/prompts/review_prompt.txt


**How the output was used**:
The response was used as a prompt-review reference. The team manually reviewed the suggestions and only adopted changes that improved clarity, output consistency, or evidence grounding.

**Files affected**:

- app/prompts/review_prompt.txt
- app/services/review_analyzer.py

## Prompt 2: Image Analysis Prompt Refinement

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review the existing image-analysis prompt for clarity and reduced hallucination.

**Exact prompt used**:

We are building DineCompass, a restaurant recommendation system that uses Gemini VLM to analyze restaurant photos for visual cues such as ambience, space suitability, food presentation, and confidence.

Please review the following existing image-analysis prompt. Suggest minimal edits to improve clarity and reduce hallucination. Keep the output structure close to the current version and do not add unnecessary fields.

**File**: app/prompts/image_prompt.txt

**How the output was used**:
The response was used to improve the clarity of the image-analysis prompt. The team reviewed the suggestions and kept the prompt focused on observable visual evidence rather than unsupported assumptions.

**Files affected**:

- app/prompts/image_prompt.txt
- app/services/image_analyzer.py

## Prompt 3: Dossier Prompt Refinement

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review the restaurant dossier-generation prompt for clarity and evidence-grounded wording.

**Exact prompt used**:

We are building DineCompass, an evidence-grounded restaurant recommendation system. The system creates a restaurant dossier using structured review analysis, visual cues when available, and basic restaurant metadata.

Please review the following existing dossier-generation prompt for clarity, consistency, and evidence-grounded wording. Do not redesign the output format. Only suggest minimal improvements that make the final recommendation summary more accurate and less likely to overstate evidence.

**File**: app/prompts/dossier_prompt.txt

**How the output was used**:
The response was used as a reference for improving dossier wording. The team manually checked whether suggested changes were consistent with the implemented data fields and final UI.

**Files affected**:

- app/prompts/dossier_prompt.txt
- app/services/dossier_generator.py

## Prompt 4: Rule-Based Ranking Code Review

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review the existing rule-based ranking module for readability, edge cases, and presentation explainability.

**Exact prompt used**:

We already implemented a rule-based ranking module for DineCompass. Please review the following code for readability, possible edge cases, and whether the scoring logic is easy to explain in a class presentation.

Do not replace it with a machine learning model. Do not rewrite the whole file. Only suggest small refactoring ideas, clearer variable names, and possible safeguards.

**File**: app/services/ranker.py

**How the output was used**:
The response was used as a code-review reference. The team manually reviewed the suggestions and only adopted minor readability or safeguard changes where appropriate. The ranking logic remained rule-based and interpretable.

**Files affected**:

- app/services/ranker.py

## Prompt 5: FastAPI Search Route Review

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review the search endpoint for bugs, error handling, and response-structure clarity.

**Exact prompt used**:

We are reviewing the FastAPI route for the DineCompass search endpoint. The route receives user inputs such as ZIP code, cuisine, party size, and budget, then calls the recommendation pipeline.

Please check the following code for obvious bugs, error-handling issues, and response-structure clarity. Do not generate a new backend. Only provide targeted comments and minimal code suggestions.

**File**: app/routes/search.py

**How the output was used**:
The response was used to identify potential error-handling and response-format issues. The team checked all suggestions against the existing backend implementation before making any changes.

**Files affected**:

- app/routes/search.py
- app/main.py
- app/models/schemas.py

## Prompt 6: Frontend Layout Review

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review frontend files for readability and class-demo presentation quality.

**Exact prompt used**:

We already have a working frontend for DineCompass. It displays Top-3 restaurant recommendation cards with review evidence, visual cues, score breakdown, and links.

Please review the following HTML/CSS/JavaScript for layout clarity and presentation quality. Do not redesign the full interface. Suggest only small improvements that make the result cards easier to read in a class demo.

**Files**:
- app/templates/index.html
- app/static/styles.css
- app/static/app.js

**How the output was used**:
The response was used as a UI review reference. The team manually selected minor layout and wording improvements to make the demo clearer.

**Files affected**:

- app/templates/index.html
- app/static/styles.css
- app/static/app.js

## Prompt 7: README Review

**Tool**: ChatGPT
**Model / Settings**: ChatGPT web interface, default settings
**Purpose**: Review README wording for accuracy, conciseness, and consistency with the implemented system.

**Exact prompt used**:

Please review the following README section for DineCompass. The goal is to make the project description accurate, concise, and consistent with the actual implementation.

Do not make exaggerated claims. Do not describe the system as fully production-ready. Keep the language suitable for an academic course project.

**How the output was used**:
The response was used to revise README wording. The team checked that the final README accurately described the implemented pipeline, limitations, and deployment status.

**Files affected**:

- README.md
