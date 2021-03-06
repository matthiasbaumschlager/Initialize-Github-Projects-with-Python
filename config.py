### Imports ###
from PyInquirer import style_from_dict, Token, prompt
from functions import _get_folders_from_project_folder
### Imports ###

class Variables:
    ##Project-Folders
    Contribution_projects_folder="/home/matthias/My Files/02 Contribution/Freelance/Coding/"
    Contribution_Subfolders= _get_folders_from_project_folder(Contribution_projects_folder)
    Contribution_Subfolders.append("New Folder")
    Learning_projects_folder="/home/matthias/My Files/04 Growth/Learning/Coding/"
    Learning_Subfolders = _get_folders_from_project_folder(Learning_projects_folder)
    Learning_Subfolders.append("New Folder")
    List_Projects_folders=[Learning_projects_folder,Contribution_projects_folder]

    ##Languages
    # Github Login - Data
    Access_Token="66b610dc8cdd435aa97041a2aa2921e9e3703326"
    Username = "matthiasbaumschlager"
    Password = "8X3KaBFwAyFh"

    #Pre-config for question-style
    style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
    })