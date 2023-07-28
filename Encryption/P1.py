import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size
bufferSize = 64 * 1024
password = "pwd"# encryption of file data.txt
with open("data.txt", "rb") as fIn:
 with open("data.txt.aes", "wb") as fOut:
  pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
# get encrypted file size
encFileSize = stat("data.txt.aes").st_size
print(encFileSize) #prints file size# decryption of file data.aes

with open("data.txt.aes", "rb") as fIn:
 with open("dataout.txt", "wb") as fOut:
  try:
# decrypt file stream
   pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
  except ValueError:
# remove output file on error
    remove("dataout.txt")

