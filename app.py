from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# In-memory list to simulate file storage
files = []

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            filename = request.form.get('filename')
            if filename:
                files.append(filename)
        return render_template('index.html', files=files)
    except Exception as e:
        app.logger.error("Error in index route: %s", e)
        return "Internal Server Error", 500

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    try:
        if index < len(files):
            if request.method == 'POST':
                new_name = request.form.get('filename')
                if new_name:
                    files[index] = new_name
                    return redirect(url_for('index'))
            return render_template('update.html', filename=files[index], index=index)
        return redirect(url_for('index'))
    except Exception as e:
        app.logger.error("Error in update route: %s", e)
        return "Internal Server Error", 500

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    try:
        if index < len(files):
            files.pop(index)
        return redirect(url_for('index'))
    except Exception as e:
        app.logger.error("Error in delete route: %s", e)
        return "Internal Server Error", 500

# When deployed on Vercel, __name__ will not be '__main__'
if __name__ == '__main__':
    app.run(debug=True)
