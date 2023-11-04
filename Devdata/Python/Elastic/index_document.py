from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('http://lnxsrv1:9200')

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'APItijdstip': 'Sat, 24 Dec 2022 04:51:31 UTC',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", document=doc)
print(resp['result'])
