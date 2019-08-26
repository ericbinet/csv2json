#!/usr/bin/env python3

import csv
import sys
import json

reader = csv.reader(sys.stdin)

headers = next(reader)
data = []
for row in reader:
    entry = {}
    for n in range(len(headers)):
        k = headers[n]
        v = row[n]
        if v:
            entry[k] = v
    data.append(entry)

json.dump(data, sys.stdout)
