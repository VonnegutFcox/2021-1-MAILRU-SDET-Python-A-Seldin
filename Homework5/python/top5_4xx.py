import re
import json
import sys

with open("access.log", 'r') as file:
    data = [
        i.split()
        for i in file if re.search(r'4\d\d', i.split()[8])
    ]
    sorted_data = sorted(
        [(i[6], i[8], int(i[9]), i[0]) for i in data],
        key=lambda x: x[2],
        reverse=True)[:5]

if __name__ == "__main__":
    if "--json" in sys.argv:
        data = {'requests:': [dict(
            {
                'url': i[0],
                'status-code': i[1],
                'request-size': i[2],
                'IP': i[3]
             }
        ) for i in sorted_data]}
        with open('json/result_top5_5xx.json', 'w') as f:
            json.dump(data, f)
    else:
        with open("result_top5_5xx", "w") as f:
            for i in sorted_data:
                f.write(f"url:{i[0]}\tstatus-code:{i[1]}\trequest-size:{i[2]}\tIP:{i[3]}\n")


