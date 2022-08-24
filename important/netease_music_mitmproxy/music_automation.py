from mitmproxy import http
import requests
# def request(flow = http.HTTPFlow):

count = 1
redundancy_list = []

def request(flow = http.HTTPFlow):
    global count
    if '.m4a' in flow.request.url:
        if not flow.request.url in redundancy_list:
            redundancy_list.append(flow.request.url)
            res = requests.get(url=flow.request.url)
            with open('music/{}.mp3'.format(count), 'wb') as f:
                f.write(res.content)

            count += 1

# def response(flow = http.HTTPFlow):
    # global count
    # if '.m4a' in flow.request.url:
    #     if not flow.request.url in redundancy_list:
    #
    #         redundancy_list.append(flow.request.url)
    #         res = requests.get(url=flow.request.url)
    #         with open('music/{}.mp3'.format(count),'wb') as f:
    #             f.write(res.content)
    #
    #
    #         count += 1