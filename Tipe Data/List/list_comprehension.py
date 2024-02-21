# untuk Elemen

my_list = [1, 2, 3, 4, 5]
new_list = [elemen * 2 for elemen in my_list]
print(new_list)

# Dg kondisi

my_list = [1, 2, 3, 4, 5]
new_list = [elemen for elemen in my_list if elemen % 2 == 0]
print(new_list)