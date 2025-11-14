-- SLA breach rate per department
SELECT department,
       COUNT(*) AS total_transactions,
       SUM(CASE WHEN duration_seconds > sla_target_seconds THEN 1 ELSE 0 END) AS breaches,
       SUM(CASE WHEN duration_seconds > sla_target_seconds THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS breach_rate
FROM operations_log
GROUP BY department
ORDER BY breach_rate DESC;

-- Cost per transaction by process step
SELECT process_step,
       AVG(cost) AS avg_cost
FROM operations_log
GROUP BY process_step
ORDER BY avg_cost DESC;