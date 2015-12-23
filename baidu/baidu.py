
from bs4 import BeautifulSoup
import urllib
import re
import random
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


base = 257
mod = 1000000007
M = 1
my_header = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
#    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9128V Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
#    "Mozilla/5.0 (Linux; U; Android 4.0.4; zh-cn; Lenovo A765e Build/IMM76I) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 Mobile Safari/537.36"
#    "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/6.0 MQQBrowser/4.1.2 Mobile/11D201 Safari/7534.48.3"
#    "Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0"
#    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V185 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.0 (Baidu; P1 4.2.2)"
#    "Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; R8007 Build/JLS36C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
#    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; V100A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/4.2 (Baidu; P1 4.2.2)"
#    "K-Touch_T619/960211_8510_V0101 Mozilla/5.0 (Linux; U; Android 2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
#    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; MI-ONE Plus Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.2 Mobile Safari/537.36"
#    "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; SAGA A728 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 baiduboxapp/042_0.4_diordna_008_084/drps_01_3.0.4_827A+AGAS/1000651c/2547DE9A4FCA9E00085BEE6497BE7E16%7C216259010978668/1"
#    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; GT-I9502 Build/JDQ39) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/5.3 (Baidu; P1 4.2.2)"
#    "CoolPad8020+_CMCC_TD/1.08 Linux/2.6.35 Android/2.3.5 Release/03.29.2012 Mozilla/5.0 AppleWebKit/533.1 Version/4.0 Mobile Safari/533.1"
#    "Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; L822S Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 baiduboxapp/042_0.4_diordna_008_084/moheel_51_2.2.4_S228L/7300088a/DE893986150F2F67CCCCBF4E8B2C6D61%7C324746020104268/1"
#    "Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.1 Mobile Safari/537.36"
#    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET4.0C; .NET4.0E"
]
def get_content(url, headers):

    random_header = random.choice(headers)

    req = urllib2.Request(url)
    req.add_header("User-Agent", random_header)
#    req.add_header("Host", "www.19lou.com")
#    req.add_header("Referer", url)
#    req.add_header("GET", url)

    try:
        content = urllib2.urlopen(req, timeout=3).read()
        return content
    except:
        return "fail"

def get_hash(url):
    a = 0
    for s in url:
        a = (a * base + ord(s)) % mod
    return a;

def get_link(content):
    
    soup = BeautifulSoup(content)

    all_div = soup.find_all('div', class_='t_con cleafix')
    """
    links = re.compile(pattern, content)
    print len(links)
    """
    links = []
    print type(soup)
    for div in all_div:
        tdiv = str(div)
        a = re.findall(re.compile(r'href="(/p.*?)"'), tdiv)
        links.append(a)
#     links.append(re.compile(r'href="(.*?)"', a))
    return links

def deal(word):
    pattern = re.compile('</br>')
    re.sub(pattern, '', word)
    pattern = re.compile(' ')
    re.sub(pattern, '', word)
    word = word + '\n'
    return word

def get_info(content, f):

#demo = '<div class="content" lz="0">                                                asdfasdfID:asdfasdf<br/>asdfasdf:asdfasdf<br/>asdfasdf:asdfasdf<br/>asdfasdf:asdfasdf,asdfasdf                        </div>                    <div class="fr_list j_floor_panel" data-list-count="1">  '
    pattern = re.compile(r'class="d_post_content j_d_post_content  clearfix">(.*?)<')
    words = re.findall(pattern, content)
    print len(words)
    for word in words:
        res = deal(word)
        f.write(res)
#        print res
    return words



start_url = "http://tieba.baidu.com/f?kw=%E6%B5%99%E6%B1%9F%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6&ie=utf-8&pn="
url = "http://tieba.baidu.com"
li = []
for i in range(11,23):
    now_url = start_url +str(i*50)
    content = get_content(now_url, my_header)
    print now_url
    links = get_link(content)
    for link in links:
        li.append(url+link[0])
cnt = 510
for link in li:
    cnt += 1
    f = open("%s.txt" % cnt, 'a')
    i = 1;
    print "cnt=", cnt
    vis = 0
    while True :
        url = link + "?pn=" + str(i)
        print url
        vis += 1
        content = get_content(url, my_header)
        if content == "fail":
            break;
        words = get_info(content, f)
        if len(words) != 30 or vis > 50:
            break
        i += 1
    f.close()
