#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Jogador import Jogador
from truco.game_logic.Problema.Baralho import Baralho
from truco.game_logic.Problema.Carta import Carta
from truco.game_logic.Problema.Time import Time
from truco.game_logic.TKinter import PlayerInterface
import random

class Mesa():

    def registrarTruco(self, set):
        self._truco = set
        return self._truco

    def registrarMao(self):
        """@ReturnType boolean"""
        self._maoAndamento = not(self._maoAndamento)
        return self._maoAndamento

    def registrarStatusRodada(self, status):
        """@ParamType aStatus boolean"""
        self._rodadaAndamento = status
        return self._rodadaAndamento
        

    def definirOrdem(self): 
        """@ReturnType Problema.Jogador[]"""
        if self._ordemRodada == []:
            nova_ordem = self._jogadores
        else:
            nova_ordem = [self._ordemRodada[1]]
            nova_ordem.append(self._ordemRodada[2])
            nova_ordem.append(self._ordemRodada[3])
            nova_ordem.append(self._ordemRodada[0])
        
        self._ordemRodada = nova_ordem
        return self._ordemRodada

    def encerramentoPartida(self):
        placar = [self._times[0].pegarPontuacao(),
                  self._times[1].pegarPontuacao()]
        
        if placar[0] >= 12 or placar[1] >= 12:
            # Partida acabou
            if placar[0] >= 12:
                vencedor = 'azul'
            else:
                vencedor = 'vermelho'
            self._PlayerInterface.AtualizarInterface()
            self._PlayerInterface.Notificar(f"FIM DE PARTIDA! TIME {vencedor} GANHOU")
            self._PlayerInterface.Notificar('O programa sera finalizado')
            self._PlayerInterface.main_window.destroy()
        # Partida continua
        
    def definirPartidaAndamento(self, aBoolean):
        self._partidaAndamento = aBoolean

    def registrarVencedor(self, aTime):
        self._vencedor = aTime

    def verificarRegistroRodadas(self):
        """@ReturnType list"""
        # return self._registroRodada
        maoEncerrada = False
        vencedor = None
        match len(self._registroRodada):
            case 1:
                #  Apenas uma rodada até o momento.
                pass
            case 2:
                #  Duas rodadas até o momento.
                if self._registroRodada[0] == self._registroRodada[1]:
                    maoEncerrada = True
                    vencedor = self._registroRodada[0]
            case 3:
                #  Três rodadas até o momento.
                maoEncerrada = True
                
                for resultado in self._registroRodada: 
                    temp = 0
                    for resultado1 in self._registroRodada:
                        if resultado1 == resultado:
                            temp = temp +1
                            if temp == 2:
                                vencedor = resultado
                                break 

        return [maoEncerrada, vencedor]
    
    def encerramentoRodada(self, jogador):
        
        cartaForte = self.comparaMonte()
        self.definirTopo(cartaForte)
        
        encerraRodada = self._jogadores[jogador].ehUltimo() 
        
        if encerraRodada:
            pontuaRodada = self.vencedorRodada(self._monte, self._topo)
            qualrodada= self.verificaRodada()
            self.registrarRodada(qualrodada, pontuaRodada) #!!
            if pontuaRodada == 0:
                vencedor = "Time azul vence a rodada"
            if pontuaRodada == 1:
                vencedor = "Time vermelho vence a rodada"
            self._PlayerInterface.Notificar(vencedor)
            self.registrarStatusRodada(False)
            
        return encerraRodada

    
    def encerramentoMao(self): # COMICAMENTE CONSISTENTE COM DIAGRAMAs
        maoEncerrada, vencedor = self.verificarRegistroRodadas()
        
        if maoEncerrada:
            self.adicionarPontuacaoTime(vencedor,self._valorMao)
            self._valorMao = 1 
            self.registrarMao()
            if vencedor == 0:
                printar = 'azul'
            else:
                printar = 'vermelho'
            self._PlayerInterface.Notificar(f'Time {printar} vence a mao')
            
        return [maoEncerrada, vencedor]

    def comparaMonte(self):
        """@ReturnType carta"""
        naipes = ["","paus","copa","espada","ouro"]
        seq = ["",4,5,6,7,'J','Q','K',1,2,3]
        cartaForte = Carta("", "")
        cartas_monte = self._monte
        for carta in cartas_monte:
            carta_temp = Carta(carta[0],carta[1])
            valorCarta = seq.index(carta_temp._valor)
            valorCartaForte = seq.index(cartaForte._valor)
            naipeCarta = naipes.index(carta_temp._naipe)
            naipeCartaForte = naipes.index(cartaForte._naipe)
            valorManilha = seq.index(self._manilha._valor)

            if valorCartaForte == valorManilha : 
                if valorCarta == valorManilha : #trativa caso a carta sendo analisada tenha valor de manilha
                    print("ENTREI NA TRATATIVA DE MANILHA NO MONTE")
                    if naipeCarta > naipeCartaForte:
                        cartaForte = carta_temp

            else: 
                print("ENTREI NA TRATATIVA SEM MANILHA NO MONTE")
                if valorCarta == valorManilha:
                    cartaForte = carta_temp
                else:
                    if valorCarta < valorCartaForte:
                        pass
                    elif valorCarta == valorCartaForte:
                        if naipeCarta > naipeCartaForte:
                            cartaForte = carta_temp
                    else:
                        # valorCarta > valorCartaForte
                        cartaForte = carta_temp
                
        return cartaForte




    def definirTopo(self, aCartaForte):
        """@ParamType aCartaForte int
        @ReturnType int"""
        self._topo = aCartaForte

    def pegarOrdem(self):
        return self._ordemRodada

    def vencedorRodada(self, aMonte, aCartaForte):
        posicao_vencedor = aMonte.index([aCartaForte._valor,aCartaForte._naipe])

        time_vencedor = posicao_vencedor % 2
        return time_vencedor

    def verificaRodada(self, *aRegistroRodadas):
        for rodada in aRegistroRodadas:
            
            if rodada == 1:
                # Time 1 venceu
                return 1
            elif rodada == 2:
                # Time 2 venceu
                return 2
            elif rodada == 3:
                # Rodada nao finalizada
                return 3

    def registrarRodada(self, aQualRodada, aVencedorRodada):
        self._registroRodada.append(aVencedorRodada)



    def adicionarPontuacaoTime(self, aTime, aPontos):
        self._times[aTime]._pontuacao = self._times[aTime]._pontuacao + aPontos


    def aumentarValorMao(self):
        if self._valorMao != 12:
            if self._valorMao == 1:
                self._valorMao = 3
            else:
                self._valorMao += 3


    def IniciarPartida(self, jogador_local): #!!
        #self._jogadores = jogadores
        self.DefinirTimes()
        self.EscolherDealer(jogador_local) 
        self._times[0].ZerarPlacar()
        self._times[1].ZerarPlacar()
        

    def DefinirTimes(self): 
        j = self._jogadores
        
        self._times[0]._jogadores = [j[0],j[2]]
        j[0]._time = 0
        j[2]._time = 0
        
        self._times[1]._jogadores = [j[1],j[3]]
        j[1]._time = 1
        j[3]._time = 1
        
        for jogador in self._jogadores:
            if jogador._nome == self._PlayerInterface.localPlayer._nome:
                self._PlayerInterface.localPlayer._time = jogador._time
        

    def EscolherDealer(self, jogador_local): 
            if jogador_local._position == 0:
                dealer = jogador_local.DefinirDealer() 


    def novaMao(self):
        self.limpaMonte()
        self.resetaTopo()
        Mao_registro =self.registrarMao()
        Rodada = self.registrarStatusRodada(True)
        self._valorMao = 1
        self._ordemRodada = self.definirOrdem() 
        self._baralho.embaralharCartas() 
        self.distribuirCartas()
        
        self._manilha = self._jogadores[0].definirManilha(self._baralho) 
        novas_maos = []
        for jogador in self._jogadores:
            nova_mao = []
            for carta in jogador._mao:
                valor = carta._valor
                naipe = carta._naipe
                nova_mao.append([valor,naipe])
            novas_maos.append(nova_mao)

        
        temp_mao = novas_maos[self._PlayerInterface.localPlayer._position]
        self._registroRodada = []
        self._PlayerInterface.localPlayer._mao = []
        carta1 = Carta(temp_mao[0][0],temp_mao[0][1])
        carta2 = Carta(temp_mao[1][0],temp_mao[1][1])
        carta3 = Carta(temp_mao[2][0],temp_mao[2][1])
        
        self._PlayerInterface.localPlayer._mao.append(carta1)
        self._PlayerInterface.localPlayer._mao.append(carta2)
        self._PlayerInterface.localPlayer._mao.append(carta3)

        self._PlayerInterface.AtualizarInterface()
        novo_estado = {'tipo': 'NovaMao', 'nova_mao': novas_maos, 'turno_mao':1, 'manilha': self._manilha._valor}
        self._PlayerInterface.Notificar(str("Nova Mão Iniciada\n Turno de " + self._PlayerInterface.localPlayer._nome))
        self._PlayerInterface.localPlayer._seuTurno = True
        self._PlayerInterface.enviarAtualizacaoPartida(novo_estado)



    def distribuirCartas(self): 

        i = 0 
        for jogador in self._jogadores:
            carta1 = self._baralho._cartas[i]
            i = i+1
            carta2 = self._baralho._cartas[i]
            i = i+1
            carta3 = self._baralho._cartas[i]
            i = i+1
            jogador._mao = [carta1, carta2, carta3]
        

    def novaRodada(self):
        self._PlayerInterface.Notificar(str("Nova Rodada Iniciada\n Turno de " + self._PlayerInterface.localPlayer._nome))
        rodadaAndamento = self.registrarStatusRodada(True)
        
        novoEstado = {'tipo':'rodada', 'rodadaAndamento':rodadaAndamento}
        self._PlayerInterface.enviarAtualizacaoPartida(novoEstado)
        self._PlayerInterface.AtualizarInterface()
        self._PlayerInterface.localPlayer._seuTurno = True

    def ColocarNaMesa(self, cardIndex, jogador): 
        carta = jogador._mao[cardIndex]
        jogador._mao[cardIndex] = None
        carta = [carta._valor,carta._naipe]
        self._monte.append(carta) 
        self._PlayerInterface.localPlayer._mao[cardIndex] = None
        return carta

    def PassarTurno(self, jogador):
        jogador._seuTurno = False
        proximo = (jogador._position + 1) % 4
        for player in self._jogadores:
            if player._position == proximo:
                return player._nome

    def QuemResponde(self):
        proximo = (self._PlayerInterface.localPlayer._position + 1) % 4
        for player in self._jogadores:
            if player._position == proximo:
                return player._nome

    def ClicarBotaoTruco(self, jogador):
        turno = jogador.verificarTurno()
        print('PEÇO TRUCO')
        if turno:
            truco = self.VerificarTrucoAndamento()
            if not truco:
                self.registrarTruco(True)
                quemResponde = self.QuemResponde()
                self._PlayerInterface.Notificar('Você pediu truco, aguardando resposta adversária')
                novoEstado = {'tipo' : 'truco', 'time' : jogador._time, 'respondido' : False, 'quemResponde' : quemResponde}
                self._PlayerInterface.enviarAtualizacaoPartida(novoEstado)
            else:
                self._PlayerInterface.Notificar("Jogada de truco em andamento")
        else:
            self._PlayerInterface.Notificar("Não é seu turno")

    def VerificarTrucoAndamento(self):
        """@ReturnType boolean"""
        return self._truco

    def receberJogada(self, aJogada):
        """@ParamType aJogada Dict{string, any}"""
        if 'tipo' in aJogada.payload:
        
            if aJogada.payload['tipo'] == 'NovaMao' and aJogada.payload['turno_mao'] == self._PlayerInterface.localPlayer._position:
                self.limpaMonte()
                self.resetaTopo()
                temp_mao = aJogada.payload['nova_mao'][(self._PlayerInterface.match_position)]
                self._PlayerInterface.localPlayer.limpaMao()
                self._valorMao = 1          
                carta1 = Carta(temp_mao[0][0],temp_mao[0][1])
                carta2 = Carta(temp_mao[1][0],temp_mao[1][1])
                carta3 = Carta(temp_mao[2][0],temp_mao[2][1])

                self._PlayerInterface.localPlayer._mao.append(carta1)
                self._PlayerInterface.localPlayer._mao.append(carta2)
                self._PlayerInterface.localPlayer._mao.append(carta3)
                
                self.setManilha(aJogada.payload['manilha'])

                self._PlayerInterface.AtualizarInterface()

                if self._PlayerInterface.localPlayer._position != 3:
                    turno = (self._PlayerInterface.localPlayer._position + 1)
                    self._PlayerInterface.enviarAtualizacaoPartida({'tipo': 'NovaMao', 'nova_mao': aJogada.payload['nova_mao'], 'turno_mao':turno, 'manilha': self._manilha._valor})
               
    
            elif aJogada.payload['tipo'] == 'rodada':
                
                self._PlayerInterface.AtualizarInterface()
                self._PlayerInterface.Notificar("Nova Rodada Iniciada")
                self.registrarStatusRodada(True)
        
            elif aJogada.payload['tipo'] == 'carta':
                

                temp_monte = aJogada.payload['monte']
                if len(temp_monte) > 4:
                    new_monte = []
                    for carta in temp_monte:
                        if carta in self._monte:
                            pass
                        else:
                            new_monte.append(carta)
                    self._monte = new_monte
                else:
                    for carta in temp_monte:
                        if carta not in self._monte:
                            self._monte.append(carta)
                
                cartaForte = self.comparaMonte()
                self.definirTopo(cartaForte)
                # self._topo = cartaForte
                self._PlayerInterface.AtualizarInterface()

                if aJogada.payload['rodadaEncerrada'] == True:
                    vence = aJogada.payload['vencedor_rodada']

                    if vence == 0:
                        printar = 'azul'
                    else:
                        printar = 'vermelho'

                    if aJogada.payload['maoEncerrada']:
                        self.registrarMao()
                        vence = aJogada.payload['vencedor_mao']
                        self.adicionarPontuacaoTime(vence, self._valorMao)
                        self.limpaRegistroRodada()
                        self.limpaMonte()
                        self.resetaTopo()
                        
                        self._PlayerInterface.AtualizarInterface()
                        self._PlayerInterface.Notificar(f'Time {printar} vence a mao')
                        self.encerramentoPartida()
                        if self._PlayerInterface.localPlayer._dealer:
                            self.novaMao()

                    else:
                        self.registrarStatusRodada(False)
                        self._PlayerInterface.Notificar(f'Time {printar} vence a rodada')
                        qualRodada = None 
                        self.registrarRodada(qualRodada,vence) 
                        self.limpaMonte()
                        self.resetaTopo()
                        
                        self._PlayerInterface.AtualizarInterface()
                        if self._PlayerInterface.localPlayer._dealer:
                            self.novaRodada()
                    
                else:
                    if aJogada.payload['proximo'] == self._PlayerInterface.localPlayer._nome:
                        self._PlayerInterface.AtualizarInterface()
                        self._PlayerInterface.Notificar(f'Turno de {aJogada.payload["proximo"]}') 
                        self._PlayerInterface.localPlayer._seuTurno = True
                
            elif aJogada.payload['tipo'] == 'truco':
                print(aJogada.payload['time'])
                print(self._PlayerInterface.localPlayer._time)
                if aJogada.payload['time'] == self._PlayerInterface.localPlayer._time:
                    if aJogada.payload['respondido']:
                        if aJogada.payload['resposta'] == 'correr':
                            print(f'sou aliado de quem pediu truco meu time é {self._PlayerInterface.localPlayer._time}')
                            self.adicionarPontuacaoTime(self._PlayerInterface.localPlayer._time, self._valorMao)
                            self.registrarMao()
                            self.registrarTruco(False)
                            self._PlayerInterface.Notificar('O adversário correu do truco, seu time pontua')
                            self.encerramentoPartida()
                            if self._PlayerInterface.localPlayer._dealer:
                                self.novaMao()
                                
                        elif aJogada.payload['resposta'] == 'aceitar':
                            self.aumentarValorMao()
                            print(f'valor da mao em {self._valorMao}, aceitar aliado')
                            self.registrarTruco(False)
                            self._PlayerInterface.Notificar('O adversário aceitou o truco, quem pediu truco deve jogar')
    
                        elif aJogada.payload['resposta'] == 'aumentar':
                            self.aumentarValorMao()
                            print(f'valor da mao em {self._valorMao}, aumentar aliado')
                            self._PlayerInterface.Notificar('Seu aliado pediu aumento ao truco adversário, aguardando resposta')
                    else:
                        self._PlayerInterface.Notificar('Seu aliado pediu truco, aguardando resposta adversária')
                else:
                    if not aJogada.payload['respondido']:
                        if aJogada.payload['quemResponde'] == self._PlayerInterface.localPlayer._nome:
                            self._PlayerInterface.localPlayer.setQuemResponde(True)
                            self._PlayerInterface.Notificar('O time adversário pediu truco e você deve responder')
                        else:
                            self._PlayerInterface.Notificar('O adversário pediu truco e seu aliado deve responder, aguardando resposta aliada')
                    else:
                        if aJogada.payload['resposta'] == 'correr':
                            print(f'sou adversario de quem pediu truco, meu time NÃO é {self._PlayerInterface.localPlayer._time}')
                            self.adicionarPontuacaoTime(aJogada.payload['time'], self._valorMao)
                            self.registrarMao()
                            self.registrarTruco(False)
                            self._PlayerInterface.Notificar('Seu aliado correu do truco, time adversário pontua')
                            self.encerramentoPartida()
                            if self._PlayerInterface.localPlayer._dealer:
                                self.novaMao()
                            
                        elif aJogada.payload['resposta'] == 'aceitar':
                            self.aumentarValorMao()
                            print(f'valor da mao em {self._valorMao}, aceitar adversario')
                            self.registrarTruco(False)
                            self._PlayerInterface.Notificar('O adversário aceitou o truco, quem pediu truco deve jogar sua carta')
                        
                        elif aJogada.payload['resposta'] == 'aumentar':
                            self.aumentarValorMao()
                            print(f'valor da mao em {self._valorMao}, aumentar adversario')
                            if aJogada.payload['quemResponde'] == self._PlayerInterface.localPlayer._nome:
                                self._PlayerInterface.Notificar('O advérsario pediu aumento do truco, e você deve responder')
                                self._PlayerInterface.localPlayer.setQuemResponde(True)
                            else:
                                self._PlayerInterface.Notificar('O advérsario pediu aumento do truco, e seu aliado deve responder')
                self._PlayerInterface.AtualizarInterface()

    def botaoResposta(self, resposta):
        if self._PlayerInterface.localPlayer.quemResponde:
            quemResponde = None
            if resposta == 'correr':
                self._PlayerInterface.Notificar(f'Você correu, time adversário pontua')
                self.registrarMao()
                if self._PlayerInterface.localPlayer._time == 0:
                    pontua = 1
                else:
                    pontua = 0 
                self.adicionarPontuacaoTime(pontua , self._valorMao)
            
                if self._PlayerInterface.localPlayer._time == 0:
                    time = 1
                else:
                    time = 0
                self.registrarTruco(False)
            elif resposta == 'aceitar':
                if self._PlayerInterface.localPlayer._time == 0:
                    time = 1
                else:
                    time = 0
                self._PlayerInterface.Notificar(f'Você respondeu {resposta}, aguardando ação adversária')    
                self.aumentarValorMao()
                self.registrarTruco(False)
            elif resposta == 'aumentar':
                time = self._PlayerInterface.localPlayer._time
                
                self.aumentarValorMao()
                quemResponde = self.QuemResponde()
                self._PlayerInterface.Notificar(f'Você respondeu {resposta}, aguardando ação adversária')
            
            
            
            self._PlayerInterface.localPlayer.setQuemResponde(False)
            novoEstado = {'tipo' : 'truco', 'time' : time, 'respondido' : True , 'resposta' : resposta, 'quemResponde' : quemResponde}
            self._PlayerInterface.enviarAtualizacaoPartida(novoEstado)
            self._PlayerInterface.AtualizarInterface()
            self.encerramentoPartida()
            
    def setInicializada(self, set):
        self._Inicializada = set
        
    def getRegistroRodada(self):
        return self._registroRodada.copy()
    
    def limpaMonte(self):
        self._monte.clear()
        
    def resetaTopo(self):
        self._topo = Carta(4,'ouro')
        
    def limpaRegistroRodada(self):
        self._registroRodada.clear()
        
    def setManilha(self, manilha):
        temp_manilha = manilha
        new_manilha = Carta(temp_manilha,'ouro')
        self._manilha = new_manilha
            
    def __init__(self, deck, time1, time2, interface):
        self._jogadores = []

        self._Inicializada = False
        """@AttributeType Problema.Jogador"""
        self._baralho = deck
        """@AttributeType Problema.Baralho"""
        self._manilha = Carta('','')
        """@AttributeType Problema.Carta"""
        self._valorMao = 1
        """@AttributeType int"""
        self._partidaAndamento = False

        self._topo = Carta(4,'ouro')
        """@AttributeType boolean"""
        self._times = [time1,time2]
        """@AttributeType Problema.Time"""
        self._rodadaAndamento = None
        """@AttributeType boolean"""
        self._maoAndamento = None
        """@AttributeType boolean"""
        self._truco = False
        """@AttributeType boolean"""
        self._monte = []
        """@AttributeType Problema.Carta*"""
        self._registroRodada = []
        """@AttributeType int*"""
        self._ordemRodada = []
        """@AttributeType Problema.Jogador*"""
        self._placar = None
        """@AttributeType int*"""
        self._vencedor = None
        """@AttributeType Problema.Time"""
        self._PlayerInterface = interface
        """@AttributeType TKinter.PlayerInterface
        # @AssociationType TKinter.PlayerInterface"""
        self._unnamed_Jogador_3 = None
        """@AttributeType Problema.Jogador
        # @AssociationType Problema.Jogador
        # @AssociationKind Aggregation"""
        self._unnamed_Baralho_ = None
        """@AttributeType Problema.Baralho
        # @AssociationType Problema.Baralho
        # @AssociationKind Aggregation"""
        self._unnamed_Time_ = []
        """@AttributeType Problema.Time*
        # @AssociationType Problema.Time[]
        # @AssociationMultiplicity 2
        # @AssociationKind Aggregation"""

