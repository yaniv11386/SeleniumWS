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
