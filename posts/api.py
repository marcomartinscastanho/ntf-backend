import os
import requests
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Origin": "https://newtumbl.com",
    "Pragma": "no-cache",
    "Referer": "https://newtumbl.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept-Language": "en-GB,en;q=0.5",
}


def login() -> str:
    logger.info("login")
    username = os.environ.get('NTF_FEEDED_NT_USERNAME', None)
    password = os.environ.get('NTF_FEEDED_NT_PASSWORD', None)
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_User_Login'
    data = {"json": f'{{"Params":["[{{IPADDRESS}}]",null,"{username}","{password}"]}}'}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    session_token = body["aResultSet"][0]["aRow"][0]["szSessionToken"]
    # TODO: use sessions to keep the token between requests instead of logging in on every request
    return session_token


def set_post_compose(session_token: str, blog_id: str) -> str:
    logger.info(f"set_post_compose: {session_token}, {blog_id}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_Post_Compose'
    data = {"json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",{blog_id},5]}}'}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    return body["aResultSet"][0]["aRow"][0]["qwPostIx"]


def upload_with_url(session_token: str, image_url: str) -> str:
    logger.info(f"upload_with_url: {session_token}, {image_url}")
    from urllib.parse import urlencode
    url = f'https://up0.newtumbl.com/sba/{session_token}/'
    data = {"json": image_url}
    r = requests.post(
        url, headers={**headers, "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
        data=urlencode(data)
    )
    if r.status_code != 200:
        raise Exception(f"request failed with error {r.status_code} and message \"{r.json()}\"")
    body = r.json()
    return body["aResults"][0]["qwPartIx"]


def upload_with_binary(session_token: str, image_url: str, image_name: str) -> str:
    logger.info(f"upload_with_binary: {session_token}, {image_url}, {image_name}")
    image_resp = requests.get(image_url)
    url = f'https://up0.newtumbl.com/sba/{session_token}/'
    files = [('image_file', (image_name, image_resp.content, image_resp.headers.get('content-type')))]
    r = requests.post(url, headers={}, files=files)
    if r.status_code != 200:
        raise Exception(f"request failed with error {r.status_code} and message \"{r.json()}\"")
    body = r.json()
    return body["aResults"][0]["qwPartIx"]


def set_post_part_insert(session_token: str, post_ix: str, part_ix: str) -> None:
    logger.info(f"set_post_part_insert: {session_token}, {post_ix}, {part_ix}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_PostPart_Insert'
    data = {"json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",0,{post_ix},5,"","",{part_ix}]}}'}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_part_update(session_token: str, post_ix: str) -> None:
    logger.info(f"set_post_part_update: {session_token}, {post_ix}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_PostPart_Update'
    data = {
        "json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",0,{post_ix},1,"",""]}}',
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_part_update_comment(session_token: str, post_ix: str, comment: str) -> None:
    logger.info(f"set_post_part_update_comment: {session_token}, {post_ix}, {comment}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_PostPart_Update'
    data = {"json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",0,{post_ix},0,"{comment}",""]}}'}
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_options(session_token: str, post_ix: str, rating: int, source: str, hashtags: str) -> None:
    logger.info(f"set_post_options: {session_token}, {post_ix}, {rating}, {source}, {hashtags}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_Post_Options'
    data = {
        "json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",0,{post_ix},0,{rating},"","{source}","{hashtags}"]}}'
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_complete(session_token: str, post_ix: str) -> None:
    logger.info(f"set_post_complete: {session_token}, {post_ix}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_Post_Complete'
    data = {
        "json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",0,{post_ix}]}}',
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_publish(session_token: str, post_ix: str) -> None:
    logger.info(f"set_post_publish: {session_token}, {post_ix}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_Post_Publish'
    data = {
        "json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",{post_ix}]}}',
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)


def set_post_queue(session_token: str, post_ix: str) -> None:
    logger.info(f"set_post_queue: {session_token}, {post_ix}")
    url = 'https://api-rw.newtumbl.com/sp/NewTumbl/set_Post_Queue'
    data = {
        "json": f'{{"Params":["[{{IPADDRESS}}]","{session_token}",{post_ix}]}}',
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code != 200:
        raise Exception
    body = r.json()
    result = body["nResult"]
    if int(result) < 0:
        error = body["aResultSet"][0]["aRow"][0]["szError"]
        raise Exception(error)
