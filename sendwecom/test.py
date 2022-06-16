import json


with open('wecom.json', 'r') as f:
    data = json.load(f)

print(data['wecom_cid'])