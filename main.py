
import cv2
from texttable import Texttable

import numpy as np
from aes import algAES
from des import algDES
from des3 import algDES3
from rsa_256 import algRSA

class Test:
    def __init__(self, path):
        self.targetImg = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        np.savetxt("output/Targettxt.txt",self.targetImg)

    def main(self):

        
        aes_enc = algAES()
        des_enc = algDES()
        des3_enc = algDES3()
        rsa_enc = algRSA()

        ## DES, output image in file and return encryption time.
        des_encryption_t = des_enc.encrypt(self.targetImg)

        ## DES3, output image in file and return encryption time.
        des3_encryption_t = des3_enc.encrypt(self.targetImg)


        ## AES, output image in file and return encryption time.
        aes_encryption_t = aes_enc.encrypt(self.targetImg)
        
        ## RSA, output image in file and return encryption time.
        rsa_encryption_t = rsa_enc.encrypt(self.targetImg)
        



        #  TargetText Table

        t = Texttable()
        t.add_rows([
            ['Algorithm', 'Block Size(bits)', "Key Size(bits)", "Time taken in nanosecs"],
            ['DES', 64,56,des_encryption_t],
            ['3DES', 64,168,des_encryption_t],
            ['AES', 128,256,aes_encryption_t],
            ['RSA', 128,256,rsa_encryption_t]])
        print(t.draw())

        f = open("output/Algorithm_table.txt","w")
        f.write(t.draw())
        f.close()

# running main
if __name__ == "__main__":
    test1 = Test("target.jpg")
    test1.main()
    
