#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import simpledialog, messagebox
from truco.game_logic.Problema.Jogador import Jogador
from truco.game_logic.Problema.Mesa import Mesa
from truco.game_logic.Problema.Baralho import Baralho
from truco.game_logic.Problema.Time import Time
from truco.game_logic.Problema.Carta import Carta
import os
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener

class PlayerInterface(PyNetgamesServerListener):

    def __init__(self):
        self.main_window = Tk()

        deck = Baralho() 
        time1 = Time(0) 
        time2 = Time(1) 
        self._table = Mesa(deck, time1, time2, self) 
        self._table._baralho = deck 
        self.localPlayer = Jogador(self._table) 
        self.remotePlayers = [] 
        nome = self.SolicitarNomeJogador()
        self.localPlayer.RegistrarNome(nome)
        self._topo = Carta(4,'ouro')

     #----------------------- Pynetgames ----------------------------------->
        self.add_listener()
        self.send_connect()
      #<----------------------- Pynetgames ----------------------------------
      
        self.main_window.mainloop() 
        #------------------ final do initialize-------------------#
        
        
        """@AttributeType TKinter.PhotoImage"""
        self._front_card = None
        """@AttributeType TKinter.PhotoImage"""
        self._card_deck = None
        """@AttributeType TKinter.PhotoImage"""
        self._logo_label = None
        """@AttributeType TKinter.Label"""
        self._botao_aceitar = None
        """@AttributeType TKinter.Button"""
        self._botao_aumentar = None
        """@AttributeType TKinter.Button"""
        self._botao_correr = None
        """@AttributeType TKinter.Button"""
        self._botao_truco = None
        """@AttributeType TKinter.Button"""
        self._unnamed_PhotoImage_ = None

        
        """@AttributeType TKinter.PhotoImage
        # @AssociationType TKinter.PhotoImage
        # @AssociationKind Aggregation"""
        self._unnamed_Label_ = None
        """@AttributeType TKinter.Label
        # @AssociationType TKinter.Label
        # @AssociationKind Aggregation"""
        self._unnamed_Frame_ = None
        """@AttributeType TKinter.Frame
        # @AssociationType TKinter.Frame
        # @AssociationKind Aggregation"""
        self._unnamed_Tk_ = None
        """@AttributeType TKinter.Tk
        # @AssociationType TKinter.Tk
        # @AssociationKind Aggregation"""
        self._unnamed_Mesa_ = None
        """@AttributeType Problema.Mesa
        # @AssociationType Problema.Mesa
        # @AssociationKind Aggregation"""
        self._unnamed_Button_ = None
        """@AttributeType TKinter.Button
        # @AssociationType TKinter.Button
        # @AssociationKind Aggregation"""
        self._unnamed_Tk_2 = None
        """@AttributeType TKinter.Tk
        # @AssociationType TKinter.Tk
        # @AssociationKind Aggregation"""
        self._unnamed_Frame_2 = []
        """@AttributeType TKinter.Frame*
        # @AssociationType TKinter.Frame[]
        # @AssociationMultiplicity 6
        # @AssociationKind Aggregation"""
        self._unnamed_Label_2 = None
        """@AttributeType TKinter.Label
        # @AssociationType TKinter.Label
        # @AssociationKind Aggregation"""
        self._unnamed_PhotoImage_2 = []
        """@AttributeType TKinter.PhotoImage*
        # @AssociationType TKinter.PhotoImage[]
        # @AssociationMultiplicity 3
        # @AssociationKind Aggregation"""
        self._unnamed_Button_2 = []
        """@AttributeType TKinter.Button*
        # @AssociationType TKinter.Button[]
        # @AssociationMultiplicity 4
        # @AssociationKind Aggregation"""



    def fill_main_window(self):
        self.main_window.title("Truco")
        self.main_window.geometry("1366x768")
        self.main_window["bg"]="#046307"
      
        self.player1_frame = Frame(self.main_window, padx=150, pady=20, bg="#046307")
        self.player1_frame.grid(row=2, column=1)
            
        self.player2_frame = Frame(self.main_window, padx=10, pady=20, bg="#046307")
        self.player2_frame.grid(row=1, column=0)
        
        self.player3_frame = Frame(self.main_window, padx=150, pady=20, bg="#046307")
        self.player3_frame.grid(row=0, column=1)
        
        self.player4_frame = Frame(self.main_window, padx=10, pady=20, bg="#046307")
        self.player4_frame.grid(row=1, column=2)
        
        self.mesa_frame = Frame(self.main_window, padx=150, pady=80, bg="#046307")
        self.mesa_frame.grid(row=1, column=1)
        
        self.placar_frame = Frame(self.main_window, padx=30, pady=30, bg="#046307")
        self.placar_frame.grid(row=0, column=0)

        # Nome do jogador local
        self.logo_label = Label(self.player1_frame, text=self.localPlayer._nome, font="arial 24", bg="#046307")
        self.logo_label.grid(row=0, column=3)

        
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_pai = os.path.dirname(diretorio_atual)
        diretorio_imagens = os.path.join(diretorio_pai,"images")
        self._back_card = PhotoImage(file=os.path.join(diretorio_imagens,"back_card2.png"))
        
        self.front_card = PhotoImage(file=os.path.join(diretorio_imagens,"a-espada.png")) 
        self.card_deck = PhotoImage(file=os.path.join(diretorio_imagens, "card_deck.png")) 

        # Imagem das cartas dos jogador 1

        self.botao_correr = Button(self.player1_frame, bd = 3, text="Correr", command= lambda:self.botaoResposta('correr'))
        self.botao_correr.grid(row=1, column=0)

        self.botao_aumentar = Button(self.player1_frame, bd = 3, text="Aumentar", command=lambda:self.botaoResposta('aumentar'))
        self.botao_aumentar.grid(row=1, column=1)

        self.cartas_viradas = Button(self.player1_frame, bd = 3, image=self._back_card, command=lambda:self.clicarCarta(0))
        self.cartas_viradas.grid(row=1, column=2)

        self.cartas_viradas1 = Button(self.player1_frame, bd = 3, image=self._back_card, command=lambda:self.clicarCarta(1))
        self.cartas_viradas1.grid(row=1, column=3)

        self.cartas_viradas2 = Button(self.player1_frame, bd = 3, image=self._back_card, command=lambda: self.clicarCarta(2))
        self.cartas_viradas2.grid(row=1, column=4)

        self.botao_truco = Button(self.player1_frame, bd = 3, text="Truco", command=lambda:self.ClicarBotaoTruco())
        self.botao_truco.grid(row=1, column=5)

        self.botao_aceitar = Button(self.player1_frame, bd = 3, text="Aceitar", command=lambda:self.botaoResposta('aceitar'))
        self.botao_aceitar.grid(row=1, column=6)
        
        

        # Mesa frame
        self.logo_label = Label(self.mesa_frame, bd = 0, image=self._back_card)
        self.logo_label.grid(row=0, column=0)
        self.logo_label = Label(self.mesa_frame, bd = 0, image=self.card_deck)
        
        self.logo_label.grid(row=0, column=1)
        self.logo_label = Label(self.mesa_frame, bd = 0, image=self._back_card)
        self.logo_label.grid(row=0, column=2)

        
        if len(self.remotePlayers) ==3: 

            aux = self.remotePlayers
            aux.append((self.localPlayer._nome, self.match_position))

            for nome,posicao in self.remotePlayers:

                if nome == self.localPlayer._nome:
                    pass
                if posicao == (self.match_position +1 )% 4:
                    nome_esquerda = nome
                if posicao == (self.match_position +2) %4:
                    nome_frente = nome
                if posicao == (self.match_position +3) %4:
                    nome_direita = nome

            #-----------------------Espaço jogador esquerda-------------------------------------------------#
            self.logo_label = Label(self.player2_frame, text=nome_esquerda, font="arial 24", bg="#046307")
            self.logo_label.grid(row=0, column=1)

            self.cartas_viradas = Label(self.player2_frame, bd = 0, image=self._back_card)
            self.cartas_viradas.grid(row=1, column=0)

            self.cartas_viradas1 = Label(self.player2_frame, bd = 0, image=self._back_card)
            self.cartas_viradas1.grid(row=1, column=1)

            self.cartas_viradas2 = Label(self.player2_frame, bd = 0, image=self._back_card)
            self.cartas_viradas2.grid(row=1, column=2)
            #-----------------------------------------------------------------------------------------------#



            #-----------------------Espaço jogador frente---------------------------------------------------#
            self.logo_label = Label(self.player3_frame, text=nome_frente, font="arial 24", bg="#046307")
            self.logo_label.grid(row=0, column=1)

            self.cartas_viradas = Label(self.player3_frame, bd = 0, image=self._back_card)
            self.cartas_viradas.grid(row=1, column=0)

            self.cartas_viradas1 = Label(self.player3_frame, bd = 0, image=self._back_card)
            self.cartas_viradas1.grid(row=1, column=1)

            self.cartas_viradas2 = Label(self.player3_frame, bd = 0, image=self._back_card)
            self.cartas_viradas2.grid(row=1, column=2)
            #-----------------------------------------------------------------------------------------------#



            #-----------------------Espaço jogador direita--------------------------------------------------#
            self.logo_label = Label(self.player4_frame, text=nome_direita, font="arial 24", bg="#046307")
            self.logo_label.grid(row=0, column=1)

            self.cartas_viradas = Label(self.player4_frame, bd = 0, image=self._back_card)
            self.cartas_viradas.grid(row=1, column=0)

            self.cartas_viradas1 = Label(self.player4_frame, bd = 0, image=self._back_card)
            self.cartas_viradas1.grid(row=1, column=1)

            self.cartas_viradas2 = Label(self.player4_frame, bd = 0, image=self._back_card)
            self.cartas_viradas2.grid(row=1, column=2)
            #-----------------------------------------------------------------------------------------------#

        if len(self._table._times) == 2:
            # Placar frame
            self.titulo_label = Label(self.placar_frame, text='Score', font="arial 24", bg="#046307")
            self.titulo_label.grid(row=0, column=1)
            placar_azul = "Time Azul : " + str(self._table._times[0]._pontuacao)
            self.time_azul_label = Label(self.placar_frame, text=placar_azul, font="arial 20", fg="blue", bg="#046307")
            self.time_azul_label.grid(row=1, column=1)
            placar_vermelho = "Time Vermelho : " + str(self._table._times[1]._pontuacao)
            self.time_vermelho_label = Label(self.placar_frame, text=placar_vermelho, font="arial 20", fg="red", bg="#046307")
            self.time_vermelho_label.grid(row=2, column=1)


    def exibirNotificacaoInicioMao(self):
        self.Notificar("Nova Mão entregue")


    def clicarCarta(self, index: int): 
        """@ReturnType Problema.Carta"""
        self.localPlayer.selecionarCarta(index)

    def SolicitarNomeJogador(self):
        """@ReturnType string"""
        input_usuario = simpledialog.askstring("Solicitacao de Nome", "Digite seu nome: ")
        if input_usuario == "":
            return "Sem nome"
        else:
            return input_usuario

    def Notificar(self, mensagem):
        messagebox.showinfo(message= mensagem)

    def set_match_id(self, match_id): 
        """@ParamType aMatch_id string"""
        self._match_id = match_id
        pass
    
    def atualizarTopo(self):

        self._topo = self._table._topo
        self._topo.get_foto_carta()
        self.logo_label.grid(row=0, column=1)
        self.logo_label = Label(self.mesa_frame, bd = 0, image=self._topo._imagem) # MONTE
        self.logo_label.grid(row=0, column=2)

    def AtualizarInterface(self):
        
        carta1 = self.localPlayer._mao[0]
        carta2 = self.localPlayer._mao[1]
        carta3 = self.localPlayer._mao[2]
        manilha = self._table._manilha
        
        self.atualizarTopo()
        
        
        manilha.get_foto_carta()

        if carta1:
            carta1.get_foto_carta()
            self.cartas_viradas = Button(self.player1_frame, bd = 3, image= carta1._imagem,command=lambda: self.clicarCarta(0))
            self.cartas_viradas.grid(row=1, column=2)

        if carta2:
            carta2.get_foto_carta()
            self.cartas_viradas1 = Button(self.player1_frame, bd = 3, image= carta2._imagem,command=lambda: self.clicarCarta(1))
            self.cartas_viradas1.grid(row=1, column=3)

        if carta3:
            carta3.get_foto_carta()
            self.cartas_viradas2 = Button(self.player1_frame, bd = 3, image= carta3._imagem,command=lambda: self.clicarCarta(2))
            self.cartas_viradas2.grid(row=1, column=4)

        self.logo_label = Label(self.mesa_frame, bd = 0, image= manilha._imagem) # MANILHA
        self.logo_label.grid(row=0, column=0)
        self.logo_label = Label(self.mesa_frame, bd = 0, image=self.card_deck)


        self.titulo_label = Label(self.placar_frame, text='Score', font="arial 24", bg="#046307")
        self.titulo_label.grid(row=0, column=1)
        placar_azul = "Time Azul : " + str(self._table._times[0]._pontuacao)
        self.time_azul_label = Label(self.placar_frame, text=placar_azul, font="arial 20", fg="blue", bg="#046307")
        self.time_azul_label.grid(row=1, column=1)
        placar_vermelho = "Time Vermelho : " + str(self._table._times[1]._pontuacao)
        self.time_vermelho_label = Label(self.placar_frame, text=placar_vermelho, font="arial 20", fg="red", bg="#046307")
        self.time_vermelho_label.grid(row=2, column=1)


    def enviarAtualizacaoPartida(self, aNovoEstado):
        self.send_move(aNovoEstado)

    def ClicarBotaoTruco(self):
        self._table.ClicarBotaoTruco(self.localPlayer)

    def botaoResposta(self, resposta):
        self._table.botaoResposta(resposta)

    def add_listener(self):		# Pyng use case "add listener"
        self.server_proxy = PyNetgamesServerProxy()
        self.server_proxy.add_listener(self)

    def send_connect(self):	# Pyng use case "send connect"
        self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

    def send_match(self): # Pyng use case "send match"
        self.server_proxy.send_match(4) #4 = quantidade de jogadores.

    def receive_connection_success(self):	# Pyng use case "receive connection"
        self.Notificar("Conectado ao servidor") 
        self.send_match() 

    def receive_disconnect(self):	# Pyng use case "receive disconnect"
        self.Notificar("Desconectado do servidor, o programa sera finalizado")
        self.main_window.destroy()
        
            
    def receive_error(self, error):	# Pyng use case "receive error"
        self.Notificar("ERRO NO SERVIDOR!! , o programa será finalizado")
        self.main_window.destroy()


    def receive_match(self, match):	# Pyng use case "receive match"
        self.set_match_id(match.match_id)
        self.match_position = match.position 
        self.localPlayer._position = match.position 

        
        self.pega_nomes_e_posicoes()
    
    def pega_nomes_e_posicoes(self): 
        if self.match_position == 0:
            jogadores = {"jogadores" : [(self.localPlayer._nome, self.match_position)],'turno_init':1}
            self.send_move(jogadores)

    

    def inicializar_mesa(self,move): 
        if 'turno_init' in move.payload:
            if move.payload['turno_init'] == self.match_position:
                if len(move.payload['jogadores']) < 4:
                    pacote = {}
                    pacote['jogadores'] = move.payload['jogadores']
                    pacote['jogadores'].append((self.localPlayer._nome, self.match_position)) 
                    turno = (self.match_position +1) % 4
                    pacote['turno_init'] = turno
                    self.send_move(pacote)
                else:
                    remotos_locais = []
                    for (jogador, position) in move.payload['jogadores']:
                        if jogador != self.localPlayer._nome:
                            remotos_locais.append((jogador, position))
                    self.remotePlayers = remotos_locais
                    if self.match_position == 3:
                        turno = 0
                    turno = (self.match_position +1) % 4
                    self.send_move({'jogadores':move.payload['jogadores'], 'turno_init': turno})
                    for nome,posicao in move.payload["jogadores"]:
                        jog_temp = Jogador(self._table)
                        jog_temp._nome = nome
                        jog_temp._position = posicao
                        self._table._jogadores.append(jog_temp)

                    

                    self._table.IniciarPartida(self.localPlayer) 
                    self.Notificar("Partida iniciada \nTime azul: " + str(self._table._times[0]._jogadores[0]._nome) + ' ,'+str(self._table._times[0]._jogadores[1]._nome)+'\nTime vermelho: '+str(self._table._times[1]._jogadores[0]._nome)+' ,'+str(self._table._times[1]._jogadores[1]._nome))
                    
                    self.fill_main_window() 
                    

                    self._table.setInicializada(True)

                    if self.localPlayer._dealer:
                        self._table.novaMao()
                        
                            
            
                                

    def receive_move(self, move):	# Pyng use case "receive move"
        if self._table._Inicializada == False: 
            self.inicializar_mesa(move) 
        else:
            self._table.receberJogada(move)
        
                            
    
    def send_move(self,move):
        self.server_proxy.send_move(self._match_id, move)

