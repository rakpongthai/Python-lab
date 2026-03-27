# 2026-TxTp02.py

from pythainlp.tokenize import word_tokenize

# เปิดไฟล์
f = open("NEWS.txt", "r", encoding="utf-8")
text = f.read()
f.close()

# ตัดคำ
words = word_tokenize(text)

count_dict = {}

# นับคำ
for w in words:
    w = w.strip()
    
    if w == "":
        continue

    if w in count_dict:
        count_dict[w] = count_dict[w] + 1
    else:
        count_dict[w] = 1

# เรียงจากมากไปน้อย
sorted_words = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

# เขียนไฟล์
f = open("Count.txt", "w", encoding="utf-8")

for word, count in sorted_words:
    f.write(word + " : " + str(count) + "\n")

f.close()

print("เสร็จแล้ว")
