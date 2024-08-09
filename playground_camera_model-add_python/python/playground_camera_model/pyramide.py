import numpy as np

class Pyramide:
    
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
        #Creates vertices of the pyramide
        # Vertices are defined relative to the center of the pyramide
        h = size * np.sqrt(2)  # Height of the pyramid from the base center to the apex
        self.Pyramide_pyramideP0 = self.create_point(0, 0, h)
        self.Pyramide_pyramideP1 = self.create_point(-size, size, -size)
        self.Pyramide_pyramideP2 = self.create_point(-size, -size, -size)
        self.Pyramide_pyramideP3 = self.create_point(size, -size, -size)
        self.Pyramide_pyramideP4 = self.create_point(size, size, -size)

        self.pyramide_points = [
            self.Pyramide_pyramideP0, self.Pyramide_pyramideP1,
            self.Pyramide_pyramideP2, self.Pyramide_pyramideP3,
            self.Pyramide_pyramideP4
        ]

    def set_position(self, pos_x, pos_y, pos_z):
        #Translate the pyramide to a new position
        translation_matrix = np.array([
            [1, 0, 0, pos_x],
            [0, 1, 0, pos_y],
            [0, 0, 1, pos_z],
            [0, 0, 0, 1]
        ])

        for pos, point in enumerate(self.pyramide_points):
            translated_vec = translation_matrix @ point
            self.pyramide_points[pos] = translated_vec

    def pyramide_drawer(self, C_T_V, V_T_Pyramide):
        pyramide_points_transform = []

        for point in self.pyramide_points:
            pyramideP = C_T_V @ V_T_Pyramide @ point
            pyramide_points_transform.append(pyramideP)

        return pyramide_points_transform
    
    def get_points(self):
        return self.pyramide_points
    
    def rotate_x(self, angle):
        """
        Rotate the pyramide around the X-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad), 0],
            [0, np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.pyramide_points = [rotation_matrix @ point for point in self.pyramide_points]

    def rotate_y(self, angle):
        """
        Rotate the pyramide around the Y-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), 0, np.sin(angle_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_rad), 0, np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.pyramide_points = [rotation_matrix @ point for point in self.pyramide_points]

    def rotate_z(self, angle):
        """
        Rotate the pyramide around the Z-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0, 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.pyramide_points = [rotation_matrix @ point for point in self.pyramide_points]
        