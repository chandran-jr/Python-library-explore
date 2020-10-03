from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title('IPL SCORE VIEWER')
url = "https:www.cricbuzz.com"


def getdata(data):
    team1,team2,team1_score,team2_score=data
    page = requests.gt(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    
    team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
    team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
    team1.config(text = team_1)
    team2.config(text = team_2)
    team1_score.config(text=team_1_score)
    team2_score.config(text=team_2_score)
    
    a = Label(root,text='IPL Viewer', font=("",40))
    a.grid(row=0,columnspan=2)
    team1 = Label(root,text="Team 1",font=("",20))
    team1.grid(row=1,column=0)
    team2 = Label(root,text="Team 2",font=("",20))
    team2.grid(row=1,column=1)
    
    team1_score = Label(root,text="hit refresh",font = ("", 20))
    team1_score.grid(row=2,column=0)
    team2_score=Label(root,text="hit refresh", font=("", 20))
    team2_score.grid(row=2,column=1)
    data = [team1,team2,team1_score,team2_score]
    refresh = Button(root,text = "Refresh",command = lambda:getdata(data),
                    height=2,width=10,font=("",20))
    refresh.grid(row=3,columnspan=2)
    root.mainloop()
