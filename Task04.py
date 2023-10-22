# Python file for Task 4 of the assignment - Rainbow Tables

import sys
from cracking import Cracking

t4_hashes = "./hashes/PasswordDictionary-hashes.txt"
t4_table = "./rainbows/alphanum_cl10000_cc10000_sl8.rt"
t4_dictionary = "./dictionaries/PasswordDictionary.txt"

def main(hashesPath=t4_hashes, rainbowPath=None, dictionaryPath=None, chainLength=None, chainCount=None, strLength=None, alphabet=None):
  # If a rainbow table path exists, use it
  if rainbowPath:
    task = Cracking(hashesPath=hashesPath, rainbowTablePath=rainbowPath) # Create a new Cracking object with the hashes and table
    task.rainbowAttack() # Rainbow attack the hashes
  else: # Else, generate a new table
    task = Cracking(hashesPath=hashesPath) # Create a new Cracking object with the hashes
    task.rainbowAttack(newTable=True, chainLength=chainLength, chainCount=chainCount, strLength=strLength, alphabet=alphabet)
  
  return print(task) # Print the cracked hashes

if __name__ == "__main__":
    # Set input variables to defaults
    input_hashes = t4_hashes
    input_table = None
    chainLength = 10000
    chainCount = 100000
    strLength = 8
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Try to pass in a dictionary and hash array from the terminal
    try:
        if len(sys.argv) == 1: raise ValueError("No args passed in")

        # Try to use dictionary and hashes if passed in
        input_hashes = sys.argv[1]
        if len(sys.argv) > 2:
          input_table = sys.argv[2]

    except ValueError as e:
       print(f"Error: {e}, using default hashes and generating a table")
    
    finally:
      if input_table:
        print(f"Using hashes: {input_hashes} and table: {input_table}")
        main(hashesPath=input_hashes, rainbowPath=input_table)
      else: 
        print(f"Using hashes: {input_hashes} and generating a table")
        # Run main() with the dictionary and hashes
        main(hashesPath=input_hashes, chainLength=chainLength, chainCount=chainCount, strLength=strLength, alphabet=alphabet)