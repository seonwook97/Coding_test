SELECT
    a.company_code,
    a.founder,
    COUNT(DISTINCT b.lead_manager_code),
    COUNT(DISTINCT c.senior_manager_code),
    COUNT(DISTINCT d.manager_code),
    COUNT(DISTINCT e.employee_code)
FROM
    company a
LEFT JOIN
    lead_manager b ON a.company_code = b.company_code
LEFT JOIN
        senior_manager c ON b.lead_manager_code = c.lead_manager_code
LEFT JOIN
        manager d ON c.senior_manager_code = d.senior_manager_code
LEFT JOIN
        employee e ON d.manager_code = e.manager_code
GROUP BY
    1, 2
ORDER BY
    1