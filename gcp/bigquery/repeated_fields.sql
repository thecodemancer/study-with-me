-- Create table
CREATE OR REPLACE TABLE demo.demo_repeated_fields (
    waktu_transaksi TIMESTAMP,
    id_transaksi STRING,
    nama_pembeli STRING,
    nama_barang ARRAY<STRING>
);

-- Insert sample data
INSERT demo.demo_repeated_fields (
    waktu_transaksi,
    id_transaksi,
    nama_pembeli,
    nama_barang
)
VALUES (TIMESTAMP("2021-01-01 10:00:00"), "1234", "Ujang", ["Ultramilk Coklat", "Kacang Atom Garuda"]),
    (TIMESTAMP("2021-01-01 11:00:00"), "1235", "Asep", ["Roti Coklat", "Ultramilk Coklat"]),
    (TIMESTAMP("2021-01-01 12:00:00"), "1236", "Kokom", ["Aqua Botol"]);

-- Fungsi2 array
SELECT *,
    ARRAY_LENGTH(nama_barang) AS qty,
    nama_barang[SAFE_OFFSET(1)] AS barang_pertama
    -- SAFE_OFFSET kalau elemen 0 tidak ada, TIDAK error dan hanya mengembalikan NULL
FROM demo.demo_repeated_fields;

-- Flatten array
SELECT
    * EXCEPT(nama_barang)
FROM demo.demo_repeated_fields,
    UNNEST(nama_barang) AS nama_barang_flatten;

-- Un-flatten array
WITH
hasil_flatten AS (
    SELECT
        * EXCEPT(nama_barang)
    FROM demo.demo_repeated_fields,
        UNNEST(nama_barang) AS nama_barang_flatten
)
SELECT
    waktu_transaksi,
    id_transaksi,
    nama_pembeli,
    ARRAY_AGG(nama_barang_flatten) AS nama_barang
FROM hasil_flatten
GROUP BY 1, 2, 3;

-- Filtering array pakai unnest
SELECT *,
    ARRAY(
        SELECT nb
        FROM UNNEST(nama_barang) AS nb
        WHERE STRPOS(nb, "Coklat") > 0
    ) AS rasa_coklat
    -- diquery biasa pake UNNEST di FROM clause
    -- terus dimasukin fungsi ARRAY
FROM demo.demo_repeated_fields;
