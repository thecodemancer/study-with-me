-- The Problem: Identify all users who logged into a platform for three or more consecutive days.

-- 1. Create a sample table in your dataset
CREATE OR REPLACE TABLE dataset_for_challenges.user_logins (
  user_id INT64,
  login_date DATE
);

-- 2. Insert sample data showing various login streaks
-- User 101 has a 4-day streak (Jan 1-4)
-- User 102 has broken streaks (no 3 consecutive days)
-- User 103 has a 3-day streak (Jan 2-4)
INSERT INTO dataset_for_challenges.user_logins (user_id, login_date) 
VALUES
  (101, '2026-01-01'), (101, '2026-01-02'), (101, '2026-01-03'), (101, '2026-01-04'), (101, '2026-01-06'),
  (102, '2026-01-01'), (102, '2026-01-03'), (102, '2026-01-04'), (102, '2026-01-06'),
  (103, '2026-01-02'), (103, '2026-01-03'), (103, '2026-01-04');


-- 3. The Gaps & Islands Solution Query
WITH UniqueLogins AS (
  -- Deduplicate logins in case a user logged in multiple times on the same day
  SELECT DISTINCT user_id, login_date 
  FROM dataset_for_challenges.user_logins
),

CalculatedGroups AS (
  SELECT 
    user_id,
    login_date,
    -- Generates a sequence (1, 2, 3...) per user ordered by date
    ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date) as row_num,
    -- The Anchor: Subtracting the row number from the date. 
    -- If dates are consecutive, this date remains identical for the entire streak.
    DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date) DAY) as island_group_id
  FROM UniqueLogins
),

StreakSummaries AS (
  SELECT 
    user_id,
    island_group_id,
    MIN(login_date) as streak_start_date,
    MAX(login_date) as streak_end_date,
    COUNT(*) as streak_length
  FROM CalculatedGroups
  GROUP BY user_id, island_group_id
)

-- Filter for users with a streak of 3 or more consecutive days
SELECT 
  user_id,
  streak_start_date,
  streak_end_date,
  streak_length
FROM StreakSummaries
WHERE streak_length >= 3
ORDER BY user_id, streak_start_date;
