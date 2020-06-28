from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
from elasticsearch_dsl import Search
import json,re
import queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'sinhala-songs'

syn_artist = ['ගයනවා','ගායනා','ගායනා','ගැයු','ගයන','ගායනය','ගායකයා','ගායකයා']
syn_lyricist = ['ලියූ','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','රචනය','රචකයා']
syn_music = ['සංගීත']
syn_adj = ['කල','කෙරූ','කර','ලද','කරන','සින්දු','ගීත','ගී','සැපයූ','හොඳම','ජනප්‍රිය','සුපිරිම','සුපිරි','ප්‍රචලිත','ප්‍රසිද්ධ','හොදම','ජනප්‍රියම']

#q = queries.multi_match_cross_fields("Sunil", ['artist_english'])
#res = client.search(index=INDEX, body=q)
#hits = res['hits']['hits']
#num_results = len(hits)
#y = json.dumps(hits[0])
#z=json.loads(y)
#print (z["_source"]["title"])

query="Sunil ගායනා කල සුපිරි සින්දු 10"


def searchq(query):
    query=query.replace('ගේ', '')
    tokens_ori = query.split()
    tokens = query.split()
    print(tokens)

    num=0
    fields=[]

    for i in range(len(tokens_ori)):
        if tokens_ori[i] in syn_adj:
            tokens.remove(tokens_ori[i])        

        if tokens_ori[i] in syn_artist:
            tokens.remove(tokens_ori[i])
            fields.append('artist')
            fields.append('artist_english')

        if tokens_ori[i] in syn_lyricist:
            tokens.remove(tokens_ori[i])
            fields.append('lyricist')

        if tokens_ori[i] in syn_music:
            tokens.remove(tokens_ori[i])
            fields.append('music')
                
        if tokens_ori[i].isdigit():
            num = int(tokens_ori[i])            
            tokens.remove(tokens_ori[i])

    query = ' '.join(tokens)
    q='';
    print(query,len(fields))
    if len(fields)==1:
        if num==0:#2
            q = queries.multi_match_phrase_prefix(query,fields)
        else:#4
            q = queries.multi_match_and_sort_prefix(query,num,fields)
    if len(fields)>1:
        if num==0:#1
            q = queries.multi_match_cross_fields(query,fields)
        else:#3
            q = queries.multi_match_and_sort_cross(query,num,fields)
    if len(fields)==0:
        if num==0:#1
            q = queries.multi_match_cross_fields(query,['title','lyrics','artist','lyricist','music','artist_english'])
        else:#3
            q = queries.multi_match_and_sort_cross(query,num,['title','lyrics','artist','lyricist','music','artist_english'])
            
    print(q)
    res = client.search(index=INDEX, body=q)
    return res
