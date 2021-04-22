import matplotlib.pyplot as plt
from birthday import Count

studentNum = [i for i in range(100)]
rate = list()

for i in range(100):
    rate.append(Count(1500, i))

print(studentNum)
print(rate)

x = range(len(studentNum))
plt.plot(studentNum, rate)
plt.xlabel("student number", fontsize=16)
plt.ylabel("same birthday rate", fontsize=16)
plt.show()
