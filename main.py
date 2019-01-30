import threading 
import indexing
import argparse
import os
import time

# pass -h argument for help
parser = argparse.ArgumentParser(description="Indexing")
parser.add_argument('-k', '--keyword', type=str, required=True ,help="Keyword")
parser.add_argument('-d', '--directory', type=str, required=True,help="Path to the document directory which has to be indexed")
parser.add_argument('-l', '--loadindex', type=bool, required=False,default=False ,help='pass "-l True"/ "--loadindex True" to load from the pickel file its fast. If want to create new index then this argument is not needed ')
args = parser.parse_args()

keyword = args.keyword
directory=args.directory
load=args.loadindex
docs=os.listdir(directory)

if __name__ == "__main__": 
    if not load:
        thread_objects=[]
        documents=[]
        set_doc=[]
        j=0
        start=time.time()
        for i in range(len(docs)):
            file_count=j
            # set of 10 documents is given to one thread 
            if i%10 !=0:
                # Collecting names of 10 documents which is to be processed by thread
                set_doc.append(docs[i])
            else:
                # Once 10 douments are found the thread is started 
                set_doc.append(docs[i])
                print('thread '+str(j)+' start')
                thread_objects.append(threading.Thread(target=indexing.main_method, args=(keyword,directory,load,set_doc,file_count,)))
                set_doc=[]
                thread_objects[j].start()
                thread_objects[j].join()
                j+=1


        end=time.time()
        print('Indexded '+str(len(docs))+' documents in '+str(end-start)+' Seconds') 
    indexing.make_dict_object()

    if load:
        set_doc=os.listdir('./Docs/')
        indexing.main_method(keyword,directory,load,set_doc,0)

