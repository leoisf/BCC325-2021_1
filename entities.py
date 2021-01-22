
class Agent:
    """Esta classe implementa uma interface para um agente"""

    def __init__(self, env):
        """ Construdor da classe Agent
            Args:
            env: referência para um ambinente
        """        
        self.env = env

    def act(self):
        """ 
            defien a ação do agente
            gera o erro NotImplementedError caso o método não for implementado ou sobrescrito
            
        """
        raise NotImplementedError('act')



class Environment:
    """Esta classe implementa uma interface para um ambiente"""
    
    def initial_percepts(self):
        """
            retorna a percepção inicial do ambiente
            gera o erro NotImplementedError caso o método não for implementado ou sobrescrito

        """
       raise NotImplementedError('initial_percepts')

    def signal(self, action):
         """
            retorna a percepção do ambiente após a execução da ação
            gera o erro NotImplementedError caso o método não for implementado ou sobrescrito

        """
        raise  NotImplementedError('signal')
