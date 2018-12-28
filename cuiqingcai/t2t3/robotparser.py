from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/p/dfd09bb91659'))
print(rp.can_fetch('*',"https://www.jianshu.com?search?q=python&page=1&type=collections"))
