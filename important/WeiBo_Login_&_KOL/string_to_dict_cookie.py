cookie_raw = 'SINAGLOBAL=9471380264253.81.1656472017890; UOR=,,login.sina.com.cn; SCF=Ak4SrzpffHhwK3ME58sR9LKcENQ8EYAre2ELWgco4CnXimqxjb9otTEyGG1c8gAyfDzo9P-H98VwSbLl95hWXhM.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WWqgvVUwh09uuICfXdsH6Rz5JpVF0201K5pSK20eo.4; SUB=_2AkMVu-zidcPxrAZZkfgVzG_raYlH-jymboUUAn7uJhMyAxh87nQCqSVutBF-XELsdeB1zqXq2XMq4fpcPCQZ4V1D; _s_tentry=-; Apache=8696520345026.321.1659404570069; ULV=1659404570152:8:2:2:8696520345026.321.1659404570069:1659319796464; XSRF-TOKEN=27g7fJfomz1y_60nxkR4x0WH; WBPSESS=Dt2hbAUaXfkVprjyrAZT_F8TjtW1Mnh-ovDHVItKM0da7QMB6c3SnWN9fIwkyPVsqFMIX-IOVSnI6hxbe3i6JUr8mxZv0Emdhzd-Yf4Gv7NxfEes7VHgDd6baam4F_jfPIrZKHG1vWjdCaxjlTh4rQ=='

def string_to_dict(cookies):
    itemDict = {}
    items = cookies.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ','')
        value = item.split('=')[1]
        itemDict[key] = value

    return itemDict


print(string_to_dict(cookie_raw))