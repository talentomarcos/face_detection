#### Obtenido de: ####
# 
# https://github.com/ageitgey/face_recognition


import cv2
import face_recognition

import network.web_service as srv

def start_face_recog_with_cam(logger, cfg, cam_ip: str = 0) -> None:
    print ("HOLA MI")
    logger.info("Starting analysing camera: %s", cam_ip)
    video_capture = cv2.VideoCapture(cam_ip)
    
    process_cam_video(logger, video_capture, cam_ip, cfg)

    video_capture.release()
    cv2.destroyAllWindows()

def process_cam_video(logger, video_capture, cam_ip, cfg) -> None:
    process_this_frame = True

    while True:
        if not process_this_frame:
            process_this_frame = not process_this_frame
            continue

        logger.info("Analysing new frame on camera: %s", cam_ip)

        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)

        if not face_locations:
            continue
        
        num_of_faces = len(face_locations)
        logger.info("%s Faces Detected on this frame", num_of_faces)
        
        for face_location in face_locations:
            process_face_on_frame(small_frame, logger, face_location, cfg)

def process_face_on_frame(frame, logger, face_location: tuple, cfg) -> None:
    logger.info("Extracting face coordinates")
    top, right, bottom, left = face_location
    face_img = frame[top:bottom, left:right]
                    
    # top *= 4
    # right *= 4
    # bottom *= 4
    # left *= 4

    logger.info("Encoding fece image to string")
    img_format = ".%s" % cfg.image_encode_format
    encoded_img = cv2.imencode(img_format, face_img)[1]
    img_str_to_send = encoded_img.tostring()
    logger.info("Face encoded string: \n%s\n\n", img_str_to_send)

    srv.send_to_server(logger, cfg, img_str_to_send)
