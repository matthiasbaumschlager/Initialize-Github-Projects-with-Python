######## Imports ########
#Packages
import os
import time
#Other files
import functions as Functions
from config import Variables as Config
######## Imports ########

class Script:
	def __init__(self):





		# Backend - doing all the work after (correct) user input.
		self.user = Functions._get_github_user(Functions._initiate_github_instance(Config.access_token))
		repo = Functions._create_repo_with_all_properties(repo_name, repo_description, auto_init, private_repo)
		if repo != False:
			if(Functions._clone_repository_to_project_folder):
				print("""Your new GitHub-Project was successfully created and is already cloned to your desired projec-folder!
					Enjoy your work :)""")
				time.sleep(4.2)


if __name__ == "__main__":
	c=Script()


