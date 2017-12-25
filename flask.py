from flask import Flask
from flask import jsonify
import test
app=Flask(__name__)
@app.route('/')
def test_flask():
    return 'test_flask'

@app.route('/')
def spider_hot():
    root_url='http:www.pythontab.com/'
    spider=test.attraction()
    attractions=spider.Crawl(root_url)
    return jsonify(attractions)

if __name__=='__main__':
 app.run()
