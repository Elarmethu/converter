from reader import Reader
from art import tprint

def logo_draw(): # draw logo project
    tprint('PDF  TO   MP3') 

def main():
    logo_draw()
    file_path = input('Enter file_path: \n')
    print(Reader.read_file(file_path))


if (__name__ == '__main__'):
    main()
