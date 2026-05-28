DECLARE i INT64;
DECLARE s STRING;
DECLARE count INT64;
DECLARE table_list ARRAY<STRING>;

SET count = 2;
SET table_list = ["incidents_2008", "incidents_2011"];

SET i = 0;
SET s = "";

WHILE i < count DO
  SET s = s || "SELECT * FROM `bigquery-public-data.austin_incidents." || table_list[OFFSET(i)] || "`";
  IF NOT i = count - 1 THEN
    SET s = s || " UNION ALL ";
  END IF;
  SET i = i + 1;
END WHILE;

SELECT s; -- to check query generated

EXECUTE IMMEDIATE s; -- run query generated
