import streamlit as st

from utils import displays, paper, translate

st.set_page_config(
    page_title="Read Paper!", 
    page_icon="📚")

st.header("論文読みが楽になるツール")

st.write("### 論文を読み込み")
uploaded_pdf_path = displays.load_pdf_drak_and_drop()
if uploaded_pdf_path is not None:
    paper = paper.Paper(pdf_path=uploaded_pdf_path)
    with st.expander("論文(En)"):
        st.write(paper.pdf_text)

# Abstract表示

# pdfの内容を翻訳
st.write("### Deepl翻訳結果を表示")
displays.display_pdf()

st.write("### 引用")

with st.sidebar:
    st.write("### 論文についてLLMに質問")