import pyfiglet
import colorama
import os
colorama.init(autoreset=True)

def clear():
    os.system('cls')

def restart():
    clear()
    main()

def main():
    clear()
    logo = pyfiglet.figlet_format("TEST", font="graffiti", justify='center')
    print(colorama.Fore.LIGHTMAGENTA_EX + logo)

    print(colorama.Fore.RED + "[1]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "Open Command Prompt" + colorama.Fore.RESET + " " + colorama.Fore.RED + "[4]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "Dunnotf") 
    print(colorama.Fore.RED + "[2]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "Open Notepad       " + colorama.Fore.RESET + " " + colorama.Fore.RED + "[5]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "rahh")
    print(colorama.Fore.RED + "[3]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "Exit               " + colorama.Fore.RESET + " " + colorama.Fore.RED + "[6]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "weeee")
    
    choice = int(input(colorama.Fore.RED + "\n[/]" + colorama.Fore.RESET + " " + colorama.Fore.LIGHTBLACK_EX + "Enter your choice: "))

    if choice == 1:
        os.system('start cmd')
    elif choice == 2:
        os.system('start notepad')
        clear()
        main()
    elif choice == 3:
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        clear()
        main()

if __name__ == "__main__":
    main()

