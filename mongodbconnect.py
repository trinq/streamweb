
#!/usr/bin/python

# Copyright (c) 2015 ObjectLabs Corporation
# Distributed under the MIT license - http://opensource.org/licenses/MIT

__author__ = 'mongolab'

# Written with pymongo-2.6 
# Documentation: http://api.mongodb.org/python/
# A python script connecting to a MongoDB given a MongoDB Connection URI.

import sys
import pymongo

### Create seed data



### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

# ='mongodb://trinq:admin%40123@ds041992.mongolab.com:41992/adyoutube' 
#MONGODB_URI = 'mongodb://127.0.0.1:27017/adyoutube'
MONGODB_URI = 'mongodb://trinq:admin%40123@ds041992.mongolab.com:41992/adyoutube'
###############################################################################
# main
###############################################################################
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

def save_data_mongo(SEED_DATA):

    
    # First we'll add a few songs. Nothing is required to create the songs 
    # collection; it is created automatically when we insert.

    songs = db['addcollection']

    # Note that the insert method can take either an array or a single dict.

    songs.insert(SEED_DATA)

    # Then we need to give Boyz II Men credit for their contribution to
    # the hit "One Sweet Day".

    
    
    ### Since this is an example, we'll clean up after ourselves.

    #db.drop_collection('songs')

    ### Only close the connection when your app is terminating

    client.close()


if __name__ == '__main__':
    main(sys.argv[1:])