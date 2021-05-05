import sys
import json

result = sum(1 for line in open('access.log', 'r'))

if __name__ == "__main__":

    if "--json" in sys.argv:
        data = {'count:': result}
        with open('json/result_top5_count_urls.json', 'w') as f:
            json.dump(data, f)
    else:
        with open("result_total_requests", "w") as file:
            file.write(f'Общее количество запросов - {result}\n')

