#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Jogador import Jogador
from truco.game_logic.Problema.Baralho import Baralho
from truco.game_logic.Problema.Carta import Carta
from truco.game_logic.Problema.Time import Time
from truco.game_logic.TKinter import PlayerInterface
import random

class Mesa():

	def registrarTruco(self):
		"""@ReturnType boolean"""
		pass

	def registrarMao(self):
		"""@ReturnType boolean"""
		pass

	def registrarStatusRodada(self, aStatus):
		"""@ParamType aStatus boolean"""
		pass

	def registraPontoMao(self, aTime, aPontuacao):
		"""@ParamType aTime Problema.Time
		@ParamType aPontuacao int"""
		pass

	def definirOrdem(self):
		"""@ReturnType Problema.Jogador[]"""
		pass

	def encerramentoPartida(self):
		"""@ReturnType boolean"""
		pass

	def definirPartidaAndamento(self, aBoolean):
		pass

	def registrarVencedor(self, aTime):
		"""@ParamType aTime Problema.Time"""
		pass

	def verificarRegistroRodadas(self):
		"""@ReturnType int*"""
		pass

	def verificarVencedorRodada(self, aRodada):
		"""@ParamType aRodada int
		@ReturnType Problema.Time"""
		pass

	def verificarEmpate(self):
		"""@ReturnType boolean"""
		pass

	def verificarRodadasEmpatadas(self):
		"""@ReturnType int*"""
		pass

	def nenhumTimePontua(self):
		pass

	def encerramentoRodada(self):
		"""@ReturnType boolean"""
		pass

	def comparaMonte(self):
		"""@ReturnType int"""
		pass

	def definirTopo(self, aCartaForte):
		"""@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def pegarOrdem(self):
		"""@ReturnType Problema.Jogador[]"""
		pass

	def vencedorRodada(self, *aMonte, aCartaForte):
		"""@ParamType aMonte Problema.Carta*
		@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def verificaRodada(self, *aRegistroRodadas):
		"""@ParamType aRegistroRodadas int*
		@ReturnType int"""
		pass

	def registrarRodada(self, aQualRodada, aVencedorRodada):
		"""@ParamType aQualRodada int
		@ParamType aVencedorRodada int"""
		pass

	def trucoRespondido(self):
		"""@ReturnType boolean"""
		pass

	def registrarRespostaTruco(self, aValor):
		"""@ParamType aValor string"""
		pass

	def timeTrucou(self):
		"""@ReturnType Problema.Time"""
		pass

	def adicionarPontuacaoTime(self, aTime, aPontos):
		"""@ParamType aTime Problema.Time
		@ParamType aPontos int"""
		pass

	def aumentarValorMao(self):
		pass

	def clicarBotao(self, aJogador):
		"""@ParamType aJogador Problema.Jogador"""
		pass

	def IniciarPartida(self): #!!
		#self._jogadores = jogadores
		print("INICIANDO PARTIDA")
		self.DefinirTimes()
		self._times[0].ZerarPlacar()
		self._times[1].ZerarPlacar()
		print(self._times)
		self._Inicializada = True

	def DefinirTimes(self): #!! no diagrama times é Time. Tem que ser um array de Time
		j = self._jogadores
		self._times.append(Time())
		self._times[0]._jogadores = [j[0],j[2]]
		self._times.append(Time())
		self._times[1]._jogadores = [j[1],j[3]]

	def EscolherDealer(self):
		num = random.randint(0,3)
		self._jogadores[num].definirDealer() #!! não sei se nos diagramas isso ta aqui. alguem ve

	def pegarPlacar(self):
		"""@ReturnType int*"""
		pass

	def novaMao(self):
		pass

	def novaRodada(self):
		pass

	def ColocarNaMesa(self, aTime):
		"""@ParamType aTime int"""
		pass

	def PassarTurno(self):
		pass

	def ClicarBotaoTruco(self):
		pass

	def VerificarTrucoAndamento(self):
		"""@ReturnType boolean"""
		pass

	def receberJogada(self, aJogada):
		"""@ParamType aJogada Dict{string, any}"""
		pass

	def __init__(self):
		self._jogadores = None

		self._Inicializada = False
		"""@AttributeType Problema.Jogador"""
		self._baralho = None
		"""@AttributeType Problema.Baralho"""
		self._manilha = None
		"""@AttributeType Problema.Carta"""
		self._valorMao = 1
		"""@AttributeType int"""
		self._partidaAndamento = False
		"""@AttributeType boolean"""
		self._times = []
		"""@AttributeType Problema.Time"""
		self._rodadaAndamento = None
		"""@AttributeType boolean"""
		self._maoAndamento = None
		"""@AttributeType boolean"""
		self._truco = None
		"""@AttributeType boolean"""
		self._monte = None
		"""@AttributeType Problema.Carta*"""
		self._registroRodada = 3
		"""@AttributeType int*"""
		self._ordemRodada = None
		"""@AttributeType Problema.Jogador*"""
		self._placar = None
		"""@AttributeType int*"""
		self._vencedor = None
		"""@AttributeType Problema.Time"""
		self._unnamed_PlayerInterface_ = None
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

