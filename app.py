import streamlit as st
from pdf2image import convert_from_bytes
import zipfile
import io

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="PDF to Images Pro", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
<div style="text-align:center;">
    <h1>📄➡️🖼️ PDF to Images Pro</h1>
    <p style="font-size:18px; color:gray;">
        Convert your PDF into high-quality images instantly
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=250)

with col2:
    st.markdown("""
    ### 🚀 Fast & Secure Conversion Tool
    ✔ High-quality PNG output  
    ✔ Instant download ZIP  
    ✔ No login required  
    ✔ 100% free tool  
    """)

st.markdown("---")

# ---------------- UPLOAD SECTION ----------------
st.markdown("## 📤 Upload Your PDF")

uploaded_file = st.file_uploader("Drag & Drop PDF here", type=["pdf"])

# ---------------- PROCESS ----------------
if uploaded_file:

    st.success("File uploaded successfully ✅")

    if st.button("🚀 Convert Now"):

        with st.spinner("Converting your PDF... ⏳"):

            images = convert_from_bytes(uploaded_file.read())

            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(zip_buffer, "w") as zip_file:

                for i, image in enumerate(images):

                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format="PNG")
                    img_bytes.seek(0)

                    zip_file.writestr(f"page_{i+1}.png", img_bytes.read())

                    st.image(image, caption=f"Page {i+1}", use_container_width=True)

            zip_buffer.seek(0)

        st.success("Conversion Complete 🎉")

        st.download_button(
            "⬇️ Download All Images (ZIP)",
            zip_buffer,
            file_name="pdf_images.zip",
            mime="application/zip"
        )

else:
    st.info("👈 Upload a PDF to start conversion")