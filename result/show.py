from PIL import Image


with open('./result/result.txt','r') as f:
    lines=f.readlines()



for i in range(50):
    dir = './result/test_pic/' + str(i) + '.jpg'
    img = Image.open(dir)
    img = img.resize((256,256), Image.ANTIALIAS)
    img.show()
    print('label:\t', lines[2*i])
    print('predict:\t', lines[2*i+1])
    input('press enter to continue\n')