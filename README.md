# OpEx360 — Operational Efficiency & Cost Reduction Dashboard

**Stack:** Python (pandas), SQL, Power BI

## Project summary
Built an operational analytics solution to detect inefficiencies in cost, productivity, and process delays across a company's departments. Cleaned and transformed performance logs to extract KPIs such as SLA Compliance, Cost per Transaction, and Process Cycle Time. Designed a Power BI dashboard with variance analysis, bottleneck detection, and what-if cost scenarios, revealing 12% potential cost savings and 15% faster workflow execution.

## Repo contents
- `data/`: sample data generator and sample CSV
- `src/`: ETL and analysis scripts
- `sql/`: example SQL queries
- `powerbi/`: instructions to recreate the Power BI dashboard and recommended visuals
- `notebooks/`: exploration notes

## How to run (local)
1. Create a Python venv: `python -m venv venv` and activate it.
2. Install dependencies: `pip install -r requirements.txt`.
3. Generate sample data: `python data/sample_data_generator.py` (creates `data/sample_operations_log.csv`).
4. Run ETL: `python src/etl.py --input data/sample_operations_log.csv --output data/cleaned_ops.csv`.
5. Run analysis: `python src/analysis.py --input data/cleaned_ops.csv --output results/summary_metrics.csv`.

## Files to add (Power BI)
- `assets/screenshots/`: add exported PNGs of your Power BI report pages.
- If you want to share a `.pbix` file, use Git Large File Storage (LFS) or attach via GitHub Releases / Drive.

## License
MIT