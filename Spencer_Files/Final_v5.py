import numpy as np
import pandas as pd
from nltk.corpus import reuters
import spacy
import os
import matplotlib.pyplot as plt
from spacy.language import Language
from spacy.tokens import Span
import pprint
import itertools
import re
import pke
import string
from nltk.corpus import stopwords

from summarizer import Summarizer

pd.set_option('display.max_columns', None)

nlp = spacy.load("en_core_web_sm")
all_stopwords = nlp.Defaults.stop_words

model = Summarizer()

#Loading the text file
input_file = open("K_Levine_Book_4.txt" , encoding='utf-8').read()
#print(input_file)
type(input_file)

#chapters = re.split("Chapter.[^a-z]+", input_file, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters
#chapters = re.split("\s*\n\d+\n([a-zA-Z].+)\n", input_file, flags = re.IGNORECASE) # added for book 2 and 3
chapters = re.split("Chapter\s\d+\n([a-zA-Z].+)\n", input_file, flags = re.IGNORECASE) # added for book 4

#print(chapters)

chapters.pop(0) # Removes the first item in list as this is "

#chapters = chapters[0:2]

#print(chapters)

df_ent = pd.DataFrame()

def df_maker(chapters):

    chapter_list = []
    title_list = []
    sent_list = []
    entity_list = []
    token_list = []
    token_pos_list = []
    token_lemma_list = []
    token_tag_list = []
    token_dep_list = []
    ent_word_list = []
    chap_sum = []
    text_list = []

    i = 1
    #for chapter in chapters:
    for chapter in range(0,len(chapters),2): #added for book 2,3 and 4

        #print(i)

        df_temp = pd.DataFrame()

        #first_line = chapter.split('\n', 1)[0]
        first_line = chapters[chapter] # added for book 2,3 and 4
        #text = chapter[chapter.index('\n')+1:]
        text = chapters[chapter + 1] # added for book 2,3 and 4
        #text_sum = model(text, min_length=50, max_length=150, ratio=0.6)

        analyzed_doc = nlp(text)

        for tokens in analyzed_doc:
            if not tokens.is_stop and not tokens.is_punct:
                # transform words into their shorter lemmatization
                token = tokens.lemma_.lower()

                analyzed_sent = nlp(tokens.sent.text)

                for entity in analyzed_sent.ents:
                    # append each word to a list
                    if '\n' not in token:
                        token_list.append(str(tokens))
                        title_list.append(first_line)
                        chapter_list.append("Chapter " + str(i))
                        token_pos_list.append(tokens.pos_)
                        token_lemma_list.append(tokens.lemma_.lower())
                        token_tag_list.append(tokens.tag_)
                        token_dep_list.append(tokens.dep_)
                        ent_word_list.append(entity.text.strip())
                        entity_list.append(entity.label_)
                        sent_list.append(tokens.sent.text)
                        #chap_sum.append(text_sum)

        i = i + 1

    df_temp['chapter_number'] = chapter_list
    df_temp['chapter_title'] = title_list
    df_temp['tokens'] = token_list
    df_temp['pos'] = token_pos_list
    df_temp['lemma'] = token_lemma_list
    df_temp['tag'] = token_tag_list
    df_temp['dep'] = token_dep_list
    df_temp['sentence'] = sent_list
    df_temp['ent_word'] = ent_word_list
    df_temp['ent_label'] = entity_list
    #df_temp['summary'] = chap_sum

    #print(df_temp.head())

    df_temp_best_ent = df_temp.groupby(['ent_word', 'ent_label']).size().groupby(level=0).idxmax()\
        .apply(lambda x: x[1]).reset_index(name='ent_label')

    df_final = pd.merge(df_temp, df_temp_best_ent, how='right')

    df_final = df_final.drop_duplicates(subset=None, keep='first', inplace=False)

    df_final["title"] = np.where(df_final['tokens'].isin(["Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms.","Mrs","Mrs."]), df_final['tokens'] + " " + df_final['tokens'].shift(-1), None)

    df_final["ent_word"] = np.where(df_final.apply(lambda x: x.tokens in x.ent_word, axis=1),df_final["ent_word"], None)
    df_final["ent_label"] = np.where(df_final["ent_word"].notna(), df_final["ent_label"],None)

    df_final['title'] = df_final['title'].shift(1)

    df_title_temp = df_final.dropna()

    title_dict = dict(zip(df_title_temp['tokens'], df_title_temp['title']))

    df_final['title'] = df_final["tokens"].apply(lambda x: title_dict.get(x))

    return df_final


df_final = df_maker(chapters)


#df_final = pd.merge(df_temp,df_ent, left_on='tokens', right_on='word',how='left')
df_final.to_csv('book_1.csv',index=False, encoding='utf-8-sig')
#df_chap_sum.to_csv('book_2_summary.csv',index=False, encoding='utf-8-sig')
