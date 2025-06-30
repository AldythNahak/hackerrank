#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json

#
# Complete the 'getAverageTemperatureForUser' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/medical_records?userId=<userId>&page=<page>
#
# The function is expected to return a String value.
# The function accepts a userId argumnent (Integer).
# In the case of an empty array result, return value '0'
#

def getAverageTemperatureForUser(userId):
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    page = 1
    temperatures = []

    while True:
        url = f"{base_url}?userId={userId}&page={page}"
        res = requests.get(url)
        data = res.json()
        
        # print(data)
        
        records = data.get('data', [])
        for record in records:
            temp = record.get('vitals', {}).get('bodyTemperature')
            if temp is not None:
                temperatures.append(temp)

        if page >= data.get('total_pages', 0):
            break
        page += 1

    if not temperatures:
        return '0'

    avg_temp = sum(temperatures) / len(temperatures)
    return f"{avg_temp:.1f}"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # userId = int(input().strip())

    # result = getAverageTemperatureForUser(userId)

    # fptr.write(result + '\n')

    # fptr.close()
    
    print(getAverageTemperatureForUser(1))
