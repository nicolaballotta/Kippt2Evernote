import os, sys
lib_path = os.path.abspath('evernote-sdk-python/lib')
sys.path.append(lib_path)

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
from bs4 import BeautifulSoup

##### Settings

# Set Kippt export file
kippt_file = ""

# Set the auth token for Evenrote
auth_token = ""

# Set the notebook where to import bookmarks
import_notebook = ""

##### END Settings

if auth_token == "":
    auth_token = raw_input("[*] Please fill in your developer token. \n" \
        "[*] To get a developer token, visit https://www.evernote.com/api/DeveloperToken.action\n" \

        "[*] Enter token: ")

if kippt_file == "":
    kippt_file = raw_input("[*] Enter Kippt export file: ")

if import_notebook == "":
    import_notebook = raw_input("[*] Enter the name of the notebook where would you like to import bookmarsk: ")


# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=False)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print "[*] Is my Evernote API version up to date? ", str(version_ok)
if not version_ok:
    exit(1)

note_store = client.get_note_store()

# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()
for notebook in notebooks:
    if notebook.name == import_notebook:
        nguid = notebook.guid
        print "[*] Filling " + import_notebook + " with guid " + nguid

soup = BeautifulSoup(open(kippt_file))

link_list = []

for element in soup.findAll('dt'):
    link_list.append([element.text, element.a['href']])

for bookmark in range(len(link_list)):

    note = Types.Note()
    nBody = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
    nBody += "<en-note>%s</en-note>" % link_list[bookmark][1]
    note.title = link_list[bookmark][0].rstrip('\n')
    note.content = nBody
    note.notebookGuid = nguid
    #note.tagNames = ["", "", ""]

    created_note = note_store.createNote(note)

    print "[*] Successfully created a new note with GUID: ", created_note.title



