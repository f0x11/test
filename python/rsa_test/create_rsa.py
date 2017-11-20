import rsa
import time

# 先生成一对密钥，然后保存.pem格式文件，当然也可以直接使用
(pubkey, privkey) = rsa.newkeys(1024)

pub = pubkey.save_pkcs1()
pubfile = open('public_{0}.pem'.format(str(int(time.time()))), 'w+')
pubfile.write(pub.decode('utf-8'))
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private_{0}.pem'.format(str(int(time.time()))), 'w+')
prifile.write(pri.decode('utf-8'))
prifile.close()
