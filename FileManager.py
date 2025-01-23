import sys
import os
import pathlib
import shutil
import itertools
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

user_directory = pathlib.Path.home()

# Example directory of the user
directory_to_clean = "Downloads"

make_others_files = False 

# Dictionary that controls what files to be made and how
user_defined = {
    # Example of the format
    ".docx": (
        "Documents",
        {
            "University": ("nus", "national university of singapore", "national_university_of_singapore", "nusc", "college"),
            "High School": ("mis", "manado independent school", "manado_independent_school", "sma"),
        },
        False
    ),
}

class FileManagementProcess(FileSystemEventHandler):
    @staticmethod
    def MoveFileTo(path, destination):
        if not os.path.exists(os.path.join(destination, os.path.basename(path))):
            FileManagementProcess.create_directories(destination)
            shutil.move(path, destination)
            logging.info(f"Moved {path} to {destination}")
        else:
            for num in itertools.count(2):
                if not os.path.exists(os.path.join(destination, f"{os.path.basename(path)}_{num}")):
                    FileManagementProcess.create_directories(destination)
                    shutil.move(path, os.path.join(destination, f"{os.path.basename(path)}_{num}"))
                    logging.info(f"Moved {path} to {os.path.join(destination, f'{os.path.basename(path)}_{num}')}")
                    break

    @staticmethod
    def create_directories(target_path):
        for file_type in user_defined:
            if user_defined[file_type][1] is None:
                os.mkdir(os.path.join(final_directory, user_defined[file_type][0]))
            else:
                for subdirectory in user_defined[file_type][1]:
                    os.makedirs(os.path.join(final_directory, user_defined[file_type][0], subdirectory), exist_ok=True)

    @staticmethod
    def assign_folder(file_path):
        for file_type in user_defined:
            if file_path.endswith(file_type):
                meta_information = user_defined[file_type]
                if meta_information[1] is None:
                    FileManagementProcess.MoveFileTo(file_path, os.path.join(final_directory, meta_information[0]))
                    return
                else:
                    for subdirectory in meta_information[1]:
                        if any([keyword in file_path.lower() for keyword in meta_information[1][subdirectory]]):
                            FileManagementProcess.MoveFileTo(file_path, os.path.join(final_directory, meta_information[0], subdirectory))
                            return
                    if meta_information[2]:
                        FileManagementProcess.MoveFileTo(file_path, os.path.join(final_directory, meta_information[0], "Others"))
                        return
        if make_others_files:
            FileManagementProcess.MoveFileTo(file_path, os.path.join(final_directory, "Others"))
            return


    def on_modified(self, event):
        print(event.src_path)
        if not any([event.src_path.endswith(file_type) for file_type in user_defined]):
            return
        with os.scandir(final_directory) as entries:
            for entry in entries:
                if entry.is_file() and not entry.name.startswith("."):
                    self.assign_folder(entry.path)
        print(event)
                    

if __name__ == "__main__":
    final_directory = os.path.join(user_directory, directory_to_clean)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = final_directory
    event_handler = FileManagementProcess()
    observer = Observer()
    observer.schedule(event_handler, final_directory, recursive=True)
    observer.start()
    print("Started!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Done!")
