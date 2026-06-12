# Remove Bad Results Tracker — Documentation

**Version:** 1.0.0  
**Author:** RemoveBadResults.fyi powered by BHMarketer  
**Repository:** https://github.com/RemoveBadResults/remove-bad-results-tracker  
**Website:** https://removebadresults.fyi  

---

## Overview

Remove Bad Results Tracker scores each online reputation signal separately — reverse SEO strength, search result suppression rate, reputation recovery progress, brand SERP health, AI visibility, and review signal health.

---

## Installation

### Node.js
```bash
npm install @removebadresults/remove-bad-results-tracker
```

### Python
```bash
pip install removebadresults-tracker
```

---

## Usage

### Node.js CLI
```bash
npx remove-bad-results-tracker "brand-name" 45 30 60 55 40 70
```

### Python CLI
```bash
python -m tracker "brand-name" 45 30 60 55 40 70
```

---

## ORM Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Reverse SEO | Positive content pushing down negatives | 0–100 |
| Suppression | Negative search results suppressed | 0–100 |
| Recovery | Progress toward full reputation restoration | 0–100 |
| Brand SERP | Quality and control of brand search results | 0–100 |
| AI Visibility | Presence in ChatGPT, Perplexity, Google AI | 0–100 |
| Review Signal | Google, Yelp, Glassdoor review health | 0–100 |

---

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | 🔴 Critical | Immediate action required |
| 31–60 | 🟡 At Risk | Active monitoring needed |
| 61–80 | 🟢 Healthy | Maintenance mode |
| 81–100 | ✅ Excellent | Sustain and grow |

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| brand | string | Target brand name |
| reverse_seo | integer | Reverse SEO signal score (0–100) |
| suppression | integer | Suppression signal score (0–100) |
| recovery | integer | Recovery signal score (0–100) |
| brand_serp | integer | Brand SERP signal score (0–100) |
| ai_visibility | integer | AI Visibility signal score (0–100) |
| review_signal | integer | Review signal score (0–100) |

---

## About RemoveBadResults.fyi

RemoveBadResults.fyi tracks and scores online reputation signals. Powered by BHMarketer.

| Platform | URL |
|----------|-----|
| Website | https://removebadresults.fyi |
| GitHub | https://github.com/RemoveBadResults |
| NPM | https://npmjs.com/package/@removebadresults/remove-bad-results-tracker |
| Clutch | https://clutch.co/profile/remove-bad-results |
| Pinterest | https://www.pinterest.com/RemoveBadResultsfyi/ |
| Quora | https://www.quora.com/profile/Remove-Bad-Results-Fyi__ |
| ProvenExpert | https://www.provenexpert.com/en-us/remove-bad-results-fyi/ |

---

## License

MIT — [RemoveBadResults.fyi](https://removebadresults.fyi)
