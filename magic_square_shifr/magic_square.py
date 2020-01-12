import numpy as np
from tkinter import *

sq3 = ['2', '7', '6', '9', '5', '1', '4', '3', '8'] # you can do encrypt for words with max size - 36 symbols.
                                                    # But you can add square with large size
sq4 = ['16', '3', '2', '13', '5', '10', '11', '8', '9', '6', '7', '12', '4', '15', '14', '1']
sq5 = ['24', '1', '19', '4', '17', '5', '2', '22', '20', '16', '18', '23', '8', '9', '7', '12', '14', '3', '21', '15',
       '6', '25', '13', '11', '10']
sq6 = ['26', '32', '18', '9', '11', '15', '7', '16', '21', '23', '20', '24', '14', '10', '25', '35', '19', '8', '34',
       '27', '6', '12', '2', '30', '17', '22', '5', '3', '31', '33', '13', '14', '36', '29', '28', '1']


def shifr(stringg):  # func for encrypt
    if (len(stringg) <= 9):
        sq = sq3
    elif (len(stringg) <= 16):
        sq = sq4
    elif (len(stringg) <= 25):
        sq = sq5
    elif (len(stringg) <= 36):
        sq = sq6
    shh = np.array(['.' for i in range(len(sq))])  # row with cypher
    for ind in range(len(stringg)):
        k = ind + 1
        i = sq.index(str(k))  # finding index of letter in Square
        shh[i] = stringg[ind]
    shh1 = []
    for i in range(len(shh)):
        if shh[i]!='.': #remove dots
            shh1.append(shh[i])
    return shh1


def rozshifr(shhifr): #func for decryption
    rozsh = []
    print(shhifr)
    print("dlina")
    print(len(shhifr))
    if len(shhifr) <= 9:
        sq = sq3
    elif len(shhifr) <= 16:
        sq = sq4
    elif len(shhifr) <= 25:
        sq = sq5
    elif len(shhifr) <= 36:
        sq = sq6
    shh = np.array(['.' for i in range(len(sq))])
    ind = 0
    for j in range(len(sq)):
        if int(sq[j]) <= len(shhifr):
            shh[j] = shhifr[ind]
            print(shh)
            ind += 1
        print(ind)
    for i in range(len(sq)):
        for j in range(len(sq)):
            if str(i+1) == sq[j] and shh[j]!='.':
                rozsh.append(shh[j])
    print(rozsh)
    print(sq)
    return rozsh


def f_zash(): # # func for encrypt button
    z = txt1.get()
    m = ''
    for i in range(len(z)):
        m += (shifr(z))[i]
    lbl11['text'] = m

def f_rozshh(): #func for decryption button
    z = txt2.get()
    sh = rozshifr(z)
    lbl22['text'] = sh


root = Tk() # СОЗДАЕМ ОКНО
root.title("Magic Square Decryption")
lbl1 = Label(root, text='Enter text for encryption')
lbl1.grid(column=0, row=0)
txt1 = Entry(root)
txt1.grid(column=0, row=1)
btn1 = Button(root, text="To encrypt", command=f_zash)
btn1.grid(column=0, row=2)
lbl11 = Label(root, text='')
lbl11.grid(column=0, row=3)
lbl2 = Label(root, text='Enter text for decryption')
lbl2.grid(column=1, row=0)
txt2 = Entry(root)
txt2.grid(column=1, row=1)
btn2 = Button(root, text="To decrypt", command=f_rozshh)
btn2.grid(column=1, row=2)
lbl22 = Label(root, text='')
lbl22.grid(column=1, row=3)
lbl = Label(root,
            text='Note: if the results of encryption or decryption\nare not as expected, check the entered data.')
lbl.grid(column=0, row=4, columnspan=2)
root.mainloop()
