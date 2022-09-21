import tkinter
canvas = tkinter.Canvas()
canvas.pack()

vyska=[]
sirka=[]
x=0
subor=open('zastavba_na_ulici.txt','r')
for riadok in subor:
    riadok=riadok.strip()
    riadok=riadok.split(' ')
    sirka.append(int(riadok[0]))
    vyska.append(int(riadok[1]))
def kresli():
    global x
    x=sirka[0]
    for i in range (len(sirka)):
        if vyska[i]==0:
            farba='green'
        else:
            farba='black'
        canvas.create_rectangle(x,200,x+sirka[i],200-vyska[i],outline=farba,fill='gray')
        x+=sirka[i]

def rozdiel():
    global x
    x=sirka[0]
    vrozdiel = entry1.get()
    for i in range (len(sirka)):
        print(x)
        if i < 4 and vyska[i]-vyska[i+1] >= int(vrozdiel):
                canvas.create_line(x+sirka[i],200-vyska[i+1],x+sirka[i],200-vyska[i],fill='red')
        if i > 0 and vyska[i]-vyska[i-1] >= int(vrozdiel):
               canvas.create_line(x,200-vyska[i-1],x,200-vyska[i],fill='red')
        x+=sirka[i]
    print(vrozdiel)
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Start',command=rozdiel)
button1.pack()
kresli()
