


def main():
    #ask the user for a file name with a extension.
    filename = input("File name: ")
    # check the file extension of the file
    index = filename.find(".")
    filetype = filename[index + 1:]
    # print image/{file_type}
    if "." in filename:
        print(f"image/{filetype}")
    else:
        print("application/octet-stream")
main()
