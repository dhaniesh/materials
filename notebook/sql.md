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

### 1211. Queries Quality and Percentage
    SELECT 
        q.query_name,
        ROUND(AVG(rating::decimal / position), 2) AS quality,
        ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
    FROM Queries q
    GROUP BY q.query_name;

### 1193. Monthly Transactions I
    SELECT TO_CHAR(trans_date,'YYYY-MM') AS month,
            country,
            COUNT(id) AS trans_count,
            SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) AS approved_count,
            SUM(amount) AS trans_total_amount,
            SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS approved_total_amount
    FROM Transactions
    GROUP BY month, country