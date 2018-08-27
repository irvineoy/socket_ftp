#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: send.py
socket client
"""

import socket
import os
import sys
import struct
from time import sleep
import args


def socket_client(filepath):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('123.206.83.254', 6666))
    except socket.error as msg:
        print msg
        sys.exit(1)

    print s.recv(1024)

    while 1:
        # filepath = raw_input('please input file path: ')
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            fhead = struct.pack('128sl', os.path.basename(filepath),
                                os.stat(filepath).st_size)
            s.send(fhead)
            print 'client filepath: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print '{0} file send over...'.format(filepath)
                    break
                s.send(data)
        s.close()
        break


if __name__ == '__main__':
    face_dir = raw_input("请输入人脸图片所在文件夹:")
    while True:
        list_dir = os.walk(face_dir)
        for root, dirs, files in list_dir:
            for file in files:
                if file[0] == '-':
                    continue
                if file == 'nohup.out': 
                    continue
                imagesDir = []
                imagesDir.append(os.path.join(root, file))
                print(imagesDir)
                # print(args.image_files)

                for filepath in imagesDir:
                    try:
                        socket_client(filepath)
                    except Exception as e:
                        print(e)
                        continue
                    renameFile = '-' + file
                    renameImages = os.path.join(root, renameFile)
                    os.rename(filepath, renameImages)
        sleep(0.1)