import requests
import urllib.parse
import re

def TestLogin():
    req = requests.get('http://www.baidu.com/')
    if len(req.text) > 1000:
        print("校园网已认证！")
        req.close()
        return 0
    url = re.search(r"href='(.*?)'" , req.text).group(1)
    req.close()
    return url

def main():
    username = 'YourAccount'
    password = 'YourPassword'
    url = TestLogin()
    if url == 0:
        return True
    req = requests.get(url)
    serviceId = re.search(r'<li><span  value="(.*?)">访问外网</span></li>' , req.text).group(1)
    req.close()
    details = urllib.parse.urlparse(url).query
    query_dict = {}
    for i in details.split('&'):
        temp_list = i.split('=')
        query_dict[temp_list[0]] = temp_list[1]
    do_dict = {
        'qrCodeId': '请输入编号',
        'username': username,
        'pwd': password,
        'validCode': '验证码',
        'validCodeFlag': 'false',
        'serviceId' : serviceId,
        'ssid' : query_dict['ssid'],
        'mac' : query_dict['mac'],
        't' : query_dict['t'],
        'wlanacname' : query_dict['wlanacname'],
        'url' : query_dict['url'],
        'nasip' : query_dict['nasip'],
        'wlanuserip' : query_dict['wlanuserip']
    }
    do_url = 'http://222.197.192.59:9090/zportal/login/do'
    req = requests.post(do_url , data = do_dict)
    req.close()
    success = TestLogin()
    if success == 0:
        return True
    else:
        print("校园网认证失败！")

if __name__ == '__main__':
    main()
