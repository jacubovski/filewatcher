
from core.settings import BASE_DIR
from core.modules.ftp_connection import ConnectionFTP
from core.modules.file_watcher import FileWatcher
import os


src_path = os.path.join(BASE_DIR, 'files/') 



watcher = FileWatcher(src_path)
watcher.run()