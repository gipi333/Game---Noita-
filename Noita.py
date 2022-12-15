from cond_sand import condition_sand
from cond_water import condition_water
from cond_smoke import condition_smoke
from cond_salt import condition_salt
from cond_fire import condition_fire
from cond_acid import condition_acid

from element_player import Sand, Water, Fire, Salt,Smoke ,Wood, Rock, Acid, Erase


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backend_bases import MouseButton

import keyboard

#from matplotlib.animation import FuncAnimation
    


#===============================================
#       Définition de la matrice de départ
#===============================================
mat_colors = ['#ffffff', '#c2b280', '#aaaaaa', '#7777aa', '#774411', '#ee3333', '#999999', '#44bb44','#dad0d0','#999393','#c90076','#ff7d00','#5cdaff']
cmap = ListedColormap(mat_colors)


fig, axs = plt.subplots()


hauteur = 160
largeur = 320

deplacement = 0
deplacement2 = 0
zoom = 0


#================================================
#       Définition des matrices de positions
#================================================
# Matrice des positions
position_sand = []
position_water = []
position_wood = []
position_rock = []
position_smoke = []
position_salt = []
position_fire = []
position_acid = []
position_thunder = []




# Matrice pour les direction g/d de l'eau et l'acide
Water_direction = []
Acid_direction = []
Thunder_direction = ['right']

deplacement_enemi=[]
deplacement_fly_enemi = []
deplacement_big_enemi = []


# Matrice pour la création de terrain
video = []




pixels = np.zeros((hauteur,largeur), dtype=int)


cax = axs.matshow(pixels,cmap=cmap)
h_pixmap = axs.matshow(pixels, cmap=cmap, vmin=0, vmax=len(mat_colors)-1)
axs.set(xlim =( 0+deplacement2, 40+deplacement2+zoom), ylim =(160+deplacement+zoom,120+deplacement))
#axs.set(xlim =( 110+deplacement2, 150+deplacement2+zoom), ylim =(160+deplacement+zoom,120+deplacement))




    
    
    
    

    
   
            
   
            
        
    
    
    
    
    
    


#Initialisation de variable pour la boucle infinie
temps =0
deplacement_player = 0
deplacement_player2 = 0

   
 
    
 
    
 
#============================================
#       Définition de l'update
#============================================
def update_uni(n=0):
    h_pixmap.set_data(pixels)
    #axs.set(xlim =( 0+deplacement2, 40+deplacement2+zoom), ylim =(160+deplacement+zoom,120+deplacement))
    axs.set(xlim =( 110+deplacement2, 150+deplacement2+zoom), ylim =(160+deplacement+zoom,120+deplacement))

    




#============================================
#       Définition des Keys
#============================================

# Définition des clicks
#----------------------
def on_click(event):       
    if (event.button == MouseButton.LEFT):
        Sand(event.xdata,event.ydata,pixels,position_sand)
    if (event.button == MouseButton.RIGHT):    
        Water(event.xdata,event.ydata)
    
# Définition des key
#----------------------
def on_key(event): 
    # Eléments
    if event.key == u'a':
        Wood(event.xdata,event.ydata,pixels,position_wood)
    if event.key == u'z':
        Smoke(event.xdata,event.ydata,pixels,position_smoke)
    if event.key == u'e':
        Salt(event.xdata,event.ydata,pixels,position_salt)
    if event.key == u'r':
        Fire(event.xdata,event.ydata,pixels,position_fire,temps)
    if event.key == u'y':
        Acid(event.xdata,event.ydata,pixels,position_acid,Acid_direction)
    if event.key == u't':
        Rock(event.xdata,event.ydata,pixels,position_rock)
    if event.key == u'w':
        Sand(event.xdata,event.ydata,pixels,position_sand)
    if event.key == u'x':
        Water(event.xdata,event.ydata,pixels,position_water,Water_direction)
        
    
        
            
    if event.key == u'b':
        Erase(event.xdata,event.ydata,pixels)
   
    #Zoom
    if event.key == u'g':
        global zoom
        zoom += 5
    if event.key == u'h':
        zoom -= 5
        
     
    # Déplacement de la fenêtre et du player
    if event.key == u'up':
        global deplacement
        if 120+deplacement > 0:
            deplacement -= 1
    if event.key == u'down':
        if 160+deplacement+zoom < hauteur:
            deplacement += 1        
    if event.key == u'right':
        global deplacement2,deplacement_player
        
        Thunder_direction.clear()
        Thunder_direction.append('right')
        #Thunder_direction[0] = 'right'
        
        
        deplacement2 += 1
            
        
        
                
                
    
    
    if event.key == u'left':
        # Déplacement de la fenetre vers la gauche si pas player
        Thunder_direction.clear()
        Thunder_direction.append('left')
        #Thunder_direction[0] = 'left'
        
        
        deplacement2 -= 1
            
        
        
            
            
      
    
                
    
   
            
            
  


# Lien entre on_click et on_key à la souris et au clavier
#---------------------------------------------------------
fig.canvas.mpl_connect('button_press_event', on_click) #☺lie la fct on_click à la souris
cid = fig.canvas.mpl_connect('key_press_event', on_key) #☺lie la fct on_key au clavier
 








#============================================
#          Boucle infinie du jeu
#============================================

while plt.fignum_exists(fig.number):
    
    temps+=1
   
    condition_sand(position_sand,position_water,pixels,hauteur,largeur)
    condition_water(position_water,pixels,Water_direction,hauteur,largeur)
    condition_smoke(position_smoke,position_water, position_sand,position_salt, pixels,hauteur,largeur)
    condition_salt(position_salt,position_water,pixels,hauteur,largeur)
    condition_fire(position_fire,position_wood,position_water,Water_direction,position_smoke,pixels,temps,hauteur,largeur)
    condition_acid(position_acid,position_water, position_wood, position_sand,position_salt, pixels,Acid_direction,hauteur,largeur)
    
     
    
        
                
    update_uni()
    plt.draw(), plt.pause(0.1)
    
    
        
            




plt.show()

keyboard.unhook_all()









