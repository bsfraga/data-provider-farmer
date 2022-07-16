from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sql_alchemy import session

Base = declarative_base()

class CompanyModel(Base):

    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(14), nullable=False)
    inscricao_estadual = Column(String(20), nullable=False)
    data_abertura = Column(String(10), nullable=False)
    site = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    cep = Column(String(10), nullable=False)
    endereco = Column(String(100), nullable=False)
    numero = Column(String(10), nullable=False)
    cidade = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    telefone_fixo = Column(String(20), nullable=False)
    celular = Column(String(20), nullable=False)

    def __init__(self, nome, cnpj, inscricao_estadual, data_abertura, site, email, cep, endereco, numero, cidade, bairro, estado, telefone_fixo, celular):
        self.nome = nome
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.data_abertura = data_abertura
        self.site = site
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.estado = estado
        self.telefone_fixo = telefone_fixo
        self.celular = celular

    def json(self):
        return {
            'nome': self.nome,
            'cnpj': self.cnpj,
            'inscricao_estadual': self.inscricao_estadual,
            'data_abertura': self.data_abertura,
            'site': self.site,
            'email': self.email,
            'cep': self.cep,
            'endereco': self.endereco,
            'numero': self.numero,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'estado': self.estado,
            'telefone_fixo': self.telefone_fixo,
            'celular': self.celular
        }

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def find_random(cls):
        return cls.query.order_by(func.random()).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, name):
        company = cls.query.filter_by(nome=name).first()
        session.delete(company)
        session.commit()