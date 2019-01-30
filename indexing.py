import os
import argparse
import pickle
import time


# create_index (A dictionary) for every keyword i.e {keyword:[filename, linenumbers....]}
# The indexed dictionary is frozen in a pickle file
# The pickle file can be stored or shared thus reduces the computaion overload i.e  it's computed only once and restored many times

def create_index(directory,docs,d,file_count):
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
    # When running this code using threads a bunch of 10 documents is index by each thread 
    # So a seperate index is created for each thread which is stored in Pickle folder
    pickle_file_name="./Pickle/index"+str(file_count)+".pickle"
    pickle_out=open(pickle_file_name,"wb")
    pickle.dump(d,pickle_out)
    pickle_out.close()
    return d

# load the dictonary from pickle file insted of indexing all documents once again
# Reads the pickle file and returns the dictonary object 
def load_index(d):
    pickle_in = open("index.pickle","rb")
    d = pickle.load(pickle_in)
    pickle_in.close()
    return d


def main_method(keyword,directory,load,set_doc,file_count):
    docs=set_doc
    from collections import defaultdict
    d = defaultdict(list)

    start_time=time.time()
    if not load:
        d=create_index(directory,docs,d,file_count)
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
        if load:
            print("Execution time ",end_time-start_time," Seconds")
            print("Highest hits occoured in page "+'"'+unique_list[length_index.index(max(length_index))][0]+'"'+'for keyword '+'"'+keyword+'"')
            return "Highest hits occoured in page "+'"'+unique_list[length_index.index(max(length_index))][0]+'"'+'for keyword '+'"'+keyword+'"'
    except:
        print('could\'nt find appropriate document for '+'"'+keyword+'"')


# Induvidual pickle files created in Pickle folder is combained into one file 
# so which can be used os one object as a whole
def make_dict_object():
    # list all pickle files
    pick_files=os.listdir('./Pickle/')
    from collections import defaultdict
    dicto = defaultdict(list)
    for obj in pick_files:
        file_path='./Pickle/'+str(obj)
        pickle_in = open(file_path,"rb")
        obj = pickle.load(pickle_in)
        pickle_in.close()
        dicto.update(obj)
    pickle_file_name="index.pickle"
    pickle_out=open(pickle_file_name,"wb")
    pickle.dump(dicto,pickle_out)
    pickle_out.close()



if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Indexing")
    parser.add_argument('-k', '--keyword', type=str, required=True ,help="Keyword")
    parser.add_argument('-d', '--directory', type=str, required=True,help="Path to the document directory which has to be indexed")
    parser.add_argument('-l', '--loadindex', type=bool, required=False,default=False ,help='pass "-l True"/ "--loadindex True" to load from the pickel file its fast. If want to create new index then this argument is not needed ')
    args = parser.parse_args()

    keyword = args.keyword
    directory=args.directory
    load=args.loadindex
    set_doc=os.listdir(directory)

    print(main_method(keyword,directory,load,set_doc,0))

    
