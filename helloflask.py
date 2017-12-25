from flask import Flask
from flask import jsonify
import attraction
app=Flask(__name__)
@app.route('/')
def test_flask():
    return 'test_flask'

@app.route('/')
def spider_hot():
    spider=attraction.SpiderMain()
    attractions=spider.Crawl()
    return jsonify(attractions)

if __name__=='__main__':
 app.run()
