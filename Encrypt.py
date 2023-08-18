import hashlib

def hash_password(password):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the password encoded as bytes
    hash_object.update(password.encode('utf-8'))

    # Get the hash value as a hexadecimal string
    hashed_password = hash_object.hexdigest()
    return hashed_password

def validate_password(input_password, stored_hashed_password):
    # Hash the input password using the same process
    hashed_input_password = hash_password(input_password)

    # Compare the hashed input password with the stored hashed password
    return hashed_input_password == stored_hashed_password

