from pathlib import Path


def test_readme_documents_fallback_behavior():
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md should exist."

    content = readme_path.read_text(encoding="utf-8").lower()

    required_phrases = [
        "fallback behavior",
        "no reviews",
        "no photos",
        "gemini review failure",
        "vlm failure",
        "partial google places records",
        "continues processing remaining candidates",
    ]

    for phrase in required_phrases:
        assert phrase in content, f"README is missing fallback documentation: {phrase}"
