import numpy as np

class Cube:
    
    @staticmethod  
    def create_point(x: float, y: float, z: float) -> np.array:
        return np.array([
            [x],
            [y],
            [z],
            [1]
        ])

    def __init__(self, size, pos_x, pos_y, pos_z):

        self.generate_vertices(size)
        self.set_position(pos_x, pos_y, pos_z)

    def generate_vertices(self, size):
        #Creates vertices of the cube
        # Vertices are defined relative to the center of the cube
        self.Cube_cubeP0 = self.create_point(-size, size, -size)
        self.Cube_cubeP1 = self.create_point(-size, -size, -size)
        self.Cube_cubeP2 = self.create_point(size, -size, -size)
        self.Cube_cubeP3 = self.create_point(size, size, -size)
        self.Cube_cubeP4 = self.create_point(-size, size, size)
        self.Cube_cubeP5 = self.create_point(-size, -size, size)
        self.Cube_cubeP6 = self.create_point(size, -size, size)
        self.Cube_cubeP7 = self.create_point(size, size, size)

        self.cube_points = [
            self.Cube_cubeP0, self.Cube_cubeP1,
            self.Cube_cubeP2, self.Cube_cubeP3,
            self.Cube_cubeP4, self.Cube_cubeP5,
            self.Cube_cubeP6, self.Cube_cubeP7
        ]

    def set_position(self, pos_x, pos_y, pos_z):
        #Translate the cube to a new position
        translation_matrix = np.array([
            [1, 0, 0, pos_x],
            [0, 1, 0, pos_y],
            [0, 0, 1, pos_z],
            [0, 0, 0, 1]
        ])

        for pos, point in enumerate(self.cube_points):
            translated_vec = translation_matrix @ point
            self.cube_points[pos] = translated_vec

    def cube_drawer(self, C_T_V, V_T_Cube):
        cube_points_transform = []

        for point in self.cube_points:
            cubeP = C_T_V @ V_T_Cube @ point
            cube_points_transform.append(cubeP)

        return cube_points_transform
    
    def get_points(self):
        return self.cube_points
