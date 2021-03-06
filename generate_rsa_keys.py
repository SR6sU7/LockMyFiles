'''
@Author: 3vil_k4li & Odelesse-Chen
@Date: 2019-12-25 14:39:38
@LastEditTime : 2019-12-25 15:11:45
@LastEditors  : Please set LastEditors
@Description: Generate the RSA private and public key
@FilePath: \LockMyFiles\generate_rsa_keys.py
'''

from __future__ import print_function
import sys
import os
import string
import ctypes

from rsa_class import RSA_Class

def generate_keys():
    private_key = RSA_Class.generate_pri()
    public_key = RSA_Class.generate_pub(private_key)
    RSA_Class.save_pri("./rsapri.pem", private_key)
    RSA_Class.save_pub("./rsapub.pem", public_key)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# check if running as administrator, this can be ignore!
def main():
    if is_admin():
        generate_keys()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:#in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

if __name__ == "__main__":
    main()
