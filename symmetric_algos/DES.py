from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def des_encrypt(msg, key):
    cipher = DES.new(key=key, mode=DES.MODE_CBC)
    msg_with_pad = pad(data_to_pad=msg, block_size=DES.block_size)
    cipher_text = cipher.encrypt(msg_with_pad)
    return cipher_text

def des_decrypt(cipher_msg, key):
    des_instance = DES.new(key=key, mode=DES.MODE_CBC)
    plaintext = des_instance.decrypt(cipher_msg)
    return plaintext

if __name__ == "__main__":
    key = b"aghzerey"
    msg = b"this is my very very important secret that no one should know it"
    cipher_msg_DES = des_encrypt(msg=msg, key=key)
    plain_text_DES = des_decrypt(cipher_msg=cipher_msg_DES, key=key)
    print(cipher_msg_DES)
    print()
    print(plain_text_DES)