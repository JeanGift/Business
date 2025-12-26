from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, static_folder='static', template_folder='.')

# Home → serve cover.html
@app.route("/")
def home():
    return render_template("cover.html")

# Secret admin route
@app.route("/voyager0x1")
def admin_secret():
    return render_template("admin.html")

# Block direct access to admin.html
@app.route("/admin.html")
def block_admin():
    abort(404)

# Serve any static file (CSS, JS, images)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Serve other public HTML pages normally (index.html, shop.html, etc.)
@app.route('/<path:page>')
def public_pages(page):
    if os.path.exists(page) and page.endswith(".html"):
        # Prevent admin.html from being accessed directly
        if page == "admin.html":
            abort(404)
        return render_template(page)
    abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
