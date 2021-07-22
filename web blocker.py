def block(files,web_list):
    redirect= input("please input ip address like this : -127.0.0.1 : ")
    with open(files,"r+") as file:
        content = file.read()
        for site in web_list:
            if site not in content:
                file.write(redirect+" "+site+"\n")

    print("web sites blocked")

def unblock(files, web_list):
    
    with open(files,"r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in web_list):
                file.write(line)
        file.truncate()

    print("site unblocked")


def inputs(work):
    files = r"C:\Windows\System32\drivers\etc\hosts"
    condition = "true"
    web_list = []
    while condition=="true":
        web_list.append(input(" Type web link : "))
        if work == "block":
            block(files,web_list)
        else:
            unblock(files,web_list)
        condition = input("if you want to "+work+" another web page the type-True :" ).lower()
                          

    print("your web pages are now "+work+", please refresh the page to see")



inputs(input("Type block/unblock what you wants : ").lower())


    
                
    
