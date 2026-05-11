@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def api_status_redirect():
    return api_status()


@app.route("/api/v1/status")
def api_status():
