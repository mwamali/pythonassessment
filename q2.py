# 2. Function that continuously asks the user for input until "exit" is typed
def ask_for_input():
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("Enter a word (or type 'exit' to stop): ")
        if user_input.lower() != "exit":
            print(user_input)