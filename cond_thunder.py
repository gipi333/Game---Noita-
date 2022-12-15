def condition_thunder( position_player, pixels, position_thunder,Thunder_direction,temps,position_fire,position_wood):
    
        
    if len(Thunder_direction)>0:
        
        
        
        
        
        
        if Thunder_direction[0] == 'right' and len(position_thunder) >0  :
            ident = 1
            while pixels[position_thunder[0][0],position_thunder[0][1]+ident] ==0:
                
                
                #pixels[position_player[0][0],position_player[0][1]+ident] = 14
                position_thunder.append([position_player[0][0],position_player[0][1]+ident,temps])
                ident += 1 
            
            # Pour le dernier pixel
            if pixels[position_thunder[-1][0],position_thunder[-1][1]+1] == 0:
                #pixels[position_thunder[-1][0],position_thunder[-1][1]+1] = 14
                position_thunder.append([position_thunder[-1][0],position_thunder[-1][1]+1,temps])
                
            for k in position_thunder:               
                pixels[k[0],k[1]] = 14
                
                
        if Thunder_direction[0] == 'left' and len(position_thunder) >0  :
            ident = -1
            while pixels[position_thunder[0][0],position_thunder[0][1]+ident] ==0:
                pixels[position_player[0][0],position_player[0][1]+ident] = 14
                position_thunder.append([position_player[0][0],position_player[0][1]+ident,temps])
                ident -= 1 
            
            # Pour le dernier pixel
            if pixels[position_thunder[-1][0],position_thunder[-1][1]-1] == 0:
                pixels[position_thunder[-1][0],position_thunder[-1][1]-1] = 14
                position_thunder.append([position_thunder[-1][0],position_thunder[-1][1]-1,temps])
                
                
      
                
      
        
    # Thunder desappear after some time
    if len(position_thunder)>0:
        if (temps == position_thunder[0][2]+10 or temps > position_thunder[0][2]+10):
           
            for k in position_thunder:               
                pixels[k[0],k[1]] = 0
            position_thunder.clear()
            
            
            
    # Thunder make the wood burn
    if len(position_thunder)>0:
        if (pixels[position_thunder[-1][0],position_thunder[-1][1]-1] == 4 ):
            
            pixels[position_thunder[-1][0],position_thunder[-1][1]-1] == 5
            position_fire.append([position_thunder[-1][0],position_thunder[-1][1]-1,temps+1])             
            
            
        if (pixels[position_thunder[-1][0],position_thunder[-1][1]+1] == 4):
            
            pixels[position_thunder[-1][0],position_thunder[-1][1]+1] == 5
            position_fire.append([position_thunder[-1][0],position_thunder[-1][1]+1,temps+1])                     
        
        
      
                    
                
                
                
    
    
    
    


