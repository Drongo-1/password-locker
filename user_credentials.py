import pyperclip
import random
import string

# Global Variables
global users_list


class User:
        Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)

