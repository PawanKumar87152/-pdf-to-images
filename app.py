import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io
from PyPDF2 import PdfMerger

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="PDF Suite", layout="wide")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- CSS UI ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

/* Title */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #1f4fff;
    margin-top: 20px;
}

/* Subtitle */
.sub {
    text-align: center;
    font-size: 18px;
    color: gray;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 120px;
    font-size: 22px;
    font-weight: 800;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
def home():
    st.markdown("<div class='title'>📄 PDF TOOL SUITE</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>All-in-one PDF tools like iLovePDF</div>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 PDF → Images"):
            st.session_state.page = "pdf2img"

    with col2:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

    with col3:
        if st.button("🏠 Reset"):
            st.session_state.page = "home"

# ---------------- PDF TO IMAGES ----------------
def pdf_to_images():

    st.title("📄➡️🖼️ PDF to Images")

    file = st.file_uploader("Upload PDF", type=["pdf"])

    if file and st.button("Convert 🚀"):

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
        st.session_state.page = "home"

# ---------------- MERGE PDF ----------------
def merge_pdf():

    st.title("📎 Merge PDF")

    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge 🚀"):

        merger = PdfMerger()

        for f in files:
            merger.append(f)

        output = "merged.pdf"
        merger.write(output)
        merger.close()

        with open(output, "rb") as f:
            st.download_button("⬇️ Download Merged PDF", f, file_name="merged.pdf")

    if st.button("⬅️ Back"):
        st.session_state.page = "home"

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "pdf2img":
    pdf_to_images()

elif st.session_state.page == "merge":
    merge_pdf()
