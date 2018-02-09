#from poll.mfunc.ssh.cheungssh_sshv2 import *
from poll.mfunc.ssh.cheungssh_thread_queue import CheungSSHThreadAdmin

if __name__ == "__main__":
    cheungssh_info = {"status": False, 'content': ""}
    parameter = {"servers": "200.200.169.212", "cmd": "ifconfig","task_type":"cmd","tid":122131,"multi_thread":0}
    CheungSSHThread = CheungSSHThreadAdmin()
    CheungSSHThread.run(parameter)

  #  execute_command()
# ch = CheungSSH_SSH()

