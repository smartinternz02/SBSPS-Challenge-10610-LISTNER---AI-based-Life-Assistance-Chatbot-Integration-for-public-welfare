from flask import Flask,request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('classification_rf.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index',methods = ['POST'])
def pred():
    gender = request.form.get('gender')
    age = request.form.get('age')
    salary = request.form.get('salary')
    input = [[int(gender), int(age), float(salary)]]
    op = model.predict(input)
    print(op)
    return render_template('index.html',Output=str(op))

if __name__ == '__main__':
    app.run()