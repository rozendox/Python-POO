class Paciente:
    def __init__(self, nome, idade, telefone, endereco, historico):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
        self.historico = historico

        class Funcionario:
    def __init__(self, nome, idade, telefone, endereco, id_funcionario):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
        self.id_funcionario = id_funcionario
        
class Agenda:
    def __init__(self):
        self.agendamentos = []

    def agendar_consulta(self, paciente, funcionario, data, horario):
        agendamento = {"tipo": "Consulta", "paciente": paciente, "funcionario": funcionario, "data": data, "horario": horario}
        self.agendamentos.append(agendamento)

    def agendar_cirurgia(self, paciente, funcionario, data, horario):
        agendamento = {"tipo": "Cirurgia", "paciente": paciente, "funcionario": funcionario, "data": data, "horario": horario}
        self.agendamentos.append(agendamento)

    def listar_agendamentos(self):
        return self.agendamentos
      
class Hospital:
    def __init__(self):
        self.pacientes = []
        self.funcionarios = []
        self.agenda = Agenda()

    def cadastrar_paciente(self, nome, idade, telefone, endereco, historico):
        paciente = Paciente(nome, idade, telefone, endereco, historico)
        self.pacientes.append(paciente)

    def cadastrar_funcionario(self, nome, idade, telefone, endereco, id_funcionario):
        funcionario = Funcionario(nome, idade, telefone, endereco, id_funcionario)
        self.funcionarios.append(funcionario)

    def agendar_consulta(self, id_paciente, id_funcionario, data, horario):
        paciente = next((p for p in self.pacientes if p.id_paciente == id_paciente), None)
        funcionario = next((f for f in self.funcionarios if f.id_funcionario == id_funcionario), None)
        self.agenda.agendar_consulta(paciente, funcionario, data, horario)

    def agendar_cirurgia(self, id_paciente, id_funcionario, data, horario):
        paciente = next((p for p in self.pacientes if p.id_paciente == id_paciente), None)
        funcionario = next((f for f in self.funcionarios if f.id_funcionario == id_funcionario), None)
        self.agenda.agendar_cirurgia(paciente, funcionario, data, horario)

    def listar_agendamentos(self):
        return self.agenda.listar_agendamentos()
    
