import os

def find_Keyword(keyword, path=os.path.abspath('.')):
    for each in os.listdir(path):
        p = os.path.join(path, each)
        if os.path.isdir(p):
            find_Keyword(keyword, path=p) #递归调用
        elif os.path.isfile(p) and keyword in p:
            print(p)
    return 1

if __name__ == '__main__':
    find_Keyword('.py')
        
