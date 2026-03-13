import cadquery as cq

solid = cq.Workplane("XY").circle(40).circle(12).extrude(11)

show_object(solid)