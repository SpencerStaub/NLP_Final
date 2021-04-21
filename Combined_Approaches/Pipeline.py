#*******************************************************
#imports
import os
import nltk
import spacy
import pandas as pd

#*******************************************************
#Gathering info from a user
print("Design a Quiz")
print("Which book would you like to use?")
print ("Here are your choices:\n")
print("The Best Bad Luck I Ever Had \n The Lions of Little Rock\n The Paper Cowboy\n The Thing I am Most Afraid Of\n Anne of Green Gables")
book = input()

#*******************************************************
#Getting the text/data
if book == "The Best Bad Luck I Ever Had":
    narrator = "Dit"
    text = "Book_1"
    data = "book_1.csv"
elif book == "The Lions of Little Rock":
    narrator = "Marlee"
    text = "Book_2"
    data = 'book_2.csv'
elif book == "The Paper Cowboy":
    narrator = "Tommy"
    text = "Book_3"
    data = 'book_3.csv'
elif book == "The Thing I am Most Afraid Of":
    narrator = "Becca"
    text = "Book_4"
    data = 'book_4.csv'
elif book == "Anne of Green Gables":
    narrator = ''
    text = "Book_5"
    data = "book_1.csv"
else:
    print("I'm sorry. That book is not in our database.")

#*******************************************************
#Loading the data from csv
df = pd.read_csv(data)
#print(df.head())
#print(df.shape)

#*******************************************************
#Creating a file dictionary
#This assumes the files are broken down into chapters in a folder

nlp = spacy.load("en_core_web_sm")

#Creating the file dictionary
# point this to the data directoryDesktop
direc = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Combined_Approaches/" + text
ext = '.txt' # Select your file delimiter

file_dict = {} # Create an empty dict

# Select only files with the ext extension
txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]

# Iterate over your txt files
for f in txt_files:
    # Open them and assign them to file_dict
    with open(os.path.join(direc,f)) as file_object:
        file_dict[f] = file_object.read()

#*******************************************************
#Select which chapter you would like to use
print("\n There are", len(txt_files), 'chapters in', book, '.')
print("Which chapter would you like to analyze?")
chapter = input()

#*******************************************************
#Extract persons -- dictionary approach
def extract_entities(doc_id, doc_text):
    analyzed_doc = nlp(doc_text)
    doc_persons = {}

    for entity in analyzed_doc.ents:
        if entity.text.strip() != "" and entity.label_ == "PERSON":
            prev_token = analyzed_doc[entity.start - 1]
            if prev_token.text in ("Doc", "Dr.", "Mr.", "Mrs.", 'Ms.'):
                name = prev_token.text + ' ' + entity.text.strip()
                if name not in doc_persons.keys():
                    relevant_sentence = (doc_id, entity.sent.text)
                    doc_persons[name] = list()
                if name in doc_persons.keys():
                    relevant_sentence = (doc_id, entity.sent.text)
                    doc_persons[name].append(relevant_sentence)
            else:
                if entity.text.strip() not in doc_persons.keys():
                    relevant_sentence = (doc_id, entity.sent.text)
                    doc_persons[entity.text.strip()] = list()

                if entity.text.strip() in doc_persons.keys():
                    relevant_sentence = (doc_id, entity.sent.text)
                    doc_persons[entity.text.strip()].append(relevant_sentence)

    return doc_persons

#*******************************************************
#Find most popular entities -- dictionary approach
def find_most_popular_entities(entity_dictionary):
    list_most_mentions = {}

    for entity in entity_dictionary:
        x = []
        for i in range(len(entity_dictionary[entity])):
            x.append(len(entity_dictionary[entity][i]))
        list_most_mentions[entity] = sum(x)

    # sort through the entities in the dictionary by the number of sentences

    return list_most_mentions

#*******************************************************
#Finding the people in each chapter
a = extract_entities(chapter + '.txt', file_dict[chapter +'.txt'])
tp = find_most_popular_entities(a)
if len(tp) > 0:
    chapter_persons = pd.DataFrame.from_dict(tp, orient = 'index')
    chapter_persons = chapter_persons.rename(columns = {0:'Count'})
    chapter_persons = chapter_persons.sort_values(by=['Count'], ascending = False)
#print(chapter_persons)

#Creating a List of the top characters in the book
combined_persons = {}

for item in txt_files:
    persons = extract_entities(item, file_dict[item])

    # For Persons
    for per in persons.keys():
        if per not in combined_persons.keys():
            combined_persons[per] = list()

        if per in combined_persons.keys():
            combined_persons[per].append(persons.get(per))

all_characters = find_most_popular_entities(combined_persons)
char_in_book = pd.DataFrame.from_dict(all_characters, orient = 'index')
char_in_book = char_in_book.rename(columns = {0:"Count"})
char_in_book = char_in_book.sort_values(by=['Count'], ascending = False)
main_char = char_in_book.head(20)
people = main_char.index.tolist()

#For question generation:
#We also need to remove the narrator from this list because he/she can't talk to him/herself.
words_remove = ['Moundville', "Negra", "Mary Lou's"]
if narrator in people:
    people.remove(narrator)
else:
    pass

for m in words_remove:
    if m in people:
        people.remove(m)
    else:
        pass
#*******************************************************
#Printing top characters in the book
print("The top 20 characters in this book are:\n Narrator:", narrator, '\n', people, '\n')

#Check the characters in each chapters against the main_character list.
#This makes sure we are asking about a fairly major character, not someone who is mentioned only once.
chapter_characters = []
for i in range(len(chapter_persons)):
    for x in people:
        if chapter_persons.index[i] == x:
            chapter_characters.append(chapter_persons.index[i])
        else:
            pass

#*******************************************************
#Printing major characters in the chapter
print("The characters in chapter", chapter, "are:\n Narrator:", narrator, '\n', chapter_characters, '\n')

#*******************************************************
#Question Generation -- dictionary approach
print(book)
print("Chapter", chapter, ": Questions for Discussion")

#This accounts for if the book has a narrator or not:
if narrator == "":
    narrator = chapter_characters[0]
    i = 1
else:
    i = 0

#This will print up to three character questions per chapter

if len(chapter_characters) == 0:
    pass
elif len(chapter_characters) == 1:
    print("What did", narrator, "talk about with", chapter_characters[i], "?")
elif len(chapter_characters) == 2:
    print("What did", narrator, "talk about with", chapter_characters[i], "?")
    print("What did", narrator, "and", chapter_characters[i+1], "discuss?")
else:
    print("What did", narrator, "talk about with", chapter_characters[i], "?")
    print("What did", narrator, "and", chapter_characters[i+1], "discuss?")
    print("What did", narrator, "say to", chapter_characters[i+2], "?")
#*******************************************************
#ADD DF APPROACH -- PERSON EXTRACTION



#*******************************************************
#ADD DF APPROACH -- LOCATION EXTRACTION??




#*******************************************************
#ADD DF APPROACH -- QUESTION GENERATION




#*******************************************************
#ADD BEN'S UNIQUE WORD CODE HERE





#*******************************************************
print("\n Would you like to print this info to a txt file? yes/no")
answer = input()
if answer == "no":
    pass
else:
    with open('Quiz', 'w') as file:
        print(book, file = file)
        print("\n Chapter", chapter, file = file)
        print("\n Questions for Comprehension", file = file)
        print("\n What did", narrator, "talk about with", chapter_characters[i], "?", file = file)
        print("\n What did", narrator, "and", chapter_characters[i+1], "discuss?", file=file)
        print("\n What did", narrator, "say to", chapter_characters[i+2], "?", file = file)


