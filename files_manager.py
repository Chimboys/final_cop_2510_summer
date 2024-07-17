class FileManager:
    def __init__(self):
        pass

    def count_characters(self, filename):
        try:
            with open(filename, 'r') as file:
                chars_counter = {}
                content = file.read()
                for char in content:
                    if char == " ":
                        continue
                    if char in chars_counter:
                        chars_counter[char] += 1
                    else:
                        chars_counter[char] = 1

                for char, freq in chars_counter.items():
                    if char == "\n":
                        print(f"'\\n': {freq} times")
                        continue
                    
                    print(f"'{char}': {freq} times")
                    
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")

    def write_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content written to {filename}")

    def sign_file(self, filename, signature):
        with open(filename, 'a') as file:
            file.write(f"\n{signature}")
        print(f"File {filename} signed with '{signature}'")
