# Call Gemini-Pro from BigQuery

Our goal is to avoid the use of notebooks in our project.

```sql
DECLARE PROJECT_ID STRING;
DECLARE DATASET_NAME STRING;
DECLARE INPUT_TABLE STRING;
DECLARE MODEL_NAME STRING;
DECLARE CONNECTION_URI STRING;
DECLARE CONNECTION_ID STRING;
DECLARE MODEL_ENDPOINT STRING;
SET PROJECT_ID = "[REPLACE_WITH_YOUR_PROJECT_ID]";
SET DATASET_NAME = "[REPLACE_WITH_YOUR_DATASET_NAME]";
SET INPUT_TABLE = "[REPLACE_WITH_YOUR_INPUT_TABLE]";
SET MODEL_NAME = "[REPLACE_WITH_YOUR_MODEL_NAME]";
SET CONNECTION_ID = "[REPLACE_WITH_YOUR_CONNECTION_ID";
SET MODEL_ENDPOINT = "gemini-pro";

--CREATE MODEL USING THE REMOTE CONNECTION
EXECUTE IMMEDIATE format("""
  CREATE MODEL IF NOT EXISTS `%s.%s.%s` 
  REMOTE WITH CONNECTION `%s` 
  OPTIONS(ENDPOINT = '%s')
""", PROJECT_ID, DATASET_NAME, MODEL_NAME, CONNECTION_ID, MODEL_ENDPOINT);

--CREATE A PROMPT TABLE
EXECUTE IMMEDIATE format ("""
  CREATE TABLE IF NOT EXISTS `%s.%s.%s` (
      prompt STRING
  );
""", PROJECT_ID, DATASET_NAME, INPUT_TABLE);

--INSERT DATA
EXECUTE IMMEDIATE format ("INSERT INTO `%s.%s.%s` VALUES('What is the purpose of dreams?')", PROJECT_ID, DATASET_NAME, INPUT_TABLE);
EXECUTE IMMEDIATE format ("INSERT INTO `%s.%s.%s` VALUES('What is the distance from Earth to the Moon?')", PROJECT_ID, DATASET_NAME, INPUT_TABLE);
EXECUTE IMMEDIATE format ("INSERT INTO `%s.%s.%s` VALUES('How long does it take the light to arrive from the Sun to platnet Earth?')", PROJECT_ID, DATASET_NAME, INPUT_TABLE);
EXECUTE IMMEDIATE format ("INSERT INTO `%s.%s.%s` VALUES('Who was Jimi Hendrix?')", PROJECT_ID, DATASET_NAME, INPUT_TABLE);
EXECUTE IMMEDIATE format ("INSERT INTO `%s.%s.%s` VALUES('Lista a los actores de la película Matrix')", PROJECT_ID, DATASET_NAME, INPUT_TABLE);

--CALL THE MODEL BY READING THE PROMPT TABLE
EXECUTE IMMEDIATE format("""
  SELECT *
  FROM
    ML.GENERATE_TEXT(
      MODEL `%s.%s.%s`,
      (SELECT prompt FROM `e%s.%s.%s`),
      STRUCT(
        0.8 AS temperature,
        1024 AS max_output_tokens,
        0.95 AS top_p,
        40 AS top_k));
  """, PROJECT_ID, DATASET_NAME, MODEL_NAME, PROJECT_ID, DATASET_NAME, INPUT_TABLE);
```

## Troubleshooting

###Error: 
Query error: bqcx-[PROJECT_NUMBER]-[4_RANDOM_DIGITS]@gcp-sa-bigquery-condel.iam.gserviceaccount.com does not have the permission to access resources used by ML.GENERATE_TEXT. Please follow https://cloud.google.com/bigquery/docs/generate-text-tutorial#grant-permissions to set up permissions. If issue persists, contact bqml-feedback@google.com for help. at [2:3]

###Solution: 
Go to `IAM` --> `GRANT ACCESS`. Then, in `Add Principals` enter the `bqcx-[PROJECT_NUMBER]-[4_RANDOM_DIGITS]@gcp-sa-bigquery-condel.iam.gserviceaccount.com` and then select the `Vertex AI User` role.

## Further reading

https://cloud.google.com/bigquery/docs/generate-text-tutorial#grant-permissions



