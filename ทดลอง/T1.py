from collections import Counter
from pythainlp.tokenize import word_tokenize
import re

text = input("พิมพ์ข้อความ: ")
text = text.lower()
text = re.sub(r"[^\w\sก-๙]", "", text)

words = text.split()
words = word_tokenize(text)
word_count = Counter(words)

total = len(words)
print("จำนวนคำทั้งหมด:", total)

top10 = word_count.most_common(10)

print("Top 10 คำที่พบบ่อย:")
for word, count in top10:
    print(word, ":", count)
