# -*- coding: utf-8 -*-
import json
import requests
import os

URL = "https://notify-api.line.me/api/notify";

def lambda_handler(event, context):
    deviceid = event['detail']['DeviceId'];
    line_token = os.environ['LINE_TOKEN']
    headers = {"Content-Type": "application/x-www-form-urlencoded","Authorization": "Bearer %s" % line_token};
    lon = event['detail']['Position'][0];
    lat = event['detail']['Position'][1];
    eventType = event['detail']['EventType'];
    
    message = "%s、いってらっしゃい！" % deviceid;
    
    if eventType == "ENTER":
        message = "%s、おかえりなさい！" % deviceid;
        
    data = {"message": message.encode("utf-8")}

    x=requests.post(URL, headers=headers, data=data);
    
    print(event);
    print(x.text);
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }