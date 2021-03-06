def multi_match_cross_fields(query, fields):
	print('multi_match_cross_fields')
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
                "aggs": {			
			"Music": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyricist": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			}
		}
	}
	return q
	
def multi_match_phrase_prefix(query, fields):
	print('multi_match_phrase_prefix')
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "phrase_prefix"
			}
		},
                "aggs": {			
			"Music": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyricist": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			}
		}
	}
	return q

def multi_match_and_sort_cross(query, num, fields):
	print('multi_match_and_sort_cross')
	q = {
		"size": num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
                "aggs": {			
			"Music": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyricist": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			}
		}
	}
	return q

def multi_match_and_sort_prefix(query, num, fields):
	print('multi_match_and_sort_prefix')
	q = {
		"size": num,
		"sort": [
			{"views": {"order": "desc"}},
		],
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "phrase_prefix"
			}
		},
                "aggs": {			
			"Music": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
			"Artist": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
			"Lyricist": {
				"terms": {
					"field": "lyricist.keyword",
					"size": 10
				}
			}
		}
	}
	return q
