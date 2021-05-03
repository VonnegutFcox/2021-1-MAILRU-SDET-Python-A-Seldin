result = sum(1 for line in open('./access.log', 'r'))

with open("result_total_requests", "w") as file:
    file.write(f'Общее количество запросов - {result}\n')

