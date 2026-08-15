import pdfplumber


class PDFParser:

    def extract_text(self, file):
        text = []

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

        return "\n".join(text).strip()


# if __name__ == "__main__":
#     parser = PDFParser()

#     text = parser.extract_text(
#         "./cv.pdf"
#     )

#     print(text)