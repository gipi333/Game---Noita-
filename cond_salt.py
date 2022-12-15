
def condition_salt(position_salt,position_water,pixels,hauteur,largeur):

    for k in range(len(position_salt)):
        i = position_salt[k][0]
        j = position_salt[k][1]
            
        if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
                
                
                
            #        Le sel tombe dans le vide
            #----------------------------------------------
                
            if pixels[i+1,j] == 0:
                pixels[i+1,j] = 8
                pixels[i,j] = 0
                position_salt[k][0]+=1                 
            elif ( pixels[i+1,j-1] == 0 ):
                pixels[i+1,j-1] = 8
                pixels[i,j] = 0
                position_salt[k][0]+=1
                position_salt[k][1]-=1            
            elif ( pixels[i+1,j+1] == 0):
                pixels[i+1,j+1] = 8
                pixels[i,j] = 0
                position_salt[k][0]+=1
                position_salt[k][1]+=1
                    
    
    
    
    
    
    
    for k in range(len(position_salt)):
        i = position_salt[k][0]
        j = position_salt[k][1]
            
        if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):                    
                    
                    
            #        Le sel remonte dans l'eau
            #----------------------------------------------
                
            if (pixels[i-1,j] == 3):
                # Changement de couleur des pixel
                pixels[i-1,j] = 8
                pixels[i,j] = 3
                # Changement de position dans les listes positions water et salt
                # Couleur pixel update mais pas leir position --> uptdate position
                position_salt[k][0]-=1
                index = position_water.index([i-1,j])
                position_water[index][0]+=1
                    
                    
            elif ( pixels[i-1,j-1] == 3):
                # Changement de couleur des pixel
                pixels[i-1,j-1] = 8
                pixels[i,j] = 3
                # Changement de position dans les listes positions water et salt
                position_salt[k][0]-=1
                position_salt[k][1]-=1 
                index = position_water.index([i-1,j-1])
                position_water[index][0]+=1
                position_water[index][1]+=1
                    
                    
            elif ( pixels[i-1,j+1] == 3):
                # Changement de couleur des pixel
                pixels[i-1,j+1] = 8
                pixels[i,j] = 3
                # Changement de position dans les listes positions water et salt
                position_salt[k][0]-=1
                position_salt[k][1]+=1 
                index = position_water.index([i-1,j+1])
                position_water[index][0]+=1
                position_water[index][1]-=1
                    
                    
               
                
                    
                