# -*- coding: utf-8 -*-
import requests

Key_List = ["vc1E8k8RnPyaj2X41MVSI1HXXvqWMgwH", "A2uvcwO7pVXlqxnHyayuqVqeGIt4AJVh", "GRnYa9DlBoW29RqqjWvyDjLozVMdcBtp",
            "k9o8U8w05xjoyvprfqZLhUdyXD6Z1nPY", "skEPF0AeMlNUM5HzbKgmB6vSfB52dqDB"]
key = Key_List[0]
User_Key_list = []
Username_list = [""]


def Roter_Hello():
    print("---")
    print("|RoTer --- 智能信息收集工具")
    print("|Version [Free 1.0.0]")
    print("|By WindStream")
    print("|键入menu以查看菜单")
    print("---")


def api_menu():
    print("---")
    print("|1.查看现有Key")
    print("|2.添加Key")
    print("|3.查看Key使用情况")
    print("|4.更改使用Key")
    print("|5.键入back以返回上一级菜单")
    print("---")


def myabout():
    print("---")
    print("|介绍:Roter是一款Python开发的开源软件,旨在简化收集网络数据的过程,请勿将其用于非法用途")
    print("|关于开源:开源地址(https://github.com/VoPlAz/RoTer),使用MIT开源协议,请自觉遵守")
    print("|开发者:WindStream(QQ:1514037660),StreamLgiht交流群:770477144")
    print("|声明:此程序禁止商用或用于非法用途,本程序不承担任何责任")


def cho_cl(cho, key):
    if cho.lower() == "menu":
        print("---")
        print("|1.Q绑查询")
        print("|2.手机反查")
        print("|3.shodan查询ip")
        print("|4.查看本机ip")
        print("|5.解析域名ip")
        print("|6.ApiKey操作")
        print("|7.关于本程序")
        print("|键入exit以退出程序")
        print("---")
    elif cho == "1":
        qq_number = input(">>>QQ Number:")
        back_text_Y = requests.get("http://23aa.top/111/api/qb.php?qq=" + qq_number)
        back_text__Y_f = back_text_Y.text.replace("{", "")
        back_text__Y_s = back_text__Y_f.replace("}", "")
        back_text__Y_t = back_text__Y_s.replace("status", "返回值")
        back_text__Y_f = back_text__Y_t.replace('"', "")
        back_text__Y_fi = back_text__Y_f.replace(",", "\n")
        back_text__Y_si = back_text__Y_fi.replace("message", "消息")
        back_text__Y_sev = back_text__Y_si.replace("phone", "手机号")
        back_text = back_text__Y_sev.replace("diqu", "归属地")
        print(back_text)
    elif cho == "2":
        phone_number = input(">>>Phone Number:")
        if phone_number == "":
            print("输入为空无法查询")
        else:
            phone_back_f = requests.get("http://23aa.top/111/api/qbphone.php?phone=" + phone_number).text
            myone = phone_back_f.replace("{", "")
            mytwo = myone.replace("}", "")
            myth = mytwo.replace("status", "返回值")
            myfou = myth.replace('"', "")
            myfiv = myfou.replace(",", "\n")
            mysix = myfiv.replace("message", "消息")
            mysev = mysix.replace("phonediqu", "归属地")
            myehi = mysev.replace(":" + phone_number, "手机号:" + phone_number)
            print(myehi)
    elif cho == "3":
        host = input(">>>ip:")
        yshodan_back = requests.get("https://api.shodan.io/shodan/host/" + host + "?key=" + key).text
        ytshodan_back = yshodan_back.replace("{", "")
        ytshodan_backt = ytshodan_back.replace("}", "")
        #shodan_back = ytshodan_backt.replace(",", "\n")
        print(ytshodan_backt)
    elif cho == "4":
        print(requests.get("https://api.shodan.io/tools/myip?key=" + key).text.replace('"', ""))
    elif cho == "5":
        hostname = input(">>>Host Name:")
        back_host_ip = requests.get("https://api.shodan.io/dns/resolve?hostnames=" + hostname + "&key=" + key).text
        back_host_ip_f = back_host_ip.replace('"', "")
        back_host_ip_s = back_host_ip_f.replace("{", "")
        back_host_ip_p = back_host_ip_s.replace("}", "")
        print(back_host_ip_p)
    elif cho == "6":
        api_menu()
        while True:
            api_cho = input(">>>")
            if api_cho == "1":
                print("---")
                print("-|" + Key_List[0])
                print("|归属账号:WindStream")
                print("-|" + Key_List[1])
                print("|归属账号:0100569")
                print("-|" + Key_List[2])
                print("|归属账号:0100569_1")
                print("-|" + Key_List[3])
                print("|归属账号:0100569_2")
                print("-|" + Key_List[4])
                print("|归属账号:0100569_3")
                print("---")
                if len(User_Key_list) == 0:
                    print("附加")
                    print("无")
                else:
                    a = -1
                    print("附加")
                    for i in User_Key_list:
                        print("-|" + User_Key_list[a + 1])
                        print("|归属账号" + Username_list[a + 1])
            elif api_cho == "2":
                userKey = input(">>>Key:")
                username = input(">>>UserName:")
                User_Key_list.append(userKey)
                Username_list.append(username)
            elif api_cho == "3":
                i_key = input(">>>Key:")
                back_Key_info = requests.get("https://api.shodan.io/api-info?key=" + i_key).text
                print(back_Key_info)
            elif api_cho == "4":
                print("目前使用的Key为" + key)
                Key = input(">>>New Key:")
                key = Key
                print("Shodan Key已更改为" + key + ".")
            elif api_cho.lower() == "back":
                break
            else:
                print("无效选项")
    elif cho == "7":
        myabout()
    elif cho.lower()=="exit":
        exit()
    else:
        print("无效选项")


Roter_Hello()
while True:
    cho = input(">>>")
    cho_cl(cho=cho, key=key)
