from cryptography.fernet import Fernet


def encrypted_file_Fernet(file_name):

    # Generate an encryption key

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    #Read the file name and encrypt it
    
    with open(file_name,'rb') as file:
        file_data = file.read()
        encrypted_data= cipher_suite.encrypt(file_data)
        
    #Write the encrypted_data to a  new file
    with open(file_name,'wb') as file:
        file.write(encrypted_data)
        
        print(f"key = {key}")
encrypted_file_Fernet("denemem.txt")     
        
        
