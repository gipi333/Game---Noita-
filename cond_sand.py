
def condition_sand(position_sand,position_water,pixels,hauteur,largeur):

    for k in range(len(position_sand)):
            i = position_sand[k][0]
            j = position_sand[k][1]
            
            if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
                if pixels[i+1,j] == 0:
                    pixels[i+1,j] = 1
                    pixels[i,j] = 0
                    position_sand[k][0]+=1  
                    
                    
                elif ( pixels[i+1,j-1] == 0 ):
                    pixels[i+1,j-1] = 1
                    pixels[i,j] = 0
                    position_sand[k][0]+=1
                    position_sand[k][1]-=1            
                elif ( pixels[i+1,j+1] == 0):
                    pixels[i+1,j+1] = 1
                    pixels[i,j] = 0
                    position_sand[k][0]+=1
                    position_sand[k][1]+=1
                    
                    
                    
                    
                    
                # Le sable coule
                elif (pixels[i+1,j] == 3):
                    pixels[i+1,j] = 1
                    pixels[i,j] = 3
                    position_sand[k][0]+=1
                    index = position_water.index([i+1,j])
                    position_water[index][0]-=1
                    
                    
                elif ( pixels[i+1,j-1] == 3):
                    pixels[i+1,j-1] = 1
                    pixels[i,j] = 3
                    position_sand[k][0]+=1
                    position_sand[k][1]-=1 
                    index = position_water.index([i+1,j-1])
                    position_water[index][0]-=1
                    position_water[index][1]+=1
                    
                    
                elif ( pixels[i+1,j+1] == 3):
                    pixels[i+1,j+1] = 1
                    pixels[i,j] = 3
                    position_sand[k][0]+=1
                    position_sand[k][1]+=1
                    index = position_water.index([i+1,j+1])
                    position_water[index][0]-=1
                    position_water[index][1]-=1