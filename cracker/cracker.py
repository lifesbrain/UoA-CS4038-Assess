import hashlib
import io

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

    # Return the password object as a string
    def info (self):
      return str(f"Hash:     {self.hash}\nSalt:     {self.salt}\nPassword: {self.password}\nAttempts: {self.attempts}")

    # Default print function
    def __str__ (self):
      return str(self.name)
    
    # Default hash function for set
    def __hash__ (self):
      return hash(self.name)

  # Cracking Init    
  def __init__ (self , hashes, dictionaryPath = None):
    self.passwords = set() # For storing set of passwords and hashes
    self.dictionaryPath = dictionaryPath # ∆ To impliment input validation
    self.dictionary = None # Not Opened until needed
    self.salted = False # Set to true if any of the hashes are salted

    # For each hash, create a password object and add it to the set
    for i in range(len(hashes)):
      try:
        password = self.Password(hashes[i]) # Create a password object
        self.passwords.add(password) # Add to the set
        if self.salted == False and password.salt != None: # Set salted to true if its false and the password is salted
          self.salted = True
      except:
        print(f"Hash '{i}' incorrectly formatted:\n'{hashes[i]}'")

  # Function to rebase a base 10 integer - take a int and a string of characters to use as the base (default base 36)
  def rebase (self, number, alphabet="0123456789abcdefghijklmnopqrstuvwxyz"):
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
  def hash (self, string):
    return hashlib.sha512(string.encode()).hexdigest()
  
  # Function to crack passwords - takes a function that provides incrementing passwords to try
  def _crack (self, passwordStream):
    count = 0 # For counting the number of attempts and the current password to try
    toCrack = [p for p in self.passwords if p.cracked == False] # Create an array of uncracked passwords

    # Place in try block to catch keyboard interrupt
    try:
      while len(toCrack) > 0: # While theres still passwords to crack
        tryPassword = next(passwordStream, None) # Get the next password to try
        if tryPassword == None: break # If there are no more passwords to try, break
        if not self.salted: tryHash = self.hash(tryPassword) # If passwords are not salted, hash the tryPassword

        # For each uncracked password try the hash
        for i in range(len(toCrack)-1, -1, -1): # Run through list backwards so elemnets are not skipped when another is removed
          if self.salted: tryHash = self.hash(tryPassword + toCrack[i].salt) # If passwords are salted, hash the tryPassword with this uncrcaked passwords salt

          # If the hash matches the uncrcaked password then update the password object and remove from the toCrack array
          if tryHash == toCrack[i].hash:
            toCrack[i].password = tryPassword
            toCrack[i].cracked = True
            toCrack[i].attempts = count+1
            toCrack.pop(i)

        # Print count every 10,000
        if count % 10000 == 0:
          print(f"Attempt {count} | Trying {tryPassword} | {len(toCrack)} passwords remaining", end="\r")

        count += 1 # Increment the count

        # If all passwords have been cracked, break
        if len(toCrack) == 0:
          break

      # Print the number of attempts on completion
      print(f"Cracking Complete | Remaining: {len(toCrack)} | Attempts: {count : < 30}")

    except KeyboardInterrupt:
      print("\nCracking Canceled")

  # Task 01 Brute Force
  def bruteForce (self):
    # Define the brute force stream function
    def bruteForceStream ():
      count = 0 # Int to rebase to password, could be used to start at a specific password or to continue from a previous attempt in future..
      while True:
        yield self.rebase(count)
        count += 1
    
    # Crack the passwords
    self._crack(bruteForceStream())

  # Task 02 Dictionary Attack
  def dictionaryAttack (self):        
    # Try to open the dictionary file
    try:
      self.dictionary = open("./dictionaries/" + self.dictionaryPath, 'r')
    except:
      print(f"Dictionary file '{self.dictionaryPath}' not found")
      return
    
    # Define the dictionary stream function to pass to the crack function
    def dictionaryStream ():
      for line in self.dictionary:
        yield line.strip()

    # Crack the passwords
    self._crack(dictionaryStream())

    # Close the dictionary file
    self.dictionary.close()

  # Default print function
  def __str__ (self):
    # Create an array of password objects for printing
    stringArray = []
    for password in self.passwords:
      stringArray.append(str(password.info()))
    
    # Return passwords as a string
    return '\n-----\n'.join(stringArray)

# Tasks Tests
if __name__ == "__main__":
  # Hashes
  t1_hashes = ['f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a', 'e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24', '4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80', 'afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b']
  t2_hashes = ['31a3423d8f8d93b92baffd753608697ebb695e4fca4610ad7e08d3d0eb7f69d75cb16d61caf7cead0546b9be4e4346c56758e94fc5efe8b437c44ad460628c70', '9381163828feb9072d232e02a1ee684a141fa9cddcf81c619e16f1dbbf6818c2edcc7ce2dc053eec3918f05d0946dd5386cbd50f790876449ae589c5b5f82762', 'a02f6423e725206b0ece283a6d59c85e71c4c5a9788351a24b1ebb18dcd8021ab854409130a3ac941fa35d1334672e36ed312a43462f4c91ca2822dd5762bd2b', '834bd9315cb4711f052a5cc25641e947fc2b3ee94c89d90ed37da2d92b0ae0a33f8f7479c2a57a32feabdde1853e10c2573b673552d25b26943aefc3a0d05699', '0ae72941b22a8733ca300161619ba9f8314ccf85f4bad1df0dc488fdd15d220b2dba3154dc8c78c577979abd514bf7949ddfece61d37614fbae7819710cae7ab', '6768082bcb1ad00f831b4f0653c7e70d9cbc0f60df9f7d16a5f2da0886b3ce92b4cc458fbf03fea094e663cb397a76622de41305debbbb203dbcedff23a10d8a', '0f17b11e84964b8df96c36e8aaa68bfa5655d3adf3bf7b4dc162a6aa0f7514f32903b3ceb53d223e74946052c233c466fc0f2cc18c8bf08aa5d0139f58157350', 'cf4f5338c0f2ccd3b7728d205bc52f0e2f607388ba361839bd6894c6fb8e267beb5b5bfe13b6e8cc5ab04c58b5619968615265141cc6a8a9cd5fd8cc48d837ec', '1830a3dfe79e29d30441f8d736e2be7dbc3aa912f11abbffb91810efeef1f60426c31b6d666eadd83bbba2cc650d8f9a6393310b84e2ef02efa9fe161bf8f41d', '3b46175f10fdb54c7941eca89cc813ddd8feb611ed3b331093a3948e3ab0c3b141ff6a7920f9a068ab0bf02d7ddaf2a52ef62d8fb3a6719cf25ec6f0061da791']
  t3_hashes = [('63328352350c9bd9611497d97fef965bda1d94ca15cc47d5053e164f4066f546828eee451cb5edd6f2bba1ea0a82278d0aa76c7003c79082d3a31b8c9bc1f58b', 'dbc3ab99'), ('86ed9024514f1e475378f395556d4d1c2bdb681617157e1d4c7d18fb1b992d0921684263d03dc4506783649ea49bc3c9c7acf020939f1b0daf44adbea6072be6', 'fa46510a'), ('16ac21a470fb5164b69fc9e4c5482e447f04f67227102107ff778ed76577b560f62a586a159ce826780e7749eadd083876b89de3506a95f51521774fff91497e', '9e8dc114'), ('13ef55f6fdfc540bdedcfafb41d9fe5038a6c52736e5b421ea6caf47ba03025e8d4f83573147bc06f769f8aeba0abd0053ca2348ee2924ffa769e393afb7f8b5', 'c202aebb'), ('9602a9e9531bfb9e386c1565ee733a312bda7fd52b8acd0e51e2a0a13cce0f43551dfb3fe2fc5464d436491a832a23136c48f80b3ea00b7bfb29fedad86fc37a', 'd831c568'), ('799ed233b218c9073e8aa57f3dad50fbf2156b77436f9dd341615e128bb2cb31f2d4c0f7f8367d7cdeacc7f6e46bd53be9f7773204127e14020854d2a63c6c18', '86d01e25'), ('7586ee7271f8ac620af8c00b60f2f4175529ce355d8f51b270128e8ad868b78af852a50174218a03135b5fc319c20fcdc38aa96cd10c6e974f909433c3e559aa', 'a3582e40'), ('8522d4954fae2a9ad9155025ebc6f2ccd97e540942379fd8f291f1a022e5fa683acd19cb8cde9bd891763a2837a4ceffc5e89d1a99b5c45ea458a60cb7510a73', '6f966981'), ('6f5ad32136a430850add25317336847005e72a7cfe4e90ce9d86b89d87196ff6566322d11c13675906883c8072a66ebe87226e2bc834ea523adbbc88d2463ab3', '894c88a4'), ('21a60bdd58abc97b1c3084ea8c89aeaef97d682c543ff6edd540040af20b5db228fbce66fac962bdb2b2492f40dd977a944f1c25bc8243a4061dfeeb02ab721e', '4c8f1a45')]

  # Dictionary
  t2_dictionary = 'PasswordDictionary.txt'

  # Task 01
  print("Task 01")
  task01 = Cracking(t1_hashes)
  task01.bruteForce()
  print(task01)

  # Task 02
  print("\nTask 02")
  task02 = Cracking(t2_hashes, t2_dictionary)
  task02.dictionaryAttack()
  print(task02)

  # Task 03
  print("\nTask 03")
  task03 = Cracking(t3_hashes, t2_dictionary)
  task03.dictionaryAttack()
  print(task03)