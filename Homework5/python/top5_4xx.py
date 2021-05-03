import re

with open("./access.log", 'r') as file:
    data = [
        i.split()
        for i in file if re.search(r'4\d\d', i.split()[8])
    ]
    sorted_data = sorted(
        [(i[6], i[8], int(i[9]), i[0]) for i in data],
        key=lambda x: x[2],
        reverse=True)[:5]

with open("result_top5_5xx", "w") as f:
    for i in sorted_data:
        f.write(f"url:{i[0]}\tstatus-code:{i[1]}\trequest-size:{i[2]}\tIP:{i[3]}")
