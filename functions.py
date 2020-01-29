######## Imports ########
##Back-end
from github import Github
import os
import time
##Front-end
from PyInquirer import Validator, ValidationError
######## Imports ########


### Front-end ###

#Configuring the validators for all questions
class Repo_name_not_empty(Validator):
	def validate(self, document):
		if(document.text == "" || document.text == None || document.text == " "):
			raise ValidationError(message="Please enter a valid name for your new Repository!")

class Repo_description_not_empty(Validator):
	def validate(self, document):
		if(document.text == "" || document.text == None || document.text == " "):
			raise ValidationError(message="Please enter a valid description for your new Repository!")










### Back-end ###
def _create_repo_with_all_properties(user,repo_name,repo_description,auto_init_bool,private_bool):
	try:
		return user.create_repo(repo_name, auto_init=auto_init_bool, description=repo_description, private=private_bool)
	except:
		return False

def _clone_repo_to_project_folder(repo_object, project_folder,language):
	try:
		clone_path=os.path.join(project_folder,language)
		if repo_object.ssh_url is None:
			raise Exception("There is no GitHub ssh repository URL!")
		if os.path.isdir(clone_path):
			raise Exception("The repository is already cloned to the selected destination!")

		# unfortunately there is no way (yet) to clone with pygithub
		clone="git clone {}".format(repo_object.ssh_url)
		os.chdir(clone_path) # Specifying the path where the cloned project needs to be copied
		os.system(clone)  # Cloning
		return True

	except Exception as e:
		print(str(e))
		time.sleep(4.2)
		exit()
		
