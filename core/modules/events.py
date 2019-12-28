import os
from datetime import date

from watchdog.events import FileSystemEventHandler
from .ftp_connection import ConnectionFTP


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        self.session = ConnectionFTP('177.53.143.13',
                                     'integracao',
                                     '@j19801980***')

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        
        print(f'event type: {event.event_type}  path : {event.src_path}')

        filename, ext = os.path.splitext(event.src_path)

        today = date.today()
        str_date = today.strftime("%d-%m-%Y %H:%m:%s")

        ftp_file_name = f"{filename}-{str_date}.{ext}"

        self.session.upload_file(ftp_file_name, 
                                 '/www/integracao_erp', 
                                 open(event.src_path, 'rb'))
        self.session.close()
