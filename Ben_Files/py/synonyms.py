# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 10 May 2021

# ======================================================================================================================
# Importing all necessary libraries

from os import path
import pandas as pd
from nltk.corpus import wordnet

# ======================================================================================================================
# Reading in the appropriate files.

base_path = path.dirname(__file__)

file_path = path.abspath(path.join(base_path, '..', 'data'))

unique_words = pd.read_csv(file_path + '/cleaned/unique_words/unique_words_by_book.csv', header=0)

# ======================================================================================================================
# Finding all synonyms in Book One and exporting as a CSV.

book_one = unique_words['Book 1']

book_1_synonyms = pd.DataFrame(columns=['Word', 'Synonyms'])

for word in book_one:
    synonyms = []

    if word != word:
        break
    else:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                synonyms.append(lemma.name())

    synonyms_cleaned = []

    [synonyms_cleaned.append(synonym) for synonym in synonyms if synonym not in synonyms_cleaned]

    if len(synonyms_cleaned) == 0:
        dummy_synonym = 'unavailable'

        book_1_synonyms = book_1_synonyms.append({'Word': word, 'Synonyms': dummy_synonym}, ignore_index=True)

    synonyms_string = ''

    for synonym in synonyms_cleaned:
        synonyms_string += synonym + ', '

    synonyms_string = synonyms_string[:-2]

    synonyms_string = synonyms_string.replace('_', ' ')

    book_1_synonyms = book_1_synonyms.append({'Word': word, 'Synonyms': synonyms_string}, ignore_index=True)

book_1_synonyms.to_csv(file_path + '/cleaned/synonyms/book_1_synonyms.csv', index=False)

# ======================================================================================================================
# Finding all synonyms in Book Two and exporting as a CSV.

book_two = unique_words['Book 2']

book_2_synonyms = pd.DataFrame(columns=['Word', 'Synonyms'])

for word in book_two:
    synonyms = []

    if word != word:
        break
    else:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                synonyms.append(lemma.name())

    synonyms_cleaned = []

    [synonyms_cleaned.append(synonym) for synonym in synonyms if synonym not in synonyms_cleaned]

    synonyms_string = ''

    for synonym in synonyms_cleaned:
        synonyms_string += synonym + ', '

    synonyms_string = synonyms_string[:-2]

    synonyms_string = synonyms_string.replace('_', ' ')

    book_2_synonyms = book_2_synonyms.append({'Word': word, 'Synonyms': synonyms_string}, ignore_index=True)

book_2_synonyms.to_csv(file_path + '/cleaned/synonyms/book_2_synonyms.csv', index=False)

# ======================================================================================================================
# Finding all synonyms in Book Three and exporting as a CSV.

book_three = unique_words['Book 3']

book_3_synonyms = pd.DataFrame(columns=['Word', 'Synonyms'])

for word in book_three:
    synonyms = []

    if word != word:
        break
    else:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                synonyms.append(lemma.name())

    synonyms_cleaned = []

    [synonyms_cleaned.append(synonym) for synonym in synonyms if synonym not in synonyms_cleaned]

    synonyms_string = ''

    for synonym in synonyms_cleaned:
        synonyms_string += synonym + ', '

    synonyms_string = synonyms_string[:-2]

    synonyms_string = synonyms_string.replace('_', ' ')

    book_3_synonyms = book_3_synonyms.append({'Word': word, 'Synonyms': synonyms_string}, ignore_index=True)

book_3_synonyms.to_csv(file_path + '/cleaned/synonyms/book_3_synonyms.csv', index=False)

# ======================================================================================================================
# Finding all synonyms in Book Four and exporting as a CSV.

book_four = unique_words['Book 4']

book_4_synonyms = pd.DataFrame(columns=['Word', 'Synonyms'])

for word in book_four:
    synonyms = []

    if word != word:
        break
    else:
        for synonym in wordnet.synsets(word):
            for lemma in synonym.lemmas():
                synonyms.append(lemma.name())

    synonyms_cleaned = []

    [synonyms_cleaned.append(synonym) for synonym in synonyms if synonym not in synonyms_cleaned]

    synonyms_string = ''

    for synonym in synonyms_cleaned:
        synonyms_string += synonym + ', '

    synonyms_string = synonyms_string[:-2]

    synonyms_string = synonyms_string.replace('_', ' ')

    book_4_synonyms = book_4_synonyms.append({'Word': word, 'Synonyms': synonyms_string}, ignore_index=True)

book_4_synonyms.to_csv(file_path + '/cleaned/synonyms/book_4_synonyms.csv', index=False)
