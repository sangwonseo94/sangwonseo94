
import feedparser
blog = "https://algorithmstudy-mju.tistory.com/rss"
rss_feed = feedparser.parse(blog)

MAX_POST_NUM = 10
latest_blog_post_list = ""
for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"


markdown_text = """  ### 
⚡ Email (Company) : sangwonseo@woorifis.com  
⚡ Email (Private) : gotkddnjs@naver.com  
⚡ Software Engineer in WooriFis ( Woori Finance Information System : Period 2020.12 ~ Now )  
⚡ My Blog Post  (https://algorithmstudy-mju.tistory.com/) """  
readme_text = f"{markdown_text}{latest_blog_post_list}"

tmp = """
⚡ [![github stats]  (https://github-readme-stats.vercel.app/api/top-langs/?username=sangwonseo94&layout=compact)](https://github.com/anuraghazra/github-readme-stats)](https://algorithmstudy-mju.tistory.com/)  
⚡ [![Solved.ac프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=gotkddnjs)](https://solved.ac/gotkddnjs)<!--[![CodeForces Profile](https://cf.leed.at?id=sangwon)](https://codeforces.com/profile/sangwon)   
"""
readme_text += tmp

with open("README.md", 'w', encoding='utf-8') as f: 
    f.write(readme_text)
