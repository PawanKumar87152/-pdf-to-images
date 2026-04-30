import streamlit as st

st.set_page_config(page_title="PDF Suite Pro", layout="wide")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- DARK MODE UI ----------------
st.markdown("""
<style>

/* BACKGROUND */
body {
    background-color: #0b1220;
    color: white;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 50px;
    font-weight: 900;
    color: #38bdf8;
}

.sub {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
}

/* FIXED GRID CONTAINER */
.block-container {
    padding-top: 2rem;
}

/* UNIFORM SQUARE BUTTONS */
.stButton > button {
    width: 100%;
    height: 150px;
    border-radius: 16px;
    font-size: 18px;
    font-weight: 900;
    border: none;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
    transition: 0.3s;
}

/* HOVER EFFECT */
.stButton > button:hover {
    transform: scale(1.05);
}

/* TILE COLORS (ALL SAME SIZE) */
div[data-testid="column"]:nth-child(1) button {
    background: #ef4444;
    color: white;
}

div[data-testid="column"]:nth-child(2) button {
    background: #22c55e;
    color: white;
}

div[data-testid="column"]:nth-child(3) button {
    background: #3b82f6;
    color: white;
}

div[data-testid="column"]:nth-child(4) button {
    background: #f59e0b;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HOME ----------------
def home():

    st.markdown("<div class='title'>📄 PDF SUITE PRO</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Dark Mode SaaS PDF Tool Dashboard</div>", unsafe_allow_html=True)

    st.markdown("---")

    # GRID (4 EQUAL TILES)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📎 Merge PDF"):
            st.session_state.page = "merge"

    with col2:
        if st.button("✂️ Split PDF"):
            st.session_state.page = "split"

    with col3:
        if st.button("🖼️ PDF → Images"):
            st.session_state.page = "pdf2img"

    with col4:
        if st.button("📷 Images → PDF"):
            st.session_state.page = "img2pdf"

# ---------------- SIMPLE PAGES ----------------
def merge():
    st.title("📎 Merge PDF")

def split():
    st.title("✂️ Split PDF")

def pdf2img():
    st.title("🖼️ PDF → Images")

def img2pdf():
    st.title("📷 Images → PDF")

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
