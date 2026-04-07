from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer('soap-sales', 
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

data_list = []

for message in consumer:
    data_list.append(message.value)
    # Save to Excel/CSV every 5 sales
    if len(data_list) % 5 == 0:
        pd.DataFrame(data_list).to_csv('local_excel_data.csv', index=False)
        print("Updated Excel file with 5 new rows!")