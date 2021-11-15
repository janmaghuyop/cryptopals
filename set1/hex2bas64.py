hs = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
bs = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print(len(hs))  # 96
print(len(bs))  # 64

i = int('49', 16) # 73
s = int('27', 16) # 39
y = int('6d', 16) # 109

print(bin(73)) # 01001001
print(bin(39)) # 00100111
print(bin(109))# 01101101

# sextets
print(str(bin(73))[:-2].replace("0b", ""))  # 010010 01
print(str(bin(39))[:-2].replace("0b", ""))  # 001001 11
print(str(bin(109))[:-2].replace("0b", "")) # 011011 01

# bin to dec
int('010010', 2) # 18 => S
# get first 2 digits from the 1st octect
# 01 0010
int('010010', 2) # 18 => S
# get first 2 digits from the 2nd sextet
# 011101
int('011101', 2) # 29 => d

# 010010 01 001001 11 011011 01
#      S       S       d


# use python modules to convert
from binascii import unhexlify, b2a_base64
bs = unhexlify(hs) # string hex to byte string
print(bs)
be = b2a_base64(bs, newline=False) # encode byte to base64
print(be)
