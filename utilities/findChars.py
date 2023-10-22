# Function for finding all characters used in a given text file

import sys

def findChars(filename):
  chars = set()

  # Try to itterate through the file
  try:
    with open(filename, 'r') as file:
      for line in file:
        for char in line:
          chars.add(char)
  except:
    print("Error: Could not open file")

  # Return a string of all characters
  return ''.join(chars)

if __name__ == '__main__':
  print(findChars(sys.argv[1]))
