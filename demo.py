import numpy as np
import matplotlib.pyplot as plt
import os
from DOTA import DOTA
import dota_utils as util
import pylab
from ResultMerge import mergebypoly

pylab.rcParams['figure.figsize'] = (20.0, 20.0)
os.makedirs('Task1', exist_ok=True)
os.makedirs('Task1_merge', exist_ok=True)
os.makedirs('restoredexample/labelTxt', exist_ok=True)

# example = DOTA('example')
# imgids = example.getImgIds(catNms=['ship', 'storage-tank'])
# imgid = imgids[0]
# img = example.loadImgs(imgid)[0]

# anns = example.loadAnns(imgId=imgid)
# example.showAnns(anns, imgid, 2)
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# examplesplit = DOTA('examplesplit')
# imgids = examplesplit.getImgIds(catNms=['plane'])
# imgid = imgids[1]
# img = examplesplit.loadImgs(imgid)[0]
# anns = examplesplit.loadAnns(imgId=imgid)
# examplesplit.showAnns(anns, imgid, 2)
# plt.savefig('demo.png')
# plt.show()

# util.groundtruth2Task1(r'examplesplit/labelTxt',
#                        r'Task1')
# mergebypoly(r'Task1', r'Task1_merge')
# util.Task2groundtruth_poly(r'Task1_merge',
#                            r'restoredexample/labelTxt')

filepath = 'example/labelTxt'
imgids = util.GetFileFromThisRootDir(filepath)
imgids = [util.custombasename(x) for x in imgids]
print(imgids)

example = DOTA(r'example')
num = 2
anns = example.loadAnns(imgId=imgids[num])
example.showAnns(anns, imgids[num], 2)
plt.show()

restored = DOTA(r'restoredexample')
num = 2
anns = restored.loadAnns(imgId=imgids[num])
restored.showAnns(anns, imgids[num], 2)
plt.show()
