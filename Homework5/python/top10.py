import sys
import json

with open("access.log", 'r') as f:
    data = [x.split()[6] for x in f]
    sorted_data = sorted([(x, data.count(x)) for x in set(data)],
                         reverse=True, key=lambda i: i[1])[:10]


if __name__ == "__main__":
    if "--json" in sys.argv:
        data = {'requests:': [dict(
            {
                'url': i[0],
                'count': i[1]
            }
        ) for i in sorted_data]}
        with open('json/result_top10.json', 'w') as f:
            json.dump(data, f)
    else:
        with open("result_top10", "w") as f:
            for x in sorted_data:
                f.write(str(x[0]) + " " + str(x[1]) + "\n")
