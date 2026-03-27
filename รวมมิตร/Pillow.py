# =========================
# IMPORT (นำเข้าไลบรารี)
# =========================
from PIL import Image, ImageChops, ImageOps
import matplotlib.pyplot as plt

# =========================
# 1. เปิดภาพ + แสดงภาพ + ดูข้อมูล
# =========================
img = Image.open("test.jpg")   # เปิดรูป
img.show()                     # แสดงรูป

print("Format:", img.format)   # ประเภทไฟล์ (JPEG, PNG)
print("Size:", img.size)       # ขนาด (กว้าง, สูง)
print("Mode:", img.mode)       # โหมดสี (RGB, L)

# =========================
# 2. อ่าน/แก้ Pixel
# =========================
r, g, b = img.getpixel((0, 0))     # อ่านค่าสี pixel
c = (r + g + b) // 3               # คำนวณค่าเฉลี่ย
img.putpixel((0, 0), (c, c, c))    # แก้ pixel เป็นสีเทา

# =========================
# 3. แปลง RGB → Gray (ทั้งภาพ)
# =========================
img_gray = img.copy()              # copy รูป
w, h = img_gray.size

for i in range(w):
    for j in range(h):
        r, g, b = img_gray.getpixel((i, j))
        c = (r + g + b) // 3
        img_gray.putpixel((i, j), (c, c, c))

img_gray.save("gray.jpg")          # บันทึกภาพ

# =========================
# 4. Gray → ขาวดำ (B/W)
# =========================
img_bw = img.copy()

for i in range(w):
    for j in range(h):
        r, g, b = img_bw.getpixel((i, j))
        c = (r + g + b) // 3

        if c > 127:                       # ค่า threshold
            img_bw.putpixel((i, j), (255, 255, 255))  # ขาว
        else:
            img_bw.putpixel((i, j), (0, 0, 0))        # ดำ

img_bw.save("bw.jpg")

# =========================
# 5. Sepia (โทนวินเทจ)
# =========================
img_sepia = img.copy()

for i in range(w):
    for j in range(h):
        r, g, b = img_sepia.getpixel((i, j))

        nr = int(0.393*r + 0.769*g + 0.189*b)
        ng = int(0.349*r + 0.686*g + 0.168*b)
        nb = int(0.272*r + 0.534*g + 0.131*b)

        # จำกัดค่าไม่เกิน 255
        nr = min(255, nr)
        ng = min(255, ng)
        nb = min(255, nb)

        img_sepia.putpixel((i, j), (nr, ng, nb))

img_sepia.save("sepia.jpg")

# =========================
# 6. แยก/รวมสี (สลับสี)
# =========================
r, g, b = img.split()                 # แยกสี
img_swap = Image.merge("RGB", (b, g, r))  # สลับแดงกับน้ำเงิน
img_swap.save("swap.jpg")

# =========================
# 7. ทำสำเนาภาพหลายไฟล์
# =========================
for i in range(5):
    img.save(f"copy_{i}.jpg")

# =========================
# 8. Crop (ตัดภาพ)
# =========================
crop_img = img.crop((10, 10, 200, 200))
crop_img.show()

# =========================
# 9. หมุน / พลิกภาพ
# =========================
img_rotate = img.rotate(45)                 # หมุน 45 องศา
img_rotate.show()

img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)  # พลิกซ้าย-ขวา
img_flip.show()

# =========================
# 10. Resize (ย่อ/ขยาย)
# =========================
img_resize = img.resize((200, 200))
img_resize.show()

# =========================
# 11. แปลงโหมดสี
# =========================
img.convert("L").show()   # เทา
img.convert("1").show()   # ขาวดำ

# =========================
# 12. Histogram (วิเคราะห์สี)
# =========================
hist = img.histogram()

r_hist = hist[0:256]
g_hist = hist[256:512]
b_hist = hist[512:768]

plt.plot(r_hist)
plt.plot(g_hist)
plt.plot(b_hist)
plt.show()

# =========================
# 13. คำนวณภาพ (Image Math)
# =========================
img2 = img.copy()

img_add = ImageChops.add(img, img2)        # รวมภาพ
img_diff = ImageChops.difference(img, img2)  # หาความต่าง

img_add.show()
img_diff.show()

# =========================
# 14. Invert (กลับสี)
# =========================
img_invert = ImageChops.invert(img)
img_invert.show()

# =========================
# 15. แบ่งภาพ 4 ส่วน
# =========================
x, y = img.size
a, b = x//2, y//2

p1 = img.crop((0, 0, a, b))
p2 = img.crop((a, 0, x, b))
p3 = img.crop((0, b, a, y))
p4 = img.crop((a, b, x, y))

new_img = Image.new("RGB", img.size, (255, 255, 255))

new_img.paste(p4, (a, b))
new_img.paste(p1, (0, 0))

new_img.show()
