
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("Image1.jpg")
#im.show()
c = im.histogram()
nr = []
ng = []
nb = []
for i in range(256):
    nr.append(c[i])
    ng.append(c[i+256])
    nb.append(c[i+512])

plt.plot(range(256), nr, c='r', label='Red')
plt.plot(range(256), ng, c='g', label='Green')
plt.plot(range(256), nb, c='b', label='Blue')

plt.style.use('_mpl-gallery')
plt.xlabel('color value (0-255)')
plt.ylabel('pixel counts')
plt.legend()
plt.show()

img_arr = np.array(im)

R = img_arr[:, :, 0]
G = img_arr[:, :, 1]
B = img_arr[:, :, 2]

print("Red")
print("ค่าสูงสุด =", np.max(R))
print("ค่าต่ำสุด =", np.min(R))
print("ค่าเฉลี่ย =", np.mean(R))

print("\nGreen")
print("ค่าสูงสุด =", np.max(G))
print("ค่าต่ำสุด =", np.min(G))
print("ค่าเฉลี่ย =", np.mean(G))

print("\nBlue")
print("ค่าสูงสุด =", np.max(B))
print("ค่าต่ำสุด =", np.min(B))
print("ค่าเฉลี่ย =", np.mean(B))



