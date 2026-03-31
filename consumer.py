import json
from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)

consumer.subscribe(['orders'])

print("📡 Listening for messages...")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"❌ Error: {msg.error()}")
        continue

    data = json.loads(msg.value().decode('utf-8'))
    print(f"📦 Received Order: {data}")