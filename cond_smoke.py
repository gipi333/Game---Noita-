def condition_smoke(position_smoke,position_water, position_sand,position_salt, pixels,hauteur,largeur):
    
    position = [position_water, position_sand,position_salt]
    pixel_color = [3, 1, 8]
    
    
    #      La fumée monte
    #----------------------------------------------
    for k in range(len(position_smoke)):          
        i = position_smoke[k][0]
        j = position_smoke[k][1]
           
            
        if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
            if pixels[i-1,j] == 0:
                pixels[i-1,j] = 6
                pixels[i,j] = 0
                position_smoke[k][0]-=1
                    
            elif ( pixels[i-1,j-1] == 0):
                pixels[i-1,j-1] = 6
                pixels[i,j] = 0
                position_smoke[k][0]-=1
                position_smoke[k][1]-=1
                
            elif (pixels[i-1,j+1] == 0):
                pixels[i-1,j+1] = 6
                pixels[i,j] = 0
                position_smoke[k][0]-=1
                position_smoke[k][1]+=1 
                    
                    
                
                        
                        
    #  Interaction entre la fumée et sable/eau/sel
    #--------------------------------------------------                 
    for o in range(len(position)): 
        for k in range(len(position_smoke)):
            i = position_smoke[k][0]
            j = position_smoke[k][1]
            
            if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
                if pixels[i-1,j] == pixel_color[o]:
                    pixels[i-1,j] = 6
                    pixels[i,j] = pixel_color[o]
                    position_smoke[k][0]-=1
                    index = position[o].index([i-1,j])
                    position[o][index][0]+=1
                    
                elif ( pixels[i-1,j-1] == pixel_color[o]):
                    pixels[i-1,j-1] = 6
                    pixels[i,j] = pixel_color[o]
                    position_smoke[k][0]-=1
                    position_smoke[k][1]-=1
                    index = position[o].index([i-1,j-1])
                    position[o][index][0]+=1
                    position[o][index][1]+=1
                   
                elif (pixels[i-1,j+1] == pixel_color[o]):
                    pixels[i-1,j+1] = 6
                    pixels[i,j] = pixel_color[o]
                    position_smoke[k][0]-=1
                    position_smoke[k][1]+=1 
                    index = position[o].index([i-1,j+1])
                    position[o][index][0]+=1
                    position[o][index][1]-=1
                    
                    
                
