# Python file for Task 4 of the assignment - Rainbow Tables
# Takes arguments for:
# --hashesPath: Path to a hashes file
# --tablePath: Path to a alreadt generated rainbow table
# --dictionary: Path to the dictionary file for generating a new table
# --chainLength: Length of each chain in the table
# --chainCount: Number of chains in the table
# --strLength: Length of the strings to be generated
# --alphabet: Alphabet to be used to generate the strings


import sys
import argparse
from cracking import Cracking

# Dictionary of defaults
t4 = {
  "hashesPath": "./hashes/PasswordDictionary-hashes.txt",
  "tablePath": "None",
  "dictionary": None,
  "chainLength": 1000,
  "chainCount": 1000,
  "strLength": 8,
  "alphabet": "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#*$@-_."
}

def main():
  # If a rainbow table path exists, use it
  if t4["tablePath"] != "None":
    print(f"Using table: {t4['tablePath']}\nTo crack hashes: {t4['hashesPath']}")

    task = Cracking(hashesPath=t4["hashesPath"], rainbowTablePath=t4["tablePath"]) # Create a new Cracking object with the hashes and table
    task.rainbowAttack() # Rainbow attack the hashes
  else: # Else, generate a new table
    print(f"Generating table with dictionary: {t4['dictionary']}\nAlphabet: {t4['alphabet']}\nString length: {t4['strLength']} Chain length: {t4['chainLength']} Chain count: {t4['chainCount']}")
    print(f"To crack hashes: {t4['hashesPath']}")

    task = Cracking(hashesPath=t4["hashesPath"], dictionaryPath=t4["dictionary"]) # Create a new Cracking object with the hashes and potential dictionary
    task.rainbowAttack(newTable=True, chainLength=t4["chainLength"], chainCount=t4["chainCount"], strLength=t4["strLength"], alphabet=t4["alphabet"]) # Generate a new table with the given parameters
  
  task.saveResults() # Save the results to a file
  print(task)
  return print(task.printInfo()) # Print the cracked hashes

if __name__ == "__main__":
  # Create parser
  parser = argparse.ArgumentParser(description="Cracker: Rainbow table attack")

  # Add arguments
  parser.add_argument("--hashesPath", type=str, help="Password hash's file Path")
  parser.add_argument("--tablePath", type=str, help="Rainbow table file path")
  parser.add_argument("--dictionary", type=str, help="Dictionary file path")
  parser.add_argument("--chainLength", type=int, help="Length of each chain in the table")
  parser.add_argument("--chainCount", type=int, help="Number of chains in the table")
  parser.add_argument("--strLength", type=int, help="Length of the strings to be generated")
  parser.add_argument("--alphabet", type=str, help="Alphabet to be used to generate the strings")

  # Parse arguments
  args = parser.parse_args()

  # If an argument is given, update the dictionary
  t4.update((key, value) for key, value in vars(args).items() if value != None)

  # Try to run the main function
  main()