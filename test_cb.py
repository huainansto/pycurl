import curl

def test(size, buf):
    print size, buf

c = curl.init()
c.setopt(curl.URL, 'http://www.python.org')
c.setopt(curl.WRITEFUNCTION, test)
c.setopt(curl.NOPROGRESS, 1)
c.setopt(curl.FOLLOWLOCATION, 1)
c.setopt(curl.MAXREDIRS, 5)
c.perform()
c.cleanup()
