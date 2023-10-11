import requests

URL = ""

def query_ceac_state_safe(loc, case_no, info):
    retry = 0
    while retry < 5:
        req = requests.post(URL, json=[[loc,case_no,info]], timeout=10)
        if ret:
            break
        retry += 1
    ret = req.json()
    return ret[case_no]


def query_ceac_state_remote(req_data):
    req = requests.post(URL, json=req_data, timeout=180)
    ret = req.json()
    return ret


# if __name__ == "__main__":
#     print(query_ceac_state_safe("BEJ","AA00A38G49"))