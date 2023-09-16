from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def aes_encrypt(msg, key):
    cipher = AES.new(key=key, mode=AES.MODE_CBC)
    msg_with_pad = pad(data_to_pad=msg, block_size=AES.block_size)
    cipher_text = cipher.encrypt(msg_with_pad)
    return cipher_text

def aes_decrypt(cipher_msg, key):
    des_instance = AES.new(key=key, mode=AES.MODE_CBC)
    plaintext = des_instance.decrypt(cipher_msg)
    return plaintext

if __name__ == "__main__":
    key = b"this_is_my_key__"
    msg = b"this is my very very important secret that no one should know it"
    cipher_msg_DES = aes_encrypt(msg=msg, key=key)
    plain_text_DES = aes_decrypt(cipher_msg=cipher_msg_DES, key=key)
    print(cipher_msg_DES)
    print()
    print(plain_text_DES)