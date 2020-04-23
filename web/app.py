from flask import Flask, render_template



app = Flask(__name__)

@app.route("/<path:name>")

def respond(name):
    bad = ("~","//","..")
    good = ('.html','.css')
    if any(s in name for s in bad):
       abort(403)
    elif any(s in name for s in good):
        try:
            return render_template(name)
        except:
            abort(404)
    name.close()




@app.errorhandler(404)
@app.errorhandler(403)

def page_not_found(error):
   return render_template('404.html', title = '404'), 404

def page_is_forbidden(error):
   return render_template('403.html', title = '403'), 403




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


