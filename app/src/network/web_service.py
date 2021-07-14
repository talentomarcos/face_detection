import http.client as httplib
from datetime import datetime

def send_to_server(logger, cfg, str_img: str) -> None:
    logger.info("Sending data to Server: %s:%s%s" % (cfg.host, cfg.port, cfg.url))
    dt = datetime.now()

    data = cfg.data
    data["time"] = dt.strftime(cfg.date_time_format) if "time" in data else logger.error("NO Time on JSON Data to send")
    data["image"] = str_img if "image" in data else logger.error("NO Image on JSON Data to send")

    logger.info("Data to send: \n%s\n\n", data)

    conn = httplib.HTTPConnection(cfg.host, cfg.port, timeout=5)

    response = False
    try:
        conn.request("POST", cfg.url, data, cfg.headers)
        response = conn.getresponse()
    except OSError as ex:
        logger.error("Error trying to stablish connection with server. Error: %s", ex)
    
    if not response:
        logger.warning("=== No Response from server ===")
        return
    
    print(response.status, response.reason)
    data = response.read()
    logger.info("Server response: \n%s\n", data)
    print(data)
    conn.close()
    logger.info("Closed connection")