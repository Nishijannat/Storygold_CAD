import cadquery as cq

hex = cq.Workplane("XY").polygon(6, 20).extrude(25)


solid = hex.edges(">>Z").fillet(1.6)


show_object(solid)

