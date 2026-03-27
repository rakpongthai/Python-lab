from PIL import Image, ImageFilter
im = Image.open("cat4.jpg")
g = im.convert("L")
edge = g.filter(ImageFilter.FIND_EDGES)

print("ขนาดภาพเดิม:", im.size)
print("ขนาดภาพ edge:", edge.size)

im.show()   
edge.show()   
edge.save("cat4_edge.jpg")
