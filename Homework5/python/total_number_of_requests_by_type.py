import sys
import json

with open('access.log', 'r') as file:
    data = [x.split()[5][1:] for x in file]
    result = dict([(x, data.count(x)) for x in set(data)])

print(result)
if __name__ == "__main__":
    if "--json" in sys.argv:
        with open('json/result_types.json', 'w') as file:
            json.dump(result, file)
    else:
        with open("result_total_requests_by_type", "w") as file:
            for x in result:
                file.write(f"{x[0]} - {x[1]}\n")
