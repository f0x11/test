# coding=utf-8
from flask import Flask, request
from flask import render_template
app = Flask(__name__)
# app.template_folder = 'templates'

@app.route("/")
def hello():
    return render_template("horoscope.html")

CITY_MAP = {
    1: '桂林',
    2: '青岛',
    3: '长沙',
    4: '澳门',
    5: '周庄',
    6: '哈尔滨',
    7: '天津',
    8: '鼓浪屿',
    9: '长白山',
    10: '九寨沟',
    11: '宜兴',
    12: '三亚',
    13: '北戴河',
    14: '大理',
    15: '北京',
    16: '拉萨',
    17: '荔波',
    18: '北海',
}

MOOD_MAP = {
    "anlian": "哎呦我去，原来我在%s表白能追到TA啊",
    "wending": "还没到七年就痒了，我决定带TA去%s挠一挠",
    "relian": "谁也别拦我和TA去%s，到时候别怪我刷屏秀恩爱虐狗",
    "jiujie": "从%s回来我就坚定信念，还是和你凑合凑合吧，未来的说不定更丑",
}

@app.route("/result")
def result():
    return render_template("result.html", city_id=1, mood="anlian",
                           mood_name=MOOD_MAP[mood] % CITY_MAP.get(int(city_id), ""))

@app.route('/qq')
def qq():
    return render_template('qq.html')


@app.route('/topic')
def topics():
    return render_template('topic_list.html')


@app.route('/note')
def note():
    return render_template('note_list.html')


@app.route('/topic_manage')
def topic_manage():
    return render_template('topic_manage.html')


@app.route('/note')
def notes():
    return render_template('note_list.html')


@app.route('/login')
def shitouren():
    return render_template('weixin/login.html')


@app.route('/bp')
def bind_phone():
    return render_template('weixin/bind_phone.html')


@app.route('/upload', methods=['POST'])
def upload():
    request.form.get('files')


@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'GET':
        return render_template('manage/manage.html')


@app.route('/share', methods=['GEt'])
def share():
    return render_template('weixin/share.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=7777)
