'''pip install pyqrcode
pip install pypng
'''


import pyqrcode
import png
import os

faculties = {
    "อักษรศาสตร์": "6805",
    "วิทยาศาสตร์": "6807"
}
 
for fac_name, stdcode in faculties.items():
    n = int(input(f"จำนวนนักศึกษาคณะ{fac_name}: "))
    if not os.path.exists(fac_name):
        os.makedirs(fac_name)

    for i in range(n):
        number = str(i+1).zfill(4)
        st = stdcode + str(number)
        qr_code = pyqrcode.create(st)
        filepath = os.path.join(fac_name, st + ".png")
        qr_code.png(filepath, scale=10)
        #qr_code.show()
        print(st)
