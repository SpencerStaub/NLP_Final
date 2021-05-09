#Preprocessing Text Files
#This code takes the text document for each book and breaks it down by chapter

#Create directories for files:
import os
import os.path
import re

path_1 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_1/"
path_2 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_2/"
path_3 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_3/"
path_4 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_4/"
path_5 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_5/"
path_6 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_6/"
path_7 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_7/"
path_8 = "/Users/kristinlevine/Documents/GitHub/NLP_Group/Kristin_Files/Book_8/"

list_of_paths = [path_1, path_2, path_3, path_4, path_5, path_6, path_7, path_8]
list_of_files = ["K_Levine_Book_1.txt", "K_Levine_Book_2.txt", "K_Levine_Book_3.txt", "K_Levine_Book_4.txt", "Anne_Green_Gables.txt", "Little_Women.txt", "Wizard_Oz.txt", "Secret_Garden.txt"]

for i in range(len(list_of_paths)):
    if not os.path.exists(list_of_paths[i]):
        os.makedirs(list_of_paths[i])

#Splitting the files
for f in range(len(list_of_files)):
    book = open(list_of_files[f], "r") #Here we open the book
    book = str(book.read()) #this is now assigning book the value of book.txt, not just the location
    chapters = re.split("CHAPTER", book, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters
    chapters.pop(0) # Removes the first item in list as this is ""
    for i in range(1, len(chapters)+1): #Loops for the number of chapters in the book, starting at chapter 1
        completeName = os.path.join(list_of_paths[f], "{}.txt".format(i))
        writeBook = open(completeName, "w+") #Opens a book with the name of i, if it does not exist, it creates one
        writeBook.write(chapters[i-1]) #Overwrites what is written in the book with the same chapter in the list
        writeBook.close() #Finally, it closes the text file

#The chapter divisions were slightly different in these books, so we had to split the files using a line break instead of the word "chapter."
list_of_paths = [path_2, path_3]
list_of_files = ["K_Levine_Book_2.txt", "K_Levine_Book_3.txt"]


#Splitting the files
for f in range(len(list_of_files)):
    book = open(list_of_files[f], "r") #Here we open the book
    book = str(book.read()) #this is now assigning book the value of book.txt, not just the location
    chapters = re.split('\n\d', book, flags = re.IGNORECASE) #Finds all the chapter markers in the book and makes a list of all the chapters
    chapters.pop(0) # Removes the first item in list as this is ""
    for i in range(1, len(chapters)+1): #Loops for the number of chapters in the book, starting at chapter 1
        completeName = os.path.join(list_of_paths[f], "{}.txt".format(i))
        writeBook = open(completeName, "w+") #Opens a book with the name of i, if it does not exist, it creates one
        writeBook.write(chapters[i-1]) #Overwrites what is written in the book with the same chapter in the list
        writeBook.close() #Finally, it closes the text file