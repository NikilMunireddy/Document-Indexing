import os
import argparse
import pickle
import time

def create_index(directory,docs,d):
    k=0
    for doc in docs:
        print(k," "+directory+'/'+doc)
        text=open(directory+'/'+doc).read()  
        for i, line in enumerate(text.split('\n')):
            for each_word in line.split(' '):
                if each_word !='':
                    if doc not in d[each_word]:
                        d[each_word].append(doc) 
        for i, line in enumerate(text.split('\n')):
            for each_word in line.split(' '):
                if each_word !='':
                    d[each_word].append(i)
        k+=1
    pickle_out=open("index.pickle","wb")
    pickle.dump(d,pickle_out)
    pickle_out.close()
    return d

def load_index(d):
    pickle_in = open("index.pickle","rb")
    d = pickle.load(pickle_in)
    pickle_in.close()
    return d


def main_method(keyword,directory,load,set_doc):

    docs=set_doc
    from collections import defaultdict
    d = defaultdict(list)

    start_time=time.time()
    if not load:
        d=create_index(directory,docs,d)
    else:
        d=load_index(d)
    

    list_index=[]
    for doc in docs:
        try:
            list_index.append(d[keyword].index(doc)) 
        except:
            pass
    
    unique_list=[]
    i=0
    for li in list_index:
        try:
            unique_list.append(d[keyword][list_index[i]:list_index[i+1]])
        except:
            unique_list.append(d[keyword][list_index[i]:])
        i+=1

    length_index=[]
    j=0
    for li in unique_list:
        length_index.append(len(unique_list[j]))
        j+=1

    end_time=time.time()
    try:
        print("Execution time ",end_time-start_time," Seconds")
        print("Highest hits occoured in page "+'"'+unique_list[length_index.index(max(length_index))][0]+'"'+'for keyword '+'"'+keyword+'"')
        return "Highest hits occoured in page "+'"'+unique_list[length_index.index(max(length_index))][0]+'"'+'for keyword '+'"'+keyword+'"'
    except:
        print("could'nt find the keyword in dictonary")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Indexing")
    parser.add_argument('-k', '--keyword', type=str, required=True ,help="Keyword")
    parser.add_argument('-d', '--directory', type=str, required=True,help="Path to the document directory which has to be indexed")
    parser.add_argument('-l', '--loadindex', type=bool, required=False,default=False ,help='pass "-l True"/ "--loadindex True" to load from the pickel file its fast. If want to create new index then this argument is not needed ')
    args = parser.parse_args()

    keyword = args.keyword
    directory=args.directory
    load=args.loadindex
    print(main_method(keyword,directory,load))

    
