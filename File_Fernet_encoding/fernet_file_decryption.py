from cryptography.fernet import Fernet


def decrypted_file_Fernet(file_name,my_key):




    cipher_suite = Fernet(my_key)
        
    #Read the file name and decrypt it
    
    with open(file_name,'rb') as file:
        encrypted_data = file.read()
        decrypted_data= cipher_suite.decrypt(encrypted_data)
        
    #Write the decrypted_data to a  new file
    with open(file_name,'wb') as file:
        file.write(decrypted_data)

decrypted_file_Fernet("denemem.txt","8PK8D5bYA68S39DK2oX4L3UOtz1k8vOVbjgbg8iHR6Q=")     
