import streamlit as st
import fitz
from PIL import Image
import io
from PyPDF2 import PdfMerger

# ---------------- CONFIG ----------------
st.set_page_config(page_title="PDF Suite Pro", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- GLASSMORPHISM CSS ----------------
st.markdown("""
<style>

/* Background */
body {
    background: linear-gradient(135deg, #e0eafc, #cfdef3);
}

/* Glass card */
.glass {
    background: rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    padding: 30px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    text-align: center;
}

/* Title */
.title {
    font-size: 48px;
    font-weight: 900;
    color: #1f4fff;
    text-align: center;
}

/* Subtitle */
.sub {
    text-align: center;
    font-size: 18px;
    color: #444;
}

/* Buttons */
.stButton > button {
    width: 100%;
    height: 120px;
    font-size: 20px;
    font-weight: 700;
    border-radius: 18px;
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.9);
    box-shadow: 0 12px 25px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>📄 PDF SUITE PRO</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Modern glassmorphism PDF tools dashboard</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### ")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 PDF → Images"):
            st.session_state.page = "pdf2img"

    with col2:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

    with col3:
        if st.button("🏠 Home"):
            st.session_state.page = "home"

# ---------------- PDF TO IMAGES ----------------
def pdf_to_images():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.title("📄➡️🖼️ PDF to Images")
    st.markdown("</div>", unsafe_allow_html=True)

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
                f"⬇️ Page {i+1}",
                buf.getvalue(),
                file_name=f"page_{i+1}.png"
            )

    if st.button("⬅️ Back"):
        st.session_state.page = "home"

# ---------------- MERGE PDF ----------------
def merge_pdf():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.title("📎 Merge PDF")
    st.markdown("</div>", unsafe_allow_html=True)

    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge 🚀"):

        merger = PdfMerger()

        for f in files:
            merger.append(f)

        output = "merged.pdf"
        merger.write(output)
        merger.close()

        with open(output, "rb") as f:
            st.download_button("⬇️ Download", f, file_name="merged.pdf")

    if st.button("⬅️ Back"):
        st.session_state.page = "home"

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "pdf2img":
    pdf_to_images()

elif st.session_state.page == "merge":
    merge_pdf()
