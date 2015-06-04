
import pymongo
import json

MONGODB_URI = 'mongodb://trinq:admin%40123@ds041992.mongolab.com:41992/adyoutube'
###############################################################################
# main
###############################################################################
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

def main():
    print "Enter your keyword:"
    tmp_keyword = raw_input()

    keyword = tmp_keyword.split()
    list_keyword =[]
    kwdoc = db['addcollection']
    
    keyword_doc = {'keyword' :' abc, d , e '}
   
    
            

    kwdoc.insert(keyword_doc)
    
    for word in keyword:
        list_keyword.append(word)
        print(word)
    
    
    print list_keyword
    print "Insert keyword to List"
    



if __name__== '__main__':
    main()




