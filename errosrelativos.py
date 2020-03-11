import numpy
import numpy as np

def erroVerdadeiro(val,	x):
    Et	=	val	-	x
    return(Et)


def erroRelativo(val,	Et):
    et	=	(Et/val)	*	100
    return(et)

def erroRelativoAproximado(sol, solant):
    ea = (abs((sol - solant)/sol))*100
    return(ea)

y=22/7

Questao1_erroverdadeiro = erroVerdadeiro(val = np.pi,x = (22/7))
Questao1_errorelativo = erroRelativo(val = np.pi,Et = (Questao1_erroverdadeiro))

print(Questao1_erroverdadeiro)
print(Questao1_errorelativo)

k = 355

Questao2_erroverdadeiro = erroVerdadeiro(val = np.pi,x = k)
Questao2_errorelativo = erroRelativo(val = np.pi,Et = (Questao2_erroverdadeiro))

print(Questao2_erroverdadeiro)
print(Questao2_errorelativo)
