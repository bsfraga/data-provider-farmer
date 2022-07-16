from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sql_alchemy import session

Base = declarative_base()

class PersonModel(Base):

    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    cpf = Column(String(14), nullable=False)
    rg = Column(String(20), nullable=False)
    data_nasc = Column(String(10), nullable=False)
    sexo = Column(String(10), nullable=False)
    signo = Column(String(20), nullable=False)
    mae = Column(String(100), nullable=False)
    pai = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)
    cep = Column(String(10), nullable=False)
    endereco = Column(String(100), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    telefone_fixo = Column(String(20), nullable=False)
    celular = Column(String(20), nullable=False)
    altura = Column(String(10), nullable=False)
    peso = Column(String(10), nullable=False)
    tipo_sanguineo = Column(String(2), nullable=False)
    cor = Column(String(20), nullable=False)

    def __init__(self, nome, idade, cpf, rg, data_nasc, sexo, signo, mae, pai, email, senha, cep, endereco, numero, bairro, cidade, estado, telefone_fixo, celular, altura, peso, tipo_sanguineo, cor):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.signo = signo
        self.mae = mae
        self.pai = pai
        self.email = email
        self.senha = senha
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.telefone_fixo = telefone_fixo
        self.celular = celular
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.cor = cor

    def json(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'cpf': self.cpf,
            'rg': self.rg,
            'data_nasc': self.data_nasc,
            'sexo': self.sexo,
            'signo': self.signo,
            'mae': self.mae,
            'pai': self.pai,
            'email': self.email,
            'senha': self.senha,
            'cep': self.cep,
            'endereco': self.endereco,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone_fixo': self.telefone_fixo,
            'celular': self.celular,
            'altura': self.altura,
            'peso': self.peso,
            'tipo_sanguineo': self.tipo_sanguineo
        }

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def find_random(cls):
        return cls.query.order_by(func.random()).first().json()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, nome):
        cls.query.filter_by(nome=nome).delete()
        session.commit()
