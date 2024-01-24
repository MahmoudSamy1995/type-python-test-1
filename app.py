from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def autocomplete(query):
    url = f'http://suggestqueries.google.com/complete/search?client=firefox&q={query}'
    response = requests.get(url)
    suggestions = response.json()[1]
        # Simulate keyword suggestions (replace with actual logic)

        # Return the suggestions as JSON response
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/autocomplete/<query>', methods=['GET'])
# def autocomplete(query):
#     try:
#         url = f'http://suggestqueries.google.com/complete/search?client=firefox&q={query}'
#         response = requests.get(url)
#         suggestions = response.json()[1]

#         # Return the suggestions as JSON response
#         return jsonify({"suggestions": suggestions})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
