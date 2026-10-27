# EFL Championship Promotion Analysis

Python and SQL analysis of the team-performance factors associated with promotion from the English Football League Championship.

An end-to-end sports analytics project examining which team-performance metrics are associated with promotion. The workflow uses pandas, scikit-learn, SQL/BigQuery, exploratory analysis, statistical modeling, and machine learning.

## Highlights

- Analyzed 480 team-season observations across 20 seasons after excluding the incomplete 2024/25 season.
- Cleaned and summarized team points, goals for/against, goal difference, shot accuracy, net shots on target, disciplinary points, and promotion status.
- Investigated a bimodal shot-accuracy distribution caused by changes in historical data-collection criteria.
- Compared linear relationships between team points and six performance indicators using regression and visual diagnostics.
- Built logistic-regression and random-forest workflows to model promotion status and inspect variable importance.

## Repository Contents

- `efl_analysis.py` - Reproducible Python analysis with logistic regression, random forest, and regression.
- `efl_table_final_clean.csv` - Cleaned team-season analysis table.
- `requirements.txt` - Python dependencies.
- `sql/promotion_analysis.sql` - BigQuery SQL for team-season summaries.

## Python Workflow

```bash
pip install -r requirements.txt
python efl_analysis.py
```

## Tools

Python, pandas, scikit-learn, BigQuery SQL, and Jupyter.

## Reproducibility

The Python analysis uses the included cleaned CSV. The SQL file is ready to adapt to a BigQuery table by replacing the project and dataset identifier.
