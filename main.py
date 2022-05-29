# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    global f
    f = open(filename, 'r')
    return "Hello World"

print(read_file_content(filename='./story.txt'))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    x = f.read()
    for char in '.,?!':
        x = x.replace(char, '')
    y = x.split()

    for item in y:
        thisDict = {
            item : y.count(item)
        }

        print (thisDict)

    #return {"as": 10, "would": 20}

count_words() 