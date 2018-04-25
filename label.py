import os
global lable , lable1


def generate(dir):
    files = os.listdir(dir)
    #files.sort()
    print ('****************')
    print ('input :',dir)
    print ('start...')
    listText = open(dir+'/'+'list.txt','w')
    print(files)
    lable1 = 1
    lable = 0
    for file in files:
        fileType = os.path.split(file)
        a = file.rfind('.')
        b =  file[0:a]
        print(b)
        if fileType[1] == '.txt':
            continue
        if(int(b)>50):
         name = dir+'/'+file + ' ' + str(int(lable1)) +'\n'
         listText.write(name)
        else :
            name = dir + '/' + file + ' ' + str(int(lable)) + '\n'
            listText.write(name)
    listText.close()
    print ('down!')
    print ('****************')

if __name__ == '__main__':
    generate('/home/tx/BaiduImageSpider/cat')