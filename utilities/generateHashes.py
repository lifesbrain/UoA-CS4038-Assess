# Function for generating a file of hashes from a file of strings

import sys
import hashlib

def generateHashes(stringFile, hashFile):
  # Try to open the files
  try:
    hashFile = open(hashFile, 'w')
    with open(stringFile, 'r') as strings:
      for line in strings:
        # write line to file
        hashFile.write(hashlib.sha512(line.encode()).hexdigest() + '\n')

    hashFile.close()
        
  except:
    print("Error: Could not open file")

if __name__ == '__main__':
  if len(sys.argv) == 3:
    generateHashes(sys.argv[1], sys.argv[2])
  elif len(sys.argv) == 2:
    hashFile = sys.argv[1].split('.')[0] + '-hashes.txt'
    generateHashes(sys.argv[1], hashFile)
  else:
    print("No file specified")
  
