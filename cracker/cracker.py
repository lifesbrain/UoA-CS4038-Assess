import hashlib

# Cracking Class, Gromit
class Cracking:
  # Password Data Structure for storing hashes and passwords
  class Password:
    def __init__ (self, hash):
      self.name = hash # For storing the name of provided hash for differentiation
      self.hash = None
      self.salt = None
      self.password = None
      self.cracked = False
      self.attempts = 0

      # If the hash is a tuple, split the hash from the salt
      if isinstance(hash, tuple):
        self.hash, self.salt = hash
      else: # Else just set the hash
        self.hash = hash

    # Default print function
    def __str__ (self):
      return str(f"Hash:     {self.hash}\nSalt:     {self.salt}\nPassword: {self.password}\nAttempts: {self.attempts}")

  # Cracking Init    
  def __init__ (self , hashes, dictionary = None):
    self.passwords = set() # For storing set of passwords and hashes
    self.dictionary = dictionary # ∆ To impliment input validation

    # For each hash, create a password object and add it to the set
    for i in range(len(hashes)):
      try:
        self.passwords.add(self.Password(hashes[i]))
      except:
        print(f"Hash '{i}' incorrectly formatted:\n'{hashes[i]}'")

  # Function to rebase a base 10 integer - take a int and a string of characters to use as the base (default base 36)
  def rebase (number, alphabet='abcdefghijklmnopqrstuvwxyz0123456789'):
    # If the number is less than the base, return the character at the index of the number
    if number < len(alphabet):
      return alphabet[number]
    else: # Else, calculate the new base number
      newNumber = ''
      while number > 0:
        newNumber = alphabet[number % len(alphabet)] + newNumber # Add remainder character to the front of the string (equivilent of, 1, then 10, then 100 etc, in base 10)
        number //= len(alphabet) # Calculate quotient for the next iteration

      return newNumber

  # Task 01 Brute Force
  def bruteForce (self):
    # Possible characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'


  # Default print function
  def __str__ (self):
    # Create an array of password objects for printing
    stringArray = []
    for password in self.passwords:
      stringArray.append(str(password))
    
    # Return passwords as a string
    return '\n-----\n'.join(stringArray)

    # Return table as a string
    return 

# task 01 test
if __name__ == "__main__":
  # Hashes
  t1_hashes = ['f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a', 'e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24', '4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80', 'afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b']
  # Dictionary

  # Task 01
  task01 = Cracking(t1_hashes)
  print(task01)