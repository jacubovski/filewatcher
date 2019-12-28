from ftplib import FTP
from core.modules.utils import make_filename_ftp


class ConnectionFTP:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.session = self.open_session()
    
    def open_session(self):
        return FTP(host=self.host, 
                   user=self.username, 
                   passwd=self.password)

    def upload_file(self, file_name, path, file):
        self.session.cwd(path)
        self.session.storbinary(f"STOR {file_name}", file)

    def close(self):
        self.session.quit()
