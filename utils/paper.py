import os
import streamlit as st
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from io import StringIO






class Paper():
    ## 論文に対する成形処理などを書く
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

        self.pdf_text = self.load_pdf()
        self.pdf_dict = self.text_to_dict()

    def load_pdf(self):
        with open(self.pdf_path, "rb") as pdf_file:
            output = StringIO()
            resource_manager = PDFResourceManager()
            laparams = LAParams()
            text_converter = TextConverter(resource_manager, output, laparams=laparams)
            page_interpreter = PDFPageInterpreter(resource_manager, text_converter)

            for i_page in PDFPage.get_pages(pdf_file):
                page_interpreter.process_page(i_page)

            output_text = output.getvalue()
            output.close()
            text_converter.close()
        os.remove(self.pdf_path)
        return output_text #"".join(output_text.splitlines())
    
    def text_to_dict(self):
        return