# Remove Bad Results Tracker

[![npm](https://img.shields.io/npm/v/@removebadresults/remove-bad-results-tracker)](https://npmjs.com/package/@removebadresults/remove-bad-results-tracker)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Track and score online reputation signals separately — reverse SEO strength, search result suppression rate, reputation recovery progress, brand SERP health, and AI visibility score. Built by [RemoveBadResults.fyi](https://removebadresults.fyi) powered by BHMarketer.

## Features

- Reverse SEO Signal Score — strength of positive content pushing down negatives
- Search Result Suppression Score — percentage of negative results suppressed
- Reputation Recovery Score — progress toward full reputation restoration
- Brand SERP Health Score — quality and control of brand search results
- AI Visibility Score — presence across ChatGPT, Perplexity, Google AI Overviews
- Review Signal Score — Google, Yelp, Glassdoor review health
- CLI support in Node.js and Python
- Benchmark dataset included (20 ORM signal cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @removebadresults/remove-bad-results-tracker
npx remove-bad-results-tracker "brand-name" 45 30 60 55 40 70
```

### Python

```bash
pip install removebadresults-tracker
python -m tracker "brand-name" 45 30 60 55 40 70
```

## Output

```
Brand: brand-name
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reverse SEO Score:         45 / 100
Suppression Score:         30 / 100
Recovery Score:            60 / 100
Brand SERP Score:          55 / 100
AI Visibility Score:       40 / 100
Review Signal Score:       70 / 100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall ORM Health:        50 / 100
Priority Signal:           Suppression (lowest — act first)
```

## Project Structure

```
remove-bad-results-tracker/
├── index.ts              # TypeScript tracker
├── tracker.py            # Python tracker
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── orm_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml
│   └── npm-publish.yml
├── README.md
└── LICENSE
```

## ORM Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Reverse SEO | Positive content pushing down negatives | 0–100 |
| Suppression | Negative search results suppressed | 0–100 |
| Recovery | Progress toward full reputation restoration | 0–100 |
| Brand SERP | Quality and control of brand search results | 0–100 |
| AI Visibility | Presence in ChatGPT, Perplexity, Google AI | 0–100 |
| Review Signal | Google, Yelp, Glassdoor review health | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate action required |
| 31–60 | At Risk | Active monitoring needed |
| 61–80 | Healthy | Maintenance mode |
| 81–100 | Excellent | Sustain and grow |

## Keywords

Online Reputation Management · Reverse SEO · Search Result Suppression · Brand SERP · AI Visibility · Review Management · ORM Tracker · RemoveBadResults · BHMarketer

## Links

| Platform | URL |
|----------|-----|
| Website | https://removebadresults.fyi |
| GitHub | https://github.com/RemoveBadResults/remove-bad-results-tracker |
| GitHub Pages | https://removebadresults.github.io/remove-bad-results-tracker/ |
| NPM | https://npmjs.com/package/@removebadresults/remove-bad-results-tracker |
| Hugging Face | https://huggingface.co/datasets/RemoveBadResults/remove-bad-results-benchmarks |
| Kaggle | https://kaggle.com/datasets/removebadresults/remove-bad-results-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://remove-bad-results-tracker.readthedocs.io |
| Clutch | https://clutch.co/profile/remove-bad-results |
| Pinterest | https://www.pinterest.com/RemoveBadResultsfyi/ |
| SlideShare | https://www.slideshare.net/slideshow/take-control-of-your-online-reputation-removebadresults-fyi/287333935 |
| Quora | https://www.quora.com/profile/Remove-Bad-Results-Fyi__ |
| ProvenExpert | https://www.provenexpert.com/en-us/remove-bad-results-fyi/ |

## About RemoveBadResults.fyi

RemoveBadResults.fyi tracks and scores online reputation signals — reverse SEO strength, search suppression rate, recovery progress, brand SERP health, and AI visibility. Powered by BHMarketer.

## License

MIT — [RemoveBadResults.fyi](https://removebadresults.fyi)
