# CSV Loader
Bash Script to help automate and sort CSV entries into Google Drive.

# Prerequisites

Python >2.7 must be installed on the system to function. You must also have permission to run bash scripts

# Installation

### Clone or download the git repo
```
$ git clone https://github.com/EdwaRen/csvLoader
$ cd csvLoader
```

### Install python packages
```
$ pip install numpy tqdm requests
```

### Authorize bash for start.sh
```
$ chmod u+x start.sh
```

### Run
```
$ ./start.sh
```
# Uploading

In main.py, parent_id is the file_id of the Google Drive Repository where all the files will be uploaded to. Parent_id has been hidden in this repo for privacy reasons but otherwise it should be a line of the form

```
parent_id = "ISUKJDJASN452DASYUDGHAND-DFS4"
```
