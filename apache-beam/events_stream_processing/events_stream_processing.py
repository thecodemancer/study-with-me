import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from google.cloud import pubsub_v1, bigquery
from google.cloud.bigquery import SchemaField
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Constants
PROJECT_ID = os.getenv("YOUR_PROJECT_ID")
TOPIC_ID = os.getenv("YOUR_TOPIC_ID")
SUBSCRIPTION_ID = os.getenv("YOUR_SUBSCRIPTION_ID")
DATASET_ID = os.getenv("YOUR_DATASET_ID", "event_data")
TABLE_ID = os.getenv("YOUR_TABLE_ID", "events")

# Define BigQuery schema
BIGQUERY_SCHEMA = {
    "fields": [
        {"name": "event_type", "type": "STRING", "mode": "REQUIRED"},
        {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
        {"name": "user_id", "type": "STRING", "mode": "REQUIRED"},
        {"name": "product_id", "type": "STRING", "mode": "NULLABLE"},
        {"name": "amount", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "level", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "score", "type": "INTEGER", "mode": "NULLABLE"},
    ]
}

def create_subscription_if_not_exists(project_id, topic_id, subscription_id):
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = f"projects/{project_id}/topics/{topic_id}"
    subscription_path = f"projects/{project_id}/subscriptions/{subscription_id}"

    try:
        subscriber.get_subscription(request={"subscription": subscription_path})
        print(f"Subscription '{subscription_id}' already exists.")
    except Exception:
        print(f"Subscription '{subscription_id}' not found. Creating it...")
        subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )
        print(f"Subscription '{subscription_id}' created.")

    return subscription_path

def create_bq_table_if_not_exists():
    client = bigquery.Client()
    dataset_ref = client.dataset(DATASET_ID)
    table_ref = dataset_ref.table(TABLE_ID)

    try:
        dataset = client.get_dataset(dataset_ref)
        print(f"Dataset '{DATASET_ID}' already exists.")
    except Exception:
        print(f"Dataset '{DATASET_ID}' not found. Creating it...")
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        client.create_dataset(dataset)
        print(f"Dataset '{DATASET_ID}' created.")

    try:
        table = client.get_table(table_ref)
        print(f"Table '{TABLE_ID}' already exists.")
    except Exception:
        print(f"Table '{TABLE_ID}' not found. Creating it...")
        schema = [SchemaField(**field) for field in BIGQUERY_SCHEMA["fields"]]
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        print(f"Table '{TABLE_ID}' created.")

def run():
    subscription_path = create_subscription_if_not_exists(PROJECT_ID, TOPIC_ID, SUBSCRIPTION_ID)
    create_bq_table_if_not_exists()

    # Define Apache Beam pipeline options
    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True

    # BigQuery table spec
    table_spec = f"{PROJECT_ID}:{DATASET_ID}.{TABLE_ID}"

    # Create the pipeline
    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | "Read from PubSub" >> beam.io.ReadFromPubSub(subscription=subscription_path)
            | "Decode Messages" >> beam.Map(lambda msg: json.loads(msg.decode("utf-8")))
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                table_spec,
                schema=BIGQUERY_SCHEMA,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            )
        )

if __name__ == "__main__":
    run()
