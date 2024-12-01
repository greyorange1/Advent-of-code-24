lists = input("Enter a list: ")
individuals = lists.split()  #seperates the input string into single words
list1 = []
list2 = []
for i in range(0, len(individuals)):
    if i % 2 == 0:
        list1.append(int(individuals[i]))
    else:
        list2.append(int(individuals[i]))
print(list1, list2)
x = 0
for i in range (0, len(list1)):
    for j in range(0, len(list2)):
        if list1[i] == list2[j]:
            x = x + list2[j]
print(x)