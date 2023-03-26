from abc import ABC, abstractmethod, abstractproperty                                              
from datetime import datetime                                                                      
                                                                                                   
                                                                                                   
class cliente:                                                                                     
    def __init__(self, endereco):                                                                  
        self.endereco = endereco                                                                   
        self.contas = []                                                                           
                                                                                                   
    # Função para realizar transações                                                              
    def realizar_transacao(self, conta, transacao):                                                
        transacao.registrar(conta)                                                                 
                                                                                                   
    # Função para adiconar contas                                                                  
    def adicionar_conta(self, conta):                                                              
        self.contas.append(conta)                                                                  
                                                                                                   
class PessoaFisica(cliente):                                                                       
    def __init__(self, nome, data_nascimento, cpf, endereco):                                      
        super().__init__(endereco)                                                                 
        self.nome = nome                                                                           
        self.data_nascimento = data_nascimento                                                     
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
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")                     
                                                                                                   
        elif saldo > 0:                                                                            
            self._saldo -= valor                                                                   
            print("\n Saque realizado com sucesso")                                                
                                                                                                   
        else:                                                                                      
            print("\n @@@ Operação falhou,! O valor informado é invalido.@@@")                     
                                                                                                   
    def depositar(self, valor):                                                                    
        if valor > 0:                                                                              
            self._saldo += valor                                                                   
            print("Deposito realizado com sucesso")                                                
                                                                                                   
        else:                                                                                      
            print("@@@ Operação falhou! O valor informado é invalido. @@@")                        
                                                                                                   
        return True                                                                                
                                                                                                   
class ContaCorrente(Conta):                                                                        
    def __init__(self, numero, cliente, limite = 500, limite_saques=3):                            
        super().__init__(numero, cliente)                                                          
        self.limite = limite                                                                       
        self.limite_saques = limite_saques                                                         
                                                                                                   
    def sacar(self, valor):                                                                        
        numero_saques = len(                                                                       
            [transacao for transacao in self.historico.transacoes                                  
             if transacao["tipo"] == Saque.__name__])                                              
                                                                                                   
        excedeu_limite = valor > self.limite                                                       
        excedeu_saques = numero_saques >= self.limite_saques                                       
                                                                                                   
        if excedeu_limite:                                                                         
            print("\n @@@ Operação falhou! O valor do saque exede o limite! @@@")                  
                                                                                                   
        elif excedeu_saques:                                                                       
            print("\n @@@ Operação falhou! Numero máximo de saques excedido! @@@")                 
                                                                                                   
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
                                                                                                   
    def adicionar_transacao(self, transacao):                                                      
        self._transacoes.append(                                                                   
            {                                                                                      
                "Tipo": transacao.__class__.__name__,                                              
                "Valor": transacao.valor,                                                          
                "data": datetime.now().strftime("%d-%m-%y %H:%M:%s"),                              
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
                                                                                                   
                                                                                                   
                                                                                                     
