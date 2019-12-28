from ftplib import FTP

class ConnectionFTP:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
    
    def session(self):
        return FTP(host=self.host)        


if __name__ == '__main__':
    conn = ConnectionFTP('177.53.143.13',
                         'integracao',
                         '@j19801980***')

    session = conn.session()

    session.quit()