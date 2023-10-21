# Python file for Task 4 of the assignment - Rainbow Tables

import sys
from cracking import Cracking

t3_hashes = "./hashes/Task03Hashes.txt"

def main(hashesPath=t3_hashes, rainbowPath=None):
  task = Cracking(hashesPath=hashesPath, rainbowTablePath=rainbowPath) # Create a new Cracking object with the hashes and table
  if task.rainbowTable == None: task.generateRainbowTable() # Generate a rainbow table if a table path wasn't passed
  task.rainbowAttack() # Rainbow attack the hashes
  return print(task) # Print the cracked hashes

if __name__ == "__main__":
    # Set input variables to defaults
    input_hashes = t3_hashes
    input_table = None

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
      # Run main() with the dictionary and hashes
      main(input_hashes, input_table)