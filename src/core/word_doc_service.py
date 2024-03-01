import os

class WordDocService:
    def open_word_document(doc_path):
        print("doc_path = ", doc_path)
        # Check if the document path exists
        if not os.path.exists(doc_path):
            print(f"Error: The document '{doc_path}' does not exist.")
            return

        """ Use os.startfile() to open the document with the default application (Microsoft Word) """
        try:
            os.startfile(doc_path, 'open')
        except OSError as e:
            print(f"Error: Failed to open the document. {e}")
