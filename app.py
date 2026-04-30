import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
import zipfile

st.set_page_config(page_title="PDF to Images Pro", layout="wide")

st.title("📄➡️🖼️ PDF to Images Pro (Fixed Version)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

def pdf_to_images(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    images = []

    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    return images

if uploaded_file:

    if st.button("Convert PDF 🚀"):

        images = pdf_to_images(uploaded_file.read())

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, "w") as zip_file:

            for i, img in enumerate(images):
                img_bytes = io.BytesIO()
                img.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                zip_file.writestr(f"page_{i+1}.png", img_bytes.read())

                st.image(img, caption=f"Page {i+1}")

        zip_buffer.seek(0)

        st.download_button(
            "⬇️ Download Images ZIP",
            zip_buffer,
            file_name="pdf_images.zip",
            mime="application/zip"
        )
else:
    st.info("Upload PDF to start")
