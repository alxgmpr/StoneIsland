# coding=utf-8

import requests
import threading
import string
import time
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Stone Island Scraper
# This could take a while...

# Made by Alex Gompper
# Twitter : @edzart/@573supreme
# Github  : @alxgmpr


# play around with the numbers and offset to make sure you're covering all the bases
class Stone(threading.Thread):
    def __init__(self, offset_a=0, offset_b=0):
        threading.Thread.__init__(self)
        self.s = requests.Session()
        self.current_id = ''
        self.current_letters = ''
        self.offset_a = offset_a
        self.offset_b = offset_b

    def get_image(self,):
        url = 'https://cdn.yoox.biz/41/41{}{}_14_f.jpg'.format(
            self.current_id,
            self.current_letters
        )
        r = self.s.head(
            url,
            allow_redirects=False
        )
        if r.status_code == 302:
            print 'code 302 :: 41{}{}'.format(self.current_id, self.current_letters)
            return False
        # save image
        if r.status_code == 200:
            r = self.s.get(
                url,
                allow_redirects=False
            )
            filename = url.split('/')[-1]
            if filename in os.listdir('img'):
                return True
            with open('img/' + filename, 'wb') as f:
                f.write(r.content)
            return True
        else:
            print 'weird status code... exiting in case banned:: 41{}{}'.format(self.current_id, self.current_letters)
            exit(-1)

    def run(self):
        for i in range(0 + self.offset_a, 26):
            for j in range(13 + self.offset_b, 26): # change this shit up

                    self.current_letters = string.ascii_uppercase[i] + string.ascii_uppercase[j]
                    for k in range(714000, 1000000):
                        self.current_id = str(k).zfill(6)
                        print 'testing :: 41{}{}'.format(self.current_id, self.current_letters)
                        if self.get_image():
                            print 'found a photo @ ID 41{}{}'.format(self.current_id, self.current_letters)
                        # time.sleep(0.2)

# this is messy and im lazy.

s = Stone()
s1 = Stone(offset_a=2, offset_b=2)
s2 = Stone(offset_a=4, offset_b=4)
s3 = Stone(offset_a=6, offset_b=6)
s4 = Stone(offset_a=8, offset_b=8)
s5 = Stone(offset_a=10, offset_b=10)
s6 = Stone(offset_a=12, offset_b=12)
s7 = Stone(offset_a=14, offset_b=14)
s8 = Stone(offset_a=16, offset_b=16)
s9 = Stone(offset_a=18, offset_b=18)
s10 = Stone(offset_a=20, offset_b=20)
s11 = Stone(offset_a=22, offset_b=22)
s12 = Stone(offset_a=24, offset_b=24)
s13 = Stone(offset_a=26, offset_b=26)
s.start()
s1.start()
s2.start()
s3.start()
s4.start()
s5.start()
s6.start()
s7.start()
s8.start()
s9.start()
s10.start()
s11.start()
s12.start()
s13.start()
