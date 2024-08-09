from playground_camera_model.cube import Cube
from playground_camera_model.polygons import Polygon
from playground_camera_model.pyramide import Pyramide
from playground_camera_model.cone import Cone

class Structure_Generator:

    @staticmethod
    def ground(width, height, depth, size=1, start_x=0, start_y=0, start_z=0):
        """
        Generate a ground structure of cubes with the specified width, height, and depth.
        """
        cubes = []

        for z in range(height):
            for row in range(width):
                for col in range(depth):
                    pos_x = start_x + col * size*2
                    pos_y = start_y + row * size*2
                    pos_z = start_z + z * size*2
                    cub = Cube(size, pos_x, pos_y, pos_z)
                    cubes.append(cub)

        return cubes
    
    def layerpolygons(width, height, depth, size=1, start_x=0, start_y=0, start_z=0):
        """
        Generate a structure of polygons with the specified width, height, and depth.
        """
        polygons = []

        for z in range(height):
            for row in range(width):
                for col in range(depth):
                    pos_x = start_x + col * size*2
                    pos_y = start_y + row * size*2
                    pos_z = start_z + z * size*2
                    poly = Polygon(size, pos_x, pos_y, pos_z)
                    polygons.append(poly)

        return polygons
    
    def layerpyramides(width, height, depth, size=1, start_x=0, start_y=0, start_z=0):
        """
        Generate a structure of pyramides with the specified width, height, and depth.
        """
        pyramides = []

        for z in range(height):
            for row in range(width):
                for col in range(depth):
                    pos_x = start_x + col * size*2
                    pos_y = start_y + row * size*2
                    pos_z = start_z + z * size*2
                    pyra = Pyramide(size, pos_x, pos_y, pos_z)
                    pyramides.append(pyra)

        return pyramides
    
    def layercones(width, height, depth, size=1, start_x=0, start_y=0, start_z=0):
        """
        Generate a structure of cones with the specified width, height, and depth.
        """
        cones = []

        for z in range(height):
            for row in range(width):
                for col in range(depth):
                    pos_x = start_x + col * size*2
                    pos_y = start_y + row * size*2
                    pos_z = start_z + z * size*2
                    co = Cone(size, pos_x, pos_y, pos_z)
                    cones.append(co)

        return cones
    
    def cube_from_polygons(size=1, start_x=0, start_y=0, start_z=0):
        """
        Generate a cube structure from four polygons with the specified size and starting position.
        """
        polygons = []

        poly1 = Polygon(size, start_x, start_y, start_z)
        polygons.append(poly1)

        poly2 = Polygon(size, start_x, start_y, start_z)
        poly2.rotate_x(90)
        polygons.append(poly2)

        poly3 = Polygon(size, start_x, start_y, start_z)
        poly3.rotate_x(270)
        poly3.rotate_y(90)
        polygons.append(poly3)

        poly4 = Polygon(size, start_x, start_y, start_z)
        poly4.rotate_y(180)
        polygons.append(poly4)

        poly5 = Polygon(size, start_x, start_y, start_z)
        poly5.rotate_x(90)
        poly5.rotate_y(180)
        polygons.append(poly5)

        poly6 = Polygon(size, start_x, start_y, start_z)
        poly6.rotate_x(270)
        poly6.rotate_y(270)
        polygons.append(poly6)

        return polygons
    

    def ramp_from_polygons(size=1, start_x=0, start_y=0, start_z=0):

        polygons = []

        poly1 = Polygon(size, start_x, start_y, start_z)
        polygons.append(poly1)

        poly2 = Polygon(size, start_x, start_y, start_z)
        poly2.rotate_x(90)
        polygons.append(poly2)

        poly3 = Polygon(size, start_x, start_y, start_z)
        poly3.rotate_x(270)
        poly3.rotate_y(90)
        polygons.append(poly3)

        return polygons

    
    def pyramide_from_polygons(size=1, start_x=0, start_y=0, start_z=0):
        polygons = []

        poly1 = Polygon(size, start_x, start_y, start_z)
        polygons.append(poly1)

        poly2 = Polygon(size, start_x, start_y, start_z)
        poly2.rotate_y(90)
        poly2.rotate_z(90)
        polygons.append(poly2)

        #poly3 = Polygon(size, start_x, start_y, start_z)
        #poly3.rotate_y(180)
        #polygons.append(poly3)

        #poly4 = Polygon(size, start_x, start_y, start_z)
        #poly4.rotate_y(270)
        #polygons.append(poly4)

        return polygons


    
    @staticmethod
    def tree(width, height, depth, size=1, start_x=0, start_y=0, start_z=0):

        cubes = []

        #3 height
        for y in range(3):
            pos_x = start_x
            pos_y = start_y
            pos_z = start_z + y * size*2
            cub = Cube(size, pos_x, pos_y, pos_z)
            cubes.append(cub)

        width1 = width  # Assuming width is defined somewhere
        depth1 = depth  # Assuming depth is defined somewhere
        start_y = 3  # Starting position on the y-axis

        for y in range(3):  # Loop for each layer of the pyramid
            for row in range(width1):  # Loop through rows of cubes
                for col in range(depth1):  # Loop through columns of cubes
                    # Calculate position for each cube
                    pos_x = width1 // 2 + col * size * 2
                    pos_y = depth1 // 2 + row * size * 2
                    pos_z = start_y + y * size * 2
                    
                    # Create a cube and append to the list
                    cub = Cube(size, pos_x, pos_y, pos_z)
                    cubes.append(cub)
            
            # Decrease width and depth for the next layer
            width1 -= 2
            depth1 -= 2


        return cubes
        #5,5
        #3,3
        #1,1