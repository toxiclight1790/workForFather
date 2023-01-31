import numpy as np
import matplotlib.pyplot as plt
 
f = open('Profiles  1  12023032221.dat', 'r')
f = f.readlines()
for jk in range(21):
    f[jk] = f[jk][:-1]

for i in range(21, len(f)):
    f[i] = f[i].split(' ')

mas = []
k=0


for l in range(20):
    mas.append(f[l][-1:])
for g in range(21,len(f)):
    frag = f[g]
    while '' in frag:
        frag.remove('')

for fgh in range(21, len(f)):
    del f[fgh][1:14]
    del f[fgh][4:]


for m in range(21, len(f)):
    h=0
    for j in range(len(f[m])):
        if f[i][j] != '':
            mas.append(f[m][j])
            h+=1
    k+=1


# print(*f, sep='\n')

plt.ioff()
for kl in range(21, len(f)):
    x = float(f[kl][0])
    y1 = float(f[kl][1])
    print(x," ", y1)
# x = [22,22,22,20]
# y1 = [16,17,19,23]

fig, ax = plt.subplots()
 
ax.plot(x, y1, 'rx', linestyle='solid')

# ax.fill_between(x, y1, interpolate=True,
#                 color='green', alpha=0.3)
 
lgnd = ax.legend(['y1'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')
 
plt.show()