import streamlit as st
import tools

st.set_page_config(page_title="PDF24 Clone", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- UI ----------------
st.markdown("""
<style>
body { background:#0b1220; color:white; }

.title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    color:#38bdf8;
}

.card button {
    width:100%;
    height:90px;
    font-size:18px;
    font-weight:800;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():
    st.markdown("<div class='title'>📄 PDF24 CLONE</div>", unsafe_allow_html=True)
    st.write("Select a tool")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

        if st.button("✂️ Split PDF"):
            st.session_state.page = "split"

    with col2:
        if st.button("🖼️ PDF → Images"):
            st.session_state.page = "pdf2img"

        if st.button("📷 Images → PDF"):
            st.session_state.page = "img2pdf"

    with col3:
        if st.button("🔄 Rotate PDF"):
            st.session_state.page = "rotate"


# ---------------- MERGE UI ----------------
def merge_ui():
    st.title("📎 Merge PDF")

    files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

    if files and st.button("Merge"):
        output = tools.merge_pdf(files)

        with open(output, "rb") as f:
            st.download_button("Download", f, file_name="merged.pdf")


# ---------------- SPLIT UI ----------------
def split_ui():
    st.title("✂️ Split PDF")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Split"):
        results = tools.split_pdf(file)

        for name, data in results:
            st.download_button(name, data, file_name=name)


# ---------------- PDF TO IMAGES ----------------
def pdf2img_ui():
    st.title("🖼️ PDF → Images")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Convert"):
        images = tools.pdf_to_images(file)

        for name, img in images:
            st.image(img)
            st.download_button(name, img, file_name=name)


# ---------------- IMAGES TO PDF ----------------
def img2pdf_ui():
    st.title("📷 Images → PDF")

    files = st.file_uploader("Upload Images", accept_multiple_files=True)

    if files and st.button("Convert"):
        pdf = tools.images_to_pdf(files)

        st.download_button("Download PDF", pdf, file_name="images.pdf")


# ---------------- ROTATE ----------------
def rotate_ui():
    st.title("🔄 Rotate PDF")

    file = st.file_uploader("Upload PDF")

    if file and st.button("Rotate"):
        pdf = tools.rotate_pdf(file)

        st.download_button("Download", pdf, file_name="rotated.pdf")


# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "merge":
    merge_ui()

elif st.session_state.page == "split":
    split_ui()

elif st.session_state.page == "pdf2img":
    pdf2img_ui()

elif st.session_state.page == "img2pdf":
    img2pdf_ui()

elif st.session_state.page == "rotate":
    rotate_ui()
