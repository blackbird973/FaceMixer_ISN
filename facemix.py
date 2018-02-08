from PIL.Image import *  #Importe la librairie PIL qui permet le "getpixel" et "putpixel"
import Image     # Permet d'ouvrir les images et d'enregistrer l'image finale

p1 = Image.open('mathieu.jpg')
p2 = Image.open('sacha.jpg')
p3 = Image.open('yoyo.jpg')
p4 = Image.open('pauline.jpg')
p5 = Image.open('rebou.jpg')
p6 = Image.open('ramain.jpg')
p7 = Image.open('chinoi.jpg')
p8 = Image.open('bastien.jpg')
p9 = Image.open('paul.jpg')

x = 0
y = 0

size = p1.size

for x in range(0, size[0]):       #Parcourt tout les pixels suivant les dimensions des photos
    for y in range (0,size[1]):
        
        (rouge1,vert1,bleu1) = p1.getpixel((x,y))  #Récupère les couleurs RVB du même
        (rouge2,vert2,bleu2) = p2.getpixel((x,y))  #pixel pour toutes les images
        (rouge3,vert3,bleu3) = p3.getpixel((x,y))
        (rouge4,vert4,bleu4) = p4.getpixel((x,y))
        (rouge5,vert5,bleu5) = p5.getpixel((x,y))
        (rouge6,vert6,bleu6) = p6.getpixel((x,y))
        (rouge7,vert7,bleu7) = p7.getpixel((x,y))
        (rouge8,vert8,bleu8) = p8.getpixel((x,y))
        (rouge9,vert9,bleu9) = p9.getpixel((x,y))
        rouge=(rouge1+rouge2+rouge3+rouge4+rouge5+rouge9+rouge8+rouge7+rouge6)/9  #Fait la moyenne de la quantité de rouge de toute 
        vert=(vert7+vert6+vert5+vert4+vert3+vert2+vert1+vert8+vert9)/9            #les images sur le pixel analysé.
        bleu=(bleu7+bleu6+bleu5+bleu4+bleu3+bleu2+bleu1+bleu8+bleu9)/9            #Idem pour le vert et bleu
        p1.putpixel((x,y),(rouge,vert,bleu))  #Remplace la quantité de rouge, de vert, et de bleu du pixel analysé par la moyenne
                                              #de rouge, de vert et de bleu de toute les images.
p1.show()
p1.save('horrora.jpg')    
