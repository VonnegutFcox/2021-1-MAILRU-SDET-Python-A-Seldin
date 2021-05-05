import re
import sys
import json

with open("access.log", 'r') as f:
    b = [x.split() for x in f]
    a = [x[0] for x in b if re.match(r'5\d\d', x[8])]
    result = sorted([(x, a.count(x)) for x in set(a)],
                    reverse=True, key=lambda i: i[1])[:5]

if __name__ == "__main__":
    if "--json" in sys.argv:
        data = {'requests:': [dict(
            {
                'IP': i[0],
                'count': i[1]
            }
        ) for i in result]}
        with open('json/result_top5_5xx.json', 'w') as f:
            json.dump(data, f)
    else:
        with open("result_top5_5xx", "w") as f:
            for i in result:
                f.write(f"IP:{i[0]}\tcount:{i[1]}\n")
