import hashlib
import sys

wordlist_location = sys.argv[1] #self explanatory
hash_input = sys.argv[2] #value of the hash

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode()) #md5
        hashed_pass = hash_ob.hexdigest()
        hash_256 = hashlib.sha256(line.strip().encode())
        hashed256 = hash_256.hexdigest()
        if hashed256 == hash_input: #change if it's md5 hash type
            print('Found cleartext password! ' + line.strip())
            exit(0)
