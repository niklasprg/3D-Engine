import cv2 as cv

class Window:

    def __init__(self):

        self.camera_system_translation_x = 0
        self.camera_system_translation_y = 0
        self.camera_system_translation_z = 0
        self.camera_system_rotation_roll = 0
        self.camera_system_rotation_pitch = 0
        self.camera_system_rotation_yaw = 0
        
        self.cube_system_translation_x = 0
        self.cube_system_translation_y = 0
        self.cube_system_translation_z = 0
        self.cube_system_rotation_roll = 0
        self.cube_system_rotation_pitch = 0
        self.cube_system_rotation_yaw = 0
        self.cube_system_scale = 0

        self.polygon_system_translation_x = 0
        self.polygon_system_translation_y = 0
        self.polygon_system_translation_z = 0
        self.polygon_system_rotation_roll = 0
        self.polygon_system_rotation_pitch = 0
        self.polygon_system_rotation_yaw = 0
        self.polygon_system_scale = 0

        self.pyramide_system_translation_x = 0
        self.pyramide_system_translation_y = 0
        self.pyramide_system_translation_z = 0
        self.pyramide_system_rotation_roll = 0
        self.pyramide_system_rotation_pitch = 0
        self.pyramide_system_rotation_yaw = 0
        self.pyramide_system_scale = 0

        self.cone_system_translation_x = 0
        self.cone_system_translation_y = 0
        self.cone_system_translation_z = 0
        self.cone_system_rotation_roll = 0
        self.cone_system_rotation_pitch = 0
        self.cone_system_rotation_yaw = 0
        self.cone_system_scale = 0

        self.camera_window_name = "camera settings"
        self.cube_window_name = "cube settings"
        self.polygon_window_name = "polygon settings"
        self.pyramide_window_name = "pyramide settings"
        self.cone_window_name = "cone settings"

        self.window_creator()
    
    def window_creator(self):
        # Create gui
        cv.namedWindow("image window", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("camera settings", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("cube settings", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("polygon settings", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("pyramide settings", cv.WINDOW_AUTOSIZE)
        cv.namedWindow("cone settings", cv.WINDOW_AUTOSIZE)
        cv.resizeWindow("camera settings", 400, 300)
        cv.resizeWindow("cube settings", 400, 300)
        cv.resizeWindow("polygon settings", 400, 300)
        cv.resizeWindow("pyramide settings", 400, 300)
        cv.resizeWindow("cone settings", 400, 300)

        cv.createTrackbar("X", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "camera settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "camera settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "camera settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "camera settings", 0, 3600, self.nothing)

        cv.createTrackbar("X", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "cube settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "cube settings", 0, 3600, self.nothing)
        cv.createTrackbar("Scale", "cube settings", 1, 10, self.nothing)

        cv.createTrackbar("X", "polygon settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "polygon settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "polygon settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "polygon settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "polygon settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "polygon settings", 0, 3600, self.nothing)
        cv.createTrackbar("Scale", "polygon settings", 1, 10, self.nothing)

        cv.createTrackbar("X", "pyramide settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "pyramide settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "pyramide settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "pyramide settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "pyramide settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "pyramide settings", 0, 3600, self.nothing)
        cv.createTrackbar("Scale", "pyramide settings", 1, 10, self.nothing)

        cv.createTrackbar("X", "cone settings", 0, 20000, self.nothing)
        cv.createTrackbar("Y", "cone settings", 0, 20000, self.nothing)
        cv.createTrackbar("Z", "cone settings", 0, 20000, self.nothing)
        cv.createTrackbar("Roll", "cone settings", 0, 3600, self.nothing)
        cv.createTrackbar("Pitch", "cone settings", 0, 3600, self.nothing)
        cv.createTrackbar("Yaw", "cone settings", 0, 3600, self.nothing)
        cv.createTrackbar("Scale", "cone settings", 1, 10, self.nothing)

        self.camera_system_translation_x = cv.setTrackbarPos("X", "camera settings", 10000)
        self.camera_system_translation_y = cv.setTrackbarPos("Y", "camera settings", 10000)
        self.camera_system_translation_z = cv.setTrackbarPos("Z", "camera settings", 11000)
        self.camera_system_rotation_roll = cv.setTrackbarPos("Roll", "camera settings", 2700)
        self.camera_system_rotation_pitch = cv.setTrackbarPos("Pitch", "camera settings", 0)
        self.camera_system_rotation_yaw = cv.setTrackbarPos("Yaw", "camera settings", 2700)

        self.cube_system_translation_x = cv.setTrackbarPos("X", "cube settings", 14000)
        self.cube_system_translation_y = cv.setTrackbarPos("Y", "cube settings", 10000)
        self.cube_system_translation_z = cv.setTrackbarPos("Z", "cube settings", 11000)
        self.cube_system_rotation_roll = cv.setTrackbarPos("Roll", "cube settings", 0)
        self.cube_system_rotation_pitch = cv.setTrackbarPos("Pitch", "cube settings", 0)
        self.cube_system_rotation_yaw = cv.setTrackbarPos("Yaw", "cube settings", 0)
        self.cube_system_scale = cv.setTrackbarPos("Scale", "cube settings", 1)

        self.polygon_system_translation_x = cv.setTrackbarPos("X", "polygon settings", 14000)
        self.polygon_system_translation_y = cv.setTrackbarPos("Y", "polygon settings", 10000)
        self.polygon_system_translation_z = cv.setTrackbarPos("Z", "polygon settings", 11000)
        self.polygon_system_rotation_roll = cv.setTrackbarPos("Roll", "polygon settings", 0)
        self.polygon_system_rotation_pitch = cv.setTrackbarPos("Pitch", "polygon settings", 0)
        self.polygon_system_rotation_yaw = cv.setTrackbarPos("Yaw", "polygon settings", 0)
        self.polygon_system_scale = cv.setTrackbarPos("Scale", "polygon settings", 1)

        self.pyramide_system_translation_x = cv.setTrackbarPos("X", "pyramide settings", 14000)
        self.pyramide_system_translation_y = cv.setTrackbarPos("Y", "pyramide settings", 10000)
        self.pyramide_system_translation_z = cv.setTrackbarPos("Z", "pyramide settings", 11000)
        self.pyramide_system_rotation_roll = cv.setTrackbarPos("Roll", "pyramide settings", 0)
        self.pyramide_system_rotation_pitch = cv.setTrackbarPos("Pitch", "pyramide settings", 0)
        self.pyramide_system_rotation_yaw = cv.setTrackbarPos("Yaw", "pyramide settings", 0)
        self.pyramide_system_scale = cv.setTrackbarPos("Scale", "pyramide settings", 1)

        self.cone_system_translation_x = cv.setTrackbarPos("X", "cone settings", 14000)
        self.cone_system_translation_y = cv.setTrackbarPos("Y", "cone settings", 10000)
        self.cone_system_translation_z = cv.setTrackbarPos("Z", "cone settings", 11000)
        self.cone_system_rotation_roll = cv.setTrackbarPos("Roll", "cone settings", 0)
        self.cone_system_rotation_pitch = cv.setTrackbarPos("Pitch", "cone settings", 0)
        self.cone_system_rotation_yaw = cv.setTrackbarPos("Yaw", "cone settings", 0)
        self.cone_system_scale = cv.setTrackbarPos("Scale", "cone settings", 1)


    def window_show(self, class_cam):
        cv.imshow("image window", class_cam.camera_image)
        cv.waitKey(10)

    def get_camera_system_translation_x(self):
        return cv.getTrackbarPos("X", self.camera_window_name)

    def get_camera_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.camera_window_name)

    def get_camera_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.camera_window_name)

    def get_camera_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.camera_window_name)

    def get_camera_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.camera_window_name)

    def get_camera_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.camera_window_name)

    def get_cube_system_translation_x(self):
        return cv.getTrackbarPos("X", self.cube_window_name)

    def get_cube_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.cube_window_name)

    def get_cube_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.cube_window_name)

    def get_cube_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.cube_window_name)

    def get_cube_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.cube_window_name)

    def get_cube_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.cube_window_name)
    
    def get_cube_system_scale(self):
        return cv.getTrackbarPos("Scale", self.cube_window_name)
    
    def get_polygon_system_translation_x(self):
        return cv.getTrackbarPos("X", self.polygon_window_name)

    def get_polygon_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.polygon_window_name)

    def get_polygon_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.polygon_window_name)

    def get_polygon_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.polygon_window_name)

    def get_polygon_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.polygon_window_name)

    def get_polygon_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.polygon_window_name)
    
    def get_polygon_system_scale(self):
        return cv.getTrackbarPos("Scale", self.polygon_window_name)
    
    def get_pyramide_system_translation_x(self):
        return cv.getTrackbarPos("X", self.pyramide_window_name)

    def get_pyramide_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.pyramide_window_name)

    def get_pyramide_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.pyramide_window_name)

    def get_pyramide_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.pyramide_window_name)

    def get_pyramide_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.pyramide_window_name)

    def get_pyramide_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.pyramide_window_name)
    
    def get_pyramide_system_scale(self):
        return cv.getTrackbarPos("Scale", self.pyramide_window_name)
    
    def get_cone_system_translation_x(self):
        return cv.getTrackbarPos("X", self.cone_window_name)

    def get_cone_system_translation_y(self):
        return cv.getTrackbarPos("Y", self.cone_window_name)

    def get_cone_system_translation_z(self):
        return cv.getTrackbarPos("Z", self.cone_window_name)

    def get_cone_system_rotation_roll(self):
        return cv.getTrackbarPos("Roll", self.cone_window_name)

    def get_cone_system_rotation_pitch(self):
        return cv.getTrackbarPos("Pitch", self.cone_window_name)

    def get_cone_system_rotation_yaw(self):
        return cv.getTrackbarPos("Yaw", self.cone_window_name)
    
    def get_cone_system_scale(self):
        return cv.getTrackbarPos("Scale", self.cone_window_name)

    @staticmethod
    def nothing(x):
        pass
