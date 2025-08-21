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


### 1174. Immediate Food Delivery II
    WITH first_orders
        AS (
            SELECT DISTINCT ON (customer_id) customer_id
                ,order_date
                ,customer_pref_delivery_date
            FROM Delivery
            ORDER BY customer_id
                ,order_date
            )
        SELECT round(avg(CASE 
                        WHEN order_date = customer_pref_delivery_date
                            THEN 1
                        ELSE 0
                        END) * 100, 2) AS immediate_percentage
        FROM first_orders;

### 550. Game Play Analysis IV
    WITH FirstLogin
    AS (
	    SELECT player_id
		    ,MIN(event_date) AS first_login_date
    	FROM Activity
	    GROUP BY player_id
    	)
    	,NextLogin
    AS (
	    SELECT f.player_id
    	FROM FirstLogin f
	    JOIN Activity a ON f.player_id = a.player_id
    		AND f.first_login_date + INTERVAL '1 DAY' = a.event_date
    	)
    SELECT ROUND(COUNT(DISTINCT n.player_id)::NUMERIC / (
    			SELECT COUNT(DISTINCT a.player_id)
    			FROM Activity a
    			), 2) AS fraction
    FROM NextLogin n;

### 2356. Number of Unique Subjects Taught by Each Teacher
    SELECT teacher_id, COUNT(DISTINCT subject_id) as cnt
    FROM Teacher
    GROUP BY teacher_id

### 1141. User Activity for the Past 30 Days I
    SELECT activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users  FROM Activity 
    WHERE activity_date BETWEEN '2019-07-27'::DATE - INTERVAL '29 DAYS' AND '2019-07-27'::DATE
    GROUP BY activity_date

### 1070. Product Sales Analysis III
    WITH m AS (
        SELECT product_id, MIN(year) AS min_year
        FROM Sales
        GROUP BY product_id
    )
    SELECT s.product_id, s.year AS first_year, s.quantity, s.price
    FROM Sales s
    JOIN m
    ON s.product_id = m.product_id AND s.year = m.min_year;

### 596. Classes With at Least 5 Students
    SELECT class
    FROM Courses
    GROUP BY class
    HAVING count(student) >= 5

### 1729. Find Followers Count
    SELECT user_id
        ,count(user_id) AS followers_count
    FROM Followers
    GROUP BY user_id
    ORDER BY user_id ASC;