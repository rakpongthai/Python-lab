from PIL import Image
im = Image.open("Image1.jpg")
#im.show()
w,h = im.size

#Gray Scale with Red
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        im.putpixel((i,j),(r,r,r))
im.show()
im.save("Red.jpg")

#Gray Scale with Green
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        im.putpixel((i,j),(g,g,g))
im.show()
im.save("Green.jpg")

#Gray Scale with Blue
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        im.putpixel((i,j),(b,b,b))
im.show()
im.save("Blue.jpg")

#Gray Scale with Max
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        Max = int(max(r,g,b))
        im.putpixel((i,j),(Max,Max,Max))
im.show()
im.save("Max.jpg")

#Gray Scale with Min
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        Min = int(min(r,g,b))
        im.putpixel((i,j),(Min,Min,Min))
im.show()
im.save("Min.jpg")

#Gray Scale with Mean
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        c = (r+g+b)//3
        im.putpixel((i,j),(c,c,c))
im.show()
#im.save("Mean.jpg")

#Black/White color
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))
        c = (r+g+b)//3
        if(c>127): im.putpixel((i,j),(255,255,255))
        else: im.putpixel((i,j),(0,0,0))
im.show()
im.save("BlackWhite.jpg")

#sepia Color
im = Image.open("WatWaAram.jpg")
w,h = im.size
for i in range(w):
    for j in range(h):
        r,g,b = im.getpixel((i,j))

        nr = int(0.393*r + 0.769*g + 0.189*b)
        ng = int(0.349*r + 0.686*g + 0.168*b)
        nb = int(0.272*r + 0.534*g + 0.131*b)

        if nr > 255: nr = 255
        else: nr = nr
        if ng > 255: ng = 255
        else: ng = ng
        if nb > 255: nb = 255
        else: nb = nb
        im.putpixel((i,j),(nr,ng,nb))
im.show()
im.save("sepia.jpg")

#cyanotype Color
from PIL import Image, ImageOps
im = Image.open("WatWaAram.jpg")

gray = ImageOps.grayscale(im)

# ทำ cyanotype 
cyanotype = ImageOps.colorize(
    gray,
    black=(0, 30, 150),     # สีเงา (น้ำเงินเข้ม)
    white=(220, 240, 255) # สีไฮไลต์ (ฟ้าอ่อน)
)
cyanotype.show()
cyanotype.save("cyanotype.jpg")



from PIL import Image

def merge9(images):
    w, h = images[0].size
    merged = Image.new("RGB", (w * 3, h * 3))

    for i, img in enumerate(images):
        row = i // 3
        col = i % 3
        merged.paste(img.resize((w, h)), (col * w, row * h))

    return merged


images = [
    Image.open("Red.jpg"),
    Image.open("Green.jpg"),
    Image.open("Blue.jpg"),
    Image.open("Max.jpg"),
    Image.open("Min.jpg"),
    Image.open("Mean.jpg"),
    Image.open("BlackWhite.jpg"),
    Image.open("sepia.jpg"),
    Image.open("cyanotype.jpg")
]

result = merge9(images)
result.show()
result.save("WatWaAram21.jpg")


