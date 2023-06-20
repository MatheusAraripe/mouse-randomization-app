from flask import Flask, render_template, request

from amostras import *
from binomial import *
from randcode import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mouse")
def mouse():
    return render_template("mouse.html")


@app.route("/tests")
def tests():
    return render_template("tests.html")

@app.route("/random", methods = ["POST"])
def random():

    data = int(request.json['user_input'])
    quant = int(request.json['quant'])

    groups_list = rand_func(data,quant)

    cont = 0
    resp = ""
    for e in groups_list:
        resp = resp + " --- " + "group " + str(cont+1) + ": " + str(e) 
        cont += 1
    
    return resp


@app.route("/T", methods = ["POST"])
def T():
    effect_size = request.json['user_input']
    #check effect size
    if effect_size == "":
        effect_size = 0.8
    else:
        effect_size = float(effect_size)

    alpha = (request.json['quant'])
    power = (request.json['quant2'])

    if alpha == "" or power == "":
        return "Please enter valid values for the arguments!"
    else:

        sample_size = teste_t(effect_size,alpha,power)

        resp = "Sample size: {} animals in group 1 and {} animals in group 2".format(sample_size, sample_size)

        return resp


@app.route("/anova", methods = ["POST"])
def anova():
    effect_size = request.json['user_input']

    if effect_size == "":
        effect_size = 0.8
    else:
        effect_size = float(effect_size)

    alpha = (request.json['quant'])
    poder_teste = (request.json['quant2'])
    n_groups = (request.json['groups'])

    if alpha == "" or poder_teste == "":
        return "Please enter valid values for the arguments!"
    else:

        n_groups=int(n_groups)
        
        sample_size = anova_sample_size(n_groups,alpha,poder_teste,effect_size)

        resp = "The total sample size is "+ str(sample_size)

        return resp


@app.route("/binomial", methods = ["POST"])
def binomial():
    
    entrada_alpha = (request.json['quant'])
    power = (request.json['quant2'])
    erro = (request.json['erro'])

    if entrada_alpha == "" or power == "" or erro == "":
        return "Please enter valid values for the arguments!"
    else:

        alpha = float(entrada_alpha)
        power = float(power)
        erro = float(erro)*100
        
        sample_size = binomial_sample_size(alpha,power,erro)

        resp = "Sample size: {} animals in group 1 and {} animals in group 2".format(int(sample_size/2), int(sample_size/2))


        return resp
        
#app.run(debug=True)
