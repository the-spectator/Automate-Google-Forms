from Queue import Queue

def give_data(no_fields):
    queue = Queue()
    with open('inp.txt','r') as f:
        for line in f:
            x =line.strip().split(',')
            try:
                assert(len(x)==no_fields)
                queue.put(x)
            except:
                pass
    return queue
