import socket
import pystray
import _thread

from PIL import Image
from pystray import MenuItem

abc = "Sunch233 Chatroom Professioanl"

#设置服务器信息
host = "127.0.0.1"
port = 18689
Client = socket.socket()

def conncetToServer():
    try:
        Client.connect((host,port))
        while True:
            msg = Client.recv(1024).decode('gbk')
            try:
                w =  msg.split("  ")
                #_thread.start_new_thread(sendMessageOnPush,(w[1],w[0]))
                sendMessageOnPush(w[1],w[0])
            except:
                #_thread.start_new_thread(sendMessageOnPush,(msg,abc))
                
                sendMessageOnPush(msg,abc)
            if msg == "on_exit":
                icon.stop()
                
    except Exception as q:
        print("错误，因为 ",q)
        
def sendMessageOnPush(text,bbb):
        icon.notify(text,bbb)
        

def sendTestMessage(icon:pystray.Icon): #测试信息发送
    icon.notify("这是一条测试信息内容",abc)

def on_exit(icon,item): #退出
    icon.stop()


menu = (MenuItem(text="发送测试推送",action=sendTestMessage),MenuItem(text="退出",action=on_exit))
image = Image.open("icon_32x32.png")
icon = pystray.Icon(abc,image,abc,menu)
_thread.start_new_thread(conncetToServer,())
icon.run()
