# Generative AI Usage

This document discloses the use of Generative AI tools in the development of **DineCompass: An Evidence-Grounded Restaurant Recommendation System**, in accordance with the course GenAI transparency policy.

## Tools Used

| Tool | Purpose | Notes |
|---|---|---|
| Gemini API | Used in the application to analyze restaurant reviews, analyze restaurant photos, and generate structured restaurant dossiers. | The prompts used by the application are stored in `app/prompts/`. |
| ChatGPT | Used as a development assistant for code review, debugging support, prompt refinement, documentation editing, and presentation preparation. | ChatGPT suggestions were reviewed and modified by the team before being used. |

## Application Prompts

The application uses manually written and revised prompts stored in:

- `app/prompts/review_prompt.txt`
- `app/prompts/image_prompt.txt`
- `app/prompts/dossier_prompt.txt`

These prompts are part of the implemented DineCompass system. They guide Gemini to extract structured review signals, visual cues, and evidence-grounded restaurant summaries.

## Development Assistance

ChatGPT was used for selected support tasks, including:

- reviewing existing code for readability and possible edge cases;
- debugging API and response-format issues;
- improving prompt clarity and output stability;
- refining README and report wording;
- improving presentation explanations;
- suggesting minor frontend layout improvements.

ChatGPT was not used to replace the team’s project work. The team made the final decisions on system design, pipeline structure, module integration, ranking logic, testing, and presentation.

## Human Contributions

The student team was responsible for:

- defining the project problem and scope;
- designing the end-to-end recommendation pipeline;
- implementing and integrating the FastAPI backend;
- connecting Google Places retrieval, review analysis, image analysis, dossier generation, and ranking modules;
- designing the lightweight review evidence retrieval step;
- implementing the rule-based ranking logic and score breakdown;
- building and testing the frontend interface;
- preparing the final report, slides, and demo.

## Prompt Record

Exact prompts used for final-stage GenAI-assisted review and refinement are recorded in:

- `docs/GENAI_PROMPTS.md`

Some early exploratory GenAI interactions were informal and were not fully retained. To avoid fabricating exact prompts, we disclose those uses generally in this file and provide exact final-stage prompts in `GENAI_PROMPTS.md`.

## Use of GenAI Output

GenAI outputs were treated as suggestions, not final answers. The team reviewed, edited, tested, and integrated changes manually. Some suggestions were rejected or simplified when they were inconsistent with the project scope or implementation.
