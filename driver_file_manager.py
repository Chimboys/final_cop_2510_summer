from files_manager import FileManager
#Write a class
#Containing 3 classes
# 1st method has param (fileneame) and it displays how many time each char appeared in text_file
# Would you use try block?

# 2nd method writes a file and has params (filename and content)


# 3rd method sign the specified file and has params (filename_to_sign, sign_itself)
# Do not delete contents, just add string at the next line after last word



# Example usage:
file_manager = FileManager()
file_manager.count_characters("final_exam.txt")  # Replace 'example.txt' with your file
file_manager.write_file("new_file.txt", "This is the content of the new file.")  # Creates or overwrites 'new_file.txt' with the specified content
file_manager.sign_file("new_file.txt", "AK_2002")  # Adds a signature to 'new_file.txt'
