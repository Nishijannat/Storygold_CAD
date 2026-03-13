import cadquery as cq

Rect1 = cq.Workplane("XY").rect(60,40).extrude(1)

solid = Rect1.faces(">Z").workplane().rarray(7,5,8,5).hole(1)


show_object(solid) 