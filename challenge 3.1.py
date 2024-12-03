corrupted_input = input("Please enter a corrupted input: ")
corrupted_input = corrupted_input.split("mul(")
result = 0
for i in corrupted_input:
    i = i.split(")")
    for j in i:
        j = j.split(",")
        prev = "0"
        for k in j:
            try:
                result = result + int(k) * int(prev)
            except ValueError:
                prev = k
                continue
            prev = k
            continue
print(result)

