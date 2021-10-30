from tkinter import * 
from tkinter import messagebox 

import subprocess

marray=[
    [0,1,2],
    [10,11,12],
    [20,21,22]
]
winner=None
turn_="O"
counter=1


def stopper(marray):
    global winner
    if marray[0][0]==marray[0][1]and marray[0][1]==marray[0][2]:
        winner=marray[0][0]

        return True
    elif marray[1][0]==marray[1][1]and marray[1][1]==marray[1][2]:
        
        winner=marray[1][1]
        return True

    elif marray[2][0]==marray[2][1]and marray[2][1]==marray[2][2]:
        winner=marray[2][2]
        return True
    

    elif marray[0][0]==marray[1][0]and marray[1][0]==marray[2][0]:
        winner=marray[0][0]
        return True
        

    elif marray[0][1]==marray[1][1]and marray[1][1]==marray[2][1]:
        winner=marray[1][1]
        return True
        

    elif marray[0][2]==marray[1][2]and marray[1][2]==marray[2][2]:
        winner=marray[2][2]
        return True   
        

    elif marray[0][0]==marray[1][1]and marray[1][1]==marray[2][2]:
        winner=marray[0][0]
        return True
        

    elif marray[0][2]==marray[1][1]and marray[1][1]==marray[2][0]:
        winner=marray[1][1]
        return True
        

    else:
        return False






board=Tk()
board.geometry("500x500") 
board.title("TIc TAc TOe")
a,b,c,d,e,f,g,h,i='-','-','-','-','-','-','-','-','-'

def cheat():
    messagebox.showwarning(f"Invalid Move ","What u did is against the rules")

def clicker00():
    global marray,turn_,counter,winner
    marray[0][0]=turn_
    button00['text']=turn_
    counter+=1
    
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X":
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"
    button00['command']=cheat
    
def clicker01():
    global marray,turn_,counter,winner
    marray[0][1]=turn_
    button01['text']=turn_
    counter+=1

    if turn_=="O":
        turn_="X"  
    elif turn_=="X":
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button01['command']=cheat

def clicker02():
    global marray,turn_,counter,winner
    button02['text']=turn_
    counter+=1
    marray[0][2]=turn_
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button02['command']=cheat

def clicker10():
    global marray,turn_,counter,winner
    button10['text']=turn_
    counter+=1
    marray[1][0]=turn_
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"
    button10['command']=cheat

def clicker11():
    global marray,turn_,counter,winner
    button11['text']=turn_
    counter+=1
    marray[1][1]=turn_
    
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button11['command']=cheat
def clicker12():
    global marray,turn_,counter,winner
    button12['text']=turn_
    counter+=1
    marray[1][2]=turn_
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()

    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"
    button12['command']=cheat

def clicker20(): 
    global marray,turn_,counter,winner
    marray[2][0]=turn_
    button20['text']=turn_
    counter+=1
    
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button20['command']=cheat

def clicker21():
    global marray,turn_,counter,winner
    button21['text']=turn_
    counter+=1
    marray[2][1]=turn_
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()
    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button21['command']=cheat

def clicker22():
    global marray,turn_,counter,winner
    button22['text']=turn_
    counter+=1
    marray[2][2]=turn_
    if turn_=="O":    
        turn_="X"  
    elif turn_=="X": 
        turn_="O"
    stopper(marray)
    if stopper(marray)==True:
        print("The winner is"+" "+winner)
        board.destroy()

    elif stopper(marray)==False and counter==9:
        winner="No one. (Draw)"
        board.destroy()
    if (counter-1)%2==0:
        label2['text']="player'O''s turn"
    else:
        label2['text']="player'X''s turn"

    button22['command']=cheat

button00=Button(text=a,command=clicker00, height=5, width=5)
button00.grid(row=0,column=0)
button01=Button(text=b,command=clicker01, height=5, width=5)
button01.grid(row=0,column=1) 
button02=Button(text=c,command=clicker02, height=5, width=5)
button02.grid(row=0,column=2)
#l1
button10=Button(text=d,command=clicker10, height=5, width=5)
button10.grid(row=1,column=0)
button11=Button(text=e,command=clicker11, height=5, width=5)
button11.grid(row=1,column=1)
button12=Button(text=f,command=clicker12, height=5, width=5)
button12.grid(row=1,column=2)
#l2
button20=Button(text=g,command=clicker20, height=5, width=5)
button20.grid(row=2,column=0)
button21=Button(text=h,command=clicker21, height=5, width=5)
button21.grid(row=2,column=1)
button22=Button(text=i,command=clicker22, height=5, width=5)
button22.grid(row=2,column=2)
label1=Label(text="Tic Tac Toe").grid(row=4,column=1)
label2=Label(text="O's Turn")
label2.grid(row=5,column=1)



board.mainloop()
declare=Tk()
declare.title("OVER")
Label1=Label(text="The winner is "+winner).pack()
def replay():
    declare.destroy()

    subprocess.call(["python3", "main.py"])
butt=Button(text="Replay",command=replay).pack()
declare.mainloop()
# print(winner,counter)    
