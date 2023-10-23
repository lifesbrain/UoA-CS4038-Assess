# Python file for Task 2 of the assignment

import sys
from cracking import Cracking

t2_hashes = "./hashes/Task02Hashes.txt"
t2_dictionary = './dictionaries/PasswordDictionary.txt'

def main(hashesPath=t2_hashes, dictionaryPath=t2_dictionary):
  task = Cracking(hashesPath=hashesPath, dictionaryPath=dictionaryPath) # Create a new Cracking object with the hashes and dictionary
  task.dictionaryAttack() # Dictionary attack the hashes
  task.saveResults() # Save the results to a file
  print(task)
  return print(task.printInfo()) # Print the cracked hashes

if __name__ == "__main__":
    # Set input variables to defaults
    input_hashes = t2_hashes
    input_dictionary = t2_dictionary

    # Try to pass in a dictionary and hash array from the terminal
    try:
        if len(sys.argv) == 1: raise ValueError("No args passed in")

        # Try to use dictionary and hashes if passed in
        input_hashes = sys.argv[1]
        if len(sys.argv) > 2:
          input_dictionary = sys.argv[2]

    except ValueError as e:
       print(f"Error: {e}, using default hashes and dictionary")
    
    finally:
      # Run main() with the dictionary and hashes
      main(input_hashes, input_dictionary)