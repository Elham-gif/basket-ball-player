from cs1graphics import*

#PLAYING COURT

BB=Canvas(800,600,"sky blue","BASKETBALL COURT")

#GROUND

R=Rectangle(800,100)
R.setFillColor("dark orange")
R.move(400,550)
BB.add(R)

#BASKETBALL POLE

P1=Rectangle(100,50,Point(100,500))
P1.setFillColor("dark blue")
BB.add(P1)

P2=Rectangle(10,390,Point(100,300))
P2.setDepth(40)
P2.setFillColor("white")
P2.setBorderColor("white")
BB.add(P2)

P3=Rectangle(100,10,Point(145,100))
P3.setFillColor("white")
P3.setBorderColor("white")
BB.add(P3)

P4=Rectangle(10,60,Point(200,100))
P4.setDepth(200)
P4.setFillColor("light blue")
BB.add(P4)

#BASKET

#BASKET=Polygon(Point(200,110),Point(200,150),Point(200,150),Point(210,110))
#BASKET.rotate(40)

basket= Layer()
W1=Ellipse(120,50)
W1.setFillColor("transparent")
W1.setBorderColor("black")
W1.move(150,350)

W2=Ellipse(110,50)
W2.setFillColor("transparent")
W2.setBorderColor("black")
W2.move(150,365)

W3=Ellipse(100,50)
W3.setFillColor("transparent")
W3.setBorderColor("black")
W3.move(150,380)

W4=Ellipse(80,30)
W4.setFillColor("transparent")
W4.setBorderColor("black")
W4.move(150,400)


basket.add(W1)
basket.add(W2)
basket.add(W3)
basket.add(W4)
basket.scale(0.5)
basket.moveTo(160,-80)
BB.add(basket)
#THE MAN

MAN=Layer()

#body
B=Rectangle(100,140,Point(700,300))
B.setFillColor("yellow")
MAN.add(B)

#face
F=Circle(40,Point(700,189))
F.setFillColor("white")
MAN.add(F)

#hands and legs

H1=Rectangle(50,10,Point(625,320))
H1.setFillColor("white")
MAN.add(H1)

H2=Rectangle(10,40,Point(670,350))
H2.setFillColor("white")
MAN.add(H2)

L2=Rectangle(10,160,Point(720,450))
L2.setFillColor("white")
MAN.add(L2)

L1=Rectangle(10,160,Point(680,450))
L1.setFillColor("white")
MAN.add(L1)


#BALL

Ball=Circle(25,Point(585,341))
Ball.setFillColor("brown")
MAN.add(Ball)
BB.add(MAN)

for i in range(200):
    MAN.move(-1,0)
for i in range(300):
    Ball.move(-0.5,-1)

for i in range(450):
    Ball.move(0,1)
