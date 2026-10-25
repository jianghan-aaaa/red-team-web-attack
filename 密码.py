
import itertools


combinations = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=3)


combinations_list = [''.join(comb) for comb in combinations]


with open('abc.txt', 'w') as file:
    for combo in combinations_list:
        file.write(combo + '\n')

print("已生成包含所有3位小写字母组合的TXT文件")
