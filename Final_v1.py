import pandas as pd

#Loading the text file
input_file = open("K_Levine_Book_1.txt" , encoding='utf-8').read()
#print(input_file)
type(input_file)

import re

chapters = re.split("Chapter.[^a-z]+", input_file, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters

chapters.pop(0) # Removes the first item in list as this is "

df_chapters = pd.DataFrame()

chapter_n = []
title = []
text_list = []

for chapter in chapters:
    i = 1
    first_line = chapter.split('\n', 1)[0]
    text = chapter[chapter.index('\n')+1:]
    #text = chapter.split('\n', 1)[1:]
    chapter_n.append("Chapter " + str(i))
    title.append(first_line)
    text_list.append(text)
    i = i + 1

df_chapters['chapter_number'] = chapter_n
df_chapters['chapter_title'] = title
df_chapters['text'] = text_list


#for i in range(1, len(chapters)+1): #Loops for the number of chapters in the book, starting at chapter 1
    #writeBook = open("{}.txt".format(i), "w+") #Opens a book with the name of i, if it does not exist, it creates one
    #riteBook.write(chapters[i-1]) #Overwrites what is written in the book with the same chapter in the list
    #writeBook.close() #Finally, it closes the text file
