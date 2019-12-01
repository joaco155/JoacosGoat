# Function: limited entries per user
# What this function does is limit the variable entered by the user
# In info you should put the requeriments you want the user to follow (string type)
# In num_char you define the maximum length of the variable to assign

def keyboard_input(info, num_char):
    screen = input(f'{info}, max {num_char} characters: ')[:num_char]

    return screen

#Example
name = keyboard_input("Insert name (max 35 lengh)", 35)
print(name)
