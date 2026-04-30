import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import fitz
from PIL import Image
import io

st.set_page_config(page_title="PDF Suite", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;'>📄 PDF TOOL SUITE</h1>
<p style='text-align:center;color:gray;'>All-in-one PDF tools like iLovePDF</p>
<hr>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR MENU ----------------
tool = st.sidebar.selectbox(
    "Choose Tool",
    [
        "Home",
        "Merge PDF",
        "Split PDF",
        "PDF to Images"
    ]
)

# ---------------- HOME ----------------
if tool == "Home":
    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=200)
    st.write("### Welcome to PDF Suite 🚀")
    st.write("Select a tool from sidebar")

# ---------------- MERGE PDF ----------------
elif tool == "Merge PDF":

    st.subheader("📎 Merge PDF")

    files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

    if files and st.button("Merge"):

        merger = PdfMerger()

        for f in files:
            merger.append(f)

        output = "merged.pdf"
        merger.write(output)
        merger.close()

        with open(output, "rb") as f:
            st.download_button("Download", f, file_name="merged.pdf")

# ---------------- SPLIT PDF ----------------
elif tool == "Split PDF":

    st.subheader("✂️ Split PDF")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Split"):

        reader = PdfReader(file)

        for i, page in enumerate(reader.pages):

            writer = PdfWriter()
            writer.add_page(page)

            output = f"page_{i+1}.pdf"

            with open(output, "wb") as f:
                writer.write(f)

            with open(output, "rb") as f:
                st.download_button(f"Download Page {i+1}", f)

# ---------------- PDF TO IMAGES ----------------
elif tool == "PDF to Images":

    st.subheader("🖼️ PDF to Images")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Convert"):

        doc = fitz.open(stream=file.read(), filetype="pdf")

        for i, page in enumerate(doc):

            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            st.image(img, caption=f"Page {i+1}")

            buf = io.BytesIO()
            img.save(buf, format="PNG")

            st.download_button(
                f"Download Page {i+1}",
                buf.getvalue(),
                file_name=f"page_{i+1}.png"
            )
