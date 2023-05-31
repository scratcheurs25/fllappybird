pipex = 0

pipey = 200

def pipe():
    global pipex
    pipex -= 1
    if pipex + 64 <= 1:
        pipex = 664