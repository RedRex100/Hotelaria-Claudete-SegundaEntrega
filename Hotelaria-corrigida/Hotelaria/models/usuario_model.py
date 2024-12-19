class Usuario:
  def __init__(self, nome, endereco, cpf, telefone, email, senha):
      self.nome = nome
      self.endereco = endereco
      self.cpf = cpf
      self.telefone = telefone
      self.email = email
      self.senha = senha
      self.reservas = []
      self.total = 0

  def adiciona_reserva(self, reserva):
      self.reservas.append(reserva)

  def soma(self,n):
      self.total += n

usuarios = []
