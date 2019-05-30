import docx2txt
import os


class FileRead:

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    def file_reader(self):
        file_full_path = f"{self.path.strip()}/{self.file_name.strip()}"
        return file_full_path

    def file_process(self):
        get_file = self.file_reader()
        get_extension = get_file.split(".")
        if get_extension[1] == 'docx':
            print(self.doc_process(get_file))
        else:
            print("Please make it .docx")
        # elif get_extension[1] == 'doc':
        #     new_name = get_file + 'x'
        #     if not os.path.exists(new_name):
        #         # Change The File Format doc to docx
        #         os.system('antiword' + get_file + '>' + new_name)
        #         self.doc_process(new_name)
        #     else:
        #         print("We Can Not Read It Because Same File Exists")

    def doc_process(self, file):
        # print(file)
        my_text = docx2txt.process(file).rsplit()
        text = []
        for text_data in my_text:
            if text_data not in text:
                text.append(text_data)
        return set(text)
