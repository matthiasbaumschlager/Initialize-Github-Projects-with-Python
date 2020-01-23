######## Imports ########
from github import Github
import os
######## Imports ########


def _initiate_github_instance(username, password):
	return Github(username,password)
	

def _create_github_user(github_instance):
	return github_instance.get_user()

def _get_clone_url(repo_object):
	return repo_object.clone_url()

def _create_repo_with_all_properties(user,repo_name,repo_description,auto_init_bool,private_bool):
	return user.create_repo(repo_name, description=repo_description, auto_init=auto_init_bool, private=private_bool)

