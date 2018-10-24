from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from model import Pessoa, Aluno

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'williamlingprog'
app.config["MONGO_URI"] = "mongodb://william:ufrj123@ds137581.mlab.com:37581/williamlingprog"
mongo = PyMongo(app)

@app.route('/')
def homepage():

    person_array = []
    person = mongo.db.persons
    cursor1 = person.find()
    for entry in cursor1:
        person_array.append(entry)

    student_array = []
    student = mongo.db.students
    cursor2 = student.find()
    for entry in cursor2:
        student_array.append(entry)

    # print (person_array)
    # print (student_array)

    return render_template("home.html", person_array=person_array, student_array=student_array)

@app.route('/insert')
def insert_page():
    return render_template("insert.html")

@app.route('/remove')
def remove_page():
    return render_template("remove.html")

@app.route('/in1', methods=['POST'])
def insert_person():
    global name1, idade1, telefone1
    name1 = str(request.form.get("name1"))
    idade1 = str(request.form.get("age1"))
    rg = str(request.form.get("rg1"))
    telefone1 = str(request.form.get("phone1"))
    pessoaAtual = Pessoa(name1, rg, idade1, telefone1)

    person = mongo.db.persons
    person.save({"name":pessoaAtual.getName(), "age":pessoaAtual.getAge(), "rg":pessoaAtual.getRG(), "phone":pessoaAtual.getPhone()})

    return redirect("/")

@app.route('/in2', methods=['POST'])
def insert_student():
    global name2, rg2, idade2, telefone2, codigo, p1, p2
    name2 = str(request.form.get("name2"))
    idade2 = str(request.form.get("age2"))
    rg2 = str(request.form.get("rg2"))
    telefone2 = str(request.form.get("phone2"))
    codigo = str(request.form.get("code"))
    p1 = float(request.form.get("p1"))
    p2 = float(request.form.get("p2"))
    dre = str(request.form.get("dre"))
    alunoAtual = Aluno(name2, rg2, idade2, telefone2, codigo, p1, p2, dre)

    student = mongo.db.students
    student.save({"name":alunoAtual.getName(), "age":alunoAtual.getAge(), "rg":alunoAtual.getRG(), "dre":alunoAtual.getDRE(), "phone":alunoAtual.getPhone(),
    "code":alunoAtual.getCode(),"p1":alunoAtual.getP1(),"p2":alunoAtual.getP2(), "mf":alunoAtual.getFinalGrade(),
    "sit":alunoAtual.getSituation()})

    return redirect("/")

@app.route('/out1', methods=['POST'])
def remove_person():
    rgout = str(request.form.get("out1"))
    person = mongo.db.persons
    person.remove({"rg":rgout})
    # for entry in cursor:
    #     id = entry['_id']
    # print (id)
    return redirect("/")

@app.route('/out2', methods=['POST'])
def remove_student():
    dreout = str(request.form.get("out2"))
    student = mongo.db.students
    student.remove({"dre":dreout})
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
