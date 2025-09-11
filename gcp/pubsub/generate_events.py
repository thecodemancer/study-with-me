import random
import time
from datetime import datetime
import pytz
from google.cloud import pubsub_v1
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
TIMEZONE = "America/Lima"
NUM_EVENTS = 5

def create_topic_if_not_exists(publisher, project_id, topic_id):
    topic_path = f"projects/{project_id}/topics/{topic_id}"
    try:
        publisher.get_topic(request={"topic": topic_path})
        print(f"Topic '{topic_id}' already exists.")
    except Exception as e:
        print(f"Topic '{topic_id}' not found. Creating it...")
        publisher.create_topic(request={"name": topic_path})
        print(f"Topic '{topic_id}' created.")
    return topic_path

def publish_event(event, topic_path, publisher):
    future = publisher.publish(topic_path, json.dumps(event).encode("utf-8"))
    print(f"Published event: {event}, message ID: {future.result()}")

def generate_user_event():
    user_events = [
        "screen_view", "user_engagement", "session_start", "first_visit", "app_update"
    ]
    return {
        "event_type": random.choice(user_events),
        "timestamp": datetime.now(pytz.timezone(TIMEZONE)).isoformat(),
        "user_id": f"user_{random.randint(1000, 9999)}"
    }

def generate_ecommerce_event():
    ecommerce_events = [
        "purchase", "add_to_cart", "view_item", "generate_lead"
    ]
    return {
        "event_type": random.choice(ecommerce_events),
        "timestamp": datetime.now(pytz.timezone(TIMEZONE)).isoformat(),
        "user_id": f"user_{random.randint(1000, 9999)}",
        "product_id": f"product_{random.randint(100, 999)}",
        "amount": round(random.uniform(10.0, 500.0), 2)
    }

def generate_game_event():
    game_events = [
        "level_start", "level_end", "tutorial_complete", "post_score"
    ]
    return {
        "event_type": random.choice(game_events),
        "timestamp": datetime.now(pytz.timezone(TIMEZONE)).isoformat(),
        "user_id": f"user_{random.randint(1000, 9999)}",
        "level": random.randint(1, 50),
        "score": random.randint(0, 10000)
    }

if __name__ == "__main__":
    publisher = pubsub_v1.PublisherClient()
    project_id = os.getenv("YOUR_PROJECT_ID")
    topic_id = os.getenv("YOUR_TOPIC_ID")

    print(project_id)
    print(topic_id)
    topic_path = create_topic_if_not_exists(publisher, project_id, topic_id)

    for _ in range(NUM_EVENTS):
        publish_event(generate_user_event(), topic_path, publisher)
        publish_event(generate_ecommerce_event(), topic_path, publisher)
        publish_event(generate_game_event(), topic_path, publisher)
        print("-" * 200)
        time.sleep(1)
