import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

pyrosim.Start_SDF("box.sdf")
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box2", pos = [x+i,y+j,z], size = [length,width,height])
            length = length*.9
            width = width*.9
            height = height*.9
            #blocks bounce without the .05 buffer
            z = z+(height)+.03
        x = 0
        y = 0
        z = 0.5
        length = 1
        width = 1
        height = 1
pyrosim.End()

