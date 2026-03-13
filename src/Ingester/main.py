import json
from confluent_kafka import Producer
from simulator import move_truck
import sys
import time
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.config import Config

producer = Producer(Config.PRODUCER_CONF)

def delivery_report(err, msg):
    if err: print(f"Message failed: {err}")
    else: print(f"Truck {msg.key().decode('utf-8')} status sent to Partition {msg.partition()}")

# start point and destination
current_pos = {"lat": 30.0444, "lon": 31.2357}
destination = {"lat": 30.0131, "lon": 31.2089}
truck_id = "TRUCK_01"

print("Starting Ingestor Service...")
try:
    while True:
        current_pos = move_truck(truck_id, current_pos, destination)
        
        producer.produce(
            topic=Config.TOPIC_TRUCK_DATA,
            key=truck_id,
            value=json.dumps(current_pos).encode('utf-8'), 
            #Dictionary -> JSON String -> UTF-8 Bytes 
            #This is called Serialization
            callback=delivery_report
        )
        
        producer.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Ingestor stopped.")