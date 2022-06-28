from glob import glob 
import shutil
import os 
data = ['cars_train','cars_valid']

for i in data:
    source = 'yolov5/data/images/'+i+'/'
    images = 'yolov5/data/images/'+i
    labels = 'yolov5/data/labels/'+i
    mydict = {
        images: ['jpg','jpeg','png'],
        labels: ['txt','xml.txt']
    }

    for destination, extension in mydict.items():
        for ext in extension:
            for file in glob(source+'*.'+ext):
                shutil.move(file, os.path.join(destination, file.split('/'[-1]))) 