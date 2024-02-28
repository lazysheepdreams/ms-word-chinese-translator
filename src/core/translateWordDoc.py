import os
import shutil
import xml.etree.ElementTree as ET
import json
import sys

# Steps
# 1. rename file to zip
# 2. extract zip to a folder
# 3. translate each file
#    - for each file in folder
#    - translate file
# 4. zip folder
# 5. rename zip file to docx

import zipfile
# import openpyxl
# import docx

class TranslateService:

    file_name = None
    zip_file_path = None
    t2s = None
    s2t = None

    # translate docx from simplified to traditional
    def translate_docx(self, file_path, action):
        self.rename_docx_to_zip(file_path)
        self.unzip_file()
        self.load_json_file()
        self.translate_files(self.zip_file_path.replace('\\','/').replace('.zip', ''), action)
        outputFileName = self.file_name.replace('.docx', '')
        if action == 's2t':
            outputFileName = outputFileName+'_TW'
        else:
            outputFileName = outputFileName+'_CN'
        self.zip_docx(self.zip_file_path.replace('.zip', ''), outputFileName)
        self.clean_up()
        print(action)

    # rename docx to zip
    def rename_docx_to_zip(self, file_path):
        # extract file name from file path
        self.file_name = os.path.basename(file_path)
        doc_file_path = os.getcwd() +'/' + self.file_name
        self.zip_file_path = doc_file_path.replace('.docx', '.zip')
        shutil.copy(file_path, doc_file_path)
        os.rename(doc_file_path, self.zip_file_path)
        return self.zip_file_path

    # unzip zip file
    def unzip_file(self):
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip:
            zip.extractall(os.path.dirname(self.zip_file_path)+'/'+self.file_name.replace('.docx', ''))
        return self.zip_file_path.replace('.zip', '')

    # load json files
    def load_json_file(self):
        self.t2s = self.load_json_file_as_map(os.path.join(self.get_app_directory(), '../dictionaries', 't2s-char.min.json'))
        self.s2t = self.load_json_file_as_map(os.path.join(self.get_app_directory(), '../dictionaries', 's2t-char.min.json'))
        return


    def get_app_directory(self):
        """Return the application's base directory."""
        # if getattr(sys, 'frozen', False):  # check if the application is bundled as an executable
        #     return os.path.dirname(sys.executable)
        # else:
        return os.path.dirname(os.path.abspath(__file__))

    def load_json_file_as_map(self,file_path):
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data

    def translate(self, action, content):
        if content == None: return
        text: str = content
        before = text
        """ loop through text and replace contents using mapped dictionary """
        if action == 't2s':
            for char in text:
                if (char in self.t2s):
                    # print(self.t2s.get(char))
                    text = text.replace(char, self.t2s.get(char))
        elif action == 's2t':
            for char in content:
                if (char in self.s2t):
                    # print(self.s2t.get(char))
                    text = text.replace(char, self.s2t.get(char))
        # if before != text:
        #     print("before: ", before, " | after: ", text)
        return text

    # translate xml file
    def translate_xml_file(self, file_path, action):
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        for element in root.iter():
            # Do something with the element
            text = self.translate(action, element.text)
            element.text = text

        tree.write(file_path, encoding="utf-8")

    # loop through each files under source directory and open file
    def translate_files(self, folderPath, action):
        print("in translate_files() folderPath = " + folderPath)
        for root, dirs, files in os.walk(folderPath):
            for filename in files:
                source_file = os.path.join(root, filename)
                if filename.endswith('.xml'):
                    self.translate_xml_file(source_file, action)


    # zip eveything inside sourcePath and rename it to .docx file
    def zip_docx(self, sourcePath, fileName='Python'):
        """ If translation is not working correctly, try changing the compression type from ZIP_DEFLATED to ZIP_STORED """
        with zipfile.ZipFile(fileName+'.docx', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(sourcePath):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, sourcePath)
                    zipf.write(file_path, arcname=arcname)

    # clean up unwanted files
    def clean_up(self):
        try:
            os.remove(self.zip_file_path)
            """ Use shutil.rmtree to remove the folder and its contents recursively """
            shutil.rmtree(self.zip_file_path.replace('.zip', ''))
            print(f"Successfully removed the folder: {self.zip_file_path.replace('.zip', '')}")
        except OSError as e:
            print(f"Error: {e}")
