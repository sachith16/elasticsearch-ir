# elasticsearch-ir
Sinhala songs search application developed using Elasticsearch and Python

## Getting Started
* Run ***createindex.py*** file to create index and insert songs
* Run ***window.py*** file and it will open the GUI window
* Enter the search query in the search box

:red_circle: _Make shure the created index have writing access_

# File Structure     	
* **createindex.py** - Create index and insert songs
* **queries.py** - ElasticSeacrch multi-match queries  
* **search.py** - Search functions that process the user query
* **window.py** - Python GUI window
* **corpus** - Original data scraped from http://sinhalasongbook.com
* **final-corpus** - Translated and formatted data used to create the index   	 

# Song Data
1. Title in Sinhala and English
2. Artist Sinhala name
3. Lyricist
4. Composer
5. Views count
6. Song lyrics in Sinhala
7. Artist English name

# Functionalities
* Search can be done using any number of fields artist name, song title etc and the result shows the best match
> ටී.එම්.ජයරත්න අම්මා සඳකි
* Identify synonyms related to specific fields like ගැයූ(artist), ලියූ(lyricist) and search within those specific fields
> අමරසිරි පීරිස් ගායනා කල ගීත
* Identify ranges given in the search query and sort by views
> ක්ලැරන්ස් විජේවර්ධන හොඳම 10
* Artist name and song title can be search in both Sinhala and English
> kasun kalhara ගැයූ ගී
* Identify names using a part of the full name
> sunil අහස පොළව
