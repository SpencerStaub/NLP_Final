# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 04/07/2021

# ======================================================================================================================
# Import Spacy and other associated libraries

import spacy
import os

nlp = spacy.load('en_core_web_sm')

# ======================================================================================================================
# Import all files into a document corpus

dir_base = 'C:/Users/super/Desktop/6312/Group Project 1/data'


def read_file(file_name):
    """
    :param file_name: The file to be read in.
    :return: The text contained within the given file.
    """
    file_text = open(file_name, encoding='utf-8').read()

    return file_text


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
# Finding all person entities in book one

book_one = book_corpus[0]['content']

book_one = book_one.lower()

for chapter_number in range(1, 62):
    if chapter_number == 61:
        chapter = book_one.split('chapter ' + str(chapter_number))[1]
        chapter = chapter.split('acknowledgments')[0]

        analyzed_chapter = nlp(chapter)

        chapter_persons = []

        for entity in analyzed_chapter.ents:
            if entity.text.strip() != '':
                if entity.label_ == 'PERSON':
                    if entity.text.strip() not in chapter_persons:
                        chapter_persons.append(entity.text.strip())

        print('Persons in Chapter {}:'.format(str(chapter_number)))

        for person in chapter_persons:
            print(person)

        print('\n')
    else:
        chapter = book_one.split('chapter ' + str(chapter_number))[1]
        chapter = chapter.split('chapter ' + str(chapter_number + 1))[0]

        analyzed_chapter = nlp(chapter)

        chapter_persons = []

        for entity in analyzed_chapter.ents:
            if entity.text.strip() != '':
                if entity.label_ == 'PERSON':
                    if entity.text.strip() not in chapter_persons:
                        chapter_persons.append(entity.text.strip())

        print('Persons in Chapter {}:'.format(str(chapter_number)))

        for person in chapter_persons:
            print(person)

        print('\n')
