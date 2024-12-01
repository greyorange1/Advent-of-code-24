def sort_new(to_be_sorted: list):
    return sorted(to_be_sorted)


lists = input('Enter a list: ')
individuals = lists.split()  #seperates the input string into single words
list1 = []
list2 = []
print(len(individuals))
for i in range(0, len(individuals)):
    if i % 2 == 0:
        print("x")
        list1.append(int(individuals[i]))
    else:
        print("y")
        list2.append(int(individuals[i]))
print(list1, list2)

temp = 0

list1 = sort_new(list1)
list2 = sort_new(list2)
for i in list1:
    temp = temp + abs(i - list2[list1.index(i)])

print(temp)
