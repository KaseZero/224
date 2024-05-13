import time
from common.common import Commonshare
class Login(Commonshare):
    def login(self,user,pwd):
        self.open("http:192.168.55.40")
        time.sleep(1)
        self.click('id','zentao')
        time.sleep(1)
        self.input('id','account',user)
        time.sleep(1)
        self.input('xpath',".//*[@id='loginPanel']/div/div[2]/form/table/tbody/tr[2]/td/input",pwd)
        time.sleep(1)
        self.click('id','submit')
        time.sleep(1)
        return self.dr.title
if __name__=='__main__':
        l=Login('Firefox')
        l.login('admin','Qwe123')
