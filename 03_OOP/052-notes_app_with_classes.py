from dataclasses import dataclass
import json
from random import sample
from time import sleep
from datetime import datetime

class InvalidOptionError(Exception):
    pass

@dataclass
class Note:
    note_file_name: str
    note_content_title: str
    note_content_body: str
    
    def generate_note_id(self):
        random_id_samples = sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 4)
        return "".join(random_id_samples)
    
    
    
    def get_data_from_json_file(self):
        try:
            with open("./files/notes-database.json", 'r') as f1:
                data:dict = json.loads(f1.read())
        except FileNotFoundError:
            data = {}
        return data

    def create_note(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = self.get_data_from_json_file()
        data[self.note_file_name] = {
            "ID": self.generate_note_id(),
            "Title": self.note_content_title,
            "Body": self.note_content_body,
            "Created_At": current_time,
            "Updated_At": current_time
        }
        with open("./files/notes-database.json", 'w') as f1:
            f1.write(json.dumps(data))
    
    def display_note(self):
        data = self.get_data_from_json_file()
        if self.note_file_name in data.keys():
            return f"\n*****\t*****\nNote Name: \t {self.note_file_name} \n\t----- \nNote Created At: \t {data[self.note_file_name]["Created_At"]} \nNote Updated At: \t {data[self.note_file_name]["Updated_At"]} \n\t----- \nNote Title: \t {data[self.note_file_name]["Title"]} \nNote Body: \t {data[self.note_file_name]["Body"]}\n*****\t*****\n"
    
    def update_database(self):
        data = self.get_data_from_json_file()
        updated_data = self.create_note(data)
        with open("./files/notes-database.json", 'w') as f1:
            f1.write(json.dumps(updated_data))        
    
    def remove_note(self):
        data = self.get_data_from_json_file()
        del data[self.note_file_name]
        with open("./files/notes-database.json", 'w') as f1:
            f1.write(json.dumps(data))

    def update_note(self):
        data = self.get_data_from_json_file()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.note_file_name in data.keys():
            data[self.note_file_name]["Title"] = self.note_content_title
            data[self.note_file_name]["Body"] = self.note_content_body
            data[self.note_file_name]["Updated_At"] = current_time
            with open("./files/notes-database.json", 'w') as f1:
                f1.write(json.dumps(data))
        else:
            raise KeyError("Note not found in the database.")
    

@dataclass
class Note_Database:
    note_file_name: str
    
    def get_data_from_json_file(self):
        try:
            with open("./files/notes-database.json", 'r') as f1:
                data:dict = json.loads(f1.read())
        except FileNotFoundError:
            data = {}
        return data
    
    def show_all_nots(self):
        data = self.get_data_from_json_file()
        data_lists = ""
        for note in data.keys():
            data_lists += f"\n- {note}.txt\t Note ID:{data[note]["ID"]}\t Created At:{data[note]["Created_At"]}"
        
        return data_lists

    def display_note(self):
        data = self.get_data_from_json_file()
        if self.note_file_name in data.keys():
            return f"\n*****\t*****\nNote Name: \t {self.note_file_name} \n\t----- \nNote Created At: \t {data[self.note_file_name]["Created_At"]} \nNote Updated At: \t {data[self.note_file_name]["Updated_At"]} \n\t----- \nNote Title: \t {data[self.note_file_name]["Title"]} \nNote Body: \t {data[self.note_file_name]["Body"]}\n*****\t*****\n"

    def search_note_by_name(self):
        data = self.get_data_from_json_file()
        if self.note_file_name in data.keys():
            return f"{self.note_file_name} is in the list.\n \n- {self.note_file_name}.txt\t Note ID:{data[self.note_file_name]["ID"]}\t Created At:{data[self.note_file_name]["Created_At"]}"
        else:
            return False




def user_flow():
    print("WELCOME TO NOTES MANAGEMENT SYSTEM")
    print("----------------------------------")
    user_main_menu = int(input(f"Choose these options: \n1.\tNote \n2.\tNote Database \n3.\tShow Note File \n4.\tSearch Note File\t\t Write 'exit' to Leave Program\n\nYour Choice (1 to 4): "))
    
    if user_main_menu == 1:
        print("NOTE SECTION")
        print("------------")
        user_note_menu = int(input(f"Note Operation: \n1.\tCreate Note \n2.\tUpdate Note \n3.\tDelete Note \n\nYour Choice (1 to 3): "))
        
        if user_note_menu == 1:
            print("CREATE NEW NOTE")
            print("---------------")
            user_note_file_name = str(input("Enter File Name (Without .txt): "))
            user_note_title = str(input("Enter Note Title: "))
            user_note_body = str(input("Enter Note Body: "))
            user_note = Note(user_note_file_name, user_note_title, user_note_body)
            print("The Progress is in Process...\n Please Wait ...")
            sleep(2)
            user_note.create_note()
            print(f"Progress Done. Here is your data. \n")
        
        elif user_note_menu == 2:
            print("UPDATE NOTE")
            print("-----------")
            user_note_file_name = str(input("Enter File Name (Without .txt): "))
            user_note_title = str(input("Enter New Note Title: "))
            user_note_body = str(input("Enter New Note Body: "))
            user_note = Note(user_note_file_name, user_note_title, user_note_body)
            print("The Progress is in Process...\n Please Wait ...")
            sleep(2)
            user_note.update_note()
            print(f"Progress Done. Here is your data. \n")
        
        elif user_note_menu == 3:
            print("DELETE NOTE")
            print("-----------")
            user_note_file_name = str(input("Enter File Name (Without .txt): "))
            user_note = Note(user_note_file_name, "-", "-")
            print("The Progress is in Process...\n Please Wait ...")
            sleep(2)
            user_note.remove_note()
            print(f"Progress Done.")
        
        else:
            raise InvalidOptionError("Invalid Option Selected. Please choose a valid option.")
    
    elif user_main_menu == 2:
        print("NOTE DATABASE SECTION")
        print("---------------------")
        user_notes_database = Note_Database("-")
        print("The Progress is in Process...\n Please Wait ...")
        sleep(2)
        print(user_notes_database.show_all_nots())
        
    elif user_main_menu == 3:
        print("SHOW NOTE FILE SECTION")
        print("----------------------")
        user_note_file_name = str(input("Enter File Name (Without .txt): "))
        user_notes_database = Note_Database(user_note_file_name)
        print("The Progress is in Process...\n Please Wait ...")
        sleep(2)
        print(user_notes_database.display_note())
    
    elif user_main_menu == 4:
        print("SEARCH NOTE FILE SECTION")
        print("------------------------")
        user_note_file_name = str(input("Enter File Name (Without .txt): "))
        user_notes_database = Note_Database(user_note_file_name)
        print("The Progress is in Process...\n Please Wait ...")
        sleep(2)
        print(user_notes_database.search_note_by_name())
    
    elif user_main_menu == 'exit':
        print("Exiting the program. Goodbye!")
        return
    
    else:
        raise InvalidOptionError("Invalid Option Selected. Please choose a valid option.")



if __name__ == "__main__":
    user_flow()