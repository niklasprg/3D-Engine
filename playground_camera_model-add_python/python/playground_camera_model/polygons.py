import numpy as np

class Polygon:
    
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
        #Creates vertices of the polygon
        # Vertices are defined relative to the center of the polygon
        self.Polygon_polygonP0 = self.create_point(size, size, -size)
        self.Polygon_polygonP1 = self.create_point(-size, -size, -size)
        self.Polygon_polygonP2 = self.create_point(size, -size, -size)
        self.Polygon_polygonP3 = self.create_point(size, size, size)

        self.polygon_points = [
            self.Polygon_polygonP0, self.Polygon_polygonP1,
            self.Polygon_polygonP2, self.Polygon_polygonP3,
            self.Polygon_polygonP0, self.Polygon_polygonP2
        ]

    def set_position(self, pos_x, pos_y, pos_z):
        #Translate the polygon to a new position
        translation_matrix = np.array([
            [1, 0, 0, pos_x],
            [0, 1, 0, pos_y],
            [0, 0, 1, pos_z],
            [0, 0, 0, 1]
        ])

        for pos, point in enumerate(self.polygon_points):
            translated_vec = translation_matrix @ point
            self.polygon_points[pos] = translated_vec

    def polygon_drawer(self, C_T_V, V_T_Polygon):
        polygon_points_transform = []

        for point in self.polygon_points:
            polygonP = C_T_V @ V_T_Polygon @ point
            polygon_points_transform.append(polygonP)

        return polygon_points_transform
    
    def get_points(self):
        return self.polygon_points
    
    def rotate_x(self, angle):
        """
        Rotate the polygon around the X-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle_rad), -np.sin(angle_rad), 0],
            [0, np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.polygon_points = [rotation_matrix @ point for point in self.polygon_points]

    def rotate_y(self, angle):
        """
        Rotate the polygon around the Y-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), 0, np.sin(angle_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_rad), 0, np.cos(angle_rad), 0],
            [0, 0, 0, 1]
        ])
        self.polygon_points = [rotation_matrix @ point for point in self.polygon_points]

    def rotate_z(self, angle):
        """
        Rotate the polygon around the Z-axis by the given angle.
        """
        angle_rad = np.radians(angle)
        rotation_matrix = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0, 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        self.polygon_points = [rotation_matrix @ point for point in self.polygon_points]
        