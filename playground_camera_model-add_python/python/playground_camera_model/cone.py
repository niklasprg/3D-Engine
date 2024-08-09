import numpy as np

class Cone:
    
    @staticmethod  
    def create_point(x: float, y: float, z: float) -> np.array:
        return np.array([
            [x],
            [y],
            [z],
            [1]
        ])

    def __init__(self, radius, height, pos_x, pos_y, pos_z, num_segments=20):

        self.radius = radius
        self.height = height
        self.num_segments = num_segments
        self.generate_vertices()
        self.set_position(pos_x, pos_y, pos_z)

    def generate_vertices(self):
        # Creates vertices of the cone
        self.Cone_apex = self.create_point(0, 0, self.height)
        self.Cone_base = [self.create_point(self.radius * np.cos(2 * np.pi * i / self.num_segments), 
                                            self.radius * np.sin(2 * np.pi * i / self.num_segments), 
                                            0) for i in range(self.num_segments)]

        self.cone_points = [self.Cone_apex] + self.Cone_base

    def set_position(self, pos_x, pos_y, pos_z):
        # Translate the cone to a new position
        translation_matrix = np.array([
            [1, 0, 0, pos_x],
            [0, 1, 0, pos_y],
            [0, 0, 1, pos_z],
            [0, 0, 0, 1]
        ])

        for pos, point in enumerate(self.cone_points):
            translated_vec = translation_matrix @ point
            self.cone_points[pos] = translated_vec

    def cone_drawer(self, C_T_V, V_T_Cone):
        cone_points_transform = []

        for point in self.cone_points:
            coneP = C_T_V @ V_T_Cone @ point
            cone_points_transform.append(coneP)

        return cone_points_transform
    
    def get_points(self):
        return self.cone_points
    
    def rotate_x(self, angle):
        """
        Rotate the cone around the X-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad), 0],
            [0, np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.cone_points = [rotation_matrix @ point for point in self.cone_points]

    def rotate_y(self, angle):
        """
        Rotate the cone around the Y-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), 0, np.sin(angle_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_rad), 0, np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.cone_points = [rotation_matrix @ point for point in self.cone_points]

    def rotate_z(self, angle):
        """
        Rotate the cone around the Z-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0, 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.cone_points = [rotation_matrix @ point for point in self.cone_points]
        
