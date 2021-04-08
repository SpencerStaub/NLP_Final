import pandas as pd
from nltk.corpus import reuters
import spacy
import os
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

nlp = spacy.load("en_core_web_sm")
all_stopwords = nlp.Defaults.stop_words

#Loading the text file
input_file = open("K_Levine_Book_2.txt" , encoding='utf-8').read()
#print(input_file)
type(input_file)

import re

#chapters = re.split("Chapter.[^a-z]+", input_file, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters
chapters = re.split("\d+\n([A-Z].+)\n", input_file, flags = re.IGNORECASE) # added for book 2

chapters.pop(0) # Removes the first item in list as this is "


df_chapters = pd.DataFrame()

chapter_list = []
title_list = []
text_list = []
sent_list = []
word_list = []
entity_list = []

i = 1

for chapter in range(0,len(chapters),2):


    #first_line = chapter.split('\n', 1)[0]
    first_line = chapters[chapter] # added for book 2
    
    #text = chapter[chapter.index('\n')+1:]
    text = chapters[chapter + 1] # added for book 2

    analyzed_doc = nlp(text)

    for entity in analyzed_doc.ents:
        if entity.text.strip() != "":

            chapter_list.append("Chapter " + str(i))
            title_list.append(first_line)
            text_list.append(analyzed_doc)
            sent_list.append(entity.sent.text)
            word_list.append(entity.text.strip())
            entity_list.append(entity.label_)

    i = i + 1

df_chapters['chapter_number'] = chapter_list
df_chapters['chapter_title'] = title_list
df_chapters['text'] = text_list
df_chapters['sentence'] = sent_list
df_chapters['word'] = word_list
df_chapters['entitiy'] = entity_list

df_chapters.to_csv('book_2.csv',index=False, encoding='utf-8-sig')

#for i in range(1, len(chapters)+1): #Loops for the number of chapters in the book, starting at chapter 1
    #writeBook = open("{}.txt".format(i), "w+") #Opens a book with the name of i, if it does not exist, it creates one
    #riteBook.write(chapters[i-1]) #Overwrites what is written in the book with the same chapter in the list
    #writeBook.close() #Finally, it closes the text file
