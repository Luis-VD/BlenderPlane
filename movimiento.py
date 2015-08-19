from bge import logic, events
import math
cont = logic.getCurrentController()
own = cont.owner
move = cont.actuators['move']
#vars
accel = 9
roll = 0.05
yaw = 0.03
pitch = 0.07
accelfric = 0.5
rollfric = 0.99
yawfric = 0.9
pitchfric = 0.95
keyboard = logic.keyboard
ACTIVE = logic.KX_INPUT_ACTIVE
JUST_RELEASED = logic.KX_INPUT_JUST_RELEASED
euy = own.worldOrientation.to_euler().y
#go forward
move.linV = [move.linV.x,move.linV.y-accel,move.linV.z]
if keyboard.events[events.UPARROWKEY] == ACTIVE:
        move.angV = [move.angV.x-pitch,move.angV.y,move.angV.z]
if keyboard.events[events.DOWNARROWKEY] == ACTIVE:
         move.angV = [move.angV.x+pitch,move.angV.y,move.angV.z]
if keyboard.events[events.ZKEY] == ACTIVE:
        move.angV = [move.angV.x,move.angV.y,move.angV.z+yaw]
        
if keyboard.events[events.XKEY] == ACTIVE:
        move.angV = [move.angV.x,move.angV.y,move.angV.z-yaw]
             
if keyboard.events[events.LEFTARROWKEY] == ACTIVE:
        move.angV = [move.angV.x,move.angV.y+roll,move.angV.z]
        
elif keyboard.events[events.RIGHTARROWKEY] == ACTIVE:
        move.angV = [move.angV.x,move.angV.y-roll,move.angV.z]
  
elif math.fabs(euy) < roll:
    dif = own.worldOrientation.to_euler().y
    move.angV = [move.angV.x,move.angV.y*0.9,move.angV.z]
    
elif math.fabs(euy) > math.pi-roll:
    dif = own.worldOrientation.to_euler().y
    move.angV = [move.angV.x,move.angV.y*0.9,move.angV.z]
      
elif euy > 0 and euy < math.pi/2:
    move.angV = [move.angV.x,move.angV.y-roll/4,move.angV.z]
    
elif euy > math.pi/2:
    move.angV = [move.angV.x,move.angV.y+roll/4,move.angV.z]
    
elif euy < 0 and euy > -math.pi/2:
    move.angV = [move.angV.x,move.angV.y+roll/4,move.angV.z]
    
elif euy < -math.pi/2:
    move.angV = [move.angV.x,move.angV.y-roll/4,move.angV.z]
    
    
#apply roll rotation
rot = own.worldOrientation.to_euler().y
extra = math.sin(rot)/5
move.angV = [move.angV.x-math.fabs(extra/8),move.angV.y,move.angV.z+extra/2]
move.linV = [move.linV.x,move.linV.y*accelfric,move.linV.z]
   
#apply rotations friction
move.angV = [move.angV.x*pitchfric,move.angV.y*rollfric,move.angV.z*yawfric]
own['rotation'] = own.worldOrientation.to_euler().y
#activate motion
cont.activate(move)