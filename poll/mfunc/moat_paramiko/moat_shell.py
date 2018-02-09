#参考文章：http://blog.csdn.net/songfreeman/article/details/50920767
import paramiko

def RsaKeyconn(filepath,host,user,pwd):
    # 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
    pkey = paramiko.RSAKey.from_private_key_file(filepath, password=pwd)
    # 建立连接
    ssh = paramiko.SSHClient()
    ssh.connect(hostname=host,
                port=22,
                username=user,
                pkey=pkey)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('accesstool -h')
    # 结果放到stdout中，如果有错误将放到stderr中
    print(stdout.read().decode())
    # 关闭连接
    ssh.close()

