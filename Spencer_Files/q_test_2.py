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

input_file = pd.read_csv("book_3.csv")

df_test = input_file[input_file['ent_label'].isin(['Date','Event','GPE','LOC','PERSON'])]

#df_test = input_file[input_file['ent_label'].isin([list_of_people])]

df_test = df_test.groupby(['sentence', 'ent_word' ,'ent_label']).size()

df_test_gb = df_test.groupby(['sentence']).size().reset_index()

df_test_gb = df_test_gb[df_test_gb[0] > 2]

print(df_test_gb.head())

for i in df_test_gb['sentence']:
    df_subset = input_file[input_file['sentence']==i]
    subject_line = df_subset[(df_subset['dep']=='nsubj') & (df_subset['ent_label']=='PERSON')]
    verb_line = df_subset[(df_subset['pos'] == 'VERB') & (df_subset['dep'] == 'ROOT')]
    verb_line_2 = df_subset[(df_subset['pos'] == 'VERB') & (df_subset['dep'] != 'ROOT')]
    object_line = df_subset[((df_subset['dep'] == 'dobj') | (df_subset['dep'] == 'conj')) & (df_subset['ent_label']=='PERSON')]
    conjuct_line = df_subset[(df_subset['dep'] == 'conj')]
    adverb_line = df_subset[(df_subset['dep'] == 'advmod')]

    sent = subject_line["sentence"].values
    subject = subject_line["ent_word"].values
    verb = verb_line['tokens'].values
    verb_2 = verb_line['tokens'].values 
    object = object_line['tokens'].values
    conjuct = conjuct_line['tokens'].values
    adverb = adverb_line['tokens'].values

    if subject.size == 1 and verb.size == 1 and object.size > 1:
        print(subject, verb, verb_2, object, conjuct, adverb)
        print(sent)
        if verb == ['said']:
            print("What did ", subject, " say to ", object, "and", conjuct)
        else:
            print("What did ", subject, " do with ", object[0], "and", object[1])

        print("Answer: ", verb, adverb, verb_2)

    # DOES NOT WORK ^^^^^^^^



print(spacy.explain('dobj'))
print(spacy.explain('conj'))
print(spacy.explain('pobj'))