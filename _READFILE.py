def FileToList(path):
    content = []
    file = open(path)
    for line in file:
        content.append(line.strip())
    # print(content)
    file.close()
    return content

