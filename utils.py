from params import *


def extract_view_count(input_count):
    """
    Extracts the number (an integer) of views from a text
    Possible input options: "14M views", "783K views", "13 views"
    Possible output options: 14,000,000, 783,000, 13

    :param input_count: Text string of views count (e.g. "58K views") | (str)
    :return: Number of views | (int)
    """
    count_text = input_count.split()[0]
    if "B" in count_text:
        views_count = float(count_text.replace("B", "")) * 1000000000
    elif "M" in count_text:
        views_count = float(count_text.replace("M", "")) * 1000000
    elif "K" in count_text:
        views_count = float(count_text.replace("K", "")) * 1000
    else:
        views_count = int(count_text)
    return views_count


def extract_upload_time(input_time):
    """
    Extracts a datetime from a given text
    Possible input options: "8 minutes ago", "23 hours ago", "1 day ago", "2 years ago" etc...
    
    :param input_time: The upload time of a video (e.g. "1 minute ago") | (str) 
    :return: datetime object of upload time | (datetime)
    """
    from datetime import datetime, timedelta
    delta = int(input_time.split()[0])
    upload_time = None
    if "minute" in input_time:
        upload_time = datetime.now() - timedelta(minutes=delta)
    elif "hour" in input_time:
        upload_time = datetime.now() - timedelta(hours=delta)
    elif "day" in input_time:
        upload_time = datetime.now() - timedelta(days=delta)
    elif "week" in input_time:
        upload_time = datetime.now() - timedelta(days=delta * DAYS_IN_WEEK)
    elif "month" in input_time:
        upload_time = datetime.now() - timedelta(days=delta * DAYS_IN_MONTH)
    elif "year" in input_time:
        upload_time = datetime.now() - timedelta(days=delta * DAYS_IN_YEAR)
    return upload_time.replace(second=0, microsecond=0)
