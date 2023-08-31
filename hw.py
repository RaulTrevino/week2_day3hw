
grocery_list={}

def shopping():


    while True:
        user_choice = input("Enter your choice: 'add' 'remove' 'view' 'quit'")
        
        if user_choice == "add":
            grocery= input("Enter item name: ")
            quantity = input('enter how many')
            grocery_list[grocery] = quantity

        
        elif user_choice == "remove":
            del_item = input("Enter item name to delete: ")
            del grocery_list[del_item]
        elif user_choice == "view":
                 print(grocery_list)

        else:
            user_choice == "quit"
            print('Goodbye')
            if user_choice.lower() == "quit":
                break


shopping()

print(grocery_list)

