#!python3

"""program to copy a cover letter model to_clipboard
just need to imput the name of the company and the job name
Te covers letters models are on a json file
"""

import pyperclip
from datetime import datetime
import json
import time
import os

# first aproach to fill, the idea is later implement a ChatGPt solution 
#    with info form the company and the job, focus the skills to best match the job description
def fill_cover_letter_model(job,company,selected_cover_letter):
    cover =  f"""{datetime.now().strftime("%B %d, %Y")} \n"""
    cover +=  f"""{selected_cover_letter["cover_letter"].format(job=job, company=company)}""" 
    return cover


def save_cover_letter(job,company,cover_letter):
    while True:
            print("Do you want to save a .txt with the cover letter  y/n? " )
            yes_no =  input("cover_letter >> ")
            if yes_no =='n':
                return
            elif yes_no =='y':
                today_for_file = datetime.now().strftime("%y%m%d")
                suggested_name = "_".join([today_for_file, company, job])
                print("Enter file name (default: {}), if file exist will be  will be replaced ".format(suggested_name))
                selection = input("cover_letter >> ") or suggested_name
                
                # create the "cover_letters" folder if it doesn't exist
                if not os.path.exists("cover_letters"):
                    os.makedirs("cover_letters")
                    
                file_path = os.path.join("cover_letters", selection+".txt")
                
                # save the cover letter to a text file
                with open(file_path, "w") as file:
                    file.write(cover_letter)
                
                return
            else:
                print("invalid selection please input 'y' or 'n'")
                continue
    
def main():
    # Loading data to fill the cover letter:
    try:
        #   The cover letter models are in a json file, adjust to the variables {job} and {company}
        with open('cover_letter_repository.json') as f:
            cover_letter_repository = json.load(f)
    except Exception as e:
        print("Error: no cover_letter_repository.json file, ", e)
        cover_letter_repository = {"CL99": {"Info": "No cover letter","cover_letter":""}}
    
    print("Enter job name: " )
    job =  input("cover_letter >> ")
    print("Enter company name: " )
    company =  input("cover_letter >> ")

    text = f"""There are {len(cover_letter_repository)} models of cover letter\n"""
    for cover_letter in cover_letter_repository:
        text += f""" -> {cover_letter} , {cover_letter_repository[cover_letter]["Info"]}\n"""
    print(text)
    print("select cover letter model: " )
    selected_cover_letter =  input("cover_letter >> ")

    if selected_cover_letter in cover_letter_repository:
        to_fill = cover_letter_repository[selected_cover_letter]
        cover_letter = fill_cover_letter_model(job,company,to_fill)
        pyperclip.copy(cover_letter)
        save_cover_letter(job,company,cover_letter)
 
    else:
        print("Select a correct Cover Letter model")    
        time.sleep(1)

if __name__ == '__main__':
    main()

