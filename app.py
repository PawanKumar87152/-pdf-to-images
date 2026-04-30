import streamlit as st
import fitz
from PIL import Image
import io
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# ---------------- PAGE ----------------
st.set_page_config(page_title="PDF Studio Pro", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- PREMIUM UI CSS ----------------
st.markdown("""
<style>

/* background gradient */
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* HERO */
.hero {
    text-align: center;
    padding: 40px 10px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 900;
    color: #38bdf8;
}

.hero p {
    font-size: 18px;
    color: #94a3b8;
}

/* BIG PRIMARY BUTTON */
.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 800;
    background: #38bdf8;
    color: black;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    background: #0ea5e9;
}

/* TOOL CARDS */
.card-btn button {
    height: 120px !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    border-radius: 18px !important;
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #0b1220;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():

    st.markdown("""
    <div class="hero">
        <h1>📄 PDF STUDIO PRO</h1>
        <p>All-in-one PDF SaaS Tool (iLovePDF Style)</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 START TOOL SUITE"):
        st.session_state.page = "tools"

# ---------------- TOOL GRID ----------------
def tools():

    st.title("🧰 Tools Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

        if st.button("🖼️ PDF → Images"):
            st.session_state.page = "pdf2img"

    with col2:
        if st.button("✂️ Split PDF"):
            st.session_state.page = "split"

        if st.button("📄 Images → PDF"):
            st.session_state.page = "img2pdf"

# ---------------- TOOLS ----------------
def merge_pdf():
    st.title("📎 Merge PDF")
    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge"):
        merger = PdfMerger()
        for f in files:
            merger.append(f)

        merger.write("merged.pdf")
        merger.close()

        with open("merged.pdf", "rb") as f:
            st.download_button("Download", f, file_name="merged.pdf")

def split_pdf():
    st.title("✂️ Split PDF")
    file = st.file_uploader("Upload PDF")

    if file and st.button("Split"):
        reader = PdfReader(file)

        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)

            buf = io.BytesIO()
            writer.write(buf)
            buf.seek(0)

            st.download_button(f"Page {i+1}", buf, file_name=f"page_{i+1}.pdf")

def pdf_to_images():
    st.title("🖼️ PDF → Images")
    file = st.file_uploader("Upload PDF")

    if file and st.button("Convert"):
        doc = fitz.open(stream=file.read(), filetype="pdf")

        for i, page in enumerate(doc):
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            st.image(img)

            buf = io.BytesIO()
            img.save(buf, "PNG")

            st.download_button(f"Page {i+1}", buf.getvalue(), file_name=f"page_{i+1}.png")

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "tools":
    tools()

elif st.session_state.page == "merge":
    merge_pdf()

elif st.session_state.page == "split":
    split_pdf()

elif st.session_state.page == "pdf2img":
    pdf_to_images()
