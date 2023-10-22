# Python file for Task 1 of the assignment

import sys
from cracking import Cracking

t1_hashes = "./hashes/Task01Hashes.txt"

def main(hashesPath=t1_hashes):
  task01 = Cracking(hashesPath=hashesPath) # Create a new Cracking object with the hashes
  task01.bruteForce() # Brute force the hashes
  print(task01)
  return print(task01.printInfo()) # Print the cracked hashes

if __name__ == "__main__":
    # Set input variables to defaults
    input_hashes = t1_hashes

    # Try to pass in a hash file from the terminal
    try:
        if len(sys.argv) == 1: raise ValueError("No args passed in")

        # Try to use hashes path if passed in
        input_hashes = sys.argv[1]

    except ValueError as e:
       print(f"Error: {e}, using default hashes")
    
    finally:
      # Run main() with the hashes path
      main(input_hashes)