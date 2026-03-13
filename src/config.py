class Config:
    KAFKA_SERVER = 'localhost:9092'
    TOPIC_TRUCK_DATA = 'truck_telemetry'
    TOPIC_ALERTS = 'delivery_alerts'

    PRODUCER_CONF = {
        'bootstrap.servers': KAFKA_SERVER,
        'acks': 'all'
    }
    
    
    CONSUMER_CONF = {
        'bootstrap.servers': KAFKA_SERVER,
        'group.id': 'monitoring_group',
        'auto.offset.reset': 'earliest'
    }
    
    
CLIENTS = {
    "C_001": {"name": "Fatma", "lat": 30.0131, "long": 31.2089, "target_package": "PKG_99"},
    "C_002": {"name": "Nour", "lat": 65.0131, "long": 378.2071, "target_package": "PKG_98"},
    "C_003": {"name": "Ahmed", "lat": 78.0131, "long": 458.2071, "target_package": "PKG_110"},
    "C_004": {"name": "Kareem", "lat": 55.0131, "long": 588.2071, "target_package": "PKG_78"}
}