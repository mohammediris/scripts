import threading

def create_threads(count,func_name):
    thread_list = []
    if count < 50:
        for t in range (count):
            thread = threading.Thread(target=)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()
    else:
        return "thread count exceeded"