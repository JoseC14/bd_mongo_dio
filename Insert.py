import pprint

import pymongo as pyM

uri = "mongodb+srv://JoseC:xxxxx@cluster0.ih675io.mongodb.net/?retryWrites=true&w=majority"

client = pyM.MongoClient(uri)

db = client.bank

clientes = db.clientes
contas = db.contas

clientes_data =[{
    "nome":"José Carlos",
    "endereco":"Sitio Lagoa",
    "CPF":"1234567890"
    },
    {
    "nome":"Maria",
    "endereco":"Bairro da Groove Street",
    "CPF":"1232881293"
    },
    {
    "nome":"Carlos João",
    "endereco":"Libert City",
    "CPF":"093487347384"
    }
    ]

# result = clientes.insert_many(clientes_data)
for cliente in clientes.find({}).sort("nome"):
    pprint.pprint(cliente)
