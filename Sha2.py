import hashlib
hash_object = hashlib.sha256(b'GHLG52')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_object1 = hashlib.sha256(b'GHLG52')
hex_dig1 = hash_object1.hexdigest()
print(hex_dig1)