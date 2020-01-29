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
#Other files
import functions as Functions
from config import Variables as Config
######## Imports ########

class Script:
	def __init__(self):

		self.user=None
		self.repo=None

		### User-Input Section ###
		greeting = Figlet(font="slant")
		print(greeting.renderText("New Project"))

		questions = [
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
		},
		{
			"type": "list",
			"name": "language",
			"message": "Please select the Programming-Language for your new project.",
			"choices": Config.List_Languages
		}]
		### User-Input Section ###

		answers=prompt(questions, style=Config.style)


		##Break the back-end for now!
		#exit()


		# Backend - doing all the work after (correct) user input.
		self.user = Github(Config.Username, Config.Password).get_user()

		try: 
			for repo in self.user.get_repos():
				if(repo.name==answers["repo_name"]):
					raise Exception("This repository already exists!")
			self.repo = Functions._create_repo_with_all_properties(self.user, answers["repo_name"], answers["repo_description"], answers["auto_init"], answers["private_repo"])
			print(self.repo.name)
		except Exception as e:
			print(str(e))
			time.sleep(4.2)
			exit()
		

		if type(self.repo) != bool:
			if(Functions._clone_repo_to_project_folder(self.repo, os.path.join(answers["project_folder"],answers["language"]))):
				print("""Your new GitHub-Project was successfully created and was cloned to your desired project-folder!
					Enjoy your work :)""")
				time.sleep(4.2)


if __name__ == "__main__":
	c=Script()


