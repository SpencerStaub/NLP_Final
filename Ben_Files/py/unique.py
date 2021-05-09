# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 10 May 2021

# ======================================================================================================================
# This file generates a list of all unique words found within a given book and outputs them as a CSV file. In
# particular, CSV files containing unique words by book and by chapter are generated.

# ======================================================================================================================
# Importing all necessary libraries

from os import path
import pandas as pd

# ======================================================================================================================
# Reading in the appropriate files.

base_path = path.dirname(__file__)

file_path = path.abspath(path.join(base_path, '..', 'data'))

book_1 = pd.read_csv(file_path + '/raw/book_1.csv', header=0)

book_2 = pd.read_csv(file_path + '/raw/book_2.csv', header=0)

book_3 = pd.read_csv(file_path + '/raw/book_3.csv', header=0)

book_4 = pd.read_csv(file_path + '/raw/book_4.csv', header=0)

# ======================================================================================================================
# Sorting books, filtering by chapters and creating and exporting DataFrames containing unique words.

# ---------
# Book One
# ---------

# Sorting by chapter number.
book_1 = book_1.sort_values(by='chapter_number').reset_index(drop=True)

# Removing all entities (i.e. proper nouns); the focus of this code is on unique words, not characters.
book_1 = book_1[book_1['pos'] != 'PROPN'].reset_index(drop=True)

# Removing tokens that start with spaces, non-breaking spaces, and racial slurs.
banned_words = [' ', "u'\xa0'", 'nigger', 'niggers']

book_1 = book_1[~book_1['tokens'].isin(banned_words)].reset_index(drop=True)

# Removing dates and tokens that start with numbers.
book_1 = book_1[~book_1['tokens'].str.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))].reset_index(drop=True)

# Removing tokens that contain a forward slash; this is a reference to hyperlinks that registered as tokens.
book_1 = book_1[~book_1['tokens'].str.contains('/')].reset_index(drop=True)

# Removing tokens that contain left brackets.
book_1 = book_1[~book_1['tokens'].str.contains("\[")].reset_index(drop=True)

# Removing tokens that contain right brackets.
book_1 = book_1[~book_1['tokens'].str.contains("\]")].reset_index(drop=True)

# Removing tokens that contain spaces.
book_1 = book_1[~book_1['tokens'].str.contains(' ')].reset_index(drop=True)

# Dropping tokens that appear more than once in a chapter.
book_1 = book_1.drop_duplicates(subset=['chapter_number', 'tokens']).reset_index(drop=True)

# Lowercasing all tokens.
book_1['tokens'] = book_1['tokens'].str.lower()

# Creating a DataFrame that will contain all unique words by chapter. This is initialized by filling it with unique
# words from chapter one.
unique_chapter_words = book_1[book_1['chapter_number'] == 'Chapter 1']

# Removing all columns in the DataFrame other than the column containing unique words.
unique_chapter_words = unique_chapter_words[['tokens']]

# Renaming the column containing unique words to the chapter it's based off of.
unique_chapter_words = unique_chapter_words.rename(columns={'tokens': 'Chapter 1'})

# This for loop iterates through the book DataFrame and appends unique words from each chapter to the unique chapter
# words DataFrame as a new column.
for chapter_number in range(2, len(book_1['chapter_number'].unique().tolist()) + 1):
    chapter_df = book_1[book_1['chapter_number'] == 'Chapter ' + str(chapter_number)]

    chapter_df = chapter_df[['tokens']].reset_index(drop=True)

    chapter_df = chapter_df.rename(columns={'tokens': 'Chapter ' + str(chapter_number)})

    unique_chapter_words = unique_chapter_words.join(chapter_df)

# Exporting the unique chapter words DataFrame to a CSV.
unique_chapter_words.to_csv(file_path + '/cleaned/unique_words/book_1_unique_words_by_chapter.csv', index=False)

# ---------
# Book Two
# ---------

# Repeating the process for book two.
book_2 = book_2.sort_values(by='chapter_number').reset_index(drop=True)

book_2 = book_2[book_2['pos'] != 'PROPN'].reset_index(drop=True)

banned_words = [' ', "u'\xa0'", 'nigger', 'niggers']

book_2 = book_2[~book_2['tokens'].isin(banned_words)].reset_index(drop=True)

book_2 = book_2[~book_2['tokens'].str.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))].reset_index(drop=True)

book_2 = book_2[~book_2['tokens'].str.contains('/')].reset_index(drop=True)

book_2 = book_2[~book_2['tokens'].str.contains("\[")].reset_index(drop=True)

book_2 = book_2[~book_2['tokens'].str.contains("\]")].reset_index(drop=True)

book_2 = book_2[~book_2['tokens'].str.contains(' ')].reset_index(drop=True)

book_2 = book_2.drop_duplicates(subset=['chapter_number', 'tokens']).reset_index(drop=True)

book_2['tokens'] = book_2['tokens'].str.lower()

unique_chapter_words = book_2[book_2['chapter_number'] == 'Chapter 1']

unique_chapter_words = unique_chapter_words[['tokens']]

unique_chapter_words = unique_chapter_words.rename(columns={'tokens': 'Chapter 1'})

for chapter_number in range(2, len(book_2['chapter_number'].unique().tolist()) + 1):
    chapter_df = book_2[book_2['chapter_number'] == 'Chapter ' + str(chapter_number)]

    chapter_df = chapter_df[['tokens']].reset_index(drop=True)

    chapter_df = chapter_df.rename(columns={'tokens': 'Chapter ' + str(chapter_number)})

    unique_chapter_words = unique_chapter_words.join(chapter_df)

unique_chapter_words.to_csv(file_path + '/cleaned/unique_words/book_2_unique_words_by_chapter.csv', index=False)

# -----------
# Book Three
# -----------

# Repeating the process for book three.
book_3 = book_3.sort_values(by='chapter_number').reset_index(drop=True)

book_3 = book_3[book_3['pos'] != 'PROPN'].reset_index(drop=True)

banned_words = [' ', "u'\xa0'", 'nigger', 'niggers']

book_3 = book_3[~book_3['tokens'].isin(banned_words)].reset_index(drop=True)

book_3 = book_3[~book_3['tokens'].str.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))].reset_index(drop=True)

book_3 = book_3[~book_3['tokens'].str.contains('/')].reset_index(drop=True)

book_3 = book_3[~book_3['tokens'].str.contains("\[")].reset_index(drop=True)

book_3 = book_3[~book_3['tokens'].str.contains("\]")].reset_index(drop=True)

book_3 = book_3[~book_3['tokens'].str.contains(' ')].reset_index(drop=True)

book_3 = book_3.drop_duplicates(subset=['chapter_number', 'tokens']).reset_index(drop=True)

book_3['tokens'] = book_3['tokens'].str.lower()

unique_chapter_words = book_3[book_3['chapter_number'] == 'Chapter 1']

unique_chapter_words = unique_chapter_words[['tokens']]

unique_chapter_words = unique_chapter_words.rename(columns={'tokens': 'Chapter 1'})

for chapter_number in range(2, len(book_3['chapter_number'].unique().tolist()) + 1):
    chapter_df = book_3[book_3['chapter_number'] == 'Chapter ' + str(chapter_number)]

    chapter_df = chapter_df[['tokens']].reset_index(drop=True)

    chapter_df = chapter_df.rename(columns={'tokens': 'Chapter ' + str(chapter_number)})

    unique_chapter_words = unique_chapter_words.join(chapter_df)

unique_chapter_words.to_csv(file_path + '/cleaned/unique_words/book_3_unique_words_by_chapter.csv', index=False)

# ----------
# Book Four
# ----------

# Repeating the process for book four.
book_4 = book_4.sort_values(by='chapter_number').reset_index(drop=True)

book_4 = book_4[book_4['pos'] != 'PROPN'].reset_index(drop=True)

banned_words = [' ', "u'\xa0'", 'nigger', 'niggers']

book_4 = book_4[~book_4['tokens'].isin(banned_words)].reset_index(drop=True)

book_4 = book_4[~book_4['tokens'].str.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))].reset_index(drop=True)

book_4 = book_4[~book_4['tokens'].str.contains('/')].reset_index(drop=True)

book_4 = book_4[~book_4['tokens'].str.contains("\[")].reset_index(drop=True)

book_4 = book_4[~book_4['tokens'].str.contains("\]")].reset_index(drop=True)

book_4 = book_4[~book_4['tokens'].str.contains(' ')].reset_index(drop=True)

book_4 = book_4.drop_duplicates(subset=['chapter_number', 'tokens']).reset_index(drop=True)

book_4['tokens'] = book_4['tokens'].str.lower()

unique_chapter_words = book_4[book_4['chapter_number'] == 'Chapter 1']

unique_chapter_words = unique_chapter_words[['tokens']]

unique_chapter_words = unique_chapter_words.rename(columns={'tokens': 'Chapter 1'})

for chapter_number in range(2, len(book_4['chapter_number'].unique().tolist()) + 1):
    chapter_df = book_4[book_4['chapter_number'] == 'Chapter ' + str(chapter_number)]

    chapter_df = chapter_df[['tokens']].reset_index(drop=True)

    chapter_df = chapter_df.rename(columns={'tokens': 'Chapter ' + str(chapter_number)})

    unique_chapter_words = pd.concat([unique_chapter_words, chapter_df], axis=1)

unique_chapter_words.to_csv(file_path + '/cleaned/unique_words/book_4_unique_words_by_chapter.csv', index=False)

# ======================================================================================================================
# Creating and exporting a DataFrame containing all unique words by book.

book_1_unique_words = book_1.drop_duplicates(subset='tokens').reset_index(drop=True)

book_1_unique_words = book_1_unique_words[['tokens']]

book_1_unique_words = book_1_unique_words.rename(columns={'tokens': 'Book 1'})

book_2_unique_words = book_2.drop_duplicates(subset='tokens').reset_index(drop=True)

book_2_unique_words = book_2_unique_words[['tokens']]

book_2_unique_words = book_2_unique_words.rename(columns={'tokens': 'Book 2'})

book_3_unique_words = book_3.drop_duplicates(subset='tokens').reset_index(drop=True)

book_3_unique_words = book_3_unique_words[['tokens']]

book_3_unique_words = book_3_unique_words.rename(columns={'tokens': 'Book 3'})

book_4_unique_words = book_4.drop_duplicates(subset='tokens').reset_index(drop=True)

book_4_unique_words = book_4_unique_words[['tokens']]

book_4_unique_words = book_4_unique_words.rename(columns={'tokens': 'Book 4'})

unique_book_words = book_1_unique_words.copy(deep=True)

unique_book_words = pd.concat([unique_book_words, book_2_unique_words], axis=1)

unique_book_words = pd.concat([unique_book_words, book_3_unique_words], axis=1)

unique_book_words = pd.concat([unique_book_words, book_4_unique_words], axis=1)

unique_book_words.to_csv(file_path + '/cleaned/unique_words/unique_words_by_book.csv', index=False)
