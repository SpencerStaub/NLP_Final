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
# Finding all definitions in Book One and exporting as a CSV.

book_one = unique_words['Book 1']

# Creating an empty DataFrame to fill with words and their definition.
book_1_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This loop goes through the values in the "Book 1" column of the "unique_words" DataFrame, finds the definition of
# the respective word. The first portion of the outer conditional handles cases where the word doesn't exist, while the
# second portion handles definition assignment.
for word in book_one:
    # There are different numbers of unique words for each book, and thus the length of "unique_words" is defined only
    # by the book with the largest number of words. All books with fewer numbers of unique words fill the empty spots
    # with nan; a value that is nan is by definition not equal to itself.
    if word != word:
        break
    else:
        # A drawback of using the wordnet corpus reader is that it can only take definitions of synonyms. In cases where
        # the synonym registered is a loosely related word, the definition retained could be very different from the
        # definition of the actual word.
        synonyms = wordnet.synsets(word)

        if len(synonyms) > 0:
            definition = synonyms[0].definition()

            book_1_definitions = book_1_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        # In certain cases, a word will have no definition. In this scenario, the definition is declared "unavailable".
        else:
            definition = 'unavailable'

            book_1_definitions = book_1_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_1_definitions.to_csv(file_path + '/cleaned/definitions/book_1_definitions.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Two and exporting as a CSV.

book_two = unique_words['Book 2']

# The same process is repeated for Book Two.
book_2_definitions = pd.DataFrame(columns=['Word', 'Definition'])

for word in book_two:
    if word != word:
        break
    else:
        synonyms = wordnet.synsets(word)

        if len(synonyms) > 0:
            definition = synonyms[0].definition()

            book_2_definitions = book_2_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        else:
            definition = 'unavailable'

            book_2_definitions = book_2_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_2_definitions.to_csv(file_path + '/cleaned/definitions/book_2_definitions.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Three and exporting as a CSV.

book_three = unique_words['Book 3']

# The same process is repeated for Book Three.
book_3_definitions = pd.DataFrame(columns=['Word', 'Definition'])

for word in book_three:
    if word != word:
        break
    else:
        synonyms = wordnet.synsets(word)

        if len(synonyms) > 0:
            definition = synonyms[0].definition()

            book_3_definitions = book_3_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        else:
            definition = 'unavailable'

            book_3_definitions = book_3_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_3_definitions.to_csv(file_path + '/cleaned/definitions/book_3_definitions.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Four and exporting as a CSV.

book_four = unique_words['Book 4']

# The same process is repeated for Book Four.
book_4_definitions = pd.DataFrame(columns=['Word', 'Definition'])

for word in book_four:
    if word != word:
        break
    else:
        synonyms = wordnet.synsets(word)

        if len(synonyms) > 0:
            definition = synonyms[0].definition()

            book_4_definitions = book_4_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        else:
            definition = 'unavailable'

            book_4_definitions = book_4_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_4_definitions.to_csv(file_path + '/cleaned/definitions/book_4_definitions.csv', index=False)
