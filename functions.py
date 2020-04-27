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
        if(document.text == "" or document.text == None or document.text == " "):
            raise ValidationError(message="Please enter a valid name for your new Repository!")

class Repo_description_not_empty(Validator):
    def validate(self, document):
        if(document.text == "" or document.text == None or document.text == " "):
            raise ValidationError(message="Please enter a valid description for your new Repository!")



### Back-end ###
def _create_repo_with_all_properties(user,repo_name,repo_description,auto_init_bool,private_bool):
    try:
        return user.create_repo(repo_name, auto_init=auto_init_bool, description=repo_description, private=private_bool)
    except:
        return False


def _get_folders_from_project_folder(Project_Folder):
    list_subfolder_names = [f.name for f in os.scandir(Project_Folder) if f.is_dir()]
    return list_subfolder_names


def _clone_repo_to_project_folder(repo_object, clone_folder):
    try:
        if repo_object.ssh_url is None:
            raise Exception("There is no GitHub ssh repository URL!")
        if os.path.isdir(os.path.join(clone_folder,repo_object.name)):
            raise Exception("The repository is already cloned to the selected destination!")

        # unfortunately there is no way (yet) to clone with pygithub
        clone="git clone {}".format(repo_object.ssh_url)
        os.chdir(clone_folder) # Specifying the path where the cloned project needs to be copied
        os.system(clone)  # Cloning
        return True

    except Exception as e:
        print(str(e))
        time.sleep(4.2)
        exit()

