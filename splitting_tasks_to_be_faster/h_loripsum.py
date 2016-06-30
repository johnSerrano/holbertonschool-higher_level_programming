import requests
from threading import Thread

class LoripsumThread(Thread):
    """docstring for LorIpsumThread"""
    def __init__(self, i):
        self.filename = i
        Thread.__init__(self)

    def run(self):
        import sys
        reload(sys)
        sys.setdefaultencoding("latin-1")
        r = requests.get('http://loripsum.net/api/1/short')
        if r.status_code != 200:
            raise Exception("Failed to retrieve data")
        with open(self.filename, 'ab') as f:
            f.write(unicode(bytes(r.text)))

if __name__ == '__main__':
    import sys
    from h_loripsum import LoripsumThread

    nb_paragraph = int(sys.argv[1])
    filename = sys.argv[2]

    threads = []
    for i in range(0, nb_paragraph):
        t = LoripsumThread(filename)
        t.start()
        threads += [t]

    for t in threads:
        t.join
