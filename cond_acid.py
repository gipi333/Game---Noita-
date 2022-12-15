def condition_acid(position_acid,position_water, position_wood, position_sand,position_salt, pixels,Acid_direction,hauteur,largeur):
    
 
    position = [position_water, position_wood, position_sand,position_salt]
    pixel_color = [3, 4, 1, 8]
                    
                    
                

    for k in range(len(position_acid)):
        
        
        i = position_acid[k][0]
        j = position_acid[k][1]
        
      
        
        
        
        if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
            if pixels[i+1,j] == 0:
                pixels[i+1,j] = 7
                pixels[i,j] = 0
                position_acid[k][0]+=1
                Acid_direction[k] = 'left'
                
            elif ( pixels[i+1,j-1] == 0):
                pixels[i+1,j-1] = 7
                pixels[i,j] = 0
                position_acid[k][0]+=1
                position_acid[k][1]-=1
                Acid_direction[k] = 'left'
               
            elif (pixels[i+1,j+1] == 0):
                pixels[i+1,j+1] = 7
                pixels[i,j] = 0
                position_acid[k][0]+=1
                position_acid[k][1]+=1 
                Acid_direction[k] = 'right'
                
                
            elif (Acid_direction[k] == 'left'): 
                if pixels[i,j-1] == 0 :
                    pixels[i,j-1] = 7
                    pixels[i,j] = 0
                    position_acid[k][1]-=1
                    Acid_direction[k] = 'left'
                else:
                    Acid_direction[k] = 'right'
            
                    
            elif (Acid_direction[k] == 'right'):
                if (pixels[i,j+1] == 0):
                    pixels[i,j+1] = 7
                    pixels[i,j] = 0
                    position_acid[k][1]+=1
                    Acid_direction[k] = 'right'
                else:
                    Acid_direction[k] = 'left'




            
    for o in range(len(position)):     
        for k in position_acid:
            i = k[0]
            j = k[1]
            if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
                    
                if pixels[i+1,j] == pixel_color[o]:
                    pixels[i+1,j] = 0
                    position[o].remove([i+1,j])
               
                if pixels[i-1,j] == pixel_color[o]:
                    pixels[i-1,j] = 0
                    position[o].remove([i-1,j])
                     
                if pixels[i,j+1] == pixel_color[o]:
                    pixels[i,j+1] = 0
                    position[o].remove([i,j+1])
            
                if pixels[i,j-1] == pixel_color[o]:
                    pixels[i,j-1] = 0
                    position[o].remove([i,j-1])
                
                
                
                
      
   
    
   
    
   
    
   
    
   
    
    
                    
               
            
           
            
                    
            
            
            
    
        
            
            
    
        
                    
                    
               

