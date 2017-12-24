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

    print("\nPrinting Entries: ", Entries[0])
    os.chdir("../")
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
        file_metadata = {
            'title': f[i],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [{'id': parent_id}]
        file = drive_service.files().insert(body=file_metadata, fields='id').execute()
        os.chdir(f[i]+"/")

        media_body = apiclient.http.MediaFileUpload(
            Entries[i],
            mimetype=MIMETYPE,
            resumable=True
            )
        # The body contains the metadata for the file.
        body = {
            'title': Entries[i],
            'description': "",
            # 'parents': folder_id,
        }
        if parent_id:
            body['parents'] = [{'id': file.get('id')}]

    # Perform the request and print the result.
        new_file = drive_service.files().insert(body=body, media_body=media_body).execute()
        pprint.pprint(new_file)
        os.chdir("../")

    os.chdir("../")


    # media_body = apiclient.http.MediaFileUpload(
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




# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.

# url = "http://download.thinkbroadband.com/1MB.zip"
# url = "http://watonomous.leanwetools002.wpengine.com/wp-content/uploads/sites/14/gravity_forms/11-22355c64a37bed0f8562f3ec11ccf735/2017/12/resume_FINAL_2av6_compressed.pdf"
# response = requests.get(url, stream=True)
# with open('test.pdf','wb') as output:
#     output.write(response.read())

# with open("1MB", "wb") as handle:
#     for data in tqdm(response.iter_content()):
#         handle.write(data)


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
from file1 import *



page_token = None
while True:
    param = {}
    if page_token:
        param['pageToken'] = page_token
    children = drive_service.children().list(folderId=parent_id, **param).execute()

    for child in children.get('items', []):
        print 'File Id: %s' % child['id']
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
