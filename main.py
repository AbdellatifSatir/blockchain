from hashlib import sha256

def generate_hash(data):

    # # Encode the data to bytes
    # data_bytes = data.encode('utf-8')
    # hash_obj = sha256()
    # # Update the hash object with the data
    # hash_obj.update(data_bytes)

    hash_obj = sha256(data.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hash_hex = hash_obj.hexdigest()

    return hash_hex

# Example usage
data = "Hello, world!"
print(data)
print(f"SHA-256: {generate_hash(data)}")  # Default is SHA-256
