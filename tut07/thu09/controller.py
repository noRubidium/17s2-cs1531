from init import app, count
from compute import index_handler
# handle different request and distribute it to different function
@app.route("/")
def index():
    index_handler()
    # render the template
    return render_template("index.html", user_count=count.read_counter())
