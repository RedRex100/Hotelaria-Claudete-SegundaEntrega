from models.usuario_model import Usuario, usuarios
import os

def adicionar_usuario(nome, endereco, cpf, telefone, email, senha):
  if any(usuario.nome == nome for usuario in usuarios):
      return False  # Nome de usuário já existe
  novo_usuario = Usuario(nome, endereco, cpf, telefone, email, senha)
  usuarios.append(novo_usuario)
  return True

def adicionar_reserva_usuario(nome_usuario, reserva):
  usuario = next((usuario for usuario in usuarios if usuario.nome == nome_usuario), None)
  if usuario:
      usuario.adiciona_reserva(reserva)
      return True 
  return False  # Usuário não encontrado

def adicionar_total(nome_usuario, n):
  usuario = next((usuario for usuario in usuarios if usuario.nome == nome_usuario), None)
  if usuario:
      usuario.soma(n)
      return True 
  return False  # Usuário não encontrado