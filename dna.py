import csv
#Command Line Argvs
import sys
#Regular Expressions
import re
#Pandas for CSV reading
import pandas as pd
#OS Operations
import os
#Permutations
import itertools

class DNA:

    def __init__(self):
        #Database path
        self.__dbPath = None

        #Database
        self.__database = None

        #Subject DNA path
        self.__sdnaPath = None

        #Subject DNA
        self.__subjectDNA = None

        #STR Dictorary
        self.__dictionary = {}

        #Match
        self.__match = "No match"

    #Init from Database STR Dictionary
    def __initSTRdict(self):
       # print(self.__database)
        print(self.__database.head(10))
        #for l in list(itertools.product(['A', 'C', 'G', 'T'],repeat=4)):
        #    self.__dictionary[''.join(l)] = 0
        #print(self.__dictionary)

    #Load Database in Memory
    def loadDatabase(self, databasePath):
        """
        Load the Database in Memory
            1.- Check if the Database path is set
            2.- Try to read the csv file using pandas
        return True: If all good
        return False: If somwthing were wrong. Check the read permissions. Check is the file is corrupted 
        """
        self.__dbPath = databasePath
        try:
            #Try to read Database
            self.__database = pd.read_csv(self.__dbPath)
            self.__initSTRdict()
            #All good
            return True
        #Catch General Exception
        except Exception as e:
            #Print Exception
            print(e)
            #An error has ocurred
            return False

    #Load Subject DNA in Memory
    def loadSubjectDNA(self, subjectDNA):
        """
        Load the Subject DNA in Memory
            1.- Check if the Subject DNA path is set
            2.- Try to read the txt file
        return True: If all good
        return False: If somwthing were wrong. Check the read permissions. Check is the file is corrupted 
        """
        #If Subject DNA is set
        self.__sdnaPath = subjectDNA
        try:
            #Try open file using with open
            with open(self.__sdnaPath, "r") as file:
                #Set Subject DNA
                self.__subjectDNA = file.read()
            print(self.__subjectDNA)
            #All good
            return True
        #Catch General Exception
        except Exception as e:
            #Print Exception
            print(e)
            #An error has ocurred
            return False



#Main Function
def main(argv):

    testing = DNA()

    # TODO: Check for command-line usage
    #Check for Arguments
    if len(argv) != 2 or argv[0][-4:].lower() != ".csv" or argv[1][-4:].lower() != ".txt":
        print("Usage: python dna.py data.csv sequence.txt")
        return
    
    #Check Database File if exists 
    if os.path.isfile(argv[0]) == False:
        print("Database file not found")
        return
    
    #Check DNA sequence File if exists
    if os.path.isfile(argv[1] == False):
        print("DNA sequence not found")
        return 

    dbpath, sdnapath = argv[0], argv[1]
    
    # TODO: Read database file into a variable
    testing.loadDatabase(dbpath)

    # TODO: Read DNA sequence file into a variable
   # testing.loadSubjectDNA(sdnapath)

    # TODO: Find longest match of each STR in DNA sequence

    # TODO: Check database for matching profiles

    return

#?????
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

#Entry Point
if __name__ == "__main__":
   main(sys.argv[1:])
