######## Imports ########
#Packages
import os
import time
from github import Github
#Other files
import functions as Functions
from config import Variables as Config
######## Imports ########

class Script:
	def __init__(self):
		# repo_name = "Test-Repository-matthiasbaumschlager"
		# repo_description = "Sth worse than the solution 42."
		# auto_init = True
		# private_repo = True
		# selected_language="Python"

		self.user=None
		self.repo=None


		# Backend - doing all the work after (correct) user input.
		self.user = Github(Config.Username, Config.Password).get_user()

		try: 
			for repo in self.user.get_repos():
				if(repo.name==repo_name):
					raise Exception("This repository already exists!")
			self.repo = Functions._create_repo_with_all_properties(self.user, repo_name, repo_description, auto_init, private_repo)
			print(self.repo.name)
		except Exception as e:
			print(str(e))
			time.sleep(4.2)
			exit()
		

		if type(self.repo) != bool:
			if(Functions._clone_repo_to_project_folder(self.repo, Config.Learning_projects_folder, selected_language)):
				print("""Your new GitHub-Project was successfully created and is already cloned to your desired project-folder!
					Enjoy your work :)""")
				time.sleep(4.2)


if __name__ == "__main__":
	c=Script()


