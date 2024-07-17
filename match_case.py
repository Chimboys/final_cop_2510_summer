'''
Write a Python function process_data(data) that categorizes the input data based on its type.
Check for these types:
1) Intiger or Float then print("Numeric")
2) String that contains numbers then print("String with Numeric Content")
3) String that does not numbers ("String")
4) Otherwise, print("Cannot be process")

'''


















def process_data(data):
    match data:
        case int() | float():
            return "Numeric value"
        case str() if data.isnumeric(): #Smth New
            return "String with Numeric Content"
        case str():
            return "String"
        case [x,y]:
            return "List with 2 elements"
        case _:
            return "Other"

# Example usage:
print(process_data(10))                 # Output: "Integer"
print(process_data("123"))              # Output: "String with Numeric Content"
print(process_data("Hello"))            # Output: "String"
print(process_data(True))               # Output: "Other"
print(process_data([1,2])) 
