import re
import mechanize

def give_feild_list(text):
    pattern = re.compile(r'<Text\w+\((\w.*?)\=.\>')
    return re.findall(pattern,text)
    pass

def myinit(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_refresh(False)
    browser.addheaders= [('user-agent','Firefox')]
    browser.open(url)
    #browser.select_form(nr = 0)
    tags = ''
    for f in browser.forms():
        tags+=str(f)
    feilds = give_feild_list(tags)
    return feilds
#print myinit('https://goo.gl/forms/dYEjzvPb30kAsvaG3')
