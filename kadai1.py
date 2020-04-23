import numpy as np
import matplotlib.pyplot as plt


# ４次ルンゲクッタによって
# dx/dy = -x^3 + sin(t)
# をとく．

def f(x, t):
    return -x**3 + np.sin(t)

a = 0.0
b = 10.0
N = 100
h = (b-a)/N

tpoints = np.arange(a, b, h)
# print(tpoints)
xpoints = []
x = 0.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1, t+0.5*h)
    k3 = h*f(x+0.5*k2, t+0.5*h)
    k4 = h*f(x+k3, t+h)
    x += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints, xpoints)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show


A分野のBを目的とする研究であり，先行研究のCという課題をDによって改善する．そして関連研究のEとは違って，本研究にはFという特徴がある．Gを評価指標とし，それがHであることによって本研究の優位性を明らかにする．