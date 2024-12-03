import re
with open("input3", "r") as f:
    corrupted_input = f.read()
corrupted_input2 = re.sub(r"don't\(\).*?do\(\)", "abrakadabra", corrupted_input, flags=re.DOTALL)
corrupted_input3 = corrupted_input2.split("mul(")
result = 0
for i in corrupted_input3:
    j = i.split(")")[0]
    j = j.split(",")
    if len(j) < 3:
        try:
            temp1 = int(j[0])
            temp2 = int(j[1])
            result += temp1 * temp2
        except ValueError:
            continue
'''
for o in range(0, len(corrupted_input2)):
    if o % 2 == 0:
        print("s")
        i = corrupted_input2[o].split("mul(")
        for j in i:
            j = j.split(")")
            for k in j:
                k = k.split(",")
                prev = "0"
                for l in k:
                    try:
                        result = result + int(l) * int(prev)
                    except ValueError:
                        prev = l
                        continue
                    prev = l
                    continue
'''
print(result)