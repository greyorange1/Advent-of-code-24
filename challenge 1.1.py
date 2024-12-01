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


def sort_new(to_be_sorted: list):
    return sorted(to_be_sorted)


temp = 0

list1 = sort_new(list1)
list2 = sort_new(list2)
for i in list1:
    temp = temp + abs(i - list2[list1.index(i)])

print(temp)
