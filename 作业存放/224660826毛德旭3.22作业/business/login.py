import time
from common.common import Commonshare
class Login(Commonshare):
    def login(self,user,pwd,i):
        c=Commonshare('Firefox')
        c.open("http:192.168.55.62")
        time.sleep(1)
        c.click('id','zentao')
        time.sleep(1)
        c.input('id','account',user)
        time.sleep(1)
        c.input('xpath',".//*[@id='loginPanel']/div/div[2]/form/table/tbody/tr[2]/td/input",pwd)
        time.sleep(1)
        c.click('id','submit')
        time.sleep(1)
        if i=='0':
            return c.dr.title
        else:
            t=c.alert().text
            c.alert().accept()
            return t

if __name__=='__main__':
        l=Login('Firefox')
        l.login('','','1')
        l.login('admin','Abc123456','0')