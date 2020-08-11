

def bayes( prob_E, prob_E_H, prob_H):
    return(prob_H*prob_E_H/prob_E)


if __name__=='__main__':
    prob_cancer=1/100000
    prob_sintoma_dado_cancer=1
    prob_sintoma_dado_no_cancer=10/99999
    prob_no_cancer=1- prob_cancer

    prob_sintomas=(prob_cancer*prob_sintoma_dado_cancer)+(prob_no_cancer*prob_sintoma_dado_no_cancer)
    prob_cancer_dado_sintoma= bayes(prob_sintomas, prob_sintoma_dado_cancer, prob_cancer)
    print(f'La probabilidad de tener cancer si tengo sintomas es de {prob_cancer_dado_sintoma}')