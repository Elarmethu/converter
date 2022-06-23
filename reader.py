from pathlib import Path
import pdfplumber
import docx


# The class responsible for reading data from files and passing them to the calling object.
class Reader():

    def __pdf_read__(file_path): 
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        pdf_text = ''.join(pages)
        return pdf_text

    def __txt_read__(file_path):
        txt_text = open(file_path).readline()
        return txt_text

    def __doc_read__(file_path):
        text = []
        doc = docx.Document(file_path)
        
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        doc_text = '\n'.join(text)
        return doc_text

    def read_file(file_path):
        #try to open file
        if (Path(file_path).is_file() == False) and (Path(file_path).suffix not in ['pdf','docx','txt']):
            return '[-] Unable to open the file!'
        
        match(Path(file_path).suffix):
            case '.pdf':
                return Reader.__pdf_read__(file_path)
            case '.txt':
                return Reader.__txt_read__(file_path)
            case '.docx':
                return Reader.__doc_read__(file_path)
            case _:
                return '[-] The file cannot be read.'
            
