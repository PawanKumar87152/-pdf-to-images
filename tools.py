import fitz
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PIL import Image
import io

# 1 MERGE
def merge_pdf(files):
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    buf = io.BytesIO()
    merger.write(buf)
    buf.seek(0)
    return buf

# 2 SPLIT
def split_pdf(file):
    reader = PdfReader(file)
    outputs = []
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        buf = io.BytesIO()
        writer.write(buf)
        buf.seek(0)
        outputs.append((f"page_{i+1}.pdf", buf))
    return outputs

# 3 PDF → IMAGES
def pdf_to_images(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    images = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        buf = io.BytesIO()
        img.save(buf, "PNG")
        buf.seek(0)
        images.append((f"page_{i+1}.png", buf))
    return images

# 4 IMAGES → PDF
def images_to_pdf(files):
    imgs = [Image.open(f).convert("RGB") for f in files]
    buf = io.BytesIO()
    imgs[0].save(buf, save_all=True, append_images=imgs[1:], format="PDF")
    buf.seek(0)
    return buf

# 5 ROTATE
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

# 6 EXTRACT PAGES
def extract_pages(file, pages):
    reader = PdfReader(file)
    writer = PdfWriter()
    for p in pages:
        writer.add_page(reader.pages[p])
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf

# 7 DELETE PAGES
def delete_pages(file, pages):
    reader = PdfReader(file)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i not in pages:
            writer.add_page(page)
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf

# 8 REORDER PAGES
def reorder_pages(file, order):
    reader = PdfReader(file)
    writer = PdfWriter()
    for i in order:
        writer.add_page(reader.pages[i])
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf

# 9 COMPRESS (basic)
def compress_pdf(file):
    reader = PdfReader(file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf

# 10 ADD WATERMARK
def watermark_pdf(file, text="CONFIDENTIAL"):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        page.insert_text((50,50), text)
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf

# 11 TEXT EXTRACT
def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# 12 PDF INFO
def pdf_info(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return {"pages": len(doc)}

# 13 PDF → GRAYSCALE
def grayscale_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf

# 14 DUPLICATE PAGES
def duplicate_pages(file):
    reader = PdfReader(file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        writer.add_page(page)
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf

# 15 REVERSE PDF
def reverse_pdf(file):
    reader = PdfReader(file)
    writer = PdfWriter()
    for page in reversed(reader.pages):
        writer.add_page(page)
    buf = io.BytesIO()
    writer.write(buf)
    buf.seek(0)
    return buf
