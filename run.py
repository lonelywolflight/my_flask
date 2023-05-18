from my_app import app
app.env = "development"
app.debug = True
if __name__ == "__main__":
    app.run()