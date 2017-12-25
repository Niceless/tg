from flask import Flask
from flask import jsonify
import attraction
app=Flask(__name__)
@app.route('/')
def hello_flask():
    return 'hello_flask'

@app.route('/')
def spider_hot():
    root_url='http://www.cncn.com/paihang/'
    spider=attraction.SpiderMain()
    attractions=spider.Crawl(root_url)
    return jsonify(attractions)

if __name__=='__main__':
 app.run()
