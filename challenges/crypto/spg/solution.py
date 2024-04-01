import string
from base64 import b64decode
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import long_to_bytes

alph = string.ascii_letters + string.digits + "~!@#$%^&*"


# This loads the data directly from the output file, so that we can use it as variable
def load_data():
    with open("./output.txt") as f:
        password = f.readline().split(" : ")[1]
        enc_flag = b64decode(
            f.readline().split(" : ")[1]
        )  # b64 decode, since it was b64 encoded in the
    return password, enc_flag


# The masterkey can be read out of the password, since based on the generate_password()
# function a random string gets fetched from half 1 or half 2. Since we are able to identify
# which character is from which half, we can recreate the master key
def obtain_master_key(password):
    master_key = ""
    for p in password:
        if p in alph[: len(alph) // 2]:
            master_key += "1"
        else:
            master_key += "0"
    print(master_key[::-1])
    return master_key[::-1]


# With the created master key and the encrypted flag, we can reverse the encryption
# using the same cipher but now with decrypt() instead of encrypt()
def decrypt_flag(master_key, enc_flag):
    key = long_to_bytes(int(master_key, 2))[::-1]
    encryption_key = sha256(key).digest()
    cipher = AES.new(encryption_key, AES.MODE_ECB)
    flag = cipher.decrypt(enc_flag)
    return flag


def pwn():
    password, enc_flag = load_data()
    master_key = obtain_master_key(password)
    flag = decrypt_flag(master_key, enc_flag)
    print(flag)


pwn()
