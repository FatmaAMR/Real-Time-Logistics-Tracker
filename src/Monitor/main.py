import json
from confluent_kafka import Consumer, KafkaError
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.config import Config

def start_consumer():
    consumer = Consumer(Config.CONSUMER_CONF)
    consumer.subscribe([Config.TOPIC_TRUCK_DATA])
    print("Starting Monitor Service...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                    continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break
            
            truck_id = msg.key().decode('utf-8')
            data = json.loads(msg.value().decode('utf-8'))
            
            if truck_id == "TRUCK_01":
                    print(f"MONITOR {truck_id} | Lat: {data['lat']} | Lon: {data['lon']} | Speed: {data['speed']} km/h | Time: {data['timestamp']}")
    except KeyboardInterrupt:
        print("Monitor Stoped...")
    finally:
            consumer.close()
        
        
if __name__ == "__main__":
    start_consumer()