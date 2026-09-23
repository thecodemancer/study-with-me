--The Problem: A loading bug created duplicate trades in a table. Delete all duplicates but keep only the row with the highest volume for each ticker on a specific date.

-- 1. Create a sample table with duplicate trades
CREATE OR REPLACE TABLE dataset_for_challenges.trades (
    trade_date DATE,
    ticker STRING,
    volume INT64,
    trader STRING
);

-- 2. Insert sample data showing duplicate entries for the same ticker and date
-- On 2026-01-15, AAPL has three rows. We only want to keep the one with 5000 volume.
-- On 2026-01-15, GOOG has two rows. We only want to keep the one with 3000 volume.
INSERT INTO dataset_for_challenges.trades (trade_date, ticker, volume, trader) VALUES
('2026-01-15', 'AAPL', 1500, 'Trader_A'),
('2026-01-15', 'AAPL', 5000, 'Trader_B'), -- <-- KEEP (Highest Volume)
('2026-01-15', 'AAPL', 1500, 'Trader_A'), -- Exact duplicate
('2026-01-15', 'GOOG', 3000, 'Trader_C'), -- <-- KEEP (Highest Volume)
('2026-01-15', 'GOOG', 1200, 'Trader_A');


-- 3. The Deduplication Solution using MERGE (The most efficient way in BigQuery)
MERGE dataset_for_challenges.trades T
USING (
  SELECT 
    trade_date, 
    ticker, 
    volume, 
    trader,
    -- Partition by what makes a row "unique", order by what determines the "winner"
    ROW_NUMBER() OVER(PARTITION BY trade_date, ticker ORDER BY volume DESC) as row_num
  FROM dataset_for_challenges.trades
) S
-- We match rows based on all attributes to pinpoint the duplicates
ON T.trade_date = S.trade_date 
   AND T.ticker = S.ticker 
   AND T.volume = S.volume 
   AND T.trader = S.trader
-- If the row number is greater than 1, it's a duplicate. Delete it!
WHEN MATCHED AND S.row_num > 1 THEN
  DELETE;


-- 4. Check the results (Should only return 2 rows total)
SELECT * FROM dataset_for_challenges.trades;
