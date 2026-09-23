# YouTube Content Intelligence Pipeline
An incremental data pipeline for collecting, transforming, and analyzing YouTube creator and content data.
___


## Architecture

```text
                 DATA ENGINEERING
                       │
YouTube API ──→ Volume ──→ Bronze
                            │
                            ↓
                         Silver
                            │
                            ↓
                       ┌─────────┐
                       │   dbt   │
                       └─────────┘
                            │
                     staging models
                            ↓
                  intermediate models
                            ↓
                       Gold marts
                            │
                            ↓
                    Dashboard / Analysis
```











