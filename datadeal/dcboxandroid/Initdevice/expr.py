import os
def device_detect():
   d=os.popen('adb devices')
   dev=d.read()
   seril=dev.split(' ')[3].split('\n')[1].split('\t')[0]
   print(type(seril))
   return seril


if __name__ == '__main__':
    device_detect()