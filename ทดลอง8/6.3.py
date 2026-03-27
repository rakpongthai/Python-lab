from PIL import Image

im1= Image.open("TestPicture.jpg")
newim1 = im1.crop((0,0,500,332))

im2= Image.open("result1.jpg")
newim2 = im2.crop((500,0,1000,332))

im3= Image.open("result2.jpg")
newim3 = im3.crop((0,332,500,664))

im4= Image.open("result3.jpg")
newim4 = im4.crop((500,332,1000,664))


def merge(images: list[Image.Image]) -> Image.Image:
   assert len(images) == 4
   w = images[0].size[0]
   h = images[0].size[1]
   
   total_w = w * 2
   total_h = h * 2
   im = Image.new("RGB", (total_w, total_h))
   for i, img in enumerate(images):
       row = i // 2
       col = i % 2
       x = col * w
       y = row * h
       im.paste(img.resize((w, h)), (x, y))
   return im

imgs = [
   newim1,
   newim2,
   newim3,
   newim4,
   
]
result = merge(imgs)
result.show()
result.save("Image04.jpg")
