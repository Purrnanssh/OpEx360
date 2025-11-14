# OpEx360 — Operational Efficiency & Cost Reduction Dashboard

**Stack:** Python (pandas) · SQL · Power BI

---

## TL;DR
OpEx360 is an end-to-end operational analytics solution that processes raw operations logs, extracts KPI metrics (SLA compliance, cost per transaction, cycle time), and visualizes them in an interactive Power BI dashboard to reveal cost-saving and efficiency opportunities. In example data, the analysis surfaced **~12% potential cost savings** and **~15% faster workflow execution** through process improvements and what-if scenarios.

---

## Why this project
Operational teams produce large volumes of event logs but often lack a consistent, data-driven process to measure bottlenecks and quantify cost impact. OpEx360 fills that gap by:
- converting raw logs into actionable KPIs,
- detecting process bottlenecks and SLA breaches,
- enabling scenario analysis to evaluate cost reduction strategies.

---

## Highlights / Outcomes
- Cleaned and transformed operations logs into a single canonical dataset.  
- Key KPIs: SLA Compliance, Cost per Transaction, Cycle Time, Cost per Second.  
- Dashboard features: KPI summary, trend analysis, department × step heatmap, bottleneck detection, what-if cost scenarios.  
- Example result: identification of ~12% cost savings opportunity and ~15% faster execution by addressing top bottlenecks.

---

## Repo structure
```
OpEx360/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   ├── sample_data_generator.py
│   └── sample_operations_log.csv (generated)
├── src/
│   ├── etl.py
│   ├── transformations.py
│   └── analysis.py
├── sql/
│   └── queries.sql
└── assets/
    └── screenshots/
```

---

## Data schema (sample_operations_log.csv)
| column | type | description |
|--------|------|-------------|
| timestamp | datetime | event timestamp |
| department | text | department name (Finance, HR, ...) |
| process_step | text | step in the process (Receive, Validate, ...) |
| transaction_id | text | unique transaction id |
| cost | float | cost attributed to transaction |
| duration_seconds | int | time taken for that step |
| sla_target_seconds | int | SLA target time for that step |
| status | text | OK / BREACH |

---

## How it works (high level)
1. **Generate / Ingest data** — sample CSV or live DB.  
2. **ETL (src/etl.py)** — load raw logs, standardize columns, compute KPIs.  
3. **Analysis (src/analysis.py)** — produce department and process summaries and scenario outputs.  
4. **Visualize (Power BI)** — interactive reports: KPIs, heatmaps, time series, what-if parameters.

---

## Quickstart — run locally (macOS / Linux)

### 1. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. Generate sample data  
```bash
python3 data/sample_data_generator.py
```

### 4. Run ETL  
```bash
python3 src/etl.py --input data/sample_operations_log.csv --output data/cleaned_ops.csv
```

### 5. Run summary analysis  
```bash
python3 src/analysis.py --input data/cleaned_ops.csv --output results/summary_metrics.csv
```

---

## Power BI Notes
- Connect to `data/cleaned_ops.csv` (or SQL query output).  
- Recommended visuals:
  - KPI cards: total cost, transactions, SLA compliance %, avg cycle time.  
  - Line chart: cycle time or cost over time.  
  - Heatmap: department × process_step.  
  - Table: SLA breaches.  
  - Parameter-driven What-If scenario for cost reduction.

---

## Key files explained
- `data/sample_data_generator.py` — creates synthetic operations dataset.  
- `src/etl.py` — loads, cleans, and computes KPIs.  
- `src/transformations.py` — all transformation logic.  
- `src/analysis.py` — summary metrics for dashboard.  
- `sql/queries.sql` — SQL for SLA and cost analysis.  
- `assets/screenshots/` — dashboard images (optional).

---

## License
MIT — see `LICENSE`.

---

## Author
Purrnanssh — Computer Science student  
Contact: prrnnssh@gmail.com
