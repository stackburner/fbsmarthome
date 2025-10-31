import requests
import hashlib


class FritzBox:

    def __init__(self):
        self.url = "url to your fritzbox"
        self.username = "smarthome"
        self.pw = "PW"
        request_result = requests.get(self.url + "/login_sid.lua", params={'version': '2'})
        self.SID = str((request_result.text).split("<SID>")[1].split("</SID>")[0])
        self.BlockTime = int((request_result.text).split("<BlockTime>")[1].split("</BlockTime>")[0])
        self.Challenge = str((request_result.text).split("<Challenge>")[1].split("</Challenge>")[0])
        if self.SID == '0000000000000000':
            challenge_split = self.Challenge.split("$")
            iter1 = int(challenge_split[1])
            salt1 = bytes.fromhex(challenge_split[2])
            iter2 = int(challenge_split[3])
            salt2 = bytes.fromhex(challenge_split[4])
            hash1 = hashlib.pbkdf2_hmac("sha256", self.pw.encode(), salt1, iter1)
            hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
            response = challenge_split[4] + "$" + hash2.hex()
            request_data = {"username": self.username, "response": response}
            request_headers = {"Content-Type": "application/x-www-form-urlencoded"}
            request_result = requests.post(self.url + "/login_sid.lua", data=request_data, headers=request_headers)
            self.SID = str(request_result.text.split("<SID>")[1].split("</SID>")[0])



    def set_temperature(self, device: str, mode=0):
        if mode == 1:
            request_payload = {'switchcmd': 'sethkrtsoll', 'sid': self.SID, 'ain': device,
                               'param': self.get_temperature(device, mode)}
        else:
            request_payload = {'switchcmd': 'sethkrtsoll', 'sid': self.SID, 'ain': device,
                               'param': self.get_temperature(device, mode)}
        request_result = requests.get(self.url + "/webservices/homeautoswitch.lua", params=request_payload)

        return str(request_result.status_code)

    def get_temperature(self, device: str, mode=0):
        if mode == 1:
            request_payload = {'switchcmd': 'gethkrkomfort', 'sid': self.SID, 'ain': device}
        else:
            request_payload = {'switchcmd': 'gethkrabsenk', 'sid': self.SID, 'ain': device}
        request_result = requests.get(self.url + "/webservices/homeautoswitch.lua", params=request_payload)
        temp = request_result.text

        return temp
