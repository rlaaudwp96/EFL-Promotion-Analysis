-- BigQuery SQL: summarize team performance and promotion outcomes.
-- Replace `project.dataset.efl_table` with your BigQuery table.

SELECT
  Season,
  Team,
  Total_Points,
  GF,
  GA,
  GD,
  Shot_Accuracy,
  Net_SOT,
  Card_Points,
  Promoted
FROM `project.dataset.efl_table`
WHERE SAFE_CAST(SUBSTR(Season, 1, 4) AS INT64) BETWEEN 2005 AND 2023
  AND Season != '2024/25'
ORDER BY Season, Total_Points DESC;

SELECT
  Season,
  COUNT(*) AS team_seasons,
  AVG(Total_Points) AS avg_points,
  AVG(GD) AS avg_goal_difference,
  COUNTIF(Promoted = 'Yes') AS promoted_teams
FROM `project.dataset.efl_table`
WHERE SAFE_CAST(SUBSTR(Season, 1, 4) AS INT64) BETWEEN 2005 AND 2023
GROUP BY Season
ORDER BY Season;
