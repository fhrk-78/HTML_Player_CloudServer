import sys
import datetime
import keyboard
import requests
from scratchclient import ScratchSession

_PRFV: str = "1"

_INF = "INFO "
_ERR = "ERROR"
_DEB = "DEBUG"

if __name__ == "__main__":
    args = sys.argv
    profile = open(f"{args[1]}.svprofile", "r", encoding="utf-8").read().split(',,')

    ntime = datetime.datetime.now()
    logf = open(f"log{ntime.strftime('%Y%m%d_%H%M%S')}.log", "w+", encoding="utf-8")

    def logadd(msg: str, mtype: str):
        if profile[3] == "false":
            if profile[4] == "true" or (profile[4] == "false" and mtype != _DEB):
                logf.write(f"[{mtype}]{ntime.strftime('%Y/%m/%d %H:%M:%S')} {msg}\n")
                print(f"[{mtype}]{ntime.strftime('%Y/%m/%d %H:%M:%S')} {msg}")

    if profile[0] != _PRFV:
        logadd("Profile version isn't correct", _ERR)
    logadd(f"{args} {profile}", _DEB)
    logadd("Connecting...", _INF)
    try:
        sc_cnt = ScratchSession(profile[1], profile[2])
    except:
        logadd("Your password or username is incorrect.", _ERR)
        sys.exit(1)
    try:
        clct = sc_cnt.create_cloud_connection(profile[5])
    except:
        logadd("Cannot connect cloud", _ERR)
        sys.exit(1)
    
    print(f"[INFO ]{ntime.strftime('%Y/%m/%d %H:%M:%S')} Quit with Q key")
    clct.set_cloud_variable("__STATUS", 0)
    clct.set_cloud_variable("__REQUEST", 0)
    
    while(True):
        try:
            if clct.get_cloud_variable("__REQUEST") != 0:
                logadd("GET URL", _INF)
                requrl = clct.get_cloud_variable("__REQUEST")
                clct.set_cloud_variable("__STATUS", 10)
                requrl_a = [requrl[x:x+3] for x in range(0, len(requrl), 3)]
                req_a = ""
                for req_b in requrl_a:
                    req_a += chr(req_b)
                try:
                    res = requests.get(req_a)
                except:
                    clct.set_cloud_variable("__STATUS", 40)
                ress = list(res.text)
                rest_a = ""
                for rst in ress:
                    rest_a += str(ord(rst)).zfill(3)
                relist = [rest_a[y:y+255] for y in range(0, len(rest_a), 255)]
                clct.set_cloud_variable("__GET1", int(relist[0]))
                if len(relist):
                    clct.set_cloud_variable("__GET2", int(relist[1]))
                    if len(relist):
                        clct.set_cloud_variable("__GET3", int(relist[2]))
                clct.set_cloud_variable("__STATUS", 20)
            
            if(keyboard.is_pressed("q")):
                break
        except:
            logadd("Cloud disconnected", _ERR)
            sys.exit(1)

    logf.close()
    logadd("Successfully completed", _INF)
    sys.exit(0)