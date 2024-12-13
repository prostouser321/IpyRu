#Обозначение:
#error1 - Нереверный запрос. (Команда не изпользуется потому что, Python автоматичиский говрит что неверный ввод. Можно использовать в пользовательских версиях.)
#
#
#
#
#
#_________________________________________________________
#
#Функции и т.д.
def logo():
    print("###               ###   #  #")
    print("#                #  #  #  #")
    print(" #    ###   #  #  #  #  #  #")  
    print(" #    #  #  #  #  ###   #  #")
    print(" #    #  #   # #  # #   #  #")
    print("###   ###     #   #  #   ##")   
    print("      #      #")
def error1():
    print("error#1")
def AppOpen():
    openApp =input("Name package App ")
    if openApp == "example.app.test":
        print("Hello world!")
        AppOpen()
    elif openApp == "IpyRu.system.aboutsystem":
        print("system name = IpyRU (NT_20_24_13+12._)")
        print("system version = V1.2.1")
        print("version createon date = 13.12.2024")
        AppOpen()
    elif openApp == "IpyRu.system.openApp":
        AppOpen()
    elif openApp == "IpyRu.system.restart":
        logo()
        AppOpen()
    elif openApp == "IpyRu.system.help":
        print("Apps: 'example.app.test' 'IpyRu.system.aboutsystem' 'IpyRu.system.openApp' 'IpyRu.system.restart' 'IpyRu.system.help' ")
        AppOpen()
#Код приложения и т.д.
logo()
AppOpen()
