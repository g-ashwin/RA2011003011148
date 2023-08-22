from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_urls', methods=['GET'])
def process_urls():
    urls = request.args.getlist('url')  
    results = []

    for url in urls:
        results.append({"url": url})

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)