from application import app
from flask import Flask, render_template, redirect, url_for
from application.model.entity.documento import Documentos


@app.route("/")
def index():
    return render_template("padrao.html")

@app.route("/financeiro")
def financeiro():
    return render_template("financeiro.html")

@app.route("/ti")
def ti():
    return render_template("ti.html")

@app.route("/rh")
def rh():
    return render_template("rh.html")

@app.route("/compras")
def compras():
    return render_template("compras.html")

@app.route("/engenharia")
def engenharia():
    return render_template("engenharia.html")

@app.route("/faturamento")
def faturamento():
    return render_template("faturamento.html")

@app.route("/admateriais")
def admateriais():
    return render_template("ADMateriais.html")


@app.route("/Fiscal")
def fiscal():
    return render_template("fiscal.html")

@app.route("/Manufatura")
def manufatura():
    return render_template("manufatura.html")

@app.route("/Contabil")
def contabil():
    return render_template("contabil.html")

@app.route("/Vendas")
def vendas():
    return render_template("vendas.html")

