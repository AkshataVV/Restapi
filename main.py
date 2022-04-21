from flask import Flask,redirect, url_for, render_template, request, jsonify
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
     if request.method == "POST":
        message = request.form["msg"]
        return redirect(url_for("message", msg=message))
     else:
        return render_template("index.html")

@app.route("/<msg>")
def message(msg):
    z = list(msg)
    for x in range(2, len(z),3): 
      
     z[x] = z[x].upper()
     cap3 = ''.join(z)
    
    return f"<h1>{cap3}</h1>"

if __name__ == "__main__":
    app.run(debug=True)