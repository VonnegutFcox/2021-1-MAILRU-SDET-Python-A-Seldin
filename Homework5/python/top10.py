with open("access.log", 'r') as f:
    a = [x.split()[6] for x in f]
    d = sorted([(x, a.count(x)) for x in set(a)], reverse=True, key=lambda i: i[1])[:10]

with open("result_top10", "w") as f:
    for x in d:
        f.write(str(x[0]) + " " + str(x[1]) + "\n")
