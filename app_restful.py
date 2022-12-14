from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [

    {
        'id': '0',
        'Nome':'Rafael',
        'Habilidades': ['Python', 'Flask']
    },

    {
        'id': '1',
        'Nome':'Augusto',
        'Habilidades': ['Django', 'Python']
     }
]

class devs (Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, Procure o adm da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return(response)
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem': 'Registro Excluido'}
class lista_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])



api.add_resource(habilidades, '/habilidades/')
api.add_resource(devs, '/dev/<int:id>/')
api.add_resource(lista_desenvolvedores, '/dev/')
if __name__ == '__main__':
    app.run(debug=True)