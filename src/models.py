import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#class Person(Base):
#    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    name = Column(String(250), nullable=False)

#class Address(Base):
#    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
#    id = Column(Integer, primary_key=True)
#    street_name = Column(String(250))
#    street_number = Column(String(250))
#    post_code = Column(String(250), nullable=False)
#    person_id = Column(Integer, ForeignKey('person.id'))
#    person = relationship(Person)
#
#    def to_dict(self):
#        return {}


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(15), nullable=False)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    suscripcion = Column(DateTime)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)
    clima = Column(String(20), nullable=False)
    terreno = Column(String(20), nullable=False)
    poblacion = Column(Integer)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    genero = Column(String(10), nullable=False)
    edad = Column(Integer)

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    modelo = Column(String(30), nullable=False)
    costo = Column(Integer)
    pasajeros = Column(Integer)

class Favorito(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planeta = relationship(Planeta)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    personaje = relationship(Personaje)
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'))
    vehiculo = relationship(Vehiculo)

    def to_add(self):
        return {}






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
