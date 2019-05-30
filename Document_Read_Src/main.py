from FileRead.file_read import FileRead

if __name__ == "__main__":
    folder_path = input("Enter Folder Path")
    file_name = input("Enter File Name With Extension")
    file = FileRead(folder_path, file_name)
    file.file_process()
