from ursina import *
import math

def update():
    global t
    t = t + 0.02
    angle = math.pi*40/180

    radius_1 = 2
    mercury.x = math.cos(t)*radius_1
    mercury.z = math.sin(t)*radius_1
    
    radius_2 = 5.2
    venus.x = math.cos(t+angle)*radius_2
    venus.z = math.sin(t+angle)*radius_2

    radius_3 = 3.6
    earth.x = math.cos(t+angle*2)*radius_3
    earth.z = math.sin(t+angle*2)*radius_3

    radius_4 = 7.6
    mars.x = math.cos(t+angle*3)*radius_4
    mars.z = math.sin(t+angle*3)*radius_4

    radius_5 = 2.8
    jupiter.x = math.cos(t+angle*4)*radius_5
    jupiter.z = math.sin(t+angle*4)*radius_5

    radius_6 = 6
    saturn.x = math.cos(t+angle*5)*radius_6
    saturn.z = math.sin(t+angle*5)*radius_6

    radius_7 = 8
    uranus.x = math.cos(t+angle*6)*radius_7
    uranus.z = math.sin(t+angle*6)*radius_7

    radius_8 = 4.4
    neptune.x = math.cos(t+angle*7)*radius_8
    neptune.z = math.sin(t+angle*7)*radius_8

	#rotate around the axis 
    sun.rotation_y += time.dt*20
     

class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            texture = 'textures/star.jpg',
            parent = scene,
            scale = 150,
            double_sided = True
		)
app = Ursina()
bg = Sky()
EditorCamera()

# load image
sun = Entity(model= "sphere",  scale=3, texture = "textures/sun.jpg")
mercury = Entity(model='obj/Mercury 1K.obj',scale=1, texture = "textures/mercury.png")
venus = Entity(model='sphere', scale=0.6, texture = 'textures/venus.jpg')
earth = Entity(model='sphere',  scale=0.8, texture = "textures/earth.jpg")
mars = Entity(model='obj/Mars 2K.obj', scale=0.2, texture = 'textures/mars.png')
jupiter = Entity(model='sphere',scale=1.2, texture = 'textures/jupiter.jpg')
saturn = Entity(model= 'sphere', scale=1, texture = 'textures/saturn.jpg')
uranus = Entity(model='sphere', scale=1, texture = 'textures/uranus.jpg')
neptune = Entity(model='sphere',  scale=1, texture = 'textures/neptun.jpg')


t = -math.pi

app.run()