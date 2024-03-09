"""
Authors:
    Alejandro Alfaro, Gaudy Esquivel Vega, Leonardo Víquez.
Library Requirements:
    pip install opencv-python
    pip install opencv-contrib-python
    pip install numpy
"""

"""
The 'os' module provides a way to interact with the operating system.
"""
import os

"""
The 'cv2' (OpenCV) module is a powerful library for computer vision and image processing.
"""
import cv2

"""
The 'numpy' module is a library for numerical operations in Python.
"""
import numpy as np

"""
The 'time' module provides various time-related functions.
"""
import time


def start_sorting(sorted_list, flip_image:bool=False, show_identified_marker:bool=False, show_images:bool=True, show_ids:bool=False, show_coordinates:bool=False)->float:
    """Starts marker recognition and stops when it determines the pattern of their arrangement.

    Args:
        sorted_list (_type_): List that marks the order in which the markers should be found.
        flip_image (bool, optional): Allows horizontal and vertical inversion of the camera image.
        show_images (bool, optional): Allows displaying or hiding the images associated with the markers. Defaults to True.
        show_ids (bool, optional): Allows displaying or hiding the IDs associated with the markers. Defaults to False.
        show_coordinates (bool, optional): Allows displaying or hiding the coordinates of the markers with reference to the image captured by the camera. Defaults to False.
        show_identified_marker (bool, optional): Allows displaying or hiding the square of the markers. Defaults to False.
    Returns:
        float: Returns the amount of seconds it took to recognize that the markers were ordered.
    """
    # Stores the start time of the marker recognition execution.
    init_time = time.time()
    
    # Create a dictionary of ARUCO markers.
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Create a camera object
    cap = cv2.VideoCapture(0)

    # Creates an empty list to store the recognized markers sorted from left to right.
    sorted_markers=[];

    # Main loop recognizes frame by frame from the camera the markers that can be observed, exits the loop when it determines that the markers are already sorted.
    while True:
        """
        ret: It is a boolean value indicating whether the capture of the frame was successful (True) or not (False).
        frame: It is the image of the captured frame.
        """
        ret, frame = cap.read()

        # Invert the image horizontally and vertically.
        if flip_image:
            frame = cv2.flip(frame, -1)

        # Detect ARUCO markers in the camera image.
        corners, ids, _ = detector.detectMarkers(frame)

        if ids is not None:
            # Draw a rectangle around the marker

            if show_identified_marker:
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            # Create a list of tuples (id, x) for each marker
            marcadores_con_x = [(id, np.mean(corner[:, 0])) for id, corner in zip(ids, corners)]

            # Sort the markers list along the x-axis
            sorted_markers = list([int(id) for id, _ in sorted(marcadores_con_x, key=lambda x: x[1])])

            # Display information or associated images for each found marker.
            for i in range(len(ids)):
                # Calculate the centroid of the marker.
                #cX = int(np.mean(corners[i][0][:, 0]))
                #cY = int(np.mean(corners[i][0][:, 1]))
                cX = int(corners[i][0][0][0])
                cY = int(corners[i][0][0][1])
                
                # Overlays the image corresponding to the marker.
                if show_images:
                    try:
                        # Path of this file
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        # Path of the image asociated with the marker id.
                        image_path = os.path.join(current_dir, 'images', f'{ids[i][0]}.png')
                        # Read the image fron url
                        image_to_overlay = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
                        frame[cY:cY+100, cX:cX+100] = image_to_overlay
                    except:
                        print ("We can't read or draw the image on the marker")
                
                # Draws the corresponding ID on the marker.
                if show_ids:
                    cv2.putText(frame, f'id={str(ids[i][0])}', (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                
                # Draws the coordinates corresponding to the marker with reference to the image capture.
                if show_coordinates:
                    cv2.putText(frame, f'X:{cX},Y:{cY}', (cX, cY+20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1,cv2.LINE_AA)
        
        # Show final image in the visor
        cv2.imshow(f'ARMem', frame)

        # Exit the loop when the markers are ordered.
        if cv2.waitKey(1) & (sorted_list==sorted_markers):
            final_time = time.time()
            # Release the camera
            cap.release()
            cv2.destroyAllWindows()
            return final_time-init_time