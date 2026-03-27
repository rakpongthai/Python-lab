from PIL import Image
im = Image.open("Red.jpg")
newim = im.crop((0,0,426,240))
#newim.show()

im1 = Image.open("Green.jpg")
newim1 = im1.crop((426,0,852,240))
#newim1.show()

im2 = Image.open("Blue.jpg")
newim2 = im2.crop((852,0,1278,240))
#newim2.show()

im3 = Image.open("Max.jpg")
newim3 = im3.crop((0,240,426,480))
#newim3.show()

im4 = Image.open("Min.jpg")
newim4 = im4.crop((426,240,852,480))
#newim4.show()

im5 = Image.open("Mean.jpg")
newim5 = im5.crop((852,240,1278,480))
#newim5.show()

im6 = Image.open("BlackWhite.jpg")
newim6 = im6.crop((0,480,426,720))
#newim6.show()

im7 = Image.open("sepia.jpg")
newim7 = im7.crop((426,480,852,720))
#newim7.show()

im8 = Image.open("cyanotype.jpg")
newim8 = im8.crop((852,480,1278,720))
#newim8.show()


def merge9(images):
    w, h = images[0].size
    merged = Image.new("RGB", (w * 3, h * 3))

    for i, img in enumerate(images):
        row = i // 3
        col = i % 3
        merged.paste(img.resize((w, h)), (col * w, row * h))

    return merged


images = [
    newim,
    newim1,
    newim2,
    newim3,
    newim4,
    newim5,
    newim6,
    newim7,
    newim8,
    
]

result = merge9(images)
result.show()
result.save("WatWaAram22.jpg")
