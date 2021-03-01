import datetime as dt

def get_current_timestamp():
    return dt.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
