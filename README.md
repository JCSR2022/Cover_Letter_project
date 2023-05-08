# Copy Cover Letter Read Me

This program is designed to make the process of creating a cover letter easier by automating certain parts of it. This script copies a cover letter model to the clipboard with the input of the company and job name. The cover letter models are saved in a JSON file.

## Requirements
- Python 3
- Pyperclip

## How to Use
1. Run the `copy_cover_letter.py` script in the terminal or in an IDE.
2. Input the job name and company name when prompted.
3. Select a cover letter model from the available options.
4. The selected cover letter will be copied to the clipboard.
5. You will be prompted to save the cover letter as a `.txt` file.

## Functions
### `fill_cover_letter_model(job, company, selected_cover_letter)`
This function is used to fill in the selected cover letter model with the input job and company names. It returns the completed cover letter.

### `save_cover_letter(job, company, cover_letter)`
This function is used to save the cover letter as a text file in the "cover_letters" folder. It prompts the user to enter a file name, or suggests one based on the current date, company, and job.

### `main()`
This is the main function that runs the program. It loads the cover letter models from the JSON file, prompts the user for input, and calls the `fill_cover_letter_model()` and `save_cover_letter()` functions.

## Example Cover Letter Models
The cover letter models are saved in a JSON file called `cover_letter_repository.json`. Each cover letter has a unique identifier (e.g. "CL99"), a short description (e.g. "Marketing Coordinator"), and the text of the cover letter with variables for the job and company names (e.g. "Dear Hiring Manager, I am excited to apply for the {job} position at {company}...").

```json
{
    "CL01": {
        "Info": "Marketing Coordinator",
        "cover_letter": "Dear Hiring Manager, I am excited to apply for the {job} position at {company}..."
    },
    "CL02": {
        "Info": "Software Engineer",
        "cover_letter": "Dear {company} Recruiting Team, I am writing to express my interest in the {job} position..."
    },
    ...
}
```
