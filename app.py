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

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

/* background */
body {
    background: linear-gradient(135deg, #eef2f3, #8e9eab);
}

/* title */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #111;
}

/* subtitle */
.sub {
    text-align: center;
    color: #333;
    font-size: 18px;
}

/* card buttons (CANVA STYLE) */
.stButton > button {
    width: 100%;
    height: 120px;
    border-radius: 20px;
    font-size: 18px;
    font-weight: 700;
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.06);
    background: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME DASHBOARD ----------------
def home():

    st.markdown("<div class='title'>🎨 PDF STUDIO PRO</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Canva-style PDF tool suite (15 tools)</div>", unsafe_allow_html=True)

    st.markdown("---")

    tools = [
        "📎 Merge PDF", "✂️ Split PDF", "🖼️ PDF → Images",
        "📷 Images → PDF", "🔄 Rotate PDF", "📄 Extract Pages",
        "🗑️ Delete Pages", "📊 PDF Info", "🔐 Protect PDF",
        "🔓 Unlock PDF", "🖋️ Watermark", "🔢 Page Numbers",
        "📦 Compress PDF", "📑 Reorder Pages", "🏠 Home"
    ]

    cols = st.columns(3)

    for i, tool in enumerate(tools):
        with cols[i % 3]:
            if st.button(tool):
                st.session_state.page = tool

# ---------------- TOOL FUNCTIONS ----------------

def merge_pdf():
    st.title("📎 Merge PDF")

    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge"):
        merger = PdfMerger()
        for f in files:
            merger.append(f)

        output = "merged.pdf"
        merger.write(output)
        merger.close()

        with open(output, "rb") as f:
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
            img.save(buf, format="PNG")

            st.download_button(f"Page {i+1}", buf.getvalue(), file_name=f"page_{i+1}.png")

# ---------------- ROUTER ----------------
page = st.session_state.page

if page == "home":
    home()

elif page == "📎 Merge PDF":
    merge_pdf()

elif page == "✂️ Split PDF":
    split_pdf()

elif page == "🖼️ PDF → Images":
    pdf_to_images()

elif page == "🏠 Home":
    st.session_state.page = "home"
    st.rerun()

else:
    st.session_state.page = "home"
