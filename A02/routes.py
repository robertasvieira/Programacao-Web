#Importa as classes Flask e render_template do módulo flask
from flask import Flask, render_template

#Cria uma instância da aplicação Flask
app = Flask(__name__)

#Define uma rota para a página inicial
@app.route('/')

#Renderiza o template 'home.html' ao acessar a rota '/'
def homepage():
    return render_template('home.html')

#Define uma rota para a página da Clínica 1
@app.route('/clinica1')

def clinica1():
    #Define dados fictícios para a Clínica da Visão
    dados = {"nome": "Clínica da Visão",  
            "especialidade": "Oftalmologia",
            "medicos": " Doutor Kleber Sathler, Doutora Marielle Araujo e Doutor Jefferson Gonçalves",
            "convenios": "UNIMED, CASSI e Promed",
            "pagamento": "Dinheiro, PIX, cartão de débito e crédito",
            "email": "clinicadavisao@gmail.com",
            "telefone": "(33) 3731-4401",
            "endereco": "Rua José Antônio Araújo, 556 - Vila Magnólia, Araçuaí - MG"
            }
    #Renderiza o template 'clinica.html' e passa os dados como parâmetro
    return render_template('clinica.html', dados=dados)

#Se o script estiver sendo executado diretamente, inicia a aplicação Flask em modo de depuração
if __name__ == "__main__":
    app.run(debug=True)
