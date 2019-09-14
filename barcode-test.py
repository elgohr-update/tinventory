import os

import requests
from PIL import Image
from io import BytesIO

from fpdf import FPDF

TEMP_DIR = "latex"
FONTS_DIR = "fonts"
default_params = {
    "code": "Code128",
    "dpi": "300",
    "imagetype": "Png"
}


def barcode(code):
    params = default_params
    params["data"] = str(code)
    r = requests.get("https://barcode.tec-it.com/barcode.ashx", params=params)
    i = Image.open(BytesIO(r.content))
    filename = os.path.join(TEMP_DIR, "barcode.png")
    i.save(filename)
    return filename


def barcode_pdf(code):
    barcode_filename = barcode(code)
    pdf = FPDF(orientation='P', unit='mm', format=(54, 17))
    pdf.add_page()
    pdf.add_font("Roboto Condensed", fname=os.path.join(FONTS_DIR, "RobotoCondensed-Regular.ttf"), uni=True)
    pdf.set_font('Roboto Condensed', size=6)
    pdf.text(3, 3, 'Eigentum der Technik-AG, Katharineum zu Lübeck')
    pdf.image(barcode_filename, 3, 3.5, 47, 14)
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(0, 13, 54, 4, style="F")
    pdf.text(3, 15, "ID: {}".format(code))
    filename = os.path.join(TEMP_DIR, "barcode.pdf")
    pdf.output(filename, 'F')


barcode_pdf("12454512465465465465")
