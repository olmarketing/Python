# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s= "a a a b c a a d c d d"
s=str.split()
print(s)
result_dic={}
new_s=[]
for i in s:
    if i not in result_dic:
        new_s.append(i)
        result_dic[i]=result_dic.get(i,0)+1
    else:
        new_s.append(f'{i}_{result_dic[i]}')
        result_dic[i]=result_dic.get(i,0)+1
print(*new_s)            
    