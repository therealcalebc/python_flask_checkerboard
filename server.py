from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<int:width>')
@app.route('/<int:width>/<int:height>')
@app.route('/<int:width>/<int:height>/<color1>')
@app.route('/<int:width>/<int:height>/<color1>/<color2>')
def play(width=8, height=8, color1='red', color2='black'):
	print("width: " + str(width))
	print("height: " + str(height))
	print("color1: " + color1)
	print("color2: " + color2)
	title = "Checkerboard"
	return render_template('index.html', title=title, width=width, height=height, color1=color1, color2=color2)

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('index.html', title='404', phrase='Sorry! No response. Try again.', num_times=1)

if __name__ == "__main__":
	app.run(debug=True)