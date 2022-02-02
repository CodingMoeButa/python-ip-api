#!/usr/bin/python3
import requests
import json

def batch(ippool):
    r = requests.post("http://ip-api.com/batch?fields=21098202", data=json.dumps(ippool))
    # print(r.text)
    return json.loads(r.text)