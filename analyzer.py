import argparse
import os
import string

#/Users/Ratat/Documents/Multi_Mode_Text_Analyzer/test.txt path


# Check the user's choice
def checkArgument(arg):
    if(arg == 'wordcount'):
        wordCount(args)
    elif(arg == 'linecount'):
        lineCount(args)
    elif(arg == 'charcount'):
        charCount(args) 
    elif(arg == 'search'):
        searchWord(args)

# Read file
def readFile(path):
    if(os.path.exists(path)):
        with open(path, 'r') as f:
            text = f.read()
            return text
    else:
        return None
    
# Calculate how many words are in a file
def wordCount(args):
    count = 0
    main_file = readFile(args.path)
    if(main_file is not None):
        if main_file.strip():
            file = main_file.split()
            count = len(file)
            print(f"There are currently {count} words in the file: {os.path.basename(args.path)}") 
        else:
            print("The file is empty")
    else:
        return None

# Calculate how many lines are in the file
def lineCount(args):
    count = 0
    main_file = readFile(args.path)
    if(main_file is not None):
        if main_file.strip():
            file = main_file.splitlines()
            count = len(file)
            print(f"There are currently {count} lines in the file: {os.path.basename(args.path)}")
        else:
            print("The file is empty")
    else:
        return None

def charCount(args):
    count = 0
    main_text = readFile(args.path)
    if(main_text is not None):
        if(main_text.strip()):
            count = len(main_text)
            print(f"There are currentlly {count} characters")
        else:
            print("Empty file")
    else:
        return None

def searchWord(args):
    file= readFile(args.path)
    count = 0
    if(file is not None):
        if(file.strip()):
            if(args.mode == 'search' and args.query == None):
                parser.error('--query is required when --mode is "search"')
            elif(args.mode == 'search' and args.query != None):
                words_array = file.split()
                for el in words_array:
                    clean_word = el.strip(string.punctuation).lower()
                    if(clean_word == (args.query).lower()):
                        count = count + 1
                print(f"'{args.query}' was seen {count} times")
        else:
            print("The file is empty")
        
    else:
        return None
    
            

parser = argparse.ArgumentParser()

#Add arguments
parser.add_argument('path', 
                    help='Choose the path to the file text')
parser.add_argument('--mode', 
                    choices=['wordcount', 'linecount', 'charcount', 'search'], 
                    help="Choose what operation to perform on the file")
parser.add_argument('--query', 
                    help='Helps you count how many times the phrase or word repeats')
parser.add_argument('--verbosity', help='Helps you debug the result')

args = parser.parse_args()

if not args.mode == None:
    checkArgument(args.mode)

print(args.path)
