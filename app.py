import streamlit as st
import tools

st.set_page_config(layout="wide")

st.title("📄 PDF24 Clone Pro")

tool = st.selectbox("Choose Tool", [
    "Merge", "Split", "PDF→Images", "Images→PDF",
    "Rotate", "Extract", "Delete", "Reorder",
    "Compress", "Watermark", "Extract Text",
    "Info", "Grayscale", "Duplicate", "Reverse"
])

file = st.file_uploader("Upload File", accept_multiple_files=True)

if tool == "Merge" and file:
    if st.button("Run"):
        out = tools.merge_pdf(file)
        st.download_button("Download", out)

elif tool == "Split" and file:
    if st.button("Run"):
        res = tools.split_pdf(file[0])
        for n, b in res:
            st.download_button(n, b)

elif tool == "PDF→Images" and file:
    if st.button("Run"):
        res = tools.pdf_to_images(file[0])
        for n, b in res:
            st.image(b)
            st.download_button(n, b)

elif tool == "Images→PDF" and file:
    if st.button("Run"):
        out = tools.images_to_pdf(file)
        st.download_button("Download", out)

elif tool == "Rotate" and file:
    if st.button("Run"):
        out = tools.rotate_pdf(file[0])
        st.download_button("Download", out)

elif tool == "Extract" and file:
    pages = st.text_input("Pages (0,1,2)")
    if st.button("Run"):
        out = tools.extract_pages(file[0], list(map(int, pages.split(","))))
        st.download_button("Download", out)

elif tool == "Delete" and file:
    pages = st.text_input("Pages to delete")
    if st.button("Run"):
        out = tools.delete_pages(file[0], list(map(int, pages.split(","))))
        st.download_button("Download", out)

elif tool == "Reorder" and file:
    order = st.text_input("Order (2,0,1)")
    if st.button("Run"):
        out = tools.reorder_pages(file[0], list(map(int, order.split(","))))
        st.download_button("Download", out)

elif tool == "Compress" and file:
    if st.button("Run"):
        out = tools.compress_pdf(file[0])
        st.download_button("Download", out)

elif tool == "Watermark" and file:
    text = st.text_input("Watermark text")
    if st.button("Run"):
        out = tools.watermark_pdf(file[0], text)
        st.download_button("Download", out)

elif tool == "Extract Text" and file:
    if st.button("Run"):
        text = tools.extract_text(file[0])
        st.text_area("Text", text)

elif tool == "Info" and file:
    if st.button("Run"):
        st.write(tools.pdf_info(file[0]))

elif tool == "Grayscale" and file:
    if st.button("Run"):
        out = tools.grayscale_pdf(file[0])
        st.download_button("Download", out)

elif tool == "Duplicate" and file:
    if st.button("Run"):
        out = tools.duplicate_pages(file[0])
        st.download_button("Download", out)

elif tool == "Reverse" and file:
    if st.button("Run"):
        out = tools.reverse_pdf(file[0])
        st.download_button("Download", out)
