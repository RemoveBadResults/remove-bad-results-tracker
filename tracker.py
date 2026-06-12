#!/usr/bin/env python3
"""
Remove Bad Results Tracker
Track and score online reputation signals separately — reverse SEO strength,
search result suppression rate, reputation recovery progress, brand SERP health,
and AI visibility score.
https://removebadresults.fyi
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_signal(scores: dict) -> str:
    labels = {
        "reverse_seo": "Reverse SEO",
        "suppression": "Suppression",
        "recovery": "Recovery",
        "brand_serp": "Brand SERP",
        "ai_visibility": "AI Visibility",
        "review_signal": "Review Signal",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 - act first)"


def track_orm(
    brand: str,
    reverse_seo: int = 45,
    suppression: int = 30,
    recovery: int = 60,
    brand_serp: int = 55,
    ai_visibility: int = 40,
    review_signal: int = 70,
) -> dict:
    """
    Track and score each ORM signal separately.

    Args:
        brand: Target brand name
        reverse_seo: Reverse SEO signal score (0-100)
        suppression: Suppression signal score (0-100)
        recovery: Recovery signal score (0-100)
        brand_serp: Brand SERP signal score (0-100)
        ai_visibility: AI Visibility signal score (0-100)
        review_signal: Review signal score (0-100)

    Returns:
        dict with individual signal scores and overall ORM health
    """
    scores = {
        "reverse_seo": reverse_seo,
        "suppression": suppression,
        "recovery": recovery,
        "brand_serp": brand_serp,
        "ai_visibility": ai_visibility,
        "review_signal": review_signal,
    }
    overall_orm_health = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "reverse_seo_score": reverse_seo,
        "suppression_score": suppression,
        "recovery_score": recovery,
        "brand_serp_score": brand_serp,
        "ai_visibility_score": ai_visibility,
        "review_signal_score": review_signal,
        "overall_orm_health": overall_orm_health,
        "priority_signal": get_priority_signal(scores),
    }


if __name__ == "__main__":
    brand = sys.argv[1] if len(sys.argv) > 1 else "brand-name"
    reverse_seo = int(sys.argv[2]) if len(sys.argv) > 2 else 45
    suppression = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    recovery = int(sys.argv[4]) if len(sys.argv) > 4 else 60
    brand_serp = int(sys.argv[5]) if len(sys.argv) > 5 else 55
    ai_visibility = int(sys.argv[6]) if len(sys.argv) > 6 else 40
    review_signal = int(sys.argv[7]) if len(sys.argv) > 7 else 70

    result = track_orm(brand, reverse_seo, suppression, recovery, brand_serp, ai_visibility, review_signal)

    print(f"Brand: {result['brand']}")
    print("=" * 40)
    print(f"Reverse SEO Score:     {result['reverse_seo_score']}/100  [{get_status(result['reverse_seo_score'])}]")
    print(f"Suppression Score:     {result['suppression_score']}/100  [{get_status(result['suppression_score'])}]")
    print(f"Recovery Score:        {result['recovery_score']}/100  [{get_status(result['recovery_score'])}]")
    print(f"Brand SERP Score:      {result['brand_serp_score']}/100  [{get_status(result['brand_serp_score'])}]")
    print(f"AI Visibility Score:   {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Review Signal Score:   {result['review_signal_score']}/100  [{get_status(result['review_signal_score'])}]")
    print("=" * 40)
    print(f"Overall ORM Health:    {result['overall_orm_health']}/100")
    print(f"Priority Signal:       {result['priority_signal']}")
