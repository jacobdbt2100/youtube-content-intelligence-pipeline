# YouTube Content Intelligence Pipeline
An incremental data pipeline for collecting, transforming, and analyzing YouTube creator and content data.
___







## Repository Structure

```text
youtube-content-intelligence-pipeline/
│
├── .gitignore
├── README.md
├── jobs/
│   ├── daily_pipeline.py
│   └── reference_pipeline.py
│
├── notebooks/
│
├── requirements.txt
│
└── src/
    ├── extraction/
    │   ├── __init__.py
    │   ├── creator_daily_stats.py
    │   ├── creators.py
    │   ├── video_category.py
    │   ├── video_daily_stats.py
    │   ├── videos.py
    │   └── youtube_client.py
    │
    └── ingestion/
        └── ...
```

## Volume

```text
Volumes/
└── youtube_content_intelligence/
    │
    ├── creator_daily_stats/
    │   └── incoming/
    │
    ├── creators/
    │   └── incoming/
    │
    ├── video_category/
    │   └── incoming/
    │
    ├── video_daily_stats/
    │   └── incoming/
    │
    └── videos/
        └── incoming/
```











