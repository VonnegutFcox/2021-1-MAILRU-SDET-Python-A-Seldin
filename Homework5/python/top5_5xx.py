import re

with open("access.log", 'r') as f:
    b = [x.split() for x in f]
    a = [x[0] for x in b if re.match(r'5\d\d', x[8])]
    result = sorted([(x, a.count(x)) for x in set(a)], reverse=True, key=lambda i: i[1])[:5]

with open("result_top5_5xx", "w") as f:
    for i in result:
        f.write(str(i[0]) + " " + str(i[1]) + "\n")
