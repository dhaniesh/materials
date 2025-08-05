### 1075. Project Employees I
    SELECT project_id,
        round(avg(e.experience_years), 2) AS average_years
    FROM Project p
    JOIN Employee e ON p.employee_id = e.employee_id
    GROUP BY p.project_id

### 1633. Percentage of Users Attended a Contest
    SELECT r.contest_id
        ,ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (
                SELECT COUNT(*)
                FROM Users
                ), 2) AS percentage
    FROM Register r
    GROUP BY r.contest_id
    ORDER BY percentage DESC
        ,r.contest_id ASC;