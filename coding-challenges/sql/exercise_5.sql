-- 1. Create a sample orders table
CREATE OR REPLACE TABLE dataset_for_challenges.orders (
  order_id INT64,
  customer_id INT64,
  order_date DATE,
  amount DECIMAL(10, 2)
);

-- 2. Insert sample data for a single customer (Customer 88)
-- Note: Order 3 and Order 4 occur on the EXACT SAME DAY (2026-04-03).
INSERT INTO dataset_for_challenges.orders (order_id, customer_id, order_date, amount) VALUES
(1, 88, '2026-04-01', 100.00), -- Cum Total: 100.00
(2, 88, '2026-04-02', 150.00), -- Cum Total: 250.00
(3, 88, '2026-04-03', 50.00),  -- Same day, Order A -> Cum Total: 300.00
(4, 88, '2026-04-03', 200.00), -- Same day, Order B -> Cum Total: 500.00
(5, 88, '2026-04-05', 75.00);  -- Cum Total: 575.00


-- 3. The Cumulative Revenue Solution Query
SELECT 
  customer_id,
  order_date,
  order_id,
  amount,
  
  -- Explicitly defining the row-based boundary prevents unintended bundling of identical dates.
  SUM(amount) OVER (
    PARTITION BY customer_id 
    ORDER BY order_date, order_id  -- Best Practice: Adding order_id guarantees a deterministic order
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_spent_rows,

FROM dataset_for_challenges.orders
ORDER BY customer_id, order_date, order_id;
