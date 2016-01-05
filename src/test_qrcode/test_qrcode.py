#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from PIL import Image
import cStringIO
import qrcode


def generate_qrcode(information, head_url):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data(information)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")

    # remote file
    head_file = urllib2.urlopen(head_url)
    tmpIm = cStringIO.StringIO(head_file.read())
    icon = Image.open(tmpIm)
    # icon = Image.open("test.png")
    # print im.format, im.size, im.mode

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    icon = icon.convert('RGBA')

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), icon)

    img.save("test1.png")


if __name__ == '__main__':
    generate_qrcode(
        'http://taiyuantest.shitouren.com/qrcode?userid=245233',
        'http://wx.qlogo.cn/mmhead/Q3auHgzwzM61v6TNibpIA7dywB7mfEZMMjSzXDIsDu5h8BdmADOFNfQ/64'
    )
