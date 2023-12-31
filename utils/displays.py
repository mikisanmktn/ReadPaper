from tempfile import NamedTemporaryFile
import streamlit as st

def load_pdf_drak_and_drop():
    uploaded_file = st.file_uploader("PDFファイルを選択してください", type='pdf')
    
    if uploaded_file is not None:
        with NamedTemporaryFile(dir='.', suffix='.pdf', delete=False) as f:
            f.write(uploaded_file.getbuffer())
            uploaded_file_path = f.name
        return uploaded_file_path

def display_pdf():
    st.write("ここに翻訳したPDFを表示")