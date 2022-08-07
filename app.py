from App import create_website

app = create_website()

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")