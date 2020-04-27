######## Imports ########
#Packages
##for back-end
import os
import time
from github import Github
##for front-end
from pyfiglet import Figlet
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
## Files from my Workspace
from config import Variables as Config
import functions as Functions
######## Imports ########
class Script:
    def __init__(self):

        self.user=None
        self.repo=None

        ### User-Input Section ###
        greeting = Figlet(font="slant")
        print(greeting.renderText("New Project"))

        questions_without_languages = [
        {
            "type": "input",
            "name": "repo_name",
            "message": "What is the name for your new Repository?",
            "validate": Functions.Repo_name_not_empty

        },
        {
            "type": "input",
            "name": "repo_description",
            "message": "Please type in a suitable description for your new Project here:",
            "validate": Functions.Repo_description_not_empty

        },
        {
            "type": "confirm",
            "name": "auto_init",
            "message": "Do you want to auto-init your Repository (includes ReadMe-File)",
            "default": False

        },
        {
            "type": "confirm",
            "name": "private_repo",
            "message": "Do you want your Repository to be private?",
            "default": True

        },
        {
            "type": "list",
            "name": "project_folder",
            "message": "In which project-folder do you want to clone your new repository?",
            "choices": Config.List_Projects_folders,
            "default": Config.List_Projects_folders[0]
        }]
        answers_without_languages=prompt(questions_without_languages, style=Config.style)
        if(answers_without_languages["project_folder"]==Config.Learning_projects_folder):
            language_choices=Config.Learning_Subfolders
        else:
            language_choices=Config.Contribution_Subfolders
        language_question=[
        {
            "type": "list",
            "name": "language",
            "message": "Please select the Programming-Language for your new project.",
            "choices": language_choices
        }]
        ### User-Input Section ###
        language_answer=prompt(language_question, style=Config.style)
        if(language_answer["language"]=="New Folder"):
            folder_name = input("Please type a name for your new folder:")
            os.mkdir(os.path.join(answers_without_languages["project_folder"],folder_name))
            ####
            if(answers_without_languages["project_folder"]==Config.Learning_projects_folder):
                language_choices=Functions._get_folders_from_project_folder(Config.Learning_projects_folder)
            else:
                language_choices=Functions._get_folders_from_project_folder(Config.Contribution_projects_folder)
            ####
            language_answer=prompt(language_question, style=Config.style)

        # Backend - doing all the work after (correct) user input.
        self.user = Github(Config.Username, Config.Password).get_user()

        try:
            for repo in self.user.get_repos():
                if(repo.name==answers_without_languages["repo_name"]):
                    raise Exception("This repository already exists!")
            self.repo = Functions._create_repo_with_all_properties(self.user, answers_without_languages["repo_name"], answers_without_languages["repo_description"], answers_without_languages["auto_init"], answers_without_languages["private_repo"])
        except Exception as e:
            print(str(e))
            time.sleep(4.2)
            exit()


        if type(self.repo) != bool:
            if(Functions._clone_repo_to_project_folder(self.repo, os.path.join(answers_without_languages["project_folder"],language_answer["language"]))):
                print("Your new GitHub-Project was successfully created and was cloned to your desired project-folder!")
                print("Enjoy your work :)")
                time.sleep(4.2)


if __name__ == "__main__":
    c=Script()


