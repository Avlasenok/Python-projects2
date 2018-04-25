import simplecrypt

with open("/Users/avlasenok/Downloads/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("/Users/avlasenok/Downloads/dic.pwd", "r") as pw:
    for password in pw:
        try:
            message = simplecrypt.decrypt(password.strip(), encrypted)
            break
        except simplecrypt.DecryptionException:
            print(password, "Incorrect")
