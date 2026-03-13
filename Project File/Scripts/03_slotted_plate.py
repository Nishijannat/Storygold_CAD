import cadquery as cq

first_rect = cq.Workplane("XY").rect(30, 20).extrude(3)
first_rect = first_rect.edges("|Z").fillet(3)

solid = first_rect.faces(">Z").workplane().slot2D(15,5).cutThruAll()

show_object(solid)