import numpy as np
import pandas as pd
from nltk.corpus import reuters
import spacy
import os
import matplotlib.pyplot as plt
from spacy.language import Language
from spacy.tokens import Span
import re




pd.set_option('display.max_columns', None)

nlp = spacy.load("en_core_web_sm")
all_stopwords = nlp.Defaults.stop_words

#Loading the text file
input_file = open("K_Levine_Book_1.txt" , encoding='utf-8').read()
#print(input_file)
type(input_file)



chapters = re.split("Chapter.[^a-z]+", input_file, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters
#chapters = re.split("\s*\n\d+\n([a-zA-Z].+)\n", input_file, flags = re.IGNORECASE) # added for book 2


chapters.pop(0) # Removes the first item in list as this is "


df_ent = pd.DataFrame()

def df_maker(chapters):

    chapter_list = []
    title_list = []
    text_list = []
    sent_list = []
    word_list = []
    entity_list = []
    token_list = []
    token_pos_list = []
    token_lemma_list = []
    token_tag_list = []
    token_dep_list = []
    sent_list_ent = []

    i = 1
    for chapter in chapters:
    #for chapter in range(0,len(chapters),2):

        df_temp = pd.DataFrame()

        first_line = chapter.split('\n', 1)[0]
        #first_line = chapters[chapter] # added for book 2
        text = chapter[chapter.index('\n')+1:]
        #text = chapters[chapter + 1] # added for book 2

        analyzed_doc = nlp(text)

        for entity in analyzed_doc.ents:
                word_list.append(entity.text.strip())
                entity_list.append(entity.label_)


        for tokens in analyzed_doc:
            if not tokens.is_stop and not tokens.is_punct:
                # transform words into their shorter lemmatization
                token = tokens.lemma_.lower()
                # append each word to a list
                if '\n' not in token:
                    token_list.append(str(tokens))
                    title_list.append(first_line)
                    sent_list.append(tokens.sent.text)
                    chapter_list.append("Chapter " + str(i))
                    token_pos_list.append(tokens.pos_)
                    token_lemma_list.append(tokens.lemma_.lower())
                    token_tag_list.append(tokens.tag_)
                    token_dep_list.append(tokens.dep_)

        i = i + 1

    #df_ent['chapter_number'] = chapter_list
    #df_ent['chapter_title'] = title_list
    #df_ent['text'] = text_list
    #df_ent['sentence'] = sent_list
    df_ent['word'] = word_list
    df_ent['entity'] = entity_list
    #df_ent['sentence'] = sent_list_ent

    df_ent_best = df_ent.groupby(['word', 'entity']).size().groupby(level=0).idxmax()\
        .apply(lambda x: x[1]).reset_index(name='entity')



    df_temp['chapter_number'] = chapter_list
    df_temp['chapter_title'] = title_list
    df_temp['tokens'] = token_list
    df_temp['pos'] = token_pos_list
    df_temp['lemma'] = token_lemma_list
    df_temp['tag'] = token_tag_list
    df_temp['dep'] = token_dep_list
    df_temp['sentence'] = sent_list

    #print(df_temp.head())

    df_final = pd.merge(df_temp,df_ent_best, left_on=['tokens'], right_on=['word'] ,how='left')
    df_final = df_final.drop_duplicates(subset=None, keep='first', inplace=False)

    #df_final_temp = df_final[(df_final['tokens'].isin(["Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms.","Mrs","Mrs."])) | (df_final['entity'] == 'PERSON')]

    df_final["title"] = np.where(df_final['tokens'].isin(["Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms.","Mrs","Mrs."]), df_final['tokens'] + " " + df_final['tokens'].shift(-1), None)
    df_final['title'] = df_final['title'].shift(1)

    df_title_temp = df_final.dropna()

    title_dict = dict(zip(df_title_temp['tokens'], df_title_temp['title']))

    df_final['title'] = df_final["tokens"].apply(lambda x: title_dict.get(x))


    return df_final

df_final = df_maker(chapters)


#df_final = pd.merge(df_temp,df_ent, left_on='tokens', right_on='word',how='left')
df_final.to_csv('book_1.csv',index=False, encoding='utf-8-sig')

#for i in range(1, len(chapters)+1): #Loops for the number of chapters in the book, starting at chapter 1
    #writeBook = open("{}.txt".format(i), "w+") #Opens a book with the name of i, if it does not exist, it creates one
    #riteBook.write(chapters[i-1]) #Overwrites what is written in the book with the same chapter in the list
    #writeBook.close() #Finally, it closes the text file
