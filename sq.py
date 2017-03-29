import feilds
import threading
import general
import mechanize
import time
from Queue import Queue

url = 'https://goo.gl/forms/ufUMaxVYKVil8aBv2'
screen_lock = threading.Semaphore(value =1)
br = []
def fillform(queue,field):
    while True:
        flag = True
        x = queue.get()
        #time.sleep(0.1)
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.set_handle_refresh(False)
        browser.addheaders = [('user-agent', 'Firefox')]
        browser.open(url)
        browser.select_form(nr = 0)
        for i in range(len(field)):
            browser.form[field[i]] = x[i]
        browser.submit()
        queue.task_done()
        if queue.empty():
            return

no_thread = 18
threads = []
field = feilds.myinit(url)
q = general.give_data(len(field))
tit = time.time()

print '***Still main****'

for i in range(no_thread):
    t=threading.Thread(name=str(i+1),target=fillform,args=(q,field,))
    t.setDaemon(True)
    threads.append(t)
    t.start()

#fillform(q,field)
q.join()

for i in threads:
    i.join()

print 'time taken is ',time.time() - tit
print '***Done***'
