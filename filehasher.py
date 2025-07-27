import hashlib

def get_file_hash(file_path, algorithm="sha256"):
    hash_func = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

if __name__ == "__main__":
    file_path = input("Please enter the file path: ")
    try:
        file_hash = get_file_hash(file_path)
        print(f"File Hash: {file_hash}")
    except FileNotFoundError:
        print(f"The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
