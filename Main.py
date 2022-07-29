import os
from threading import Thread
from time import perf_counter
from PIL import Image

dir = "./"
imgi = ".webp"
imgo = ".jpg"
flist = []

for root,dirs,files, in os.walk(dir):
    flist.extend( (os.path.join(root,f) for f in files if f.endswith(imgi)))

def main():
    flist_iter = len(flist)

    # create threads
    threads = [Thread(target=conv, args=(x, flist_iter, flist[x], imgi, imgo))
            for x in range(flist_iter)]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()

def conv(x, flist_iter, n, imgi, imgo):
    x += 1
    size1 = (os.path.getsize(n) / 1000)
    size1 = "{:.02f}".format(size1)
    out = n.replace(imgi, imgo)
    img = Image.open(n)
    img.save(out, quality=75)
    size2 = (os.path.getsize(out) / 1000)
    size2 = "{:.02f}".format(size2)
    if(size2 > size1):
        os.remove(out)
    else:
        os.remove(n)
    print(x, "of", flist_iter, "converted. From", size1, "KB to", size2, "KB")

if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
