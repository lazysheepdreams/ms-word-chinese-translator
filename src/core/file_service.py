import os
import shutil

class FileService:

    @staticmethod
    def get_app_directory() -> str:
        return os.path.dirname(os.path.realpath(__file__))
    
    @staticmethod
    def create_temp_dir() -> str:
        return os.path.join(FileService.get_app_directory(), 'temp')
    
    @staticmethod
    def remove_file_extension(file_name: str) -> str:
        return os.path.splitext(file_name)[0]
    
    @staticmethod
    def remove_folder_dir(folder_dir: str):
        try:
            os.remove(folder_dir)
            """ Use shutil.rmtree to remove the folder and its contents recursively """
            shutil.rmtree(folder_dir)
            print(f"Successfully removed the folder: {folder_dir}")
        except OSError as e:
            print(f"Error: {e}")