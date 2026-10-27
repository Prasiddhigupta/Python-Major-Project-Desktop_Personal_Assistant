import os
import time
import webbrowser
from datetime import datetime


class PersonalAssistant:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("\nWelcome! I am", self.name)
        print("Your Personal Assistant is ready.")

    def show_menu(self):
        print("\n===== PERSONAL ASSISTANT =====")
        print("1. Tell Date and Time")
        print("2. Open Notepad")
        print("3. Open Calculator")
        print("4. Open YouTube")
        print("5. Open Google")
        print("6. Search a File")
        print("7. Set a Reminder")
        print("8. Exit")

    def tell_time(self):
        now = datetime.now()
        print("Date:", now.strftime("%d-%m-%Y"))
        print("Time:", now.strftime("%I:%M %p"))

    def open_notepad(self):
        print("Opening Notepad...")
        if os.name == "nt":
            os.system("start notepad")
        else:
            print("This option is for Windows.")

    def open_calculator(self):
        print("Opening Calculator...")
        if os.name == "nt":
            os.system("start calc")
        else:
            print("This option is for Windows.")

    def open_youtube(self):
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    def open_google(self):
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    def search_file(self):
        file_name = input("Enter the file name to search: ").strip()

        if not file_name:
            print("Please enter a file name.")
            return

        folders = [
            os.path.join(os.path.expanduser("~"), "Desktop"),
            os.path.join(os.path.expanduser("~"), "Documents"),
            os.path.join(os.path.expanduser("~"), "Downloads")
        ]

        found_files = []

        print("Searching... Please wait.")

        for folder in folders:
            if not os.path.isdir(folder):
                continue

            for root, dirs, files in os.walk(folder, onerror=lambda error: None):
                for file in files:
                    if file_name.lower() in file.lower():
                        found_files.append(os.path.join(root, file))

        if found_files:
            print("\nFiles found:")
            for file_path in found_files:
                print(file_path)
        else:
            print("No matching file found.")

    def set_reminder(self):
        message = input("What should I remind you about? ").strip()

        if not message:
            print("Reminder message cannot be empty.")
            return

        try:
            seconds = int(input("After how many seconds? "))

            if seconds <= 0:
                print("Please enter a number greater than zero.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

        print("Reminder set successfully!")
        print("You can wait here; the reminder will appear when time is up.")

        time.sleep(seconds)

        print("\n===== REMINDER =====")
        print(message)

    def run(self):
        self.greet()

        while True:
            self.show_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                self.tell_time()

            elif choice == "2":
                self.open_notepad()

            elif choice == "3":
                self.open_calculator()

            elif choice == "4":
                self.open_youtube()

            elif choice == "5":
                self.open_google()

            elif choice == "6":
                self.search_file()

            elif choice == "7":
                self.set_reminder()

            elif choice == "8":
                print("Thank you for using the Personal Assistant!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")


assistant = PersonalAssistant("Desktop Personal Assistant")
assistant.run()