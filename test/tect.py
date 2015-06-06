
import pymongo
import json
import datetime

MONGODB_URI = 'mongodb://trinq:admin%40123@ds041992.mongolab.com:41992/adyoutube'
###############################################################################
# main
###############################################################################
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

def main():
    print "Dien keyword muon theo doi:"
    tmp_keyword = raw_input()
    # convert String  to json de insert vao mongodb
    keyword_doc = inputkeyword(tmp_keyword)
      
    kwdoc = db['addcollection']
   # keyword_doc = { 'keyword':'abc, deee , e333'}
    kwdoc.insert(keyword_doc)
    
    
### 
### Lay keyword moi nhat tu database mongodb
def getnewkeyword():
    kwdoc = db['addcollection']
    tempt = kwdoc.find(fields = {"keyword"}).sort("_id", -1).limit(1) 
    for doc in tempt:
        print 'Da Insert xong keyword:::: '+ doc['keyword']
    return doc['keyword']

def inputkeyword(keywordtw):
    info = dict()
    
    if(keywordtw!=""):
        info["keyword"] = keywordtw
    return info

    

    
    
    
    



if __name__== '__main__':
    main()
    getnewkeyword()
    




