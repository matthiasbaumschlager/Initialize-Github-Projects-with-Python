######## Imports ########
from github import Github
import os
######## Imports ########


# def _initiate_github_instance(access_token):
# 	return Github(access_token)

# def _get_github_user(github_instance):
# 	return github_instance.get_user()

def _create_repo_with_all_properties(user,repo_name,repo_description,auto_init_bool,private_bool):
	try:
		return user.create_repo(repo_name, auto_init=auto_init_bool, description=repo_description, private=private_bool)
	except:
		return False

def _clone_repo_to_project_folder(repo_object, project_folder,language):
	try:
		if repo_object.ssh_url is None:
			raise Exception("There is no GitHub ssh repository URL!")

		# unfortunately there is no way (yet) to clone with pygithub
		clone="git clone {}".format(repo_object.ssh_url)
		os.chdir(os.path.join(project_folder,language))  # Specifying the path where the cloned project needs to be copied
		os.system(clone)  # Cloning
		return True

	except Exception as e:
		print(str(e))
		return False
