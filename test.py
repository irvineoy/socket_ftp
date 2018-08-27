

face_dir = raw_input("请输入人脸图片所在文件夹")
while(True):
    list_dir = os.walk('face_dir')
    for root, dirs, files in list_dir:
        for file in files:
            if file[0] == '-':
                continue
            if file == 'nohup.out': 
                continue
            imagesDir = []
            imagesDir.append(os.path.join(root, file))
            # print(imagesDir)
            # print(args.image_files)
            for filepath in imagesDir:
                try:
                    socket_client(filepath)
                except Exception as e:
                    print(e)
                    with open('/home/facenet/src/face/-{}.json'.format(file), 'w') as json_file:
                        json_file.write('no face')
                    continue
                renameFile = '-' + file
                renameImages = os.path.join(root, renameFile)
                os.rename(filepath, renameImages)
    sleep(0.1)