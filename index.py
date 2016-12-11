#pour caliber decommenter les ligne avec "(calibration)" et changer le nb de la ligne qui correspond "(calibration)"
from sense_hat import SenseHat
import time
import sys

a = int()             #variable
c = int()
q = int(255)          #couleur par default
w = int()
e = int()
r = int()
sense = SenseHat()
sense.clear()

while True:
  x, y, z = sense.get_accelerometer_raw().values()    #avoir donner (brute) de l'accelero

  #x = round(x, 0)      #arrondie (ici commenter )
  #y = round(y, 0)      ##/   /
  #z = round(z, 0)      ##/   /

  if x>0.5 :          #test de seuil (limite de l'accelero pour compter les pas) de x (calibration)
    #print (a)        #affichage de a (ici commenter) (calibration)
    a=a+1
  if y<-1 :           # de y (calibration)
    #print (a)        #affichage de a (ici commenter) (calibration)
    a=a+1
  if z>1 :            # de z (calibration)
    #print (a)        #affichage de a (ici commenter) (calibration)
    a=a+1
  if a>7 :            # change de ligne 
    a=0
    c=c+1
  if c>7 and r == 0:            # limite de 8x8 
    c=0
    q=0
    w=255                       #change de couleur
    r = 1
    sense.clear()
  if c>7 and r == 1:
    c=0
    w=0
    e=255                       #change de couleur
    r = 2
    sense.clear()
  if c>7 and r == 2:
    c=0
    q=0
    sense.show_message("STOP")      #affichage de stop
    sys.exit()                      #quite le prog
    
  #b = str(a)             #affichage de la valeur de les pas en chiffre (ici commenter)
  #sense.show_letter(b)   #/    /
    
  print("x=%s, y=%s, z=%s" % (x, y, z))        #affichage des info (calibration)
    
  sense.set_pixel(a, c, [e, w, q])    #affichage de la valeur de les pas en pixel le plus important /!\.
    
  time.sleep(0.1)       #vitesse de la boucle en s (calibration)
  
