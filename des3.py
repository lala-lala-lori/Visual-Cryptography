import sys
import cv2
import numpy as np
import time


from Cryptodome.Cipher import DES3
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes




class algDES3:

    def __init__(self):

        ## Key from random bytes
        key  = get_random_bytes(24)
        self.cipher = DES3.new(key, DES3.MODE_ECB)

    def encrypt(self, img):
        """
         encrypt img, save encrypted image as aes_img.jpg
         returns encryption_time 
        """

        byteImg = img.tobytes()
        ## Padding
        PadbyteImg = pad(byteImg, 8)

        ## Encrypting bytes

        st_time = time.time_ns()

        encBytes = self.cipher.encrypt(PadbyteImg)

        enc_time = time.time_ns()-st_time

        # Convert ciphertext bytes to encrypted image data
        encBytes = encBytes[:len(byteImg)]
        encImg = np.frombuffer(encBytes, dtype=img.dtype).reshape(img.shape)
        
        np.savetxt("output/$des3_ciphertxt.txt",encImg)


        cv2.imwrite("output/$des3_img.jpg", encImg)


        return enc_time


