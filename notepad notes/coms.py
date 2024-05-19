import whtsapp_cmd
import mail
import sms_cmd

while True:
    print("Menu:")
    print("1. Whatsappe")
    print("2. Mail")
    print("3. Sms")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        whtsapp_cmd.run()
    elif choice == "2":
        mail.run()
    elif choice == "3":
        sms_cmd.run()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting the program.")
