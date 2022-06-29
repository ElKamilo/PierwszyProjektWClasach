dupa = ['kibel', 'sraka', 'pies', 'chuj']
kupa = ['mus', 'grus', 'zus']
nico = []

index = 1
index2 = 1

for i in dupa:
    print(f'{index} {i}')
    index += 1
    for j in i:
        print(f'{index2} {j}')
        # sss = input()
        # nico.append(sss)
    choice = input()
    if choice == index:
        nico.append(choice)
print(nico)