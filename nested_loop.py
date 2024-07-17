data = [
    {'student1': ('Alice', 85, 'Math'), 'student2': ('Bob', 90, 'Science')},
    {'student3': ('Charlie', 78, 'History'), 'student4': ('David', 92, 'Art')},
    {'student5': ('Eve', 88, 'Math'), 'student6': ('Frank', 80, 'Science')}
]

#how to print student number, their name, grade, and class



#print student whose score more than or equalt to 85, and their classes


# use XYZ data structure that stores class and how many students took it



#Analyze the following loop! 
nums = [[1,2,3],[4,5,6]]
for l in nums:
    for number in l:
        if number % 4 == 0:
            print(f"Found a number divisible by 4 in a list: {number}")
            break
    else:
        print("No number divisible by 4")
else:
    print("Will it be printed?")









#Q1
for dictionary in data:
    for student_number, (name, score, class_name) in dictionary.items():
        print(f"Student Number: {student_number}, Name: {name}, Score: {score}, Class: {class_name}")

for dictionary in data:
    for student_number in dictionary:
        name, score, class_name = dictionary[student_number]
        print(f"Student Number: {student_number}, Name: {name}, Score: {score}, Class: {class_name}")

#Q2
# Print students whose score is more than or equal to 85, and their classes
for dictionary in data:
    for student_number in dictionary:
        name, score, class_name = dictionary[student_number]
        if score >= 85:
            print(f"Student Number: {student_number}, Name: {name}, Class: {class_name}")

#Q3
# Data structure to store classes and how many students took them
class_counts = dict()

for dictionary in data:
    for student_number in dictionary:
        name, score, class_name = dictionary[student_number]
        if class_name in class_counts:
            class_counts[class_name] += 1
        else:
            class_counts[class_name] = 1

# Print the classes and how many students took them
for class_name, count in class_counts.items():
    print(f"Class: {class_name}, Number of Students: {count}")


