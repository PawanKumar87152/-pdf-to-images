import streamlit as st
import fitz
from PIL import Image
import io
from PyPDF2 import PdfMerger

st.set_page_config(page_title="PDF SaaS Suite", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
def home():
    st.markdown("""
        <div style="text-align:center;">
            <h1>📄 PDF SaaS Suite</h1>
            <p style="color:gray;">All-in-one PDF tools like iLovePDF</p>
        </div>
    """, unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=200)

    if st.button("🚀 Start Using Tools"):
        st.session_state.page = "dashboard"

# ---------------- TOOL DASHBOARD ----------------
def dashboard():

    st.title("🧰 Choose a Tool")

    tools = st.columns(3)

    with tools[0]:
        if st.button("📄 PDF → Images"):
            st.session_state.page = "pdf2img"

    with tools[1]:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

    with tools[2]:
        if st.button("🏠 Back Home"):
            st.session_state.page = "home"

# ---------------- PDF TO IMAGES ----------------
def pdf_to_images():

    st.title("📄➡️🖼️ PDF to Images")

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
                f"⬇️ Download Page {i+1}",
                buf.getvalue(),
                file_name=f"page_{i+1}.png"
            )

    if st.button("⬅️ Back"):
        st.session_state.page = "dashboard"

# ---------------- MERGE PDF ----------------
def merge_pdf():

    st.title("📎 Merge PDFs")

    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge"):

        merger = PdfMerger()

        for f in files:
            merger.append(f)

        output = "merged.pdf"
        merger.write(output)
        merger.close()

        with open(output, "rb") as f:
            st.download_button("⬇️ Download Merged PDF", f, file_name="merged.pdf")

    if st.button("⬅️ Back"):
        st.session_state.page = "dashboard"

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "dashboard":
    dashboard()

elif st.session_state.page == "pdf2img":
    pdf_to_images()

elif st.session_state.page == "merge":
    merge_pdf()
