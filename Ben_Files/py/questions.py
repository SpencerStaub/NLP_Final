# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 10 May 2021

# ======================================================================================================================
# Importing all necessary libraries

from os import path
import pandas as pd
import random

# ======================================================================================================================
# Reading in the appropriate files.

base_path = path.dirname(__file__)

file_path = path.abspath(path.join(base_path, '..', 'data'))

book_1_unique_words = pd.read_csv(file_path + '/cleaned/unique_words/book_1_unique_words_by_chapter.csv', header=0)

book_2_unique_words = pd.read_csv(file_path + '/cleaned/unique_words/book_2_unique_words_by_chapter.csv', header=0)

book_3_unique_words = pd.read_csv(file_path + '/cleaned/unique_words/book_3_unique_words_by_chapter.csv', header=0)

book_4_unique_words = pd.read_csv(file_path + '/cleaned/unique_words/book_4_unique_words_by_chapter.csv', header=0)

# ======================================================================================================================
# Taking in input for what book questions will be generated off of.

continue_selection = 'yes'

book_one_count = 1

book_two_count = 1

book_three_count = 1

book_four_count = 1

while continue_selection == 'yes':
    book_selection_input = str(input('What book would you like to generate questions from? Please type one of the following:\n\nBook One | Book Two | Book Three | Book Four\n\nAnswer: '))

    number_of_questions = int(input('\nHow many questions would you like to be asked? Questions will cover the entirety of the book.\n\nNumber of questions: '))

    # ==================================================================================================================
    # Creating a sub_selection
    # ==================================================================================================================
    # Generating questions for book one.

    if book_selection_input == 'Book One':
        quiz = 'Quiz #' + str(book_one_count) + '\n\n'

        book = 1

        for question in range(1, number_of_questions + 1):
            chapter_number = random.randrange(start=1, stop=61)

            chapter_sub_selection = book_1_unique_words[['Chapter ' + str(chapter_number)]]

            chapter_sub_selection = chapter_sub_selection.dropna().reset_index(drop=True)

            word_number = random.randrange(start=0, stop=len(chapter_sub_selection.index))

            word = chapter_sub_selection['Chapter ' + str(chapter_number)].iloc[word_number]

            quiz += 50 * '-' + '\nQuestion #' + str(question) + ':\n' + 50 * '-' + '\n'

            quiz += 'In Chapter ' + str(chapter_number) + ', the word "' + word + '" appears.\n\nWhat is the definition of "' + word + '"?'

            quiz += '\n\nWhat is a synonym for "' + word + '"?\n\n'

        test_questions = open(file_path + '/cleaned/questions/book_' + str(book) + '/book_' + str(book) + '_quiz_' + str(book_one_count) + '.txt', 'w', encoding='utf-8')

        test_questions.write(quiz)

        test_questions.close()

        print('\nA list of ' + str(number_of_questions) + ' questions have been written to the text file "book_' + str(book) + '_quiz_' + str(book_one_count) + '.txt". See the folder "book_' + str(book) + '" for more details.')

        book_one_count += 1

    elif book_selection_input == 'Book Two':
        quiz = 'Quiz #' + str(book_two_count) + '\n\n'

        book = 2

        for question in range(1, number_of_questions + 1):
            chapter_number = random.randrange(start=1, stop=57)

            chapter_sub_selection = book_2_unique_words[['Chapter ' + str(chapter_number)]]

            chapter_sub_selection = chapter_sub_selection.dropna().reset_index(drop=True)

            word_number = random.randrange(start=0, stop=len(chapter_sub_selection.index))

            word = chapter_sub_selection['Chapter ' + str(chapter_number)].iloc[word_number]

            quiz += 50 * '-' + '\nQuestion #' + str(question) + ':\n' + 50 * '-' + '\n'

            quiz += 'In Chapter ' + str(chapter_number) + ', the word "' + word + '" appears.\n\nWhat is the definition of "' + word + '"?'

            quiz += '\n\nWhat is a synonym for "' + word + '"?\n\n'

        test_questions = open(file_path + '/cleaned/questions/book_' + str(book) + '/book_' + str(book) + '_quiz_' + str(book_two_count) + '.txt', 'w', encoding='utf-8')

        test_questions.write(quiz)

        test_questions.close()

        print('\nA list of ' + str(number_of_questions) + ' questions have been written to the text file "book_' + str(book) + '_quiz_' + str(book_two_count) + '.txt". See the folder "book_' + str(book) + '" for more details.')

        book_two_count += 1

    elif book_selection_input == 'Book Three':
        quiz = 'Quiz #' + str(book_three_count) + '\n\n'

        book = 3

        for question in range(1, number_of_questions + 1):
            chapter_number = random.randrange(start=1, stop=49)

            chapter_sub_selection = book_2_unique_words[['Chapter ' + str(chapter_number)]]

            chapter_sub_selection = chapter_sub_selection.dropna().reset_index(drop=True)

            word_number = random.randrange(start=0, stop=len(chapter_sub_selection.index))

            word = chapter_sub_selection['Chapter ' + str(chapter_number)].iloc[word_number]

            quiz += 50 * '-' + '\nQuestion #' + str(question) + ':\n' + 50 * '-' + '\n'

            quiz += 'In Chapter ' + str(chapter_number) + ', the word "' + word + '" appears.\n\nWhat is the definition of "' + word + '"?'

            quiz += '\n\nWhat is a synonym for "' + word + '"?\n\n'

        test_questions = open(file_path + '/cleaned/questions/book_' + str(book) + '/book_' + str(book) + '_quiz_' + str(book_three_count) + '.txt', 'w', encoding='utf-8')

        test_questions.write(quiz)

        test_questions.close()

        print('\nA list of ' + str(number_of_questions) + ' questions have been written to the text file "book_' + str(book) + '_quiz_' + str(book_three_count) + '.txt". See the folder "book_' + str(book) + '" for more details.')

        book_three_count += 1

    elif book_selection_input == 'Book Four':
        quiz = 'Quiz #' + str(book_four_count) + '\n\n'

        book = 4

        for question in range(1, number_of_questions + 1):
            chapter_number = random.randrange(start=1, stop=39)

            chapter_sub_selection = book_2_unique_words[['Chapter ' + str(chapter_number)]]

            chapter_sub_selection = chapter_sub_selection.dropna().reset_index(drop=True)

            word_number = random.randrange(start=0, stop=len(chapter_sub_selection.index))

            word = chapter_sub_selection['Chapter ' + str(chapter_number)].iloc[word_number]

            quiz += 50 * '-' + '\nQuestion #' + str(question) + ':\n' + 50 * '-' + '\n'

            quiz += 'In Chapter ' + str(
                chapter_number) + ', the word "' + word + '" appears.\n\nWhat is the definition of "' + word + '"?'

            quiz += '\n\nWhat is a synonym for "' + word + '"?\n\n'

        test_questions = open(file_path + '/cleaned/questions/book_' + str(book) + '/book_' + str(book) + '_quiz_' + str(book_four_count) + '.txt', 'w', encoding='utf-8')

        test_questions.write(quiz)

        test_questions.close()

        print('\nA list of ' + str(number_of_questions) + ' questions have been written to the text file "book_' + str(book) + '_quiz_' + str(book_four_count) + '.txt". See the folder "book_' + str(book) + '" for more details.')

        book_four_count += 1

    continue_selection = str(input('\nWould you like to create another question list? Please enter either \'yes\' or \'no\'.\n\nAnswer: '))
