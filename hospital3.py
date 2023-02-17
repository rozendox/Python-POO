import os
import pickle
import hashlib


class Paciente:
    def __init__(self, nome, idade, cpf, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Funcionario:
    def __init__(self, nome, idade, cpf, endereco, telefone, email, cargo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.cargo = cargo
class Agenda:
    def __init__(self):
        self.consultas = []
        self.cirurgias = []

    def marcar_consulta(self, paciente, data, hora):
        consulta = (paciente, data, hora)
        self.consultas.append(consulta)

    def marcar_cirurgia(self, paciente, data, hora):
        cirurgia = (paciente, data, hora)
        self.cirurgias.append(cirurgia)

class Hospital:
    def __init__(self):
        self.pacientes = []
        self.funcionarios = []
        self.agenda = Agenda()
        self.logged_in_user = None

    def cadastrar_paciente(self, nome, idade, cpf, endereco, telefone, email):
        paciente = Paciente(nome, idade, cpf, endereco, telefone, email)
        self.pacientes.append(paciente)

    def cadastrar_funcionario(self, nome, idade, cpf, endereco, telefone, email, cargo):
        funcionario = Funcionario(nome, idade, cpf, endereco, telefone, email, cargo)
        self.funcionarios.append(funcionario)

    def selecionar_tipo_procedimento(self, tipo_procedimento):
        if tipo_procedimento == "consulta":
            self.marcar_consulta()
        elif tipo_procedimento == "cirurgia":
            self.marcar_cirurgia()
        else:
            print("Tipo de procedimento inválido.")

    def marcar_consulta(self):
        if not self.logged_in_user:
            print("Você precisa fazer login para marcar uma consulta.")
            return

        paciente = self.selecionar_paciente()
        if not paciente:
            print("Paciente não encontrado.")
            return

