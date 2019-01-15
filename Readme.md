# Index any type of documents and search the suitable documents based on the keyword within no time

## Create index for the documents using multi threading 
## A set of 10 documents is given to one thread 
## Threading reduces the time required to create index by 8 times (approx)
Command to create index
```
python3 main.py --keyword "Your keyword" --directory /path/to/your/directory 
```
![Image description](./screenshorts/loadFalse.png)

Command to search file using index
```
 python3 main.py --keyword "Your keyword" --directory /path/to/your/directory --loadindex True
```
## Load the indexwhich is already created, this is very fast since it uses the index to find the suitable document
![Image description](./screenshorts/loadTrue.png)