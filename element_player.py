#================================================
#       Définition des différents éléments
#================================================

def Sand(col,lign,pixels,position_sand):
    pixels[int(lign),int(col)] = 1
    pixels[int(lign),int(col)+2] = 1
    pixels[int(lign),int(col)-2] = 1
    pixels[int(lign)+2,int(col)] = 1
    pixels[int(lign)-2,int(col)] = 1
    position_sand.append([int(lign),int(col)+2])
    position_sand.append([int(lign),int(col)-2])
    position_sand.append([int(lign)+2,int(col)])
    position_sand.append([int(lign)-2,int(col)])
    position_sand.append([int(lign),int(col)])
    
def Water(col,lign,pixels,position_water,Water_direction):
    pixels[int(lign),int(col)] = 3
    position_water.append([int(lign),int(col)])
    Water_direction.append(['left'])

def Wood(col,lign,pixels,position_wood):
    pixels[int(lign),int(col)] = 4
    pixels[int(lign),int(col)+1] = 4
    pixels[int(lign),int(col)-1] = 4
    pixels[int(lign)+1,int(col)] = 4
    pixels[int(lign)-1,int(col)] = 4
    pixels[int(lign)+1,int(col)+1] = 4
    pixels[int(lign)-1,int(col)-1] = 4
    pixels[int(lign)+1,int(col)-1] = 4
    pixels[int(lign)-1,int(col)+1] = 4
    position_wood.append([int(lign),int(col)+1])
    position_wood.append([int(lign),int(col)-1])
    position_wood.append([int(lign)+1,int(col)+1])
    position_wood.append([int(lign)-1,int(col)-1])
    position_wood.append([int(lign)+1,int(col)-1])
    position_wood.append([int(lign)-1,int(col)+1])
    position_wood.append([int(lign)+1,int(col)])
    position_wood.append([int(lign)-1,int(col)])
    position_wood.append([int(lign),int(col)])
      
def Rock(col,lign,pixels,position_rock):
    pixels[int(lign),int(col)] = 9
    pixels[int(lign),int(col)+1] = 9
    pixels[int(lign),int(col)-1] = 9
    pixels[int(lign)+1,int(col)] = 9
    pixels[int(lign)-1,int(col)] = 9
    pixels[int(lign)+1,int(col)+1] = 9
    pixels[int(lign)-1,int(col)-1] = 9
    pixels[int(lign)+1,int(col)-1] = 9
    pixels[int(lign)-1,int(col)+1] = 9
    position_rock.append([int(lign),int(col)+1])
    position_rock.append([int(lign),int(col)-1])
    position_rock.append([int(lign)+1,int(col)+1])
    position_rock.append([int(lign)-1,int(col)-1])
    position_rock.append([int(lign)+1,int(col)-1])
    position_rock.append([int(lign)-1,int(col)+1])
    position_rock.append([int(lign)+1,int(col)])
    position_rock.append([int(lign)-1,int(col)])
    position_rock.append([int(lign),int(col)])
    
def Smoke(col,lign,pixels,position_smoke):
    pixels[int(lign),int(col)] = 6
    position_smoke.append([int(lign),int(col)]) 
   
def Salt(col,lign,pixels,position_salt):
    pixels[int(lign),int(col)] = 8
    position_salt.append([int(lign),int(col)])    
    
def Fire(col,lign,pixels,position_fire,temps):
    pixels[int(lign),int(col)] = 5
    position_fire.append([int(lign),int(col),temps])
    
def Acid(col,lign,pixels,position_acid,Acid_direction):
    pixels[int(lign),int(col)] = 7
    position_acid.append([int(lign),int(col)])
    Acid_direction.append(['left'])

def Player(col,lign,pixels,position_player):
    pixels[int(lign),int(col)] = 10
    pixels[int(lign)+1,int(col)] = 10
    pixels[int(lign)+2,int(col)] = 10
    position_player.append([int(lign),int(col)])
    position_player.append([int(lign)+1,int(col)])
    position_player.append([int(lign)+2,int(col)])
       
def Erase(col,lign,pixels):
    pixels[int(lign),int(col)] = 0

def Thunder(pixels,position_thunder,Thunder_direction, position_player,temps):
    if (Thunder_direction[0] == 'right' and pixels[position_player[0][0],position_player[0][1]+1] ==0):
        pixels[position_player[0][0],position_player[0][1]+1] = 14
        position_thunder.append([position_player[0][0],position_player[0][1]+1,temps+1])
    elif (Thunder_direction[0] == 'left' and pixels[position_player[0][0],position_player[0][1]-1] ==0):
        pixels[position_player[0][0],position_player[0][1]-1] = 14
        position_thunder.append([position_player[0][0],position_player[0][1]-1,temps+1])
    else :
        pass
    
    
    
    
    