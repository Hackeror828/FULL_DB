import subprocess
import sys

print("""
 _______       ___   .___________.    ___         .______        ___           _______. _______ 
|       \     /   \  |           |   /   \        |   _  \      /   \         /       ||   ____|
|  .--.  |   /  ^  \ `---|  |----`  /  ^  \       |  |_)  |    /  ^  \       |   (----`|  |__   
|  |  |  |  /  /_\  \    |  |      /  /_\  \      |   _  <    /  /_\  \       \   \    |   __|  
|  '--'  | /  _____  \   |  |     /  _____  \     |  |_)  |  /  _____  \  .----)   |   |  |____ 
|_______/ /__/     \__\  |__|    /__/     \__\    |______/  /__/     \__\ |_______/    |_______|
                                                                                                    
      """)



print("""
   __  ___        __                                               
  /  |/  /__ ____/ /__                                             
 / /|_/ / _ `/ _  / -_)                                            
/_/  /_/\_,_/\_,_/\__/                                             
              __                                                   
             / /  __ __                                            
            / _ \/ // /                                            
           /_.__/\_, /                                             
                /___/_         __                    ___  ___  ___ 
                / // /__ _____/ /_____ _______  ____( _ )|_  |( _ )
               / _  / _ `/ __/  '_/ -_) __/ _ \/ __/ _  / __// _  |
              /_//_/\_,_/\__/_/\_\\__/_/  \___/_/  \___/____/\___/ 
                                                                   
""")






def run_config():
    """Run the config script."""
    print("Running config script...")
    subprocess.run([sys.executable, 'config.py'])

def run_user():
    """Run the user script."""
    print("Running user script...")
    subprocess.run([sys.executable, 'user.py'])

def run_server():
    """Run the server script."""
    print("Running server script...")
    subprocess.run([sys.executable, 'server.py'])

def display_menu():
    """Display the main menu."""
    print("\nMain Menu:")
    print("1. Run config script")
    print("2. Run user script")
    print("3. Run server script")
    print("4. Exit")

def main():
    """Main function to handle user choices."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            run_config()
        elif choice == '2':
            run_user()
        elif choice == '3':
            run_server()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
