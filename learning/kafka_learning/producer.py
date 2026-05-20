from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    data = {'item': 'soap', 'quantity': 1, 'price': 5.99}
    producer.send('soap-sales', value=data)
    print("Sent soap sale to Kafka")
    time.sleep(2) # Send one every 2 seconds