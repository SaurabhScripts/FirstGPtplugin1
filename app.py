from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DUCKDUCKGO_API_URL = "https://api.duckduckgo.com/?q={query}&format=json"

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    response = requests.get(DUCKDUCKGO_API_URL.format(query=query))
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch search results"}), 500

    data = response.json()
    results = [{"title": result["Text"], "link": result["FirstURL"]} for result in data["Results"]]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

