import streamlit as st
import fitz
from PIL import Image
import io
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# ---------------- CONFIG ----------------
st.set_page_config(page_title="PDF Studio Pro", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- DARK UI ----------------
st.markdown("""
<style>

body {
    background-color: #0b1220;
    color: white;
}

/* big title */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: 900;
    color: #38bdf8;
}

/* button */
.stButton > button {
    width: 100%;
    height: 80px;
    font-size: 20px;
    font-weight: 800;
    border-radius: 15px;
}

/* sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
def home():

    st.markdown("<div class='title'>📄 PDF STUDIO PRO</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=150)

    st.markdown("### Welcome 👋")

    # BIG SELECT TOOL BUTTON
    if st.button("🚀 SELECT TOOL"):
        st.session_state.page = "tools"

# ---------------- SIDEBAR (TOOLS MENU) ----------------
def sidebar():

    with st.sidebar:
        st.title("🧰 Tools")

        if st.button("🏠 Home"):
            st.session_state.page = "home"

        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

        if st.button("✂️ Split PDF"):
            st.session_state.page = "split"

        if st.button("🖼️ PDF → Images"):
            st.session_state.page = "pdf2img"

# ---------------- TOOL 1: MERGE ----------------
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
            st.download_button("⬇️ Download", f, file_name="merged.pdf")

# ---------------- TOOL 2: SPLIT ----------------
def split_pdf():

    st.title("✂️ Split PDF")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Split 🚀"):

        reader = PdfReader(file)

        for i, page in enumerate(reader.pages):

            writer = PdfWriter()
            writer.add_page(page)

            buf = io.BytesIO()
            writer.write(buf)
            buf.seek(0)

            st.download_button(f"Page {i+1}", buf, file_name=f"page_{i+1}.pdf")

# ---------------- TOOL 3: PDF TO IMAGES ----------------
def pdf_to_images():

    st.title("🖼️ PDF → Images")

    file = st.file_uploader("Upload PDF")

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

# ---------------- ROUTER ----------------
sidebar()

if st.session_state.page == "home":
    home()

elif st.session_state.page == "tools":
    st.title("🧰 Select a Tool from Sidebar")

elif st.session_state.page == "merge":
    merge_pdf()

elif st.session_state.page == "split":
    split_pdf()

elif st.session_state.page == "pdf2img":
    pdf_to_images()
