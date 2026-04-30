import fitz
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PIL import Image
import io

# ---------------- MERGE ----------------
def merge_pdf(files):
    merger = PdfMerger()

    for f in files:
        merger.append(f)

    output = "merged.pdf"
    merger.write(output)
    merger.close()

    return output


# ---------------- SPLIT ----------------
def split_pdf(file):
    reader = PdfReader(file)
    results = []

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        buf = io.BytesIO()
        writer.write(buf)
        buf.seek(0)

        results.append((f"page_{i+1}.pdf", buf))

    return results


# ---------------- PDF → IMAGES ----------------
def pdf_to_images(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    results = []

    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        results.append((f"page_{i+1}.png", buf))

    return results


# ---------------- IMAGES → PDF ----------------
def images_to_pdf(files):
    imgs = []

    for f in files:
        img = Image.open(f).convert("RGB")
        imgs.append(img)

    buf = io.BytesIO()
    imgs[0].save(buf, save_all=True, append_images=imgs[1:], format="PDF")
    buf.seek(0)

    return buf


# ---------------- ROTATE ----------------
def rotate_pdf(file):
    reader = PdfReader(file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(90)
        writer.add_page(page)

    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)

    return buf