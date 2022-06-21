from art import tprint
from gtts import gTTS
from pathlib import Path
import pdfplumber

def pdf_to_mp3(file_path = 'test.pdf'):
    if (Path(file_path).is_file() == False) or (Path(file_path).suffix != '.pdf'): # check file information
        return 'File not exist in path!';
    
    #open pdf file and read them
    with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    #get pdf information to text
    pdftext = ''.join(pages)
    tts = gTTS(pdftext, lang='en', slow=False)
    file_name = Path(file_path).stem #get file name without suffix

    #save our mp3 file.
    tts.save(f'{file_name}.mp3')
    return f'[+] {file_name}.mp3 successfully saved!'

def logo_draw(): # draw logo project
    tprint('PDF  TO   MP3')    



def main():
    logo_draw()

    file_path = input("\n Enter a file's path. \n")
    print(pdf_to_mp3(file_path=file_path))

if (__name__ == '__main__'):
    main()