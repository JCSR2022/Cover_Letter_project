#!python3

import os
import json
#from translate import Translator

class repository:
    """Class to mannage the Cover letters repository ."""
    cmd_principal_menu = {
            "help":{"desc":"show cmd list"},
            "ls":{"desc":"List all cover Letters availables"},
            "show":{"desc":"enter menu to Show the content on a selected cover letter"},
            "insert":{"desc":"Move to insert menu "},
            "del":{"desc":"delete a cover letter model"},
            "exit":{"desc":"exit menu"}
            }
    
    def __init__(self):
        self.repository_name = "cover_letter_repository.json"
        self.repository_path = os.path.join(os.getcwd(),"cover_letter_repository.json")
        try:
            with open(self.repository_path) as f:
                self.cover_letter_repository = json.load(f)
        except Exception as e:
            print("Error: ", e)

    def __str__(self):
        return f"Working on the repository {self.repository_path} \n {self.cover_letter_repository}"
    
    def insert_cover(self, cover_key,cover_info,cover_letter_model):
        """
        Method to introduce a new cover letter model, most have:
        cover_key, example : "CL05" 
        cover_info, example: "Cover Leeter especial for data Enginner focus on web solutions"
        cover_letter_model, example: "I have interes in the {job} position at {company} because i am a star in web solutions"
        """
        self.cover_letter_repository[cover_key] ={"Info":cover_info,"cover_letter":cover_letter_model}
        with open(self.repository_path, 'w') as f:
             json.dump(self.cover_letter_repository, f)
        
        return cover_key, self.cover_letter_repository[cover_key]
    
    def cover_letters_list(self):
        return list(self.cover_letter_repository.keys())
    
    def print_cover_letters_list(self):
        cover_letters = self.cover_letters_list()
        cover_letters.sort()
        for cover_leter in cover_letters:
            print(f"{cover_leter} - {self.cover_letter_repository[cover_leter]['Info']}")
    
    def print_cover_letter_content(self,cover_leter):
        print(f"{cover_leter} - {self.cover_letter_repository[cover_leter]['cover_letter']}")    
    
    def remove_cover(self, cover_key):
        """
        Method to remove a cover letter model 
        """
        try:
            if cover_key in self.cover_letter_repository:
                del self.cover_letter_repository[cover_key] 
                with open(self.repository_path, 'w') as f:
                    json.dump(self.cover_letter_repository, f)
            else:
                print(f"{cover_key} not in cover letter repository ")
        except Exception as e:
            print("Error: ", e)
    
    @classmethod
    def not_standard(cls, path_and_name):
        """
        If the repository is not on the actual directory and standard name can give the path
        """
        obj = cls()
        obj.repository_path = path_and_name
        obj.repository_name = os.path.basename(obj.repository_path)
        try:
            with open(obj.repository_path) as f:
                obj.cover_letter_repository = json.load(f)
        except Exception as e:
            print("Error: ", e)
        return obj
    
    @staticmethod
    # def translate(text="",From_lang="es",To_lang="en"):
    #     """
    #     simple translator.
    #     input ("es","en",text) #translate from spanish to english
    #     """
    #     # method implementation here
    #     translator = Translator(from_lang= From_lang, to_lang= To_lang)
    #     translation = translator.translate(text)
    #     return translation
    
    def enter_long_text():
        print("Press Enter to finish:")
        text_input = []
        while True:
            line = input()
            if line == '':
                break
            text_input.append(line)
        return "\n".join(text_input)



def display_menu(menu):
    print("Please execute a comand:")
    for menu_option in menu:
        print(f"[{menu_option}],{menu[menu_option]['desc']} ")    

def interact_show_menu(selection,cover_letter_repo):
    print(f"Enter the Cover to show")
    while True:
        selection_to_show = input(f"cover\{selection} >> ")
        if selection_to_show in cover_letter_repo.cover_letters_list():
            cover_letter_repo.print_cover_letter_content(selection_to_show)
        elif selection_to_show == "exit":
            break
        else:
            print("Invalid cmd or selection, Try again.")
    return

def interact_insert_menu(selection,cover_letter_repo):
    while True:
        print("Enter the name of the cover letter (examp: CL34 or Cover_for_Astronaut_job):")
        name = input(f"cover\{selection} >> ")
        
        if name in cover_letter_repo.cover_letters_list():
            while True:
                acction = input(f"cover\{selection} >>it already exists, do you want to replace it y/n? ")
                if acction =='n':
                    return
                elif acction =='y':
                    break
                else:
                    print("invalid selection please input 'y' or 'n'")
                    continue
        
        print("Enter information to refer the cover letter:")
        info = input(f"cover\{selection} >> ")
        print("""
Enter content of the cover letter 
Remember to use {job} and {company} 
where making reference to the the values will be changing.
""")
        cover_letter = repository.enter_long_text()
        cover_letter_repo.insert_cover(name,info,cover_letter)
        while True:
            cont_or_finish = input(f"cover\{selection} >>insert another y/n? ")
            if cont_or_finish =='n':
                return
            elif cont_or_finish =='y':
                break
            else:
                print("invalid selection please input 'y' or 'n'")
                continue
    return

def interact_del_menu(selection,cover_letter_repo):
    try:
        print(f"Please enter the Cover letter name to erase")
        while True:
            cover_key_erase = input(f"cover\{selection} >> ")
            if cover_key_erase in cover_letter_repo.cover_letters_list():
                cover_letter_repo.remove_cover(cover_key_erase) 
                print(f" {cover_key_erase} Deleted successfully")
                return   
            else:
                print(f"{cover_key_erase} not in cover letter repository ")
                return
    except Exception as e:
        print("Error: ", e)
    return


def main():
    try:
        cover_letter_repo = repository()
        while True:
            selection = input("cover >> ")
            if selection in cover_letter_repo.cmd_principal_menu:
                #valids = ['help','ls', 'show', 'insert', 'del', 'exit']
                if selection == "help":
                    display_menu(cover_letter_repo.cmd_principal_menu )
                    
                if selection == "ls":
                    cover_letter_repo.print_cover_letters_list()
                    
                if selection == "show":
                    interact_show_menu(selection,cover_letter_repo)
                    
                if selection == "insert":
                    interact_insert_menu(selection,cover_letter_repo)
                
                if selection == "del":
                    interact_del_menu(selection,cover_letter_repo)                   

                
                if selection == "exit":
                    print("Goodbye!")
                    break
                
            else:
                print("Invalid cmd. Please try again.")
    
        
    except Exception as e:
        print("Error: ", e)


if __name__ == '__main__':
    main()
