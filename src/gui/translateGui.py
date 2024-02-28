from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from core.translateWordDoc import TranslateService
import os

class TranslateGUI:
    def __init__(self, root):
        
        self.logo_icon_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
        self.word_icon_path = os.path.join(os.path.dirname(__file__), 'word.ico')
        
        self.root = root
        self.root.title("Word文档 繁/简体转换器")
        self.root.iconbitmap(self.logo_icon_path)
        self.root.resizable(False, False)

        self.word_icon = ImageTk.PhotoImage(Image.open(self.word_icon_path))
        
        self.file_path = StringVar(name='original_file_path')
        self.file_path.set('No File Selected')

        # Widgets
        self.uploadLable = Label(root, text="请上传需要转换的Word文件档")
        self.uploadButton = Button(root, text="上传", command=self.selectDoc)
        self.s2tButton = Button(root, text="简体 -> 繁体", command=self.s2t)
        self.t2sButton = Button(root, text="繁体 -> 简体", command=self.t2s)

        self.wordButton = Button(root, image=self.word_icon)
        self.wordLable = Label(root, textvariable=self.file_path)

        # Layout
        self.uploadLable.grid(row=0, column=0)
        self.uploadButton.grid(row=0, column=1)
        self.s2tButton.grid(row=2, column=0)
        self.t2sButton.grid(row=2, column=1)

        self.service = TranslateService()

    def selectDoc(self):
        print(self.file_path.get())
        file_path = filedialog.askopenfilename(initialdir = "./",title = "选择文件",filetypes = (("Word Docs","*.docx"),("All files","*.*")))
        if file_path:
            self.file_path.set(file_path)
            self.wordButton.grid(row=0, column=2)
            self.wordLable.grid(row=1, column=2)
        
        print(self.file_path.get())

    def s2t(self):
        print("in s2t()")
        # set in-progress message
        self.service.translate_docx(self.file_path.get(), 's2t')
        # set complete message

    def t2s(self):
        print("in t2s()")
        # set in-progress message
        self.service.translate_docx(self.file_path.get(), 't2s')
        # set complete message