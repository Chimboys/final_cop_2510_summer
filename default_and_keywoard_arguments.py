#What is the default parameter?
#What is the keyword argument?
#What is the difference between them?

'''
1) Define a function create_profile that takes several parameters, some with default values.
2) Include parameters like name (no default), age (no default), profession (default to 'Engineer'),
and hobbies (a list with default values).
3) Inside the function, assemble and return a dictionary that summarizes the profile.
4) Demonstrate calling this function with only the required argument, with one or two optional arguments,
and using keyword arguments.
'''
















def create_profile(name, age, profession='Engineer', hobbies=['reading', 'coding']):
    """
    Creates a user profile dictionary with provided values,
    using default values for missing information.
    """
    profile = {
        'Name': name,
        'Age': age,
        'Profession': profession,
        'Hobbies': hobbies
    }
    return profile

# Example calls
basic_profile = create_profile('Alice', 23, hobbies=["diving"]) #Look , still used engineer but could assign hobby
print(basic_profile)

prof = "Chief"
#will it work if
# custom_profile = create_profile('Bob', age = 30, prof, hobbies=['painting', 'cycling'])

custom_profile = create_profile('Bob', 30, prof, hobbies=['painting', 'cycling'])
print(custom_profile)

keyword_profile = create_profile(name='Charlie',  age=22, profession='Artist')
print(keyword_profile)


#Python allows you to mix positional arguments and keyword arguments in a function call.
#However, once you start using keyword=value, all next arguments has to be keyword argumentts
#Best practice, if started with one of them just use it
