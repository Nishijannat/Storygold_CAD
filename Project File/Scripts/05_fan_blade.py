import cadquery as cq
import math

base = cq.Workplane("XY").circle(20).circle(5).extrude(2)

r = 17 
hole_r = 1.5 
angles = [0, 90, 180, 270] # angle = 3*(360/blade number)

base_hole = base 
for angle in angles:
    x = r * math.cos(math.radians(angle)) 
    y = r * math.sin(math.radians(angle)) 
    base_hole = base_hole.faces(">Z").workplane().moveTo(x, y).hole(hole_r)

#base_hole = base.faces(">Z").workplane().rarray(17, 4, 5, 1).hole(1.5)

blade1 = cq.Workplane("XY").rect(15,1.2).extrude(1.7).translate((12.5, 0, 1))


solid = base_hole
for i in range(12):
    if i % 3 ==0:
        holed = blade1.faces(">Z").workplane().rarray(17, 2, 5, 1).hole(1.5)
        solid = solid.union(holed.rotate((0, 0, 0), (0, 0, 1), i*30))
    else:
       solid = solid.union(blade1.rotate((0, 0, 0), (0, 0, 1), i*30))

show_object(solid)