import math
def cy_surface_area(height,radius):
    cy_lat_Sur = 2*(math.pi)*(radius)*(height)
    print("cylindrical lateral surface area :", cy_lat_Sur)
    cy_to_sur = 2*(math.pi)*(radius)*(radius+height)
    print("cylindrical total surface area :", cy_to_sur)

def cy_volume(height,radius):
    cy_volume_1 = (math.pi)*(radius)*2*(height)
    print("cylindrical volume:", cy_volume_1)
    
height = 10;
radius = 20;
cy_surface_area(height,radius)
cy_volume(height,radius)
