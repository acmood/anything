
from bs4 import BeautifulSoup
import urllib
import re
import random
import urllib2

base = 257
mod = 1000000007
M = 1
my_header = [
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9128V Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo A765e Build/IMM76I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36"
    "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/6.0 MQQBrowser/4.1.2 Mobile/11D201 Safari/7534.48.3"
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0"
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V185 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)"
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; R8007 Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V100A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.2.2)"
    "K-Touch_T619/960211_8510_V0101 Mozilla/5.0 (Linux; U; Android 2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; MI-ONE Plus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36"
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; SAGA A728 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/042_0.4_diordna_008_084/drps_01_3.0.4_827A+AGAS/1000651c/2547DE9A4FCA9E00085BEE6497BE7E16%7C216259010978668/1"
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I9502 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.2.2)"
    "CoolPad8020+_CMCC_TD/1.08 Linux/2.6.35 Android/2.3.5 Release/03.29.2012 Mozilla/5.0 AppleWebKit/533.1 Version/4.0 Mobile Safari/533.1"
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; L822S Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_008_084/moheel_51_2.2.4_S228L/7300088a/DE893986150F2F67CCCCBF4E8B2C6D61%7C324746020104268/1"
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.1 Mobile Safari/537.36"
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET4.0C; .NET4.0E"
]
def get_content(url, headers):

    random_header = random.choice(headers)

    req = urllib2.Request(url)
    req.add_header("User-Agent", random_header)

    content = urllib2.urlopen(req).read()
    return content

def get_hash(url):
    a = 0
    for s in url:
        a = (a * base + ord(s)) % mod
    return a;

def func(tag):
    return tag.has_attr('href') and re.compile("zstu")

def get_link(content):
    
    soup = BeautifulSoup(content)

    all_a = soup.find_all('a', href = re.compile('19lou'))

    print len(all_a)
    links = []
    for a in all_a:
        link = a['href']
        print link
        links.append( link )

    return links

def get_info(num, url):
    print url
    urllib.urlretrieve(url, '%s.html' % num)
li = {}


url = "http://www.19lou.com/r/1/hzcsjjt.html"
q = []
q.append(url)
hashvalue = get_hash(url)
#print type(li)
li[hashvalue] = 1;
tot = 0
rear = 1;
while len(q) != 0 :
    url = q[0]
    del q[0]
    tot += 1

    content = get_content(url, my_header)
    get_info(tot, url)

    links = get_link(content)
    print len(links)
    for link in links:
        hashvalue = get_hash(link)
        print hashvalue
        if not li.has_key(hashvalue):
            if rear < M:
                q.append(link)
                li.update({hashvalue:1})
                rear += 1
print rear


"""
my_headers = [
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.2 (Baidu; P1 4.1.2)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.4)
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; 8720 Build/IML74K) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.5.20.0 (Baidu; P1 4.0.3)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5830i Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.2 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; DOEASY-E905 Build/IML74K) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.0.3)
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; OPPOR801 Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/5.3.5 (Baidu; P1 2.3.6)
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; 2345Explorer 3.5.0.12758)
    Bird T9508_TD/1.0 Linux/2.6.35 Android/2.3.5 Release/7.16.2012 
    "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D167 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.7_1C2%254enohPi/1005623a/D4EEB20265BF5D0AE7DEF718EE153BF559121987AONKKKBDELQ/1
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; SAMSUNG-GT-N7108_TD/1.0 Android/4.1.1 Release/08.30.2012 Browser/AppleWebKit534.30 Build/JRO03C) ApplelWebkit/534.30 (KHTML,like Gecko) Version/4.0 Mobile Safari/534.30
    UCWEB/2.0 (Linux; U; Adr 4.0.4; zh-CN; ZTE U807) U2/1.0.0 UCBrowser/9.6.3.413 U2/1.0.0 Mobile
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; RLT Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_458_084/9856TM_51_2.2.4_TLR/7300088a/91B9E725BB62981D1128E68D0C7AD07C%7C211610029568368/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; ZTE M901C Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.2.2)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729)
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; MI 3C Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.0.1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 UBrowser/1.0.739.0 Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; R819T Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.1)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo S7t Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.0 (Baidu; P1 4.0.4)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; vivo X3t Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo E3 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; Coolpad 7020 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo X510t Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo S880i Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (6.1.0)
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; CNCDialer; 360SE)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; Coolpad 7620L Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.0.435 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 2.3.9; zh-cn; HTC Desire HD Build/GRJ90) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo S720 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1
    "Lenovo-A390t_TD/S100 Release/11.2012 Mozilla/5.0 (Linux; U; Android 4.0.3) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; V976 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GN100 Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HUAWEI G750-T01 Build/HuaweiG750-T01) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2S Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R821T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SM-N9008 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.0.435 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo S7t Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R821T Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baidubrowser/4.5.20.0 (Baidu; P1 4.2.2)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2)
    "Mozilla/5.0 (Linux; Android 4.4.2; HTC D816t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; Lenovo A820t Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.3 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; X909 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI P7-L00 Build/HuaweiP7-L00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.1.447 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.0.1
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 718; qdesk 2.4.1265.203; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GN777 Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.5 Mobile Safari/533.1
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36 QQBrowser/7.7.24696.400
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; G10A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.2.2)
    "CoolPad8085_CMCC_TD/1.0 Linux/3.0.8 Android/4.0 Release/04.10.2013 Browser/AppleWebkit534.3
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; InfoPath.2)
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2SC Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.3 (Baidu; P1 4.1.1)
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HM 1SC Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; W66 Build/JZO54K) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; R815T Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R821T Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/4.9 (Baidu; P1 4.2.2)
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.1.5_enohpi_6311_046/1.1.7_2C2%255enohPi/1099a/766973F6649DBE5B60383BE6C8ED755345C0D8563ONLKOLSRAH/1
    "Mozilla/5.0 (Linux; U; Android 4.3.0; zh-cn; Hong m2 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.3.0)
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; MALN; 360SE)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36 QQBrowser/7.6.22690.400
    "UCWEB/2.0 (Linux; U; Adr 2.3.6; zh-CN; ZTE V889D) U2/1.0.0 UCBrowser/9.5.2.394 U2/1.0.0 Mobile
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HUAWEI Y600-U00 Build/HUAWEIY600-U00) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; MI 2S Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.5.442 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; QQBrowser/7.7.24562.400)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36 SE 2.X MetaSr 1.0
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; Lenovo A269i Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/5.0 (Baidu; P1 2.3.6)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; vivo Y11 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_008_084/KBB_61_2.1.4_11Y+oviv/7300002a/588E7B40C49CB7BB415165DD973183AF%7C664082410704568/1
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KB974487)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; OPSSON D1 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36
    "MASTONE G3_TD/1.0 Android/2.3 Release/4.20.2012 Browser/AppleWebKit533.1 Profile/MIDP-2.0
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo S7i(t) Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.5; .NET CLR 2.0.50727; {D9D54F49-E51C-445e-92F2-1EE3C2313240})
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2A Build/JRO03L) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.1.1)
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0; QQBrowser/7.7.24562.400) like Gecko
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; HUAWEI C8812 Build/HuaweiC8812) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.2 (Baidu; P1 4.0.3)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; HTC T528t Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 SogouMSE,SogouMobileBrowser/2.6.3
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; 2013022 Build/HM2013022) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; W9100B Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.1 (Baidu; P1 4.0.4)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; A18 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; 360SE)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y11i T Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.2.2)
    "Lenovo A376/S100 Release/11.2012 Mozilla/5.0 (Linux; U; Android 4.0.3) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2SC Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "MQQBrowser/4.5/Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Coolpad 7295C Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "MQQBrowser/3.6/Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; ZUOKU K3 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "HUaRUI_HR-TD2000_CMCC_TD/1.0 Android/2.3.7 (LinuxOS 2.6.35.7) Release/12.20.2011 Browser/WAP2.0
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; Lenovo A880 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.5.2.394 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo Y3t Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; Coolpad 7295A Build/JZO54K) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48 Safari/537.36 QQBrowser/7.7.24562.400
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; R809T Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.1)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.6.2.404 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; unknown Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.3 (Baidu; P1 4.4.4)
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
    "Mozilla/5.0 (iPhone; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A501 Safari/9537.53 HaoWangZhiDaQuan 3.9.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; NX403A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36 SE 2.X MetaSr 1.0
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; TD668 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.3 (Baidu; P1 4.1.1)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%254enohPi/1099a/038C116F6E7531AA81783CD8F25A4058C110727D8ONASNLALOD/1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; 2345Explorer)
    "Mozilla/5.0 (iPad; U; CPU OS 5_1 like Mac OS X) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10 UCBrowser/2.4.3.253
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; QQDownload 734; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.5)
    "OPPO_R821T/V1 Linux/3.4.5 Android/4.2.2 Release/03.26.2013 Browser/AppleWebKit534.30 Mobile Safari/534.30 MBBMS/2.2 System/Android 4.2.2;
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; SCH-P709 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.1.360
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; vivo S3+ Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y15T Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Bestsonny_T962_TD/T962_V1.00 Linux/2.6.35 Android/2.3.5 (Android 2.3.5) Release/12.28.2012 Browser/AppleWebKit533.1 Mobile baiduboxapp/4.2 (Baidu; P1 4.0.4)
    "K-Touch_T619+/960226_8514_V0101 Mozilla/5.0 (Linux; U; Android 2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; Media Center PC 6.0)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI G520-0000 Build/HuaweiG520-0000) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; 2013023 Build/HM2013023) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.5; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI C8813Q Build/HuaweiC8813Q) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.1.2)
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; vivo X3t Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.1)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%253enohPi/1099a/90E1151AA706810DACB3D5C84781A4D72FB1DDF4COCPQEJSRSH/1
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; OPPOR801 Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; H30-T00 Build/HuaweiH30-T00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; X909T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; GT-S7562 Build/IMM76I) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3.5 (Baidu; P1 4.0.4)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; GT-I8558 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.9.439 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HM NOTE 1TD Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; CIKAA Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "UCWEB/2.0 (Linux; U; Adr 4.2.2; zh-CN; vivo Y11i T) U2/1.0.0 UCBrowser/9.4.1.362 U2/1.0.0 Mobile
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo S7i(t) Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D169 baiduboxapp/0_0.0.1.5_enohpi_069_046/1.7_1C2%253enohPi/1099a/60A52EC62AE7DD5F2801004E2511FECB3E85DC0EEFGJGGLLHQJ/1
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; GT-S7562 Build/IMM76I) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.0.4)
    "vivo_Y11iW/1.0 Linux/3.4.5 Android/4.2.2 Release/02.09.2014 Browser/AppleWebKit534.30 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mobile Safari/534.30 Android 4.2.2
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0) LBBROWSER
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; {D9D54F49-E51C-445e-92F2-1EE3C2313240})
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Coolpad 8297 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/4.9 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; Lenovo A360 Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-CN; GT-N7100 Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.6.428 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D169 Safari/9537.53
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; X817 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/023_0.4_diordna_0821_027/EENOiG_71_1.2.4_718X/1001177c/7459F6C9DCA74A447E09F176C1D5D96B%7C0/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y15T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_458_084/KBB_71_2.2.4_T51Y+oviv/7300002a/AC00AF3DF250810AF4A1DABD075BB2B6%7C054631420338268/1
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; zh-cn) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8B117
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; R815T Build/JOP40D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.1)
    "CoolPad8295M_CMCC_TD/1.0 Linux/3.4.5 Android/4.1.2 Release/03.31.2013 Browser/AppleWebKit534.30 Mobile Safari/534.30 MBBMS/2.2 System/Android 4.1.2;
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y20T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; TY-K-Touch W655/K-Touch_W655_V1.2; 320*480;  CTC/2.0) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R831T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-CN; MT25i Build/4.1.B.0.631) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.5.418 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; AOLE G3 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R833T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; MI 2S Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.0.435 U3/0.8.0 Mobile Safari/533.1
    "JUC (Linux; U; 4.0.3; zh-cn; Lenovo A658t; 480*854) UCWEB8.7.2.214/145/33876
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%254enohPi/1099a/C09354491F6E31324262AD7BA23519AC30647C0D9OREQHMJEGT/1
    "Mozilla/5.0 (Linux; Android 4.4.2; zh-cn; SAMSUNG SM-N900 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; HUAWEI G520-5000 Build/HuaweiG520-5000) AppleWebKit/534.30 (KHTML, like Gecko) FlyFlow/2.4 Version/4.0 Mobile Safari/534.30 baidubrowser/042_11.61.4.2_diordna_458_084/IEWAUH_61_2.1.4_0005-025G-IEWAUH/1000445d/072E062FC982834300BF9E3ADC7FBEE3%7C561900200232868/1
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2A Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5830i Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; MOFUT T3MT Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.2.1.400
    "Coolpad7269_CUCC_WCDMA/1.0 Linux/3.4.5 Android/4.2 Release/6.28.2013 Browser/AppleWebkit533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; NX999-1 Build/Android4.2.1) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/042_8.3_diordna_008_084/1-999XN_01_1.2.4_1-999XN/1000680a/8388C13873809E41B928D2007CF3A739%7C6414310
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI 2SC Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.0.1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%253enohPi/1099a/634B19883057049E54200968E929423839F8F1AF4ONJTMERPFS/1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E; Media Center PC 6.0)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; Coolpad7295 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HUAWEI Y511-T00 Build/HUAWEIY511-T00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.1 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; MI 3C Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; R827T Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_069_045/OPPO_71_2.2.4_T728R/1000687c/A6082D018E331C106611E381F94FCBF2%7C966836720422368/1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_6311_046/1.1.7_2C2%256enohPi/1099a/E9C316D560F9ED936675A1D582D0A68EEB1F2DD30FNKISMJDKP/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Bird i7 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; Lenovo A708t Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.9.439 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; QQDownload 718; {D9D54F49-E51C-445e-92F2-1EE3C2313240})
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-CN; HUAWEI C8813DQ Build/HuaweiC8813DQ) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.6.2.404 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 baiduboxapp/0_0.0.3.5_enohpi_069_046/6.0.7_1C2%254enohPi/1099a/7BDB0B15D80C1D13D3C39298773276911728C6A09FCEDFQGPCM/1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D167 baiduboxapp/0_0.0.1.5_enohpi_069_046/1.7_1C2%254enohPi/1005623a/BE6B49DBA00820401F07F3C0CF66FAC181A2410CFOGKHHLFRJN/1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%253enohPi/1099a/C7B84D8219A7BC65B75C2FE472C65B1D7F8AA6018OGLLILTRFD/1
    "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; DOOV_D2 Build/DOOV) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; vivo Y11 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_008_084/KBB_61_2.1.4_11Y+oviv/7300002a/0196708200CD57C0C5C17BFC059F3B0D%7C910007855478842/1
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; SM-G7108 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.3)
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Shuame; .NET CLR 2.0.50727)
    "JUC (Linux; U; 4.1.2; zh-cn; Lenovo A820t; 540*960) UCWEB8.7.2.214/145/33706
    "MQQBrowser/4.3/Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Philips T3566 Build/Philips_T3566) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; SAMSUNG-GT-I8268_TD/1.0 Android/4.1.2 Release/11.15.2012 Browser/AppleWebKit534.30 Build/JRO03L) ApplelWebkit/534.30 (KHTML,like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; Android 4.4.2; zh-cn; SAMSUNG-SCH-I959 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; vivo V1 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; vivo X1St Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Lenovo A850 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_069_045/OVONEL_71_2.2.4_058A+ovoneL/1001565b/09A0A50CF1DD584B1EA097DE4E1DD425%7C196707020951368/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; Coolpad 7295C Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) FlyFlow/2.4 Version/4.0 Mobile Safari/534.30 baidubrowser/042_11.61.4.2_diordna_069_045/daplooC_71_2.2.4_C5927-daplooC/1000943c/1266D8B4783BCAF6C7641F3284C034CF%7C510284320370268/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; HUAWEI G730-T00 Build/HuaweiG730-T00) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/4.9 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-CN; DOOV S2y Build/DOOVS2y) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.6.428 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201 baiduboxapp/0_0.0.3.5_enohpi_069_046/1.1.7_1C2%253enohPi/1099a/BF001CBA35565EBBEFCCA8807F87CE7B6456C44E2FGJHQCBPFT/1
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-CN; MI 2SC Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.9.439 U3/0.8.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; VIKA-T1 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo A630t Build/IMM76D) UC AppleWebKit/534.31 (KHTML, like Gecko) Mobile Safari/534.31
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; SIM-Note Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; Coolpad8750 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.1 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-CN; SM-N9008V Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.7.8.425 U3/0.8.0 Mobile Safari/533.1

    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; SM-G3508I Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; HUAWEI G610-U00 Build/HuaweiG610-U00) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/5.0 (Baidu; P1 4.2.1)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; JY-G2 Build/IMM76D) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.0.4)
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; MI 1S Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-CN; X907 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.8.0.435 U3/0.8.0 Mobile Safari/533.1
    "SAMSUNG-GT-S6818_TD/1.0 Android/4.1.2 Release/02.03.2013 Browser/ApplelWebkit/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; HUAWEI G700-U00 Build/HuaweiG700-U00) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.1 (Baidu; P1 4.2.1)
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; ETON T760 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; {D9D54F49-E51C-445e-92F2-1EE3C2313240})
    "Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9128V Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo A765e Build/IMM76I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36
    "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/6.0 MQQBrowser/4.1.2 Mobile/11D201 Safari/7534.48.3
    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V185 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)
    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; R8007 Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V100A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.2.2)
    "K-Touch_T619/960211_8510_V0101 Mozilla/5.0 (Linux; U; Android 2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; MI-ONE Plus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36
    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; SAGA A728 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/042_0.4_diordna_008_084/drps_01_3.0.4_827A+AGAS/1000651c/2547DE9A4FCA9E00085BEE6497BE7E16%7C216259010978668/1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I9502 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.2.2)
    "CoolPad8020+_CMCC_TD/1.08 Linux/2.6.35 Android/2.3.5 Release/03.29.2012 Mozilla/5.0 AppleWebKit/533.1 Version/4.0 Mobile Safari/533.1
    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; L822S Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_008_084/moheel_51_2.2.4_S228L/7300088a/DE893986150F2F67CCCCBF4E8B2C6D61%7C324746020104268/1
    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.1 Mobile Safari/537.36
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET4.0C; .NET4.0E
]
"""