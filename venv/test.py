my_list = ['*','*','*','*','*','*','*','*']

new_list = my_list[::-1]

my_list.extend(new_list)
print(len(my_list))
for i in range(0,(len(my_list)//2)+1):
    print(my_list)
    my_list[i]= '0'
    my_list[-i-1]= '0'
print(len(my_list))




# print(my_list)
# for i in range(0,len(my_list)-1):
#     for j in range(i+1,len(my_list)):
#         if my_list[i]>my_list[j]:
#             my_list.insert(i,my_list.pop(j))
#
# print(my_list)