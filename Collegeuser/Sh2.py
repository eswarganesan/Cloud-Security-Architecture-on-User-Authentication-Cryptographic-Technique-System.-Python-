import hashlib
hash_string = 'confidential data'
sha_signature=hashlib.sha256(hash_string.encode()).hexdigest()
print(sha_signature)