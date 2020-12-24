"""
Author : Byunghyun Ban
Last Modification : 2020.12.25.
bhban@kakao.com
https://github.com/needleworm/pixabay_crawling
"""

import sys
import os
import pixabay_crawler as pc

# 검색 키워드
keyword = sys.argv[1]

# 이미지 장 수
numImages = int(sys.argv[2])

# 결과물을 저장할 폴더 이름
result_dir = sys.argv[3]
if result_dir not in os.listdir():
    os.mkdir(result_dir)

# 크롤링을 수행합니다
pc.crawling(keyword, numImages, result_dir)
