import imp
from reader import Reader
from listener import Listener
from art import tprint
import imp

def logo_draw(): # draw logo project
    tprint('CONVERTER') 

def main():
    logo_draw()
    type_action = input("Enter what you want to do: 'listen' or 'record'. \n")
    file_path = input('Enter the file with the fully specified path to it. \n')

    if type_action == "'listen'" or type_action == 'listen':
        print(Listener.write_file(file_path))
    elif  type_action == "'record'" or type_action == 'record':
        print(Reader.read_file(file_path))


if (__name__ == '__main__'):
    main()
