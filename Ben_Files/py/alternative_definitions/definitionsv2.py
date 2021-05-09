# Benjamin Lee
# Professor Stephen Kunath
# DATS 6312-10: NLP for Data Science
# Due: 10 May 2021

# ======================================================================================================================
# This is an alternative version of "definitions.py" whereby BeautifulSoup is used to pull definitions from the HTML
# code associated with the webpage containing a given word's definition.

# ======================================================================================================================
# Regarding runtime

# This code takes a ridiculous amount of time to run. In particular, making requests to a webpage and pulling all of the
# HTML takes a proportionately long time. I averaged four second for each request, which means for a corpus of over
# 11,000 words, this code would take roughly twelve hours to finish. In contrast, "definitions.py" takes mere seconds. I
# recommend using "definitions.py", despite its slight inaccuracy in defining the closest synonym of a word rather than
# the word itself.

# ======================================================================================================================
# Importing all necessary libraries

from os import path
import pandas as pd

import re
import requests
from bs4 import BeautifulSoup

# ======================================================================================================================
# Reading in the appropriate files.

base_path = path.dirname(__file__)

file_path = path.abspath(path.join(base_path, '../..', 'data'))

unique_words = pd.read_csv(file_path + '/cleaned/unique_words/unique_words_by_book.csv', header=0)

# ======================================================================================================================
# Finding all definitions in Book One and exporting as a CSV.

book_one = unique_words['Book 1']

book_1_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This process is similar to the process outlined in "definitions.py", but this loop uses BeautifulSoup to retain the
# definitions contained in the meta tags of the dictionary.com webpage for a given word.
for word in book_one:
    if word != word:
        break
    else:
        # Making a request to dictionary.com using the given word in the hyperlink.
        request = requests.get('http://dictionary.reference.com/browse/' + word + '?s=t')

        # Parsing the HTML code using BeautifulSoup.
        soup = BeautifulSoup(request.content, 'html.parser')

        # Finding all instances of the meta tag where the "name" attribute is set to "description".
        meta_soup = soup.find_all('meta', attrs={'name': 'description'})

        if len(meta_soup) > 0:
            # The meta tags contain the definitions; this chunk splits the content of the meta tag to retain only
            # the definition.
            definition = re.split('definition,|See', str(meta_soup[0]))

            # If the content split by the definition has a list length less than two, then the definition is
            # unavailable. There are certainly workarounds, but to generalize this in a loop is tricky.
            if len(definition) < 2:
                definition = 'unavailable'
            else:
                # Assuming the definition list follows the typical format, the actual definition is the second list
                # item. This chunk strips leading and trailing whitespace and capitalizes the first word of the
                # definition.
                definition = definition[1].lstrip().rstrip().capitalize()

            book_1_definitions = book_1_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        # Sometimes, there are no meta tags whose "name" attribute is set to "description". I'm not sure why
        else:
            definition = 'unavailable'

            book_1_definitions = book_1_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_1_definitions.to_csv(file_path + '/cleaned/definitions/book_1_definitions_beautiful_soup.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Two and exporting as a CSV.

book_two = unique_words['Book 2']

book_2_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This process is similar to the process outlined in "definitions.py", but this loop uses BeautifulSoup to retain the
# definitions contained in the meta tags of the dictionary.com webpage for a given word.
for word in book_two:
    if word != word:
        break
    else:
        # Making a request to dictionary.com using the given word in the hyperlink.
        request = requests.get('http://dictionary.reference.com/browse/' + word + '?s=t')

        # Parsing the HTML code using BeautifulSoup.
        soup = BeautifulSoup(request.content, 'html.parser')

        # Finding all instances of the meta tag where the "name" attribute is set to "description".
        meta_soup = soup.find_all('meta', attrs={'name': 'description'})

        if len(meta_soup) > 0:
            # The meta tags contain the definitions; this chunk splits the content of the meta tag to retain only
            # the definition.
            definition = re.split('definition,|See', str(meta_soup[0]))

            # If the content split by the definition has a list length less than two, then the definition is
            # unavailable. There are certainly workarounds, but to generalize this in a loop is tricky.
            if len(definition) < 2:
                definition = 'unavailable'
            else:
                # Assuming the definition list follows the typical format, the actual definition is the second list
                # item. This chunk strips leading and trailing whitespace and capitalizes the first word of the
                # definition.
                definition = definition[1].lstrip().rstrip().capitalize()

            book_2_definitions = book_2_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        # Sometimes, there are no meta tags whose "name" attribute is set to "description". I'm not sure why
        else:
            definition = 'unavailable'

            book_2_definitions = book_2_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_2_definitions.to_csv(file_path + '/cleaned/definitions/book_2_definitions_beautiful_soup.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Three and exporting as a CSV.

book_three = unique_words['Book 3']

book_3_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This process is similar to the process outlined in "definitions.py", but this loop uses BeautifulSoup to retain the
# definitions contained in the meta tags of the dictionary.com webpage for a given word.
for word in book_three:
    if word != word:
        break
    else:
        # Making a request to dictionary.com using the given word in the hyperlink.
        request = requests.get('http://dictionary.reference.com/browse/' + word + '?s=t')

        # Parsing the HTML code using BeautifulSoup.
        soup = BeautifulSoup(request.content, 'html.parser')

        # Finding all instances of the meta tag where the "name" attribute is set to "description".
        meta_soup = soup.find_all('meta', attrs={'name': 'description'})

        if len(meta_soup) > 0:
            # The meta tags contain the definitions; this chunk splits the content of the meta tag to retain only
            # the definition.
            definition = re.split('definition,|See', str(meta_soup[0]))

            # If the content split by the definition has a list length less than two, then the definition is
            # unavailable. There are certainly workarounds, but to generalize this in a loop is tricky.
            if len(definition) < 2:
                definition = 'unavailable'
            else:
                # Assuming the definition list follows the typical format, the actual definition is the second list
                # item. This chunk strips leading and trailing whitespace and capitalizes the first word of the
                # definition.
                definition = definition[1].lstrip().rstrip().capitalize()

            book_3_definitions = book_3_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        # Sometimes, there are no meta tags whose "name" attribute is set to "description". I'm not sure why
        else:
            definition = 'unavailable'

            book_3_definitions = book_3_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_3_definitions.to_csv(file_path + '/cleaned/definitions/book_3_definitions_beautiful_soup.csv', index=False)

# ======================================================================================================================
# Finding all definitions in Book Four and exporting as a CSV.

book_four = unique_words['Book 4']

book_4_definitions = pd.DataFrame(columns=['Word', 'Definition'])

# This process is similar to the process outlined in "definitions.py", but this loop uses BeautifulSoup to retain the
# definitions contained in the meta tags of the dictionary.com webpage for a given word.
for word in book_four:
    if word != word:
        break
    else:
        # Making a request to dictionary.com using the given word in the hyperlink.
        request = requests.get('http://dictionary.reference.com/browse/' + word + '?s=t')

        # Parsing the HTML code using BeautifulSoup.
        soup = BeautifulSoup(request.content, 'html.parser')

        # Finding all instances of the meta tag where the "name" attribute is set to "description".
        meta_soup = soup.find_all('meta', attrs={'name': 'description'})

        if len(meta_soup) > 0:
            # The meta tags contain the definitions; this chunk splits the content of the meta tag to retain only
            # the definition.
            definition = re.split('definition,|See', str(meta_soup[0]))

            # If the content split by the definition has a list length less than two, then the definition is
            # unavailable. There are certainly workarounds, but to generalize this in a loop is tricky.
            if len(definition) < 2:
                definition = 'unavailable'
            else:
                # Assuming the definition list follows the typical format, the actual definition is the second list
                # item. This chunk strips leading and trailing whitespace and capitalizes the first word of the
                # definition.
                definition = definition[1].lstrip().rstrip().capitalize()

            book_4_definitions = book_4_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)
        # Sometimes, there are no meta tags whose "name" attribute is set to "description". I'm not sure why
        else:
            definition = 'unavailable'

            book_4_definitions = book_4_definitions.append({'Word': word, 'Definition': definition}, ignore_index=True)

book_4_definitions.to_csv(file_path + '/cleaned/definitions/book_4_definitions_beautiful_soup.csv', index=False)
