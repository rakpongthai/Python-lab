from PIL import Image
im = Image.open("cat3.jpg")
x = int(input("input ความกว้าง :"))

w, h = im.size
scale = x / w
new_h = int(h * scale)
im1 = im.resize((x, new_h))

print("ก่อน:", im.size)
print("หลัง:", im1.size)

im1.save("cat3_resized.jpg")
im1.show()
