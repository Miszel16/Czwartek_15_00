from fpdf import FPDF

# ctrl + shift + P
# Python: Select Interpreter
# python.useEnvironmentsExtension

A4W = 210
A4H = 297

pdf = FPDF()
pdf.add_page()

pdf.add_font('DejaVu', '', "DejaVuSansCondensed.ttf")

pdf.set_font('DejaVu', size=32)
pdf.set_text_color(255,0,0)


pdf.text(x=30, y=20, text="Oferta biura Huricane Travel's")

pdf.image(
    "logo.png",
    x=A4W*0.25,
    y=A4W*0.25,
    w=A4W*0.5,
    h=A4W*0.5
)

pdf.set_font('DejaVu', size=24)
pdf.set_text_color(0,0,0)
pdf.text(x=40, y=A4W*0.75+20, text="Oferta wycieczki - Piękna Polska")

pdf.output("oferta-biura-podrozy.pdf")