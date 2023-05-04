#Command Line Argvs
import sys
#Pandas for CSV reading
import pandas as pd
#OS Operations
import os

class MatchDNA:

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

        #Matches
        self.__matches = {}

    #Load Database in Memory
    def loadDatabase(self, databasePath):
        """
        Load the Database in Memory
            1.- Check if the Database path is set
            2.- Try to read the csv file using pandas
        return True: If all good
        return False: If somwthing were wrong. Check the read permissions. Check is the file is corrupted 
        """
        if databasePath == None: return False
        self.__dbPath = databasePath
        try:
            #Try to read Database
            self.__database = pd.read_csv(self.__dbPath)
            #print(self.__database)
            #Read STR to build dictionary
            for strseq in self.__database.columns[1:]: 
               self.__dictionary[strseq] = 0
            #All good
            return True
        #Memory Error & OSError Exception family
        except (MemoryError, OSError) as e:
            print("Memory Error or OS Error " + e)
            return False
        #General Exception
        except Exception as e:
            print("Unexpected Exception: " + e)
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
        if subjectDNA == None: return False
        self.__sdnaPath = subjectDNA
        try:
            #Try open file using with open
            with open(self.__sdnaPath, "r") as file:
                #Set Subject DNA
                self.__subjectDNA = file.read()
            #All good
            return True
        #Memory Error & OSError Exception family
        except (MemoryError, OSError) as e:
            print("Memory Error or OS Error " + e)
            return False
        #General Exception
        except Exception as e:
            print("Unexpected Exception: " + e)
            return False

    #Find Longest STR Match
    def findSTRFromSubjectDNA(self):
        """
        Using longest_match predefine function
        """
        try:
            for strseq in self.__dictionary:
                self.__dictionary[strseq] = longest_match(self.__subjectDNA, strseq)
            return True
        #Memory Error
        except MemoryError as e:
            print("Memory Error: " + e)
            return False
        #General Exception
        except Exception as e:
            print("Unexpected Exception: " + e)
            return False


    #Find Match In Database using Subject DNA
    def findMatchInDatabase(self):
        """
        Find match in the database using the subject DNA
        Iterate over the rows searching for a match
        """
        try:
            #Iterate over the rows on database
            for row in range(len(self.__database)):
                #Iterate over the STR Dictionary
                for strseq in self.__dictionary:
                    #If Match in Database
                    if self.__database.loc[row, strseq ] == self.__dictionary[strseq]:
                        #Add subject to matches
                        if self.__database.loc[row, "name"] not in self.__matches:
                            self.__matches[self.__database.loc[row, "name"]] = 1
                            continue
                        #Increase match count for this subject
                        self.__matches[self.__database.loc[row, "name"]] += 1
            #Print Match percent
            match = False
            for subject in self.__matches:
                #print(subject + " " + str(self.__matches[subject]*100/len(self.__dictionary)) + "%")
                if self.__matches[subject] == len(self.__dictionary):
                    print(subject)
                    match = True
            #If match not found
            if not match: print("No match")
            return True
        except MemoryError as e:
            print("Memory Error " + e)
            return False
        except Exception as e:
            print("Unexpected Exception: " + e)
            return False

    #Print Data
    def printData(self):
        print(self.__database)
        print(self.__dictionary)
        print(self.__matches)




#Validate Argv
def validateArgv(argv):
    #Check for Arguments
    if len(argv) != 2 or argv[0][-4:].lower() != ".csv" or argv[1][-4:].lower() != ".txt":
        return "Usage: python dna.py data.csv sequence.txt"
    
    #Check if Database File exists 
    if os.path.isfile(argv[0]) == False:
        return "Database file not found"
    
    #Check if DNA sequence File exists
    if os.path.isfile(argv[1] == False):
        return "DNA sequence not found"
        
    return True

#Main Function
def main(argv):

    testing = MatchDNA()
    argv = ["databases/small.csv", "sequences/1.txt"]

    # TODO: Check for command-line usage
    validation = validateArgv(argv)
    if validation != True:
        print(validation)
        return

    dbpath, sdnapath = argv[0], argv[1]
    
    # TODO: Read database file into a variable
    testing.loadDatabase(dbpath)

    # TODO: Read DNA sequence file into a variable
    testing.loadSubjectDNA(sdnapath)

    # TODO: Find longest match of each STR in DNA sequence
    testing.findSTRFromSubjectDNA()

    # TODO: Check database for matching profiles
    testing.findMatchInDatabase()

    #testing.printData()

    return

#Longest Match predefine fucntion
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
