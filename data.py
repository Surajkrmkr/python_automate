import platform

weekNo = "6"

isMac = platform.system() == 'Darwin'
isWindows = platform.system() == 'Windows'

def get_Brave_Path():
    if isMac:
        return "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    elif isWindows:
        return "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    else:
        return ""

def get_path():
    if isMac:
        return "/Users/surajkrmkr/Storage/Xiaomi Contract/THEMES/Week"
    elif isWindows:
        return "E:\\Xiaomi Contract\\THEMES\\Week"
    else:
        return ""
    
def get_Tag_Path():
    if isMac:
        return path+"/1tags/"
    elif isWindows:
        return path+"\\1tags\\"
    else:
        return ""

def get_Copyright_Path():
    if isMac:
        return path+"/1copyright/"
    elif isWindows:
        return path+"\\1copyright\\"
    else:
        return ""

def get_Path_Separator():
    if isMac:
        return "/"
    elif isWindows:
        return "\\"
    else:
        return ""
    
rootPath = get_path()
path = rootPath+weekNo
