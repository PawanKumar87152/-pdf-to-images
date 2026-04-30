import streamlit as st

st.set_page_config(page_title="PDF Studio Pro", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- DARK CANVA UI ----------------
st.markdown("""
<style>

/* background */
body {
    background-color: #0b1220;
    color: white;
}

/* sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
    font-weight: 600;
}

/* title */
.title {
    font-size: 42px;
    font-weight: 900;
    color: #38bdf8;
}

/* subtitle */
.sub {
    color: #94a3b8;
}

/* buttons */
.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 12px;
    font-weight: 700;
    border: none;
    transition: 0.3s;
}

/* hover */
.stButton > button:hover {
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (CANVA STYLE MENU) ----------------
with st.sidebar:

    st.title("📁 PDF STUDIO")

    st.markdown("---")

    if st.button("🏠 Home"):
        st.session_state.page = "home"

    if st.button("📎 Merge PDF"):
        st.session_state.page = "merge"

    if st.button("✂️ Split PDF"):
        st.session_state.page = "split"

    if st.button("🖼️ PDF → Images"):
        st.session_state.page = "pdf2img"

    if st.button("📷 Images → PDF"):
        st.session_state.page = "img2pdf"

    if st.button("📄 Extract Pages"):
        st.session_state.page = "extract"

    if st.button("🗑️ Delete Pages"):
        st.session_state.page = "delete"

# ---------------- HOME ----------------
def home():
    st.markdown("<div class='title'>🎨 PDF STUDIO PRO</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Canva-style Sidebar SaaS PDF Tool</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.info("👈 Select a tool from sidebar to start")

# ---------------- TOOLS (PLACEHOLDERS + READY STRUCTURE) ----------------
def merge():
    st.title("📎 Merge PDF")
    st.write("Upload and merge PDFs here")

def split():
    st.title("✂️ Split PDF")

def pdf2img():
    st.title("🖼️ PDF → Images")

def img2pdf():
    st.title("📷 Images → PDF")

def extract():
    st.title("📄 Extract Pages")

def delete():
    st.title("🗑️ Delete Pages")

# ---------------- ROUTER ----------------
if st.session_state.page == "home":
    home()

elif st.session_state.page == "merge":
    merge()

elif st.session_state.page == "split":
    split()

elif st.session_state.page == "pdf2img":
    pdf2img()

elif st.session_state.page == "img2pdf":
    img2pdf()

elif st.session_state.page == "extract":
    extract()

elif st.session_state.page == "delete":
    delete()
