import random
random_numbers = [random.randint(1, 200000) for _ in range(100000)]
f = open("E:\\YFY\\YDAT\\src\\input.in", "w")
f.write(" ".join(map(str, random_numbers)))
f.write(" -1")
f.close()