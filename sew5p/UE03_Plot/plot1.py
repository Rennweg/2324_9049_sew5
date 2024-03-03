import matplotlib.pyplot as plt
import math
PI = math.pi
X = [-PI+ i * (2*PI/1024) for i in range(1024)] # CNT Werte von -pi ... +pi
C = [ math.cos(x) for x in X ] # CNT cosinuswerte für x von -pi ... +pi
S = [ math.sin(x) for x in X ]

plt.plot(X, C)
plt.plot(X, S)
plt.figure(figsize=(10,6), dpi=80)



plt.xlim(min(X)*1.1, max(X)*1.1)
plt.ylim(min(C)*1.1, max(C)*1.1)

plt.xticks( [-PI, -PI/2, 0, PI/2, PI])
plt.yticks([-1, 0, +1])

plt.xticks([-PI, -PI/2, 0, PI/2, PI],
[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
[r'$-1$', r'$0$', r'$+1$'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

t = 2*PI/3
plt.plot([t,t],[0,math.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.cos(t),], 50, color ='blue')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
xy=(t, math.sin(t)), xycoords='data',
xytext=(+10, +30), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t,t],[0,math.sin(t)], color ='red', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.sin(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
xy=(t, math.cos(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
ax.set_axisbelow(True)



t = -PI / 4
plt.plot([t, t], [0, math.cos(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [math.cos(t), ], 50, color='red')
plt.annotate(r'$\sin(\minus\frac{\pi}{4})=-\frac{\sqrt{2}}{2}$',
             xy=(t, math.sin(t)), xycoords='data',
             xytext=(-10, -30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, math.sin(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [math.sin(t), ], 50, color='blue')
plt.annotate(r'$\cos(\minus\frac{\pi}{4}))=\frac{\sqrt{2}}{2}$',
             xy=(t, math.cos(t)), xycoords='data',
             xytext=(-90, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))



plt.plot(X, C, color="yellow", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="green", linewidth=2.5, linestyle="-.", label="sine")
plt.legend(loc='upper left', frameon=False)
plt.title("Plot von Luca Sautter, HTL3R")



plt.savefig("plot1_sautter.png",dpi=72)
plt.show()