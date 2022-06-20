import os
from NHentai import NHentai
import re

nhentai = NHentai()

hentai = nhentai.search(query="382453" , page=1)

tags = hentai.title.english
print(tags)
# sorted_tags = {}
# tags_list = []

# for tag in tags:
    
#     if (tag.type in sorted_tags):
#         print(tag.type)
        
#     sorted_tags.update({tag.type : tag.name})
    
# print(sorted_tags)
