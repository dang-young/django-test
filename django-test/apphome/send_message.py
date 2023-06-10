import ssl
ssl.OPENSSL_VERSION = ssl.OPENSSL_VERSION.replace("LibreSSL", "OpenSSL")
import requests
import json

with open(r"kakao_code.json","r") as fp:
    tokens = json.load(fp)


def send_message(name):

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
    headers={"Authorization" : "Bearer " + tokens["access_token"]}

    result = json.loads(requests.get(friend_url, headers=headers).text)
    friends_list = result.get("elements")

    for friend in friends_list:
        if friend['profile_nickname'] == name:
            friend_id = friend['uuid']
            break

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    data={
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type": "location",
            "address": "서울시 동작구 사당동 708-400",
            "address_title": "상수국밥",
            "content": {
                "title": "10 Minutes Left!",
                "description": "see the menu below",
                "image_url": "https://lh3.googleusercontent.com/p/AF1QipPCQYy2P8le-pdwSobk-vbRy-3Ta2tobdRzP1Ru=s680-w680-h510",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "social": {
                "like_count": 182,
                "comment_count": 56,
                # "shared_count": 300,
                # "view_count": 400,
                "subscriber_count": 1283
            },
            # "button_title": "Menu",
            "buttons": [
                {
                    "title": "Menu",
                    "link": {
                        "web_url": "http://www.daum.net",
                        "mobile_web_url": "http://m.daum.net"
                    }
                },
                {
                    "title": "Map",
                    "link": {
                        "android_execution_params": "contentId=100",
                        "ios_execution_params": "contentId=100"
                    }
                }]
        })
    }
    response = requests.post(url, headers=headers, data=data)


    response.status_code
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))