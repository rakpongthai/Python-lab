
pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.sc.su.ac.th"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

# ดึงข้อความทั้งหมด
text = soup.get_text()

# แยกเป็นบรรทัด
x = text.split("\n")

# ลบบรรทัดว่าง
x = [s for s in x if s.strip() != ""]

# แสดงผล
for line in x:
    print(line)


#pip uninstall pytube -y
#pip install pytubefix
from pytubefix import YouTube

url = "https://youtu.be/2GJfWMYCWY0"

yt = YouTube(url)

video = yt.streams.get_highest_resolution()
video.download(filename="video.mp4")

print("ดาวน์โหลดเสร็จแล้ว")

#pip install PyPDF2 pdfplumber pillow
import os
from PyPDF2 import PdfReader
import pdfplumber
from PIL import Image

file_path = "cat2.pdf"

# -------------------------
# 📏 ขนาดไฟล์
# -------------------------
size = os.path.getsize(file_path)
print("ขนาดไฟล์:", size, "bytes")

# -------------------------
# 📄 จำนวนหน้า
# -------------------------
reader = PdfReader(file_path)
num_pages = len(reader.pages)
print("จำนวนหน้า:", num_pages)

# -------------------------
# 📝 ดึงข้อความ
# -------------------------
with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"\n--- หน้า {i+1} ---")
        print(text)

# -------------------------
# 🖼 ดึงรูปภาพ
# -------------------------
with pdfplumber.open(file_path) as pdf:
    for i, page in enumerate(pdf.pages):
        for j, img in enumerate(page.images):
            x0, top, x1, bottom = img["x0"], img["top"], img["x1"], img["bottom"]

            # crop รูป
            cropped = page.within_bbox((x0, top, x1, bottom)).to_image()
            cropped.save(f"image_page{i+1}_{j+1}.png")

print("เสร็จแล้ว")

#pip install pytesseract pillow opencv-python
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR.exe"

img = cv2.imread("text11.jpg")

# แปลงเป็นขาวดำ
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold เพิ่มความคม
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh)

print(text)

#pip install rembg pillow
from rembg import remove
from PIL import Image

# เปิดรูป
input_path = "cat4.jpg"
output_path = "สวยยย12.png"

input_img = Image.open(input_path)

# ลบพื้นหลัง
output_img = remove(input_img)

# บันทึก (ต้องเป็น PNG เพื่อให้พื้นหลังโปร่งใส)
output_img.save(output_path)

print("ลบพื้นหลังเสร็จแล้ว")
