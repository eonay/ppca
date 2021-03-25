#!/usr/bin/env python
# -*- coding: utf-8 -*-

file1 = open('c0-cpu_memory-v1.out', 'r', encoding='utf-8')
file2 = open('c1-cpu_memory-v1.out', 'r', encoding='utf-8')

list1 = []
list2 = []
arquivo = open('c0-memory-v1.csv', 'w', encoding='utf-8')
print('Memória, Controlador (c0), Controlador (c1)', file=arquivo)
#ordem = -2

for line in file1:
    #ordem +=1
    line = line.rstrip()
    if 'cs' in line:
        continue
    line.split()
    v = line[6:10]

    #print(ordem, v)
    #print(ordem, v, file=arquivo)

    list1.append(v)


file1.close()


for line in file2:
    #ordem +=1
    line = line.rstrip()
    if 'cs' in line:
        continue
    line.split()
    v = line[6:10]

    #print(ordem, v)
    #print(ordem, v, file=arquivo)

    list2.append(v)
file2.close()





for i in range(len(list1)):
    print(i+1, ',',list1[i], ',', list2[i], file=arquivo)


arquivo.close()