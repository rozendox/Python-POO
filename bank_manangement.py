from abc import ABC, abstractmethod, abst
from datetime import datetime            
                                         
                                         
class cliente:                           
    def __init__(self, endereco):        
        self.endereco = endereco         
        self.contas = []                 
                                         
    # Função para realizar transações    
    def realizar_transacao(self, conta, t
        transacao.registrar(conta)       
                                         
    # Função para adiconar contas        
    def adicionar_conta(self, conta):    
        self.contas.append(conta)        
                                         
class PessoaFisica(cliente):             
    def __init__(self, nome, data_nascime
        super().__init__(endereco)       
        self.nome = nome                 
        self.data_nascimento = data_nasci
        self.cpf = cpf                   
                                         
class Conta:                             
    def __init__(self, numero, cliente): 
        # propriedades privadas          
        self._saldo = 0                  
        self._numero = numero            
        self._agencia = "0001"           
        self._cliente = cliente          
        self._historico = Historico()    
                                         
    @classmethod                         
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)       
                                         
    @property                            
    def saldo(self):                     
        return self._saldo               
                                         
    @property                            
    def numero(self):                    
        return self._numero              
                                         
    @property                            
    def agencia(self):                   
        return self._agencia             
                                         
    @property                            
    def cliente(self):                   
        return self._cliente             
                                         
    @property                            
    def historico(self):                 
        return self.historico            
                                         
    def sacar(self, valor):              
        saldo = self.saldo               
        excedeu_saldo = valor > saldo    
                                         
        if excedeu_saldo:                
            print("\n@@@ Operação falhou!
                                         
        elif saldo > 0:                  
            self._saldo -= valor         
            print("\n Saque realizado com
                                         
        else:                            
            print("\n @@@ Operação falhou
                                         
    def depositar(self, valor):          
        if valor > 0:                    
            self._saldo += valor         
            print("Deposito realizado com
                                         
        else:                            
            print("@@@ Operação falhou! O
                                         
        return True                      
                                         
class ContaCorrente(Conta):              
    def __init__(self, numero, cliente, l
        super().__init__(numero, cliente)
        self.limite = limite             
        self.limite_saques = limite_saque
                                         
    def sacar(self, valor):              
        numero_saques = len(             
            [transacao for transacao in s
             if transacao["tipo"] == Saqu
                                         
        excedeu_limite = valor > self.lim
        excedeu_saques = numero_saques >=
                                         
        if excedeu_limite:               
            print("\n @@@ Operação falhou
                                         
        elif excedeu_saques:             
            print("\n @@@ Operação falhou
                                         
        else:                            
            return super().sacar(valor)  
                                         
        return False                     
                                         
    def __str__(self):                   
        return f"""\                     
            Agência:\t{self.agencia}     
            C/c:\t\t{self.numero}        
            Titular:\t{self.cliente.nome}
            """                          
                                         
class Historico:                         
    def __init__(self):                  
        self._transacoes = []            
                                         
    @property                            
    def transacoes(self):                
        return self._transacoes          
                                         
    def adicionar_transacao(self, transac
        self._transacoes.append(         
            {                            
                "Tipo": transacao.__class
                "Valor": transacao.valor,
                "data": datetime.now().st
            }                            
        )                                
                                         
class Transacao(ABC):                    
    @property                            
    @abstractproperty                    
    def valor(self):                     
        pass                             
                                         
    @abstractproperty                    
    def registrar(self, conta):          
        pass                             
                                         
class Saque(Transacao):                  
    pass                                 
                                         
class deposito(Transacao):               
    pass                                 
                                         
