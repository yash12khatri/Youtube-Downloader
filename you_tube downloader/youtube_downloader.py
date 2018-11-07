
from tkinter import *
import os
import time
import PIL
from PIL import Image, ImageTk
from tkinter import ttk
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib 
import pytube
from pytube import YouTube

class Client(QWebPage):    
    def __init__(self,url):
        self.app=QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

'''
def downloader(l):
    get_true = True
    while get_true:
        try:
            yt=YouTube(l)
            get_true=False
        except:
            print("Connection Error")
            continue
    mp4files = yt.filter('mp4')
    try:
        print(yt.filename)
        print(mp4files[-1])
    except:
        pass
    video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    try:
        video.download(SAVE_PATH)
    except:
        print("Error, Maybe Duplicate File")
        '''
'''
url=input("enter URL of playlist")
print("fetching playlist from youtube")
client_response=Client(url)
source=client_response.mainFrame().toHtml()
soup=bs.BeautifulSoup(source,'html.parser')
#js_test=soup.find('a')
print(soup.title.text)
#SAVE_PATH = r"C:/Users/Yash K/Desktop/download videos/"
i=1
print(str(len(soup.findAll('a',{'class':'pl-video-title-link'})))+" videos found ")
for link in soup.findAll('a',{'class':'pl-video-title-link'}):
    vidname=str(link.string)+'.mp4'
    vidurl="https://www.youtube.com"+link['href']
    print(vidname,vidurl)
    print("connecting to servers.........")
    yt = pytube.YouTube(vidurl)
    quality="720p"#input("enter quality ") 
    vids= yt.streams.filter(progressive=True).all()
    for i in range(len(vids)):
        print(str(vids[i]))
 
    flag=0
    for i in range(len(vids)):
        if((quality in str(vids[i])) and('mp4') in str(vids[i])):
           flag=1
           print(str(vids[i]))
           print("the size of file is "+str(int(vids[i].filesize)/(1024*1024))+"MB")
           print(yt.title)
           print("downloading start.....")
           vids[i].download()
           break 
    if(flag==1):
           print(str(yt.title)+' DOWNLOADED')
    else:
           print("video quality you have entered is not avaliable")
    i=i+1  
   ''' 
'''
atag = soup.findAll('a',{'class':'pl-video-title-link'})
atag = atag.findAll('a',{'class':'yt-uix-tile-link'})
atag = atag.findAll('a',{'class':'yt-uix-sessionlink'})
atag = atag.findAll('a',{'class':'spf-link'})



'''
'''
print(link.get('href'))
    print(link.get('is'))
    print(link.get('class'))
'''


def second_page(root):
    root.destroy()
    second=Tk()
    second.geometry("600x350+10+10")
    second.configure(background="Orange")
    second.title("Download Video")
    
    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\back.png")
    photo1 = ImageTk.PhotoImage(image)
    button1=Button(second,relief='flat' ,bg="Orange",image=photo1,text="Back to Home",font=('Tempus Sans ITC', 10, 'bold'),command=lambda:main_bypass(second))
    button1.place(x=400,y=150)
    
    l1=Label(second, text='Enter URL',font="Verdana",bg="Orange")
    l2=Label(second, text='Select Video Quality',font="Verdana",bg="Orange")
    l1.place(x=30,y=30)
    l2.place(x=30,y=90)
    
    e1 = Entry(second,width=50)
    e1.place(x=270,y=30)
    e1.focus_set()
    var = StringVar(second)
    var.set("720p") # initial value 
    option = OptionMenu(second, var, "720p", "480p", "360p", "240p","144p")
    option.config(compound='right')
    option.place(x=270,y=90)
    status=Label(second,text="Ready to download....",bd=1,relief=SUNKEN,anchor=W)
    status.pack(side=BOTTOM,fill=X)
    
    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\download.png")
    photo2 = ImageTk.PhotoImage(image)
    button2=Button(second,relief='flat',bg="Orange",image=photo2,text="Download",font=('Tempus Sans ITC', 10, 'bold'),command=lambda: download_vid(second,status,e1.get(),var.get()))
    button2.place(x=50,y=150)
 
    second.mainloop()


def first_page(root):
    root.destroy()
    first=Tk()
    first.geometry("600x350+10+10")
    first.configure(background="Orange")
    first.title("Download Video")

    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\back.png")
    photo1 = ImageTk.PhotoImage(image)
    button1=Button(first,relief='flat',bg="Orange",image=photo1,text="Back to Home",font=('Tempus Sans ITC', 10, 'bold'),command=lambda:main_bypass(first))
    button1.place(x=400,y=150)
    
    l1=Label(first, text='Enter PlayList URL',font="Verdana",bg="Orange")
    l2=Label(first, text='Select Video Quality',font="Verdana",bg="Orange")
    l1.place(x=30,y=30)
    l2.place(x=30,y=90)
    
    e1 = Entry(first,width=50)
    e1.place(x=270,y=30)
    e1.focus_set()
    var = StringVar(first)
    
    var.set("720p") # initial value 
    option = OptionMenu(first, var, "720p", "480p", "360p", "240p","144p")
    option.config(compound='right')
    option.place(x=270,y=90)
    status=Label(first,text="Ready to download....",bd=1,relief=SUNKEN,anchor=W)
    status.pack(side=BOTTOM,fill=X)


    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\download.png")
    photo2 = ImageTk.PhotoImage(image)
    button2=Button(first,relief='flat',bg="Orange",image=photo2,text="Download Playlist",font=('Tempus Sans ITC', 10, 'bold'),command=lambda:download_playlist(first,status,e1.get(),var.get()))
    button2.place(x=50,y=150)

    first.mainloop()
    
def get_soup_obj(url):
    client_response=Client(url)
    source=client_response.mainFrame().toHtml()
    soup=bs.BeautifulSoup(source,'html.parser')
    return soup

 
def download_playlist(first,status,vidurl,quality):
    status.configure(text="Analysing.....")
    print("hello")
    first.update_idletasks() 
    soup=get_soup_obj(vidurl)
    
    first.destroy()
    '''
    playlist_window=Tk()
    playlist_window.geometry("700x700+70+70")
    playlist_window.title(soup.title.text)
    #js_test=soup.find('a')
    status=Label(playlist_window,text=str(len(soup.findAll('a',{'class':'pl-video-title-link'})))+" videos found ",bd=1,relief=SUNKEN,anchor=W)
    status.pack(side=BOTTOM,fill=X)
    playlist_window.update_idletasks()
    time.sleep(2)
    '''
    SAVE_PATH = r"C:\Users\Yash K\Downloads"
    i=1 
    for link in soup.findAll('a',{'class':'pl-video-title-link'}):
        vidname=str(link.string)
        vidurl="https://www.youtube.com"+link['href']
        print(vidname,vidurl)
        print("connecting to servers.........")
        yt = pytube.YouTube(vidurl)
        quality="720p"#input("enter quality ") 
        vids= yt.streams.filter(progressive=True).all()
        for i in range(len(vids)):
            print(str(vids[i]))
     
        flag=0
        for i in range(len(vids)):
            if((quality in str(vids[i])) and('mp4') in str(vids[i])):
               flag=1
               print(str(vids[i]))
               print("the size of file is "+str(int(vids[i].filesize)/(1024*1024))+"MB")
               print(yt.title)
               print("downloading start.....")
               vids[i].download(SAVE_PATH )
               break 
        if(flag==1):
               print(str(yt.title)+' DOWNLOADED')
        else:
               print(str(vids[i]))
               print("the size of file is "+str(int(vids[0].filesize)/(1024*1024))+"MB")
               print(yt.title)
               print("downloading start.....")
               vids[0].download(SAVE_PATH) 
        i=i+1  
    #root.mainloop()

def download_vid(window,status,vidurl,quality):  
    status.configure(text="connecting to servers.........")
    window.update_idletasks()
    get_true = True
    while get_true:
        try:
            yt=YouTube(vidurl)
            get_true=False
        except:
            status.configure(text="Connection Error")
            window.update_idletasks()
            continue
    vids= yt.streams.filter(progressive=True).order_by('resolution').desc().all()
                   
    if(quality in str(vids)):
        flag=0
        for i in range(len(vids)):
            if(quality in str(vids[i]) ):
               flag=1
               #status.configure(text=str(vids[i]))
               #window.update_idletasks() 
               size_temp="the size of file is "+str(int(vids[i].filesize)/(1024*1024))+"MB"
               status.configure(text=size_temp)
               window.update_idletasks() 
               time.sleep(2)
               status.configure(text="downloading.... "+yt.title)
               window.update_idletasks() 
               #progressbar = Progressbar(window,orient=HORIZONTAL, length=200, mode='determinate')
               #progressbar.pack(side="bottom")
               #progressbar.start()
               try:
                   vids[i].download()
                   status.configure(text=str(yt.title)+' DOWNLOADED')
                   window.update_idletasks() 
                   break
               #progressbar.stop() 
               except:
                   print("Error, Maybe Duplicate File") 
    else:
        print(str(vids[0]))
        print("the size of file is "+str(int(vids[0].filesize)/(1024*1000))+"MB")
        print(yt.title)
        print("downloading start.....")
        progressbar = ttk.Progressbar(window,orient=HORIZONTAL, length=200, mode='determinate')
        progressbar.pack(side="bottom")
        progressbar.start()
        vids[0].download()
        progressbar.stop()
        print(str(yt.title)+' DOWNLOADED')
                   
  
def main_bypass(second):
    second.destroy()
    main_window()
    
def main_window():
    root=Tk()                
    root.title("Youtube Downloader")
    root.geometry("600x350+10+10")
    root.configure(background='Orange')

    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\home.png")
    photo = ImageTk.PhotoImage(image)
    l1 = Label(root,image=photo,bg="Orange")
    l1.place(x=220,y=10)

    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\download_video.png")
    photo1 = ImageTk.PhotoImage(image)
    button1=Button(root,relief='flat' ,bg="Orange",text="download video",image=photo1,font=('Tempus Sans ITC', 10, 'bold'),command=lambda:second_page(root))
    button1.place(x=100,y=140)


    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\playlist.png")
    photo2 = ImageTk.PhotoImage(image)
    button2=Button(root,bg="Orange",relief='flat',text="download playlist",image=photo2,font=('Tempus Sans ITC', 10, 'bold'),command=lambda:first_page(root))
    button2.place(x=380,y=140)
    

    image = PIL.Image.open(r"C:\Users\Yash K\Desktop\you_tube downloader\\close.png")
    photo3 = ImageTk.PhotoImage(image)
    button3=Button(root,relief='flat',bg="Orange",text="CLOSE",image=photo3,font=('Tempus Sans ITC', 10, 'bold'),command=root.destroy)
    button3.place(x=10,y=260)

    root.mainloop()


main_window()     
        
'''        
        top=Toplevel(root) 
        top.title("Download video from YouTube")
        top.geometry("700x700") 
        label_1=Label(top,text="Enter URL here...")
        entry_1=Entry(top)
        label_1.grid(row=0,sticky=E)
        entry_1.grid(row=0,column=1,sticky=N)
        label_2=Label(top,text="Quality") 
        label_2.grid(row=1) 
        exit_button=Button(top,text="exit",command=top.destroy)
        exit_button.grid(row=0,column=7)
        top.mainloop()
'''



