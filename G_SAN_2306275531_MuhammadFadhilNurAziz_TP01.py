#Muhammad Fadhil Nur Aziz
#2306275531
#SAN
#TP 01

import turtle #import
balok = turtle.Turtle() #namain jadi balok 
layar = turtle.Screen() #namain jadi layar
jarak_tower = 0 #gunanya buat rumus menentukan posisi koor x
#buat loop untuk input
while True:
    banyak_tower = (layar.numinput("Tower to Build", "Enter the number of towers you want to build (int) ", minval=1))
    if banyak_tower is None or not banyak_tower.is_integer():
        layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
        continue
    if banyak_tower > 1:
        jarak_tower = (layar.numinput("Distance between Towers", "Enter the distance berween towers (int) ", minval=2,maxval=5))
        if jarak_tower is None or not jarak_tower.is_integer():
            layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
            continue
        beda_layers = (layar.numinput("Tower Layer Difference", "Enter the number of layer differences between each tower (int) ", minval=2,maxval=5))
        if beda_layers is None or not beda_layers.is_integer():
            layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
            continue
    lebar = (layar.numinput("Brick Width", "Enter the width of a brick (int) ",minval=1,maxval=35))
    if lebar is None or not lebar.is_integer():
        layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
        continue
    tinggi = (layar.numinput("Brick Height", "Enter the height of a brick (int) ",minval=1,maxval=25))
    if tinggi is None or not tinggi.is_integer():
        layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
        continue
    layers_pertama = (layar.numinput("The Number of First Tower Layers", "Enter the number of layers for the first tower (int) ",maxval=25))
    if layers_pertama is None or not layers_pertama.is_integer():
        layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
        continue
    lebar_layers = (layar.numinput("Layer Width", "Enter the width of the layer (int) ",maxval=10))
    if lebar_layers is None or not lebar_layers.is_integer():
        layar.numinput("Error", "Anda memasukkan tipe bukan integer, silahkan ulang", default="Error!")
        continue
    break  
#is_integer buat cek integer kalo bukan integer bakal masukin message error

banyak_tower = int(banyak_tower)
if banyak_tower > 1:
    jarak_tower = int(jarak_tower)
    beda_layers = int(beda_layers)
lebar = int(lebar)
tinggi = int(tinggi)
layers_pertama = int(layers_pertama)
lebar_layers = int(lebar_layers)
#buat ubah dari float ke int karena numinput float

#buat menentukan titik awal
total_lebar = (lebar_layers * lebar * banyak_tower) + (jarak_tower * lebar * (banyak_tower-1))
posisi_awal_x = -total_lebar / 2 #minus biar ke kiri

balok.penup() #penup awal awal karena defaultnya 0, 0
balok.goto(posisi_awal_x, -300)  # Starting position
balok.pendown()
count = 0 #buat count brick nya nanti
balok.fillcolor("#CA7F65")
balok.speed(150)
for i in range (layers_pertama): #banyak tinggi
    for i in range(lebar_layers): #banyak baris
        balok.begin_fill()
        for i in range (2):
            balok.forward(lebar)#alas
            balok.left(90)
            balok.forward(tinggi)#tinggi
            balok.left(90)
        balok.forward(lebar)
        count += 1 #akan nambah terus
        balok.end_fill()
    balok.penup()
    balok.goto (balok.xcor() - lebar_layers * lebar, balok.ycor() + tinggi) #ke layer berikutnya
    balok.pendown()
balok.end_fill()

balok.fillcolor("#693424")
balok.goto (balok.xcor() - (1/2 * lebar), balok.ycor() )
for i in range (lebar_layers + 1):
    balok.begin_fill()
    for i in range (2):
        balok.forward(lebar)#alas
        balok.left(90)
        balok.forward(tinggi)#tinggi
        balok.left(90)
    balok.forward(lebar)#alas
    count += 1
    balok.end_fill()
balok.penup()

#go to jamur
balok.goto (balok.xcor() - ((lebar_layers+1)*lebar/2)- lebar/2 , balok.ycor() + tinggi)
balok.pendown()
balok.fillcolor("#674876")
balok.begin_fill()
for i in range (2):
    balok.forward(lebar)#alas
    balok.left(90)
    balok.forward(tinggi)#tinggi
    balok.left(90)
balok.end_fill()
balok.penup()
balok.goto(balok.xcor() - (1/2 * lebar), balok.ycor() + tinggi) #bikin kotak jamur
balok.fillcolor("#9556eb")
balok.right(90)
balok.pendown()
balok.begin_fill()
balok.circle(lebar,-180) #bikin lingkaran jamur
balok.right(90)
balok.backward(lebar*2)
balok.end_fill()
balok.penup()
#kalo towernya lebih dari satu
if banyak_tower > 1:
    for i in range (banyak_tower - 1): #sampai towernya = 1 baru berenti
        balok.goto (balok.xcor() + ((lebar_layers+1)*lebar/2) + lebar/2 + (jarak_tower * lebar), -300) #pindah ke ke kanan dan sesuaindengan jarak inpur
        balok.pendown()
        balok.fillcolor("#CA7F65")
        for i in range (layers_pertama + beda_layers): #ntar nambah terus
            for i in range(lebar_layers): #banyak baris
                balok.begin_fill()
                for i in range (2):
                    balok.forward(lebar)#alas
                    balok.left(90)
                    balok.forward(tinggi)#tinggi
                    balok.left(90)
                balok.forward(lebar)
                count += 1
                balok.end_fill()
            balok.penup()
            balok.goto (balok.xcor() - lebar_layers * lebar, balok.ycor() + tinggi)#ke layer berikutnya
            balok.pendown()
        balok.end_fill()

        balok.fillcolor("#693424")
        balok.goto (balok.xcor() - (1/2 * lebar), balok.ycor() )
        for i in range (lebar_layers+1):
            balok.begin_fill()
            for i in range (2):
                balok.forward(lebar)#alas
                balok.left(90)
                balok.forward(tinggi)#tinggi
                balok.left(90)
            balok.forward(lebar)#alas
            count +=1
            balok.end_fill()
        balok.penup()
        layers_pertama += beda_layers #biar nambah layernya
        #go to jamur
        balok.goto (balok.xcor() - ((lebar_layers+1)*lebar/2)- lebar/2 , balok.ycor() + tinggi) #ke koordinat jamur
        balok.fillcolor("#674876")
        balok.pendown()
        balok.begin_fill()
        for i in range (2):
            balok.forward(lebar)#alas
            balok.left(90)
            balok.forward(tinggi)#tinggi
            balok.left(90)
        balok.end_fill()
        balok.penup()
        balok.goto(balok.xcor() - (1/2 * lebar), balok.ycor() + tinggi) #ke pala jamur
        balok.fillcolor("#9556eb")
        balok.right(90)
        balok.pendown()
        balok.begin_fill()
        balok.circle(lebar,-180)
        balok.right(90)
        balok.backward(lebar*2)
        balok.end_fill()
        balok.penup()
    balok.goto (0, -320)
    balok.write(f"{banyak_tower} Super Mario Towers have been built with a total of {count} bricks", align= "Center") #kalo lkebih dari 1 towers
    turtle.exitonclick()
else: #yang ini kalo towernya cuman 1 langsung kesini
    balok.goto (posisi_awal_x, -320)
    balok.write(f"{banyak_tower} Super Mario Tower have been built with a total of {count} bricks",align ="Center") #kalo satu tower
    turtle.exitonclick()

#collaborator
#Farrel Dharmawan
#Faiz Akram Pribadi
#Fauzan Putra Sanjaya
#Muhammad Farhan Ramadhan
#Muhammad Daffa Abyaz Tjiptadi