dct = {}
#n = 'anything'

while True:
    n = input()
    if n == "STOP":
        break
    if n in dct:
        dct[n] += 1
    else:
        dct[n] = 1

for i in dct:
    print(i, "-", dct[i], "times")