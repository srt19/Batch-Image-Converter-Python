import os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image

dir = "./"
imgi = ".jpg"
imgo = ".webp"
flist = []
maxWorker = 4

for root,dirs,files, in os.walk(dir):
    flist.extend( (os.path.join(root,f) for f in files if f.endswith(imgi)))

def main():
    num = 1
    flist_iter = len(flist)
    worker = ThreadPoolExecutor(maxWorker)

    for x in range(len(flist)):
        worker.submit(conv, num, flist_iter, flist[x], imgi, imgo)
        num+=1

def conv(num, flist_iter, x, imgi, imgo):
    size1 = (os.path.getsize(x) / 1000)
    size1 = "{:.02f}".format(size1)
    out = x.replace(imgi, imgo)
    img = Image.open(x)
    img.save(out, quality=75)
    size2 = (os.path.getsize(out) / 1000)
    size2 = "{:.02f}".format(size2)
    if(size2 > size1):
        os.remove(out)
    else:
        os.remove(x)
    print(num, "of", flist_iter, "converted. From", size1, "KB to", size2, "KB")

if __name__ == "__main__":
    main()
