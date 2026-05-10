from app.models.schemas import ImageAnalysisResult, ReviewAnalysisResult


def test_review_analysis_fallback_values():
    result = ReviewAnalysisResult(
        signature_dishes=[],
        service="Unknown",
        value="Unknown",
        wait_impression="Unknown",
        vibe="Unknown",
        pros=["No review evidence was available."],
        cons=[],
        evidence=[],
    )

    assert result.service == "Unknown"
    assert result.value == "Unknown"
    assert result.wait_impression == "Unknown"
    assert result.vibe == "Unknown"
    assert result.evidence == []
    assert "No review evidence" in result.pros[0]


def test_image_analysis_fallback_values():
    result = ImageAnalysisResult(
        visual_vibe="unknown",
        space_impression="unknown",
        food_visual_cues=[],
        group_suitability="unknown",
        visual_confidence="low",
        image_evidence_summary="No image evidence was available.",
    )

    assert result.visual_vibe == "unknown"
    assert result.space_impression == "unknown"
    assert result.food_visual_cues == []
    assert result.group_suitability == "unknown"
    assert result.visual_confidence == "low"
    assert "No image evidence" in result.image_evidence_summary
