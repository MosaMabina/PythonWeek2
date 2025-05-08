# 1.Creating an empty list
my_list = []

#2. Appending elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3.Inserting second value
my_list.insert(1,15)

# 4.extending list
my_list.extend([50,60,7])

# 5.removing last element from list
my_list.pop()

# 6.sorting list in ascending order
my_list.sort()

# 7.finding and printing index of value 30
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)