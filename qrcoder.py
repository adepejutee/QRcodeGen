# -*- coding: utf-8 -*-
"""
Created on Wed July 19 01:24:07 2023

@author: ADEPEJU
"""

import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://www.facebook.com")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("facebook.png")
