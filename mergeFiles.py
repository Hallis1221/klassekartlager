def merge():
    open("elever.txt", "w").close()
    with open('elever.txt', 'w') as file:
        jenter = open("jenter.txt", "r")
        gutter = open("gutter.txt", "r")
        file.writelines(jenter)
        file.writelines(gutter)