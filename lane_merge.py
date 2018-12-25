from visual import *
import math
import time

#creates the display for simulation
lenroad = 3000
scene = display(title = "Lane Merge Simulation", width = 1280, height = 768)
road= box (pos=(0,0,0), length=lenroad, height=200, width=0.5, color=color.blue)
car_len = 7.5
deltat = 0.005
#ball = sphere(pos = (0,0,0), radius = 10, color = color.white)
acceleration_0_x = 0
acceleration_0_y = 0
acceleration_1_x = 0
acceleration_1_y = 0
algorithm_enable = True
d = -30
v_x = 0
v_y = 0
theta = -10
lane_0_v = 20
lane_1_v = 20
Ncars = 5
new_velo = 0
dis_law = 35
x_val = 0
speed_law = 120
diam = 2*car_len
lane_0_car = []
lane_1_car = []


#returns true or false depending on if collision is detected or not
def collision(lane_1_car,lane_0_car,i):
    if math.sqrt(((lane_0_car[i].pos.x - (lane_1_car[i].pos.x))**2) + (lane_0_car[i].pos.y - lane_1_car[i].pos.y)**2) <= (lane_0_car[i].radius * 2):
        return True
    elif math.sqrt(((lane_0_car[i].pos.x - (lane_1_car[i-1].pos.x))**2) + (lane_0_car[i].pos.y - lane_1_car[i-1].pos.y)**2) <= (lane_0_car[i].radius * 2):
        return True
    elif math.sqrt(((lane_0_car[i-1].pos.x - (lane_1_car[i-1].pos.x))**2) + (lane_0_car[i-1].pos.y - lane_1_car[i-1].pos.y)**2) <= (lane_0_car[i].radius * 2):
        return True
    elif math.sqrt(((lane_0_car[i-1].pos.x - (lane_1_car[i].pos.x))**2) + (lane_0_car[i].pos.y - lane_1_car[i].pos.y)**2) <= (lane_0_car[i].radius * 2):
        return True
    elif math.sqrt(((lane_0_car[i].pos.x - (lane_0_car[i-1].pos.x))**2) + (lane_0_car[i].pos.y - lane_0_car[i-1].pos.y)**2) <= (lane_0_car[i].radius * 2):
        return True
    elif math.sqrt(((lane_1_car[i].pos.x - (lane_1_car[i-1].pos.x))**2) + (lane_1_car[i].pos.y - lane_1_car[i-1].pos.y)**2) <= (lane_1_car[i].radius * 2):
        return True
    else:
        return False
    
#measures distance between respective cars within their lanes
def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)**2
    sq2 = (yi-yii)**2
    return math.sqrt(sq1 + sq2)


def one_car_d(lane_0_car,lane_1_car,i):
    if distance(lane_0_car[i].pos.x,lane_0_car[i+1].pos.x,lane_0_car[i].pos.y,lane_0_car[i+1].pos.y) == lane_0_car[i].radius:
        return True
    elif distance(lane_1_car[i].pos.x,lane_1_car[i+1].pos.x,lane_1_car[i].pos.y,lane_1_car[i+1].pos.y) == lane_0_car[i].radius:
        return True
    if distance(lane_0_car[i].pos.x,lane_1_car[i].pos.x,lane_0_car[i].pos.y,lane_1_car[i].pos.y) == lane_0_car[i].radius:
        return True
    elif distance(lane_0_car[i].pos.x,lane_1_car[i+1].pos.x,lane_0_car[i].pos.y,lane_1_car[i+1].pos.y) == lane_0_car[i].radius:
        return True
    elif distance(lane_0_car[i].pos.x,lane_1_car[i-1].pos.x,lane_0_car[i].pos.y,lane_1_car[i-1].pos.y) == lane_0_car[i].radius:
        return True

#checks velocity of the car in each lane and returns true or false based on speed respective to the law
def speed_check(lane_0_car,i):
    if math.sqrt((lane_0_car[i].velocity.x) ** 2 + (lane_0_car[i].velocity.y) ** 2 + (lane_0_car[i].velocity.z) ** 2) > speed_law:
        return True
    else:
        return False

#checks distance between this car and the one in front and returns true or false based on if the distance is within the law or not
def front_dis_check_one_lane(lane_0_car,i):
    if distance(lane_0_car[i].pos.x,lane_0_car[i-1].pos.x,lane_0_car[i].pos.y,lane_0_car[i-1].pos.y) < dis_law:
        return True
    else:
        return False

#checks distance between car car and the one in the back and returns true or false based on if the distance is within the law or not
def back_dis_check_01_lane(lane_0_car,lane_1_car,i):
    if distance(lane_0_car[i].pos.x,lane_1_car[i+1].pos.x,lane_0_car[i].pos.y,lane_1_car[i+1].pos.y) < dis_law:
        return True
    else:
        return False

def back_dis_check_10_lane(lane_0_car,lane_1_car,i):
    if distance(lane_0_car[i].pos.x,lane_1_car[i].pos.x,lane_0_car[i].pos.y,lane_1_car[i].pos.y) < dis_law:
        return True
    else:
        return False
    
#checks distance between each car post-lane merge and returns true or false based on wether it is within the law or not
def dis_check_comb_lane(lane_0_car,lane_1_car,i):
    if distance(lane_0_car[i].pos.x,lane_1_car[i].pos.x,lane_0_car[i].pos.y,lane_1_car[i].pos.y) < dis_law:
        return True
    #elif distance(lane_i_car[i].pos.x,lane_j_car[i-1].pos.x,lane_i_car[i].pos.y,lane_j_car[i-1].pos.y):
    #    return True
    #elif distance(lane_i_car[i-1].pos.x,lane_j_car[i].pos.x,lane_i_car[i-1].pos.y,lane_j_car[i].pos.y):
#        return True
#    elif distance(lane_i_car[i-1].pos.x,lane_j_car[i-1].pos.x,lane_i_car[i-1].pos.y,lane_j_car[i].pos.y):
#        return True
    else:
        return False
#finds the x coordinate of the vector on the second turn to straighten back out
def x_coord(x1,y1,y2,theta):
    x2 = (y1-y2)/(math.tan(math.pi*theta/180)) + x1
    return x2
#finds out the amount of acceleration needed to successfully merge without having an accident or a traffic jam.  
def get_acceleration(distance, car_len):
    if algorithm_enable == True and (distance - car_len)/2 < dis_law:
        acceleration = 2*(dis_law-(distance - car_len)/2)*0.5
    else:
        acceleration = 0
    return acceleration


 #initializes each of the lanes of cars
for i in range(Ncars):
    lane_0_car += [sphere (pos=(-(lenroad/2),50,5), radius = car_len,color = color.yellow)]
    lane_0_car[i].velocity = vector(lane_0_v,0,0)
    lane_0_car[i].pos.x = d * i - (lenroad/4)
    lane_1_car += [sphere (pos=(-(lenroad/2),-20,5), radius = car_len,color = color.green)]
    lane_1_car[i].velocity = vector(lane_1_v,0,0)
    lane_1_car[i].pos.x = d * i - (lenroad/4) - d/3

    #Finds the position at which the first lane merges into the second
    
x_val = x_coord(-300,50,-20,-theta)

#main program checks for certain conditions and advances the position of the cars
while 1:
    rate(1000)
    for i in range(Ncars):
        
        #Figures out when road turns and turns to that angle and maintains the same magnitude of velocity
        
        if lane_0_car[i].pos.x > -300 and lane_0_car[i].pos.x < x_val:
            v_x = lane_0_v * (math.cos((math.pi*theta)/180))
            v_y = lane_0_v * (math.sin((math.pi*theta)/180))
            lane_0_car[i].velocity = vector(v_x,v_y,0)

            #Figures out when road becomes straight again and reacts, it also maintains same magnitude of velocity
            
        elif lane_0_car[i].pos.x >= x_val and lane_0_car[i].color == color.yellow:
            v_x = lane_0_v * (math.cos(0)) + acceleration_0_x * deltat
            v_y = lane_0_v * (math.sin(0)) + acceleration_0_y * deltat
            lane_0_car[i].velocity = vector(v_x,v_y,0)

        if lane_0_car[i].pos.x < -300:
            if algorithm_enable == True and front_dis_check_one_lane(lane_0_car,i) == True:
                acceleration_0_x = 1
                v_x = v_x + (-1 * acceleration_0_x  * deltat)
                v_y = v_y + (-1 * acceleration_0_y  * deltat)
                if v_x < 0:
                    v_x = 0
                if v_y < 0:
                    v_y = 0;
                lane_0_car[i].velocity = vector(v_x,v_y,0)
            else:
                lane_0_car[i].velocity = vector(lane_0_v,0,0)
                acceleration_0_x = 0
                acceleration_0_y = 0

        if lane_1_car[i].pos.x < -300:
            if algorithm_enable == True and front_dis_check_one_lane(lane_1_car,i) == True:
                acceleration_1_x = 1
                v_x = v_x + (-1 * acceleration_1_x  * deltat)
                v_y = v_y + (-1 * acceleration_1_y  * deltat)
                if v_x < 0:
                    v_x = 0
                if v_y < 0:
                    v_y = 0;
                lane_1_car[i].velocity = vector(v_x,v_y,0)
            else:
                lane_1_car[i].velocity = vector(lane_0_v,0,0)
                acceleration_1_x = 0
                acceleration_1_y = 0
            

        if collision(lane_0_car,lane_1_car,i) == True:
            lane_0_car[i].color = color.red
            lane_1_car[i].color = color.red
        if lane_0_car[i].color == color.red:
            lane_0_car[i].velocity = vector(0,0,0)
        if lane_1_car[i].color == color.red:
            lane_1_car[i].velocity = vector(0,0,0)
            

        #print x_val
        if lane_0_car[i].pos.x >= x_val:
            if i < Ncars-1 and back_dis_check_01_lane(lane_0_car,lane_1_car,i) == True:
                distance_0 = distance(lane_0_car[i].pos.x,lane_1_car[i+1].pos.x,lane_0_car[i].pos.y,lane_1_car[i+1].pos.y)
                acceleration_0_x = get_acceleration(distance_0,car_len)
            else:
                acceleration_0_x = 0
                #print "stopping to accelerate 0"
            lane_0_car[i].color = color.green
            #print lane_0_car[0].velocity.x
        else:
            acceleration_0_x = 0
            
        lane_0_car[i].velocity.x += acceleration_0_x * deltat
        lane_0_car[i].velocity.y += acceleration_0_y * deltat
        lane_0_car[i].pos.x += (lane_0_car[i].velocity.x * deltat) + 1/2 * (acceleration_0_x + (deltat ** 2))
        lane_0_car[i].pos.y += (lane_0_car[i].velocity.y * deltat) + 1/2 * (acceleration_0_y + (deltat ** 2))
        
        
        if lane_1_car[i].pos.x >= x_val:
            if i < Ncars and back_dis_check_10_lane(lane_0_car,lane_1_car,i) == True:
                distance_1 = distance(lane_0_car[i].pos.x,lane_1_car[i].pos.x,lane_0_car[i].pos.y,lane_1_car[i].pos.y)
                acceleration_1_x = get_acceleration(distance_1,car_len)
            else:
                acceleration_1_x = 0
                #print "stopping to accelerate 1"
            #print acceleration_1_x
            #print lane_1_car[0].velocity.x
        else:
            acceleration_1_x = 0
            
        lane_1_car[i].velocity.x += acceleration_1_x * deltat
        lane_1_car[i].velocity.y += acceleration_1_y * deltat
        lane_1_car[i].pos.x += (lane_1_car[i].velocity.x * deltat) + 1/2 * (acceleration_1_x + (deltat ** 2))
        lane_1_car[i].pos.y += (lane_1_car[i].velocity.y * deltat) + 1/2 * (acceleration_1_y + (deltat ** 2))
        
            
        if lane_0_car[i].color == color.red:
            lane_0_car[i].velocity = vector(0,0,0)
        if lane_1_car[i].color == color.red:
            lane_1_car[i].velocity = vector(0,0,0)
        if lane_0_car[i].pos.x > (lenroad/2) and lane_1_car[i].pos.x > (lenroad/2):
            lane_0_car[i].velocity.x = 0
            lane_1_car[i].velocity.x = 0
            break

            
            
 
 
