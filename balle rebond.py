from tkinter import *
from math import cos, sin, tan, pi, sqrt


largeur= 400
hauteur=300
rayon_balle=15
v0=70
alpha=pi/2.2
dx=2

#position initiale
x=15    
x_decalage=0
#y=hauteur-15
sens=1
y=hauteur-((-10/(2*v0**2*cos(alpha)**2))*(sens*(x-x_decalage))**2+tan(alpha)*(sens*(x-x_decalage))+15)
x_prec=x
y_prec=y

def deplacement():
    global x,x_decalage,y,dx,rayon_balle,largeur,hauteur,v0,alpha,sens,x_prec,y_prec
    
    x+=dx
    a=(-10/(2*v0**2*cos(alpha)**2))
    b=tan(alpha)
    y=hauteur-(a*(sens*(x-x_decalage))**2+b*(sens*(x-x_decalage))+15)
    
    #rebond à droite ou à gauche
    if x+rayon_balle+dx>largeur or x-rayon_balle+dx<0:
        dx=-dx
        sens=-sens
        if sens<0:
            x2=(-b-sqrt(b*b-4*a*15))/(2*a)
            x_decalage=largeur+(largeur-x_decalage)
        else:
            x_decalage=-x_decalage
        print("rebond bord",x,x_decalage)
        
    #rebond au sol
    if y+rayon_balle>hauteur:
        x_decalage=x
        v0=v0/1.1
        x+=dx
        y=hauteur-((-10/(2*v0**2*cos(alpha)**2))*(sens*(x-x_decalage))**2+tan(alpha)*(sens*(x-x_decalage))+15)
        print("rebond sol",x,x_decalage)

    Canevas.coords(balle,x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle)
    Canevas.create_line(x_prec,y_prec,x,y)
    x_prec=x
    y_prec=y

    if -b/(2*a)<2*rayon_balle:
        fenetre.destroy()
    
    #màj toutes les 50ms
    fenetre.after(10,deplacement)


fenetre=Tk()

Canevas=Canvas(fenetre,height=hauteur,width=largeur)
Canevas.pack(padx=5,pady=5)

balle=Canevas.create_oval(x-rayon_balle,y-rayon_balle,x+rayon_balle,y+rayon_balle,fill='red')
#if -b/(2*a)<rayon_balle:
deplacement()

fenetre.mainloop()

for i in range(10):
    print(i)
print("fini")

