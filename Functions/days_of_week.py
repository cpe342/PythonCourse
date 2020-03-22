
def return_day(num):
    week={
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        7:"Saturday"
    }
    if num>7 or num<1:
        return None
    else:
        return week[num]
    