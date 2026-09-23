--The Problem: Write a query to identify the Nth highest distinct employee salary.

-- 1. Create a sample employees table
CREATE TABLE dataset_for_challenges.employees (
    employee_id INT INTEGER,
    employee_name STRING,
    department STRING,
    salary DECIMAL(10, 2)
);

-- 2. Insert sample data (including duplicate salaries to show how ties are handled)
INSERT INTO dataset_for_challenges.employees (employee_id, employee_name, department, salary) VALUES
(1, 'Alice', 'Engineering', 120000.00), -- 1st highest
(2, 'Bob', 'Engineering', 120000.00),   -- 1st highest (tied)
(3, 'Charlie', 'Marketing', 110000.00), -- 2nd highest
(4, 'David', 'Sales', 95000.00),       -- 3rd highest
(5, 'Eve', 'Engineering', 95000.00),    -- 3rd highest (tied)
(6, 'Frank', 'Marketing', 80000.00);    -- 4th highest

-- 3. Query to find the Nth highest salary (e.g., N = 3)
-- Change the '3' in the WHERE clause to find any Nth salary level.
WITH RankedSalaries AS (
    SELECT 
        employee_id,
        employee_name,
        department,
        salary,
        -- DENSE_RANK() ensures unique salary tiers are ranked sequentially (1, 2, 3...)
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM 
        dataset_for_challenges.employees
)
SELECT 
    employee_id,
    employee_name,
    department,
    salary,
    salary_rank
FROM 
    RankedSalaries
WHERE 
    salary_rank = 3; -- <-- Replace 3 with your variable 'N'
