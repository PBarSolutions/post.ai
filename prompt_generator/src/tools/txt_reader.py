

def txt_read(filepath):

    file = open(filepath, 'r')

    content = file.read()
    file.close()

    return content


