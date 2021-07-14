###########################################################################################################
########################################### Basic Configuration ###########################################

log_file_name = "face_detection.log"

############################################ Server Connection ############################################

host = "http://desarrollo.datamatic.com.uy"
port = 86
url = "/mt4/index.php?r=ws/clock2/start"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
}

image_encode_format = "jpg"
date_time_format = "%Y-%m-%d %H:%M:%S"

data = {
    "deviceId" : "1485",
    "local" : 113,
    "ext": ".jpg",

    # This fields are NEEDED
    "time" : str(),
    "image": str()
}

############################################### IP Cameras ################################################

ip_cameras_ips_list = [
    0, # Web Camera - REMOVE to use only IP Cameras

    # "rtsp://user:pass@IP_HOST",
    # "http://user:pass@IP_HOST",
]

###########################################################################################################