# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# 4/13/2021

# ======================================================================================================================
# Importing all necessary libraries and loading the English language model (Spacy).

import spacy
import os

nlp = spacy.load('en_core_web_sm')

# ======================================================================================================================
# Establishing the base directory and reading in the necessary files.

dir_base = 'C:/Users/super/Desktop/6312/Group Project 1/data'


def read_file(filename):
    """
    :param filename: The file to be read in.
    :return: The text contained within the given file.
    """
    input_file_text = open(filename, encoding='utf-8').read()

    return input_file_text


def read_directory_files(directory):
    """
    :param directory: The path to the folder containing the necessary files.
    :return: A list containing the name and content of every file in the given directory.
    """
    file_texts = []

    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    for file in files:
        file_text = read_file(os.path.join(directory, file))

        file_texts.append({'file': file, 'content': file_text})

    return file_texts


book_corpus = read_directory_files(dir_base)

# ======================================================================================================================
# Initializing a variable containing the contents of "K_Levine_Book_1.txt" and finding all unique words.

count = 0

for book in book_corpus:
    file = book['content']

    unique_words = []

    words_dict = {}

    file = file.lower()

    file = nlp(file)

    file_stop_words = nlp.Defaults.stop_words

    file_lemmatized = [token.lemma_ for token in file if not token in file_stop_words]

    file_lemmatized_cleaned = list(filter(lambda lemma: not lemma.startswith(('\t', ' ', '\n', '-', '_', ',', "'", '"', '.',
                                                                              '\'', u'\xa0', '&', '0', '1', '2', '3', '4',
                                                                              '5', '6', '7', '8', '9')), file_lemmatized))

    file_lemmatized_cleaned = list(filter(lambda lemma: not len(lemma) < 3, file_lemmatized_cleaned))

    for val in file_lemmatized_cleaned:
        if ']' in val:
            file_lemmatized_cleaned.remove(val)
        elif '[' in val:
            file_lemmatized_cleaned.remove(val)
        elif '“' in val:
            file_lemmatized_cleaned.remove(val)
        elif '—' in val:
            file_lemmatized_cleaned.remove(val)

    for word in set(file_lemmatized_cleaned):
        if word not in words_dict.keys():
            words_dict[word] = file_lemmatized_cleaned.count(word)
        else:
            words_dict[word] = words_dict.get(word, 0) + 1

    for key, value in words_dict.items():
        if value == 1:
            unique_words.append(key)

    unique_words = sorted(unique_words)

    print('The unique words in book {} are:'.format(book['file']))

    for word in unique_words:
        print(word)

    count += 1

    with open('Book{}_UniqueWords.txt'.format(count), 'w', encoding='utf-8') as f:
        for item in unique_words:
            f.write('%s\n' % item)
