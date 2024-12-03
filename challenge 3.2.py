corrupted_input = input("Please enter a corrupted input: ")
corrupted_input = corrupted_input.split("don't()")
dos = ""
for i in range(0, len(corrupted_input)):
    if i % 2 == 0:
        dos = dos + corrupted_input[i]
dos = dos.split("mul(")
result = 0
for i in dos:
    i = i.split(")")
    prev = "0"
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
