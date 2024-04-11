from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_to_pdf(input_text_file, output_pdf_file):
    with open(input_text_file, 'r') as txt:
        content = txt.read()

    pdf = canvas.Canvas(output_pdf_file, pagesize=letter)
    pdf.setFont("Helvetica", 12)
    font_size = 12
    line_height = 14  

    page_height = letter[1]
    y = page_height - 50  

    lines = content.split('\n')
    for line in lines:
        pdf.drawString(50, y, line)
        y -= line_height

        if y <= 50:
            pdf.showPage()
            y = page_height - 50  

    pdf.save()

input_text_file = "archivo.txt"
output_pdf_file = "archivo.pdf"

convert_to_pdf(input_text_file, output_pdf_file)

print(f"Proceso completado. Archivo PDF creado: {output_pdf_file}")
