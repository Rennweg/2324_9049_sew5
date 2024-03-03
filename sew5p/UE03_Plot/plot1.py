import matplotlib.pyplot as plt
import math
PI = math.pi
X = [-PI+ i * (2*PI/1024) for i in range(1024 + 1)] # CNT Werte von -pi ... +pi
C = [ math.cos(x) for x in X ] # CNT cosinuswerte für x von -pi ... +pi
S = [ math.sin(x) for x in X ]

plt.plot(X, C)
plt.plot(X, S)
plt.figure(figsize=(10,6), dpi=80)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")
plt.savefig("plot1_sautter.png",dpi=72)
plt.show()