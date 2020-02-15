import files_list
import files_delete
from datetime import datetime
import time
if __name__ == "__main__":
    while True:
        files = files_list.get_files_list()
        if files == -1:
            print("failed files get")
        else:
            now_time = datetime.now()
            for file in files:
                file_upload_time = datetime.fromtimestamp(file["timestamp"])
                if 30 <= (now_time - file_upload_time).days:
                    print((now_time - file_upload_time).days)
                    files_delete.delete(file["file_id"])
        files = []
        time.sleep(86400)
