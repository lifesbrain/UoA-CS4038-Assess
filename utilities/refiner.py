# Takes a string and an int then applies the refiner to the string int times

import sys
import hashlib

def rebase (number, alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#*$@-_."):
  base = len(alphabet) # Set the base to the length of the alphabet
  # If the number is less than the base, return the character at the index of the number
  if number < base:
    return alphabet[number]
  else: # Else, calculate the new base number
    newNumber = ''
    while number > 0:
      newNumber = alphabet[number % len(alphabet)] + newNumber # Add remainder character to the front of the string (equivilent of, 1, then 10, then 100 etc, in base 10)
      number //= base # Calculate quotient for the next iteration

    return newNumber
# Function to hash a string
def hash (string):
  return hashlib.sha512(string.encode()).hexdigest()

# Reduce function which takes a hash and rebases it to a compliant string
def reduce (hash):
  # Rebase the base16 hash to a base10 int
  hashInt = int(hash, 16)
  # Rebase the base10 int to a string of base[alphabet length] and trim
  # ∆ This could be more efficent by trimming before rebase
  reduced = rebase(hashInt)[:8]
  return reduced

def main(startString, count):
  for i in range(count):
    hashString = hash(startString)
    string = reduce(hashString)
    print(f"Hash: {hashString} | String: {string}", end="\r")

  print("\n" + hashString)

if __name__ == "__main__":
  main("2010", 50)
