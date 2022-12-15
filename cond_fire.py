
def condition_fire(position_fire,position_wood,position_water,Water_direction,position_smoke,pixels,temps,hauteur,largeur):
    
 

    for k in range(len(position_fire)):
            i = position_fire[k][0]
            j = position_fire[k][1]
            l = position_fire[k][2]
            
            
            if (i<(hauteur-1) and i>0 and j<(largeur-1) and j>0):
                
                #      Le feu éjecte de la fumée
                #----------------------------------------------
                if pixels[i-1,j] == 0:
                    pixels[i-1,j] = 6
                    position_smoke.append([i-1,j])  
                    
                    
                    
                #      Le feu se propage dans le bois
                #----------------------------------------------
                if pixels[i-1,j] == 4:
                    pixels[i-1,j] = 5
                    position_fire.append([i-1,j,temps+1]) #marche pas qd on met juste temps pq?? rapport ac 2 prem pixel
                    position_wood.remove([i-1,j])
                                    
                if pixels[i+1,j] == 4:
                    pixels[i+1,j] = 5
                    position_fire.append([i+1,j,temps+1]) 
                    position_wood.remove([i+1,j])
                    
                if pixels[i,j-1] == 4:
                    pixels[i,j-1] = 5
                    position_fire.append([i,j-1,temps]) 
                    position_wood.remove([i,j-1])
                
                if pixels[i,j+1] == 4:
                    pixels[i,j+1] = 5
                    position_fire.append([i,j+1,temps]) 
                    position_wood.remove([i,j+1])
                    
                    
                    
                
    #      Le feu disparait dans l'eau
    #----------------------------------------------           
 
    for k in position_fire:
        i = k[0]
        j = k[1]
        l = k[2]
                
        if pixels[i-1,j] == 3:
            pixels[i-1,j] = 0
            pixels[i,j] = 0
            index = position_water.index([i-1,j])
            del Water_direction[index]
            position_water.remove([i-1,j])           
            position_fire.remove([i,j,l])
   
                      
        elif pixels[i+1,j] == 3:
            pixels[i+1,j] = 0
            pixels[i,j] = 0
            index = position_water.index([i+1,j])
            del Water_direction[index]
            position_water.remove([i+1,j])           
            position_fire.remove([i,j,l])
                     
    
                        
        elif pixels[i,j-1] == 3:
            pixels[i,j-1] = 0
            pixels[i,j] = 0
            index = position_water.index([i,j-1])
            del Water_direction[index]
            position_water.remove([i,j-1])        
            position_fire.remove([i,j,l])
            
   
            
        elif pixels[i,j+1] == 3:
            pixels[i,j+1] = 0
            pixels[i,j] = 0
            index = position_water.index([i,j+1])
            del Water_direction[index]
            position_water.remove([i,j+1])
            position_fire.remove([i,j,l])
            
   
    
   
    
   
    
   
    
   
    
   
    
    #      Le feu se meurt après 10 tours
    #----------------------------------------------
    for k in position_fire:
            i = k[0]
            j = k[1]
            l = k[2]
            
            
            if (temps == l+10 or temps > l+10):
                pixels[i,j] = 0
                position_fire.remove(k)
                    
                
                    
                    
               
            
           
            
                    
            
            
            
    
        
            
            
    
        
                    
                    
               