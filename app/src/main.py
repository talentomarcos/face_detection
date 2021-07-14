import logging as logger
import concurrent.futures as cf

import config as cfg
import models.video_face_recognition as vfr

def init_logger() -> None:
    format = "%(asctime)s: %(message)s"
    logger.basicConfig(filename=cfg.log_file_name, format=format, level=logger.INFO, datefmt="%Y-%m-%d %H:%M:%S")

def start_analysing_cameras(cfg, logger) -> None:
    cams_to_analyse = cfg.ip_cameras_ips_list

    if not cams_to_analyse:
        logger.error("=== NO Cameras to analyse!!! ===")
        return

    num_of_cams = len(cams_to_analyse)
    logger.info("Cameras to use: %s", num_of_cams)

    with cf.ThreadPoolExecutor(max_workers=num_of_cams) as executor:
        for cam_ip in cams_to_analyse:
            logger.info("Thread for Camera: %s", cam_ip)
            executor.map(vfr.start_face_recog_with_cam, (logger,), (cfg, ), (cam_ip, ))

if __name__ == "__main__":
    init_logger()

    if not cfg or not vfr:
        logger.error("NO Config, Model found !!!")
        exit()

    logger.info("###### STARTING Face Recognition ######")
    start_analysing_cameras(cfg, logger)
    logger.info("###### ENDING Face Recognition ######")




