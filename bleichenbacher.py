from roots import *
from Crypto.Hash import SHA
import sys

message = sys.argv[1]
messageDigest = SHA.new(message.encode()).hexdigest()
ASNMagic = "003021300906052B0E03021A05000414"
Prefix = "0001FF"

fullDigest = Prefix + ASNMagic + messageDigest

fullDigest = fullDigest + "A"*(512-len(fullDigest))


D = int(fullDigest, 16)


Signature = integer_nthroot(D, 3)[0]

# Your code to forge a signature goes here.
print(integer_to_base64(Signature).decode())
