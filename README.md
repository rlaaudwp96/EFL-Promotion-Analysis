# EFL Championship Promotion and Points Analysis

An end-to-end sports analytics project examining which team-performance metrics are associated with promotion from the English Football League Championship. The workflow combines R, SQL, BigQuery, exploratory data analysis, statistical modeling, and machine learning.

## Highlights

- Analyzed 480 team-season observations across 20 seasons after excluding the incomplete 2024/25 season.
- Cleaned and summarized team points, goals for/against, goal difference, shot accuracy, net shots on target, disciplinary points, and promotion status.
- Investigated a bimodal shot-accuracy distribution caused by changes in historical data-collection criteria.
- Compared linear relationships between team points and six performance indicators using regression and visual diagnostics.
- Built logistic-regression and random-forest workflows to model promotion status and inspect variable importance.

## Repository Contents

- `EFL_Final.qmd` - Main Quarto analysis and statistical report.
- `ML_efl.qmd` - Machine-learning workflow for promotion classification.
- `efl_table_final_clean.csv` - Cleaned team-season analysis table.
- `EFL.ipynb` - Notebook version of the project workflow.
- `EFL_Final.html` / `EFL_Final.pdf` - Rendered report outputs.

## Tools

R, tidyverse, tidymodels, ggplot2, broom, BigQuery SQL, DBI, bigrquery, randomForest, Quarto, and Jupyter.

## Reproducibility

The main report imports a summary table from BigQuery and also reads the included cleaned CSV for local analysis. To reproduce the cloud-import section, configure a BigQuery project and dataset with the required credentials, then update the project identifiers in `EFL_Final.qmd`.
