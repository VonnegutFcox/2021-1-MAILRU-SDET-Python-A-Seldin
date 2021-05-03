import re

with open('./access.log', 'r') as file:
    content = file.read()
    result = {}
    for i in ['GET', 'POST', 'HEAD', 'DELETE', 'PUT', 'OPTIONS', 'CONNECT']:
        match_pattern = re.findall(rf'{i}', content)
        lineCount = re.split("\n", content)
        result[i] = len(match_pattern)

with open("result_total_requests_by_type", "w") as file:
    for x in result.items():
        file.write(str(x[0]) + " - " + str(x[1]) + "\n")
