from accessify import private
from pathlib import Path
import pdfplumber

class Reader():

    @private
    def pdf_read(file_path):
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        pdf_text = ''.join(pages)
        return pdf_text

    @private
    def txt_read(file_path):
        txt_text = open(file_path).readline()
        return txt_text


    def read_file(file_path):
        #try to open file
        if (Path(file_path).is_file() == False) and (Path(file_path).suffix not in ['pdf','docx','doc','txt']):
            return 'unable to open the file!'
        
        match(Path(file_path).suffix):
            case 'pdf':
                return Reader.pdf_read(file_path)
            case 'txt':
                return Reader.txt_read(file_path)
            
