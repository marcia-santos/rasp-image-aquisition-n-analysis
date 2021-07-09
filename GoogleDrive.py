from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#Archive ID - There is a way to automate this, if I want.
fileID = '1SJNq6xM1-E6UweIp8ShGve_YtLQDBBkl'

def Upload(file_type, file_name):

    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({"mimeType": file_type, "parents": [{"kind": "drive#fileLink", "id": fileID}]})
    file1.SetContentFile(file_name)
    file1.Upload() # Upload the file.
    print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   

