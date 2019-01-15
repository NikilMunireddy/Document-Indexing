import threading 
import indexing
import argparse
import os
import time

parser = argparse.ArgumentParser(description="Indexing")
parser.add_argument('-k', '--keyword', type=str, required=True ,help="Keyword")
parser.add_argument('-d', '--directory', type=str, required=True,help="Path to the document directory which has to be indexed")
parser.add_argument('-l', '--loadindex', type=bool, required=False,default=False ,help='pass "-l True"/ "--loadindex True" to load from the pickel file its fast. If want to create new index then this argument is not needed ')
args = parser.parse_args()

keyword = args.keyword
directory=args.directory
load=args.loadindex
docs=os.listdir('./Docs/')
print(len(docs))

if __name__ == "__main__": 
    thread_objects=[]
    documents=[]
    set_doc=[]
    j=0
    start=time.time()
    for i in range(len(docs)):
        if i%10 !=0:
            set_doc.append(docs[i])
        else:
            set_doc.append(docs[i])
            print('t start')
            thread_objects.append(threading.Thread(target=indexing.main_method, args=(keyword,directory,load,set_doc,)))
            set_doc=[]
            thread_objects[j].start()
            thread_objects[j].join()
            j+=1


    end=time.time()
    print("Done!",end-start) 


