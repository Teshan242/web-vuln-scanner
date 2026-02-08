from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


def create_pdf(data):
    pdf_path = "report.pdf"

    # Register a Unicode font (optional)
    pdfmetrics.registerFont(UnicodeCIDFont("HYSMyeongJo-Medium"))

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    normal.fontName = "HYSMyeongJo-Medium"

    story = []

    story.append(Paragraph("🛡 Web Vulnerability Scan Report", normal))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"URL: {data['url']}", normal))
    story.append(Paragraph(f"HTTPS Enabled: {data['https']}", normal))

    # Show headers as comma-separated string, or None
    missing_headers = ', '.join(data['missing_headers']) if data['missing_headers'] else 'None'
    story.append(Paragraph(f"Missing Headers: {missing_headers}", normal))

    story.append(Paragraph(f"Forms Found: {data['forms']}", normal))
    story.append(Paragraph(f"Severity Level: {data['severity']}", normal))

    doc.build(story)
    return pdf_path
