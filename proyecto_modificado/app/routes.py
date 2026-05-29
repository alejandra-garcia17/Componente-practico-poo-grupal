from flask import render_template

from app import app

from aprendizaje.bloque0 import Block0
from aprendizaje.bloque1 import Block1
from aprendizaje.bloque2 import Block2
from aprendizaje.bloque3 import Block3
from aprendizaje.bloque4 import Block4
from aprendizaje.bloque5 import Block5
from aprendizaje.bloque6 import Block6
from aprendizaje.bloque7 import Block7
from aprendizaje.bloque8 import Block8
from aprendizaje.bloque9 import Block9
from aprendizaje.bloque10 import Block10
from aprendizaje.bloque11 import Block11
from aprendizaje.bloque12 import Block12
from aprendizaje.bloque13 import Block13
from aprendizaje.bloque14 import Block14
from aprendizaje.bloque15 import Block15
from aprendizaje.bloque16 import Block16
from aprendizaje.bloque17 import Block17
from aprendizaje.bloque18 import Block18
from aprendizaje.bloque19 import Block19
from aprendizaje.bloque20 import Block20



@app.route("/")
def inicio():

    bloque = Block0()

    return render_template(
        "/index.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )


@app.route("/bloque1")
def bloque1():

    bloque = Block1()

    return render_template(
        "bloque1.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3(),
        ejercicio4=bloque.exercise4()
    )

@app.route("/bloque2")
def bloque2():

    bloque = Block2()

    return render_template(
        "bloque2.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )
@app.route("/bloque3")
def bloque3():

    bloque = Block3()

    return render_template(
        "bloque3.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )
@app.route("/bloque4")
def bloque4():

    bloque = Block4()

    return render_template(
        "bloque4.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )
@app.route("/bloque5")
def bloque5():

    bloque = Block5()

    return render_template(
        "bloque5.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque6")
def bloque6():

    bloque = Block6()

    return render_template(
        "bloque6.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque7")
def bloque7():

    bloque = Block7()

    return render_template(
        "bloque7.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque8")
def bloque8():

    bloque = Block8()

    return render_template(
        "bloque8.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1()
    )

@app.route("/bloque9")
def bloque9():

    bloque = Block9()

    return render_template(
        "bloque9.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque10")
def bloque10():

    bloque = Block10()

    return render_template(
        "bloque10.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )


@app.route("/bloque11")
def bloque11():

    bloque = Block11()

    return render_template(
        "bloque11.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque12")
def bloque12():

    bloque = Block12()

    return render_template(
        "bloque12.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque13")
def bloque13():

    bloque = Block13()

    return render_template(
        "bloque13.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque14")
def bloque14():

    bloque = Block14()

    return render_template(
        "bloque14.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )


@app.route("/bloque15")
def bloque15():

    bloque = Block15()

    return render_template(
        "bloque15.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3(),
        ejercicio4=bloque.exercise4()
    )

@app.route("/bloque16")
def bloque16():

    bloque = Block16()

    return render_template(
        "bloque16.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque17")
def bloque17():

    bloque = Block17()

    return render_template(
        "bloque17.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque18")
def bloque18():

    bloque = Block18()

    return render_template(
        "bloque18.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )

@app.route("/bloque19")
def bloque19():

    bloque = Block19()

    return render_template(
        "bloque19.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1(),
        ejercicio2=bloque.exercise2(),
        ejercicio3=bloque.exercise3()
    )
@app.route("/bloque20")
def bloque20():

    bloque = Block20()

    return render_template(
        "bloque20.html",
        bloque=bloque,
        ejercicio1=bloque.exercise1()
    )
