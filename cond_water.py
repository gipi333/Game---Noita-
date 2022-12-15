def condition_water(position_water,pixels,Water_direction,hauteur,largeur):
    
    
    for k in range(len(position_water)):
        
        
        i = position_water[k][0]
        j = position_water[k][1]
        
      
        
        
        
        if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
            if pixels[i+1,j] == 0:
                pixels[i+1,j] = 3
                pixels[i,j] = 0
                position_water[k][0]+=1
                Water_direction[k] = 'left'
                
            elif ( pixels[i+1,j-1] == 0):
                pixels[i+1,j-1] = 3
                pixels[i,j] = 0
                position_water[k][0]+=1
                position_water[k][1]-=1
                Water_direction[k] = 'left'
               
            elif (pixels[i+1,j+1] == 0):
                pixels[i+1,j+1] = 3
                pixels[i,j] = 0
                position_water[k][0]+=1
                position_water[k][1]+=1 
                Water_direction[k] = 'left'
                
                
            elif (Water_direction[k] == 'left'): 
                if pixels[i,j-1] == 0 :
                    pixels[i,j-1] = 3
                    pixels[i,j] = 0
                    position_water[k][1]-=1
                    Water_direction[k] = 'left'
                else:
                    Water_direction[k] = 'right'
            
                    
            elif (Water_direction[k] == 'right'):
                if (pixels[i,j+1] == 0):
                    pixels[i,j+1] = 3
                    pixels[i,j] = 0
                    position_water[k][1]+=1
                    Water_direction[k] = 'right'
                else:
                    Water_direction[k] = 'left'
                    
                    
                    
                    
            
                    
                    
            