f = open('Profiles  1  12023032221.dat', 'r')
f = f.readlines()
for i in range(21, len(f)):
    f[i] = f[i].split(' ')

mas = []
k=0
for i in range(20):
    mas.append(f[i][:-1])
for i in range(21, len(f)):
    h=0
    for j in range(len(f[i])):
        if f[i][j] != '':
            mas[k].append(f[i][j])
            h+=1
    k+=1


print(mas)
