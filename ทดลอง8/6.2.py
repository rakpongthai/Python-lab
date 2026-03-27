from PIL import Image
img = Image.open("TestPicture.jpg")
w,h = img.size
 
mean = Image.new("RGB",(w,h))
sepia = Image.new("RGB",(w,h))
cyan = Image.new("RGB",(w,h))
 
for i in range(w):
    for j in range(h):
        r,g,b = img.getpixel((i,j))
        c = (r+g+b)//3
        mean.putpixel((i,j),(c,c,c))
        nr = min(255,int(0.393*r+0.769*g+0.189*b))
        ng = min(255,int(0.349*r+0.686*g+0.168*b))
        nb = min(255,int(0.272*r+0.534*g+0.131*b))
        if nr > 255: nr = 255
        else: nr = nr
        if ng > 255: ng = 255
        else: ng = ng
        if nb > 255: nb = 255
        else: nb = nb
        sepia.putpixel((i,j),(nr,ng,nb))
        cyan.putpixel((i,j),(0,g,b))
 
mean.show()
sepia.show()
cyan.show()
 
mean.save("result1.jpg")
sepia.save("result2.jpg")
cyan.save("result3.jpg")
