from flask import Flask, render_template, request

# Replace with your actual website data (title, URL)
websites = [
    ("Google", "https://www.google.com/"),
    ("Wikipedia", "https://www.wikipedia.org/"),
    ("Facebook", "https://www.facebook.com/"),
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", websites=websites)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()  # Convert query to lowercase for case-insensitive search
    filtered_websites = []
    for website in websites:
        if query in website[0].lower():  # Search website title (lowercase)
            filtered_websites.append(website)
    return render_template("search_results.html", websites=filtered_websites, query=query)

if __name__ == "__main__":
  app.run(debug=True)
