```text
youtube-content-intelligence-pipeline-and-analytics/
│
├── jobs/
│   ├── daily_pipeline.py
│   └── reference_pipeline.py
│
├── notebooks/
│   ├── 00_setup_infrastructure.ipynb
│   │
│   ├── bronze/
│   │   ├── creator_daily_stats.ipynb
│   │   ├── creators.ipynb
│   │   ├── video_category.ipynb
│   │   ├── video_daily_stats.ipynb
│   │   └── videos.ipynb
│   │
│   └── silver/
│       ├── creator_daily_stats.ipynb
│       ├── creators.ipynb
│       ├── video_category.ipynb
│       ├── video_daily_stats.ipynb
│       └── videos.ipynb
│
├── src/
│   ├── youtube_client.py
│   │
│   └── extraction/
│       ├── creator_daily_stats.py
│       ├── creators.py
│       ├── video_category.py
│       ├── video_daily_stats.py
│       └── videos.py
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   │
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   ├── tests/
│   └── dbt_project.yml
│
├── requirements.txt
├── README.md
└── repo_structure.md
```













