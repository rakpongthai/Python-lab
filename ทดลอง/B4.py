from PIL import Image, ImageFilter

img = Image.open("cat5.jpg")
x1, y1, x2, y2 = 100, 100, 400, 400
box = img.crop((x1, y1, x2, y2))
blur = box.filter(ImageFilter.GaussianBlur(radius=10))
img.paste(blur,(x1, y1))
img.save("cat5.Blur.jpg")
