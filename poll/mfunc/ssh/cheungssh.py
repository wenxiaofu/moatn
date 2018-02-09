import sys,os,json,random,time,threading
sys.path.append('/home/cheungssh/bin')
sys.path.append('/home/cheungssh/mysite/mysite/cheungssh')
sys.path.append('/home/cheungssh/mysite/mysite/cheungssh/deployment_protocol')
from poll.mfunc.ssh.cheungssh_error import CheungSSHError
from poll.mfunc.ssh.cheungssh_thread_queue import CheungSSHThreadAdmin
from poll.mfunc.ssh.client_info import resolv_client
from poll.mfunc.ssh.cheungssh_modul_controler import CheungSSHControler

def execute_command():
    cheungssh_info = {"status": False, 'content': ""}
    try:
        id = str(random.randint(90000000000000000000, 99999999999999999999))
        parameter = {"servers":"200.200.169.212","cmd":"ifconfig"}
        if not parameter:
            raise CheungSSHError("错误码:CHB0000000000")
        try:
            parameter = json.loads(parameter)
        except:
            raise CheungSSHError("错误码:CHB0000000001")
        try:
            servers = parameter["servers"]
            cmd = parameter["cmd"]
        except:
            raise CheungSSHError("错误码:CHB0000000002")
        parameter["tid"] = id
        CheungSSHThread = CheungSSHThreadAdmin()

        CheungSSHThread.run(parameter)

        client_info = resolv_client()
        client_info["cmd"] = cmd
        # client_info["parameter"]=parameter
        client_info = dict(client_info, **parameter)

        init_status = {"content": "", "status": False, "stage": "running"}  # stage为running或者done,
        client_info = dict(client_info, **init_status)

        servers = client_info["servers"]
        _alias = []
        for sid in servers:
            try:
                host_alias = CheungSSHControler.convert_id_to_ip(sid)["content"]["alias"]
                _alias.append(host_alias)
            except Exception as e:

                pass
        client_info["alias"] = _alias

        client_info = json.dumps(client_info, encoding="utf8", ensure_ascii=False)

        #REDIS.rpush('command.history', client_info)
        cheungssh_info["content"] = id
        cheungssh_info["status"] = True
    except Exception as e:
        cheungssh_info["status"] = False
        cheungssh_info["content"] = str(e)
    return cheungssh_info