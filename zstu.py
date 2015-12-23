
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
#    req.add_header("Host", "www.19lou.com")
#    req.add_header("Referer", url)
#    req.add_header("GET", url)


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



url = "http://tieba.baidu.com/f?kw=%D5%E3%BD%AD%C0%ED%B9%A4%B4%F3%D1%A7&fr=index"
li = {}
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
