import base64
import numpy as np 
from PIL import Image 
from Crypto.Cipher import Blowfish,AES,ARC2
from Crypto.Util.Padding import pad,unpad 




def encrypt_aes(key,img_encoded):
    iv = key 
    cipher = AES.new(key,AES.MODE_CBC,iv)
    cipherimage = cipher.encrypt(pad(img_encoded,16))
    return cipherimage
    

def encrypt_rc2(key,img_encoded):
    iv = b"12345678"
    cipher = ARC2.new(key,ARC2.MODE_CBC,iv)
    cipherimage = cipher.encrypt(pad(img_encoded,8))
    return cipherimage

def encrypt_blowfish(key,img_encoded):
    iv = b"12345678" 
    cipher = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    cipherimage = cipher.encrypt(pad(img_encoded,8))
    return cipherimage

def decrypt_aes(key,img_encoded):
    iv = key
    cipher = AES.new(key,AES.MODE_CBC,iv)
    decrypted_image = unpad(cipher.decrypt(img_encoded),16)
    return decrypted_image
  
def decrypt_rc2(key,img_encoded):
    iv = b"12345678"
    cipher = ARC2.new(key,ARC2.MODE_CBC,iv)
    decrypted_image = unpad(cipher.decrypt(img_encoded),8)
    return decrypted_image

def decrypt_blowfish(key,img_encoded):
    iv = b"12345678" 
    cipher = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    decrypted_image = unpad(cipher.decrypt(img_encoded),8)
    return decrypted_image

def read_image(file_path):
    with open(file_path,'rb') as file:
        image = file.read()
    return image
    
def save_image(encrypted_string,destination_path):
    with open(destination_path,'wb') as file:
        file.write(encrypted_string)


    
    