from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/get_lines', methods=['POST'])
def find_segment():
    act_number = int(request.form['actNum'])
    scene_number = int(request.form['sceneNum'])
    start_line = int(request.form['startLine'])
    end_line = int(request.form['endLine'])
    accumulated = []
    with open('static/the-merchant-of-venice.txt', 'r', encoding="utf8") as f:
        lines = [line.strip() for line in f]
        line_num = 1
        for i in range(len(lines)-1):
            inside = i + 2
            if lines[i].isnumeric() and lines[i+1].isnumeric() and int(lines[i]) == act_number and int(lines[i+1]) == scene_number:
                for j in range(len(lines)):
                    if start_line <= line_num <= end_line:
                        accumulated.append(lines[inside])
                    elif line_num > end_line:
                        break
                        line_num = 1
                    line_num+=1
                    inside+=1
    result = " ".join(accumulated)
    return render_template("results.html", output=result)


if __name__ == '__main__':
    app.run()
