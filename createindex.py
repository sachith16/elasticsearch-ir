from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re
import queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'sinhala-songs'

index = Index(INDEX,using=client)
    res = index.create()
    print (res)
    
with open('sampledata/songs.json','r') as f:
        all_songs = json.loads(f.read())
        print (len(all_songs))
        for i in range(500):            
            y = json.dumps(all_songs[i])
            z=json.loads(y)
            
            lyricist=""
            if "Lyrics" in z:
                lyricist=z["Lyrics"]

            music=""
            if "Music" in z:
                music=z["Music"]
                
            e={
                "title" :  z["title"],
                "lyrics" : z["song_lyrics"],
                "artist" : z["Artist"],
                "lyricist" : lyricist,
                "music": music,
                "views": z["views"],
                "artist_english": z["english_artist"]
            }
            #print(e)
            res=client.index(index=INDEX,id=i,body=e)
            print (res)
        
