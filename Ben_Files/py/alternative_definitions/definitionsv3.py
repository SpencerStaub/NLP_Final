# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 10 May 2021

# ======================================================================================================================
# This is an alternative version of "definitions.py" whereby PyDictionary is used to pull definitions for a given word
# from the WordNet corpus reader. The results were more or less the same as "definitions.py": the definition of the
# closest synonym is generated instead of the given word.

# ======================================================================================================================
# Importing all necessary libraries

from os import path
import pandas as pd
from PyDictionary import PyDictionary

# ======================================================================================================================
# Reading in the appropriate files.

base_path = path.dirname(__file__)

file_path = path.abspath(path.join(base_path, '../..', 'data'))

unique_words = pd.read_csv(file_path + '/cleaned/unique_words/unique_words_by_book.csv', header=0)

# ======================================================================================================================
# Finding all definitions in Book One and exporting as a CSV.

book_one = unique_words['Book 1']

book_1_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This process uses PyDictionary, which may not be installed on your machine. In any case, PyDictionary uses wordnet to
# find definitions, and unfortunately still takes the definition of the closest synonym of the word. This is no more
# efficient than "definitions.py".
for word in book_one:
    definition = PyDictionary.meaning(word)

    book_1_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_1_definitions.to_csv(file_path + '/cleaned/definitions/book_1_definitions_beautiful_soup.csv', index=False)
