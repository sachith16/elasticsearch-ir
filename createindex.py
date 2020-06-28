from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re
import queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'sinhala-songs'

index = Index(INDEX,using=client)
res = index.create()
print (res)
    
with open('final-corpus/songs.json','r') as f:
        all_songs = json.loads(f.read())
        print (len(all_songs))
        for i in range(500):            
            y = json.dumps(all_songs[i])
            z=json.loads(y)
                
            e={
                "title" :  z["title"],
                "lyrics" : z["lyrics"],
                "artist" : z["artist"],
                "lyricist" : z["lyricist"],
                "music": z["music"],
                "views": z["views"],
                "artist_english": z["artist_english"]
            }
            #print(e)
            res=client.index(index=INDEX,id=i,body=e)
            #print (res)
        
