-- The Problem: Group consecutive user event logs into discrete sessions, where a session ends if there is an inactivity gap of 30 minutes or more.
-- 1. Create a sample web events table
CREATE OR REPLACE TABLE dataset_for_challenges.web_events (
  user_id INT64,
  event_timestamp TIMESTAMP,
  event_name STRING
);

-- 2. Insert sample data for a single user (User 505)
-- Session 1: 3 rapid events (10:00, 10:15, 10:20)
-- Gap of 45 minutes -> Session 2 starts at 11:05 (10:20 to 11:05 is > 30 mins)
-- Gap of 10 minutes -> Session 2 continues at 11:15
-- Gap of 35 minutes -> Session 3 starts at 11:50 (11:15 to 11:50 is > 30 mins)
INSERT INTO dataset_for_challenges.web_events (user_id, event_timestamp, event_name) VALUES
(505, '2026-03-01 10:00:00 UTC', 'page_view'),
(505, '2026-03-01 10:15:00 UTC', 'click'),
(505, '2026-03-01 10:20:00 UTC', 'add_to_cart'),
(505, '2026-03-01 11:05:00 UTC', 'page_view'),   -- New Session (45 min gap)
(505, '2026-03-01 11:15:00 UTC', 'purchase'),
(505, '2026-03-01 11:50:00 UTC', 'page_view');   -- New Session (35 min gap)


-- 3. The Sessionization Solution Query
WITH FlaggedEvents AS (
  SELECT 
    user_id,
    event_timestamp,
    event_name,
    -- Step 1: Look backward to get the timestamp of the user's previous action
    LAG(event_timestamp) OVER(PARTITION BY user_id ORDER BY event_timestamp) as prev_timestamp
  FROM dataset_for_challenges.web_events
),

SessionStarts AS (
  SELECT *,
    -- Step 2: Calculate the gap in minutes. 
    -- If it's the user's first event (prev_timestamp IS NULL) OR gap >= 30, flag it as a new session start (1)
    CASE 
      WHEN prev_timestamp IS NULL THEN 1
      WHEN TIMESTAMP_DIFF(event_timestamp, prev_timestamp, MINUTE) >= 30 THEN 1
      ELSE 0 
    END as is_new_session
  FROM FlaggedEvents
)

-- Step 3: Use a running sum over the binary flags to generate sequential session numbers
SELECT 
  user_id,
  event_timestamp,
  event_name,
  TIMESTAMP_DIFF(event_timestamp, prev_timestamp, MINUTE) as mins_since_last_event,
  -- Generating the unique session identifier per user
  SUM(is_new_session) OVER(
    PARTITION BY user_id 
    ORDER BY event_timestamp 
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) as session_id
FROM SessionStarts
ORDER BY user_id, event_timestamp;
