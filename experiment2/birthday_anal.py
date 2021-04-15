from birthday import get_p
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

m = 2000
n = [i for i in range(100)]
q = [get_p(m, i) for i in n]

plt.plot(n, q)
plt.xlabel("student number")
plt.ylabel("probability")
plt.legend()

plt.savefig(fname='pic.png')
plt.show()
