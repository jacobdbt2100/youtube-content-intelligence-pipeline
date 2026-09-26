# YouTube Content Intelligence Pipeline & Analytics

An incremental data pipeline for collecting, transforming, and analyzing YouTube creator and content data.
___

## Architecture

### Data engineering layer

```text
Python
  ↓
API extraction
  ↓
Raw files
  ↓
Bronze
  ↓
PySpark
  ↓
Silver
```

### Analytics engineering / analytical modeling layer

```text
Silver
  ↓
dbt + SQL
  ↓
stg models
  ↓
int models
  ↓
Gold marts
```

**Repo 2**

## YouTube Content Intelligence App

```text
Gold data
   ↓
Plotly interactive visualizations
   ↓
Streamlit app / interactive dashboard
   ↓
Streamlit Community Cloud hosting / deployment
```

## Modelling

- What questions should this project answer?
- What metrics/KPIs answer those questions?
- Which metrics can we reliably calculate from our current data?
- What additional data, if any, would be needed?
- Define the Gold models around those metrics
- Then build the dbt staging → intermediate → marts layer.
- Finally, the visualization becomes largely a matter of presenting the already-defined analytical outputs.














