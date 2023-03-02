
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# one_list, two_list=zip(*orbits)
# my_list=[]
# for i in range(len(one_list)):
#     for j in range(len(two_list)):
#         if one_list[i]==two_list[i]:
#             my_list.append(0)
#         else:
#              s=one_list[i]*two_list[i]
#              my_list.append(s)   

# for i in range(len(one_list)):
#           if my_list[i] == max(my_list):
#             print(orbits[i])

from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
maximum = max(list(map(lambda x:pi*x[0]*x[1], (filter(lambda i: i[0]!=i[1],orbits)))))
far=filter(lambda y:pi*y[0]*y[1] == maximum, orbits)
print(*list(far))





