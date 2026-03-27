from PIL import Image
import numpy as np

im = Image.open("cat.png")
img = im.convert("L")
arr = np.array(img)
print("ค่าเฉลี่ย: ", arr.mean())
print("ค่าส่วนเบี่ยงเบนมาตรฐาน: ", arr.std())
img.show()
img.save("cat_gray.png")
