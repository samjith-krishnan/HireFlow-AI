from .pdf_parser import PDFParser
from .docx_parser import DOCXParser


class ParserFactory:

    @staticmethod
    def get_parser(file):
        filename = file.name.lower()

        if filename.endswith(".pdf"):
            return PDFParser()

        if filename.endswith(".docx"):
            return DOCXParser()

        raise ValueError(
            "Unsupported resume format. "
            "Only PDF and DOCX files are supported."
        )