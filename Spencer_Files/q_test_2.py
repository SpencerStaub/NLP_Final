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

for i in df_test_gb['sentence']:
    df_subset = input_file[input_file['sentence']==i]
    subject_line = df_subset[(df_subset['dep']=='nsubj') & (df_subset['ent_label']=='PERSON')]
    verb_line = df_subset[(df_subset['dep'] == 'ROOT')]
    object_line = df_subset[(df_subset['dep'] == 'dobj')]
    conjuct_line = df_subset[(df_subset['dep'] == 'conj')]
    adverb_line = df_subset[(df_subset['dep'] == 'advmod')]






    if len(subject_line) + len(verb_line) > 2:
        sent = subject_line["sentence"].values
        subject = subject_line["ent_word"].values
        verb = df_subset[(df_subset['tokens'])].values
    if len(object_line) > 1:
        object = df_subset[(df_subset['tokens'])].values
    if len(conjuct_line) > 1:
        conjuct = df_subset[(df_subset['tokens'])].values
    if len(adverb_line) > 1:
        adverb = df_subset[(df_subset['tokens'])].values

    print(subject, verb, object, conjuct, adverb)
    print(sent)

    # DOES NOT WORK ^^^^^^^^



print(spacy.explain('dobj'))
print(spacy.explain('conj'))
print(spacy.explain('pobj'))