from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from src.core.translate_service import TranslateService
from src.core.word_doc_service import WordDocService
import os

class TranslateGUI:
    def __init__(self, root):
        
        self.logo_icon_path = os.path.join(os.path.dirname(__file__), 'resources', 'favicon.ico')
        self.word_icon_path = os.path.join(os.path.dirname(__file__), 'resources', 'word.ico')
        
        self.root = root
        self.root.title("Word文档 繁/简体转换器")
        self.root.iconbitmap(self.logo_icon_path)
        self.root.resizable(False, False)

        self.word_icon = ImageTk.PhotoImage(Image.open(self.word_icon_path))
        
        self.file_path = StringVar(name='original_file_path')
        self.notification_message = StringVar(name='notification_message')

        # Widgets
        self.uploadLabel = Label(root, text="请上传需要转换的Word文件档")
        self.uploadButton = Button(root, text="上传", command=self.selectDoc)
        self.s2tButton = Button(root, text="简体 -> 繁体", command=self.s2t)
        self.t2sButton = Button(root, text="繁体 -> 简体", command=self.t2s)

        self.wordButton = Button(root, image=self.word_icon, command=self.openDoc)
        self.wordLabel = Label(root, textvariable=self.file_path)

        self.notificationLabel = Label(root, textvariable=self.notification_message)

        # Layout
        self.uploadLabel.grid(row=0, column=0)
        self.uploadButton.grid(row=0, column=1, sticky=W)
        self.notificationLabel.grid(row=1, column=0)
        self.s2tButton.grid(row=3, column=0)
        self.t2sButton.grid(row=3, column=1)

        self.service = TranslateService()

    def selectDoc(self):
        print(self.file_path.get())
        file_path = filedialog.askopenfilename(initialdir = "./",title = "选择文件",filetypes = (("Word Docs","*.docx"),("All files","*.*")))
        if file_path:
            self.file_path.set(file_path)
            self.wordButton.grid(row=0, column=2)
            self.wordLabel.grid(row=1, column=1, columnspan=2)
            self.notification_message.set("File Selected")
        
        print(self.file_path.get())

    def openDoc(self):
        WordDocService.open_word_document(self.file_path.get())

    def s2t(self):
        print("in s2t()")
        self.notification_message.set("转换中...")
        self.root.update_idletasks()
        try:
            self.service.translate_docx(self.file_path.get(), 's2t')
            self.notification_message.set("转换完成")
        except:
            self.notification_message.set("转换失败, 请确保当前路径无同名文档")

    def t2s(self):
        print("in t2s()")
        self.notification_message.set("转换中...")
        self.root.update_idletasks()
        try:
            self.service.translate_docx(self.file_path.get(), 't2s')
            self.notification_message.set("转换完成")
        except:
            self.notification_message.set("转换失败, 请确保当前路径无同名文档")