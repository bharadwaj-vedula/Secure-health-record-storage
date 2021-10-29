import cryptography as cp 
import streamlit as st
from PIL import Image
import os
import base64

st.set_option('deprecation.showfileUploaderEncoding', False)
option = st.sidebar.radio("Operations",["Encrypt","Decrypt"])

#Encrypt
if option == "Encrypt":
    st.title("Image Encryption")
    st.write("\n")
    st.write("\n")    
    st.subheader("Upload image for Encryption")

    def read_image(image):
        return image.read()

    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'],key =1)
    if uploaded_file is not None:
        data = read_image(uploaded_file)
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.success(f"File uploaded sucessfully.")

    key = st.text_input("Enter key").encode('utf-8')
    if len(key) != 16:
        st.warning("The Key length should be 16")
    selections = ['AES' , 'Blowfish' , 'RC2']
    option2 = st.selectbox("Select an Algorithm for Encryption",selections,index = 0)
    
    if option2 == "AES":
        st.info(f"Using {option2} for Encryption")
        if st.button("Encrypt"):
            encrypted_data = cp.encrypt_aes(key,data)
            st.success(f"Encrypted {len(encrypted_data)} {len(data)}")
            st.download_button(label = "Download Encrypted File", data = encrypted_data, file_name = "encrypted_data.jpg")

    if option2 == "Blowfish":
        st.info(f"Using {option2} for Encryption")
        if st.button("Encrypt"):
            encrypted_data = cp.encrypt_blowfish(key,data)
            st.success(f"Encrypted {len(encrypted_data)} {len(data)}")
            st.download_button(label = "Download Encrypted File", data = encrypted_data, file_name = "encrypted_data.jpg")
        
    if option2 == "RC2":
        st.info(f"Using {option2} for Encryption")        
        if st.button("Encrypt"):
            encrypted_data = cp.encrypt_rc2(key,data)
            st.success(f"Encrypted {len(encrypted_data)} {len(data)}")
            st.download_button(label = "Download Encrypted File", data = encrypted_data, file_name = "encrypted_data.jpg")
    

#Decrypt
if option == "Decrypt":
    st.title("Image Decryption")
    st.write("\n")
    st.write("\n")   
    st.subheader("Upload image for Decryption")

    def read_image(image):
        return image.read()
        
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'] , key =2)
    if uploaded_file is not None:
        data = read_image(uploaded_file)
        st.success(f"File uploaded sucessfully.")

    key = st.text_input("Enter key").encode('utf-8')
    if len(key) != 16:
        st.warning("The Key length should be 16")    
    selections = ['AES' , 'Blowfish' , 'RC2']
    option2 = st.selectbox("Select an Algorithm for Decryption",selections,index = 0)

    if option2 == "AES":
        st.info(f"Using {option2} for Decryption")
        if st.button("Decrypt"):
            decrypted_data = cp.decrypt_aes(key,data)
            st.download_button(label = "Download Decrypted File", data = decrypted_data, file_name = "decrypted_data.jpg")
            st.success("Decrypted")

    if option2 == "Blowfish":
        st.info(f"Using {option2} for Decryption")
        if st.button("Decrypt"):
            decrypted_data = cp.decrypt_blowfish(key,data)
            st.download_button(label = "Download Decrypted File", data = decrypted_data, file_name = "decrypted_data.jpg")
            st.success("Decrypted")

    if option2 == "RC2":
        st.info(f"Using {option2} for Decryption")
        if st.button("Decrypt"):
            decrypted_data = cp.decrypt_rc2(key,data)
            st.download_button(label = "Download Decrypted File", data = decrypted_data, file_name = "decrypted_data.jpg")
            st.success("Decrypted")






