#!/usr/bin/python

"""Google Drive Quickstart in Python.

This script uploads a single file to Google Drive.
"""
import urllib2

from tqdm import tqdm
import requests
import pprint
import time


import httplib2
import apiclient.discovery
import apiclient.http
import oauth2client.client
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

import glob, os


# FILENAME = []
Entries = []
AllEntry = []
Folders = ["Software Interface Management", "Sensor Fusion", "Perception", "Prediction", "Local Mapping", "Path Planning", "Simulation", "User Interface", "Embedded Implementation and Controls", "Signals Processing and Amplifier Design", "Vehicle Dynamics", "Sensor Mounting and Cooling", "Internal Affairs", "Marketing", "Finance", "Sponsorship", "Website", "Graphic Design", "All Entries"]
n = ["Software","SensorFusion","Perception",
"Prediction",    "Local",  "Path", "Simulation", "User", "Embedded", "Signals", "Vehicle", "SensorMount","Internal","Marketing","Finance", "Sponsorship", "Website","Graphic"]




def getEntries():
    os.chdir("Subteams/")
    f = Folders
    for i in range(0, len(f)):
        os.chdir(f[i]+"/")

        for file in glob.glob("*.csv"):
            Entries.append(file)

        os.chdir("../")

    os.chdir("../")
    print("Entries", Entries)
    # os.chdir("Subteams/")
    #
    # for file in glob.glob("*.csv"):
    #     AllEntry.append(file)
    # print("\nPrinting Entries: ", AllEntry[0])
    # os.chdir("../")




def insertFolders(parent_id):
    f = Folders
    os.chdir("Subteams/")

    for i in range(0, len(f)):

        # Inserts Folder
        file_metadata = {
            'title': f[i],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [{'id': parent_id}]
        file = drive_service.files().insert(body=file_metadata, fields='id').execute()
        os.chdir(f[i]+"/")

        # Inserts SubteamLead csv into Google Sheets
        file_metadata = {
            'title': Entries[i*2],
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload( Entries[i*2] ,mimetype='text/csv',resumable=True)
        if parent_id:
            file_metadata['parents'] = [{'id': file.get('id')}]

        new_file = drive_service.files().insert(body=file_metadata, media_body=media, fields='id' ).execute()

        # Inserts SubteamLead + CoreMember csv into Google Sheets
        file_metadata = {
            'title': Entries[(i*2)+1],
            'mimeType': 'application/vnd.google-apps.spreadsheet'
        }
        media = MediaFileUpload( Entries[(i*2)+1] ,mimetype='text/csv',resumable=True)
        if parent_id:
            file_metadata['parents'] = [{'id': file.get('id')}]

        new_file = drive_service.files().insert(body=file_metadata, media_body=media, fields='id' ).execute()





        # pprint.pprint(new_file)


        os.chdir("../")

    os.chdir("../")




OAUTH2_SCOPE = 'https://www.googleapis.com/auth/drive'

# Location of the client secrets.
CLIENT_SECRETS = 'client_secrets.json'

# Path to the file to upload.
# FILENAME[0] = 'document.txt'

# Metadata about the file.


# Perform OAuth2.0 authorization flow.
flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRETS, OAUTH2_SCOPE)
flow.redirect_uri = oauth2client.client.OOB_CALLBACK_URN
authorize_url = flow.step1_get_authorize_url()
print 'Go to the following link in your browser: ' + authorize_url
code = raw_input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an authorized Drive API client.
http = httplib2.Http()
credentials.authorize(http)
drive_service = apiclient.discovery.build('drive', 'v2', http=http)

# Insert a file. Files are comprised of contents and metadata.
# MediaFileUpload abstracts uploading file contents from a file on disk.

MIMETYPE = 'text/csv'
DESCRIPTION = ''

# file_metadata = {
#     'title': 'Wato_Apps_' + time.strftime("%Y/%m/%d"),
#     'mimeType': 'application/vnd.google-apps.folder'
# }
# file = drive_service.files().insert(body=file_metadata, fields='id').execute()
# parent_id = file.get('id')
parent_id = "1uTqv3QvjhGlQP3tp1xaquWf9-PBVUpL_"
# parent_id = "13FiNDz6lRKnz9quo-pKXl6FAIy55Stc3"



page_token = None
while True:
    param = {}
    if page_token:
        param['pageToken'] = page_token
    children = drive_service.children().list(folderId=parent_id, **param).execute()

    for child in children.get('items', []):
        # print 'File Id: %s' % child['id']
        drive_service.children().delete(folderId=parent_id, childId=child['id']).execute()

    page_token = children.get('nextPageToken')
    if not page_token:
        break
    # except errors.HttpError, error:
    #     print 'An error occurred: %s' % error
    #     break
getEntries()



insertFolders(parent_id)


#         FILENAME[x],
#         mimetype=MIMETYPE,
#         resumable=True
#         )
#         # The body contains the metadata for the file.
#     body = {
#     'title': FILENAME[x],
#     'description': "",
#     # 'parents': folder_id,
#     }
#     if parent_id:
#         body['parents'] = [{'id': parent_id}]
#
#
#     # Perform the request and print the result.
#     new_file = drive_service.files().insert(body=body, media_body=media_body).execute()

# items = results.get('files', [])
# print(items)
#
# for x in range(0, count):
#     # print(FILENAME[x])
#     # print(folder_id)
#     media_body = apiclient.http.MediaFileUpload(
#         FILENAME[x],
#         mimetype=MIMETYPE,
#         resumable=True
#         )
#         # The body contains the metadata for the file.
#     body = {
#     'title': FILENAME[x],
#     'description': "",
#     # 'parents': folder_id,
#     }
#     if parent_id:
#         body['parents'] = [{'id': parent_id}]
#
#
#     # Perform the request and print the result.
#     new_file = drive_service.files().insert(body=body, media_body=media_body).execute()
#     pprint.pprint(new_file)
