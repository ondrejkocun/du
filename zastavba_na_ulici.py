import tkinter  #importovanie kniznice
canvas = tkinter.Canvas()   #nastaevnie platna                                  #ano viem ze sa to dalo v jednom defe ale nevadi 
canvas.pack()

vyska=[]    #deklaracia zoznamov
sirka=[]
x=0 #deklaracia premennych
subor=open('zastavba_na_ulici.txt','r') #otvorenie suboru na citanie
for riadok in subor: #nacitanie riadkov zo suboru 
    riadok=riadok.strip() #odsranenie neviditelnych znakov z riadku
    riadok=riadok.split(' ')    #rozdelenie riadka na 2 casti 
    sirka.append(int(riadok[0])) #pridanie prvej casti riadku do sirky
    vyska.append(int(riadok[1])) #pridanie druhejj casti riadku do vysky
def kresli(): #funkcia na vykreslenie budov
    global x    #deklaracia globalnej premmenej
    x=sirka[0] #nastavenie premmenej na prvu hodnottu zoznamu sirka
    for i in range (len(sirka)): #cyklus na vykreslenie budov
        if vyska[i]==0:     #podmienka na vyber farby 
            farba='green'
        else:
            farba='black'
        canvas.create_rectangle(x,200,x+sirka[i],200-vyska[i],outline=farba,fill='gray') #kreslenie budov
        x+=sirka[i] #zvacsovanie premmenej

def rozdiel(): #funkcia na kreslenie rozdielovych ciar
    global x    #deklaracia globanej premennej
    x=sirka[0]  #nastaevnie premmenej na pru hodnotu zoznamu sirka
    vrozdiel = entry1.get() #nastavenie premmenej na hodnotu z entry
    for i in range (len(sirka)): #cyklus na prejdenie a porovnanie kazdej vysky 
        if i < 4 and vyska[i]-vyska[i+1] >= int(vrozdiel):  #podmienka na urcenie vyskoveho rozdielu
                canvas.create_line(x+sirka[i],200-vyska[i+1],x+sirka[i],200-vyska[i],fill='red')    #nakreslenie cervenej ciary
        if i > 0 and vyska[i]-vyska[i-1] >= int(vrozdiel):   #podmienka na urcenie vyskoveho rozdielu
               canvas.create_line(x,200-vyska[i-1],x,200-vyska[i],fill='red')   #nakreslenie cervenej ciary
        x+=sirka[i] #zvacsenie hodnoty premmenej
    print(vrozdiel)     
entry1 = tkinter.Entry()    #nastavenie entry okna
entry1.pack()
button1 = tkinter.Button(text='Start',command=rozdiel) #nastavenie buttonu
button1.pack()
kresli()    #vyvolanie premmenej
