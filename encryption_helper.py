# pip install cryptography
from simplecrypt import encrypt, decrypt
import sys

def read_encrypted(password, filename, string=True):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
        if string:
            return plaintext.decode('utf8')
        else:
            return plaintext

def write_encrypted(password, filename, plaintext):
    with open(filename, 'wb') as output:
        ciphertext = encrypt(password, plaintext)
        output.write(ciphertext)

def main():
    # We use this script to generate encrypted credentail for an exchange
    password = str(sys.argv[1])
    api_secret = str(sys.argv[2])
    exchange_name = sys.argv[3]

    write_encrypted(password,"txts/{}".format(exchange_name),api_secret)

if __name__ == "__main__":
    main()
