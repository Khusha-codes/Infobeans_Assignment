from reportlab.pdfgen import canvas

pdf = canvas.Canvas("student.pdf")

pdf.drawString(100, 750, "Student Report")
pdf.drawString(100, 700, "Name: Kirti")
pdf.drawString(100, 650, "Course: B.Tech IT")

pdf.save()