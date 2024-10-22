"""
Este script demonstra várias estruturas de dados em Python, incluindo:
- Listas (List)
- Tuplas (Tuple)
- Dicionários (Dict)
- Conjuntos (Set)
- Fila (Queue)
- Pilha (Stack)
- Arrays
- Named Tuples (Tuplas Nomeadas)
- DefaultDict
- Counter
- Deque

Versão: 1.97
Autor: Prof. Sauer
Site: www.sauer.pro.br
Email: sauer@simplificatreinamentos.com.br
Instagram: https://www.instagram.com/prof.alesauer/
Facebook: https://www.facebook.com/prof.alesauer/
YouTube:  https://www.youtube.com/@prof.alesauer
LinkedIn: www.linkedin.com/in/alesauer
"""

# Importando bibliotecas necessárias
from collections import namedtuple, defaultdict, Counter, deque
import array

# Listas (List)
# São mutáveis, ordenadas e permitem elementos duplicados.
minha_lista = [1, 2, 3, 4, 5]
minha_lista.append(6)  # Adicionando um elemento
print("Lista:", minha_lista)

# Tuplas (Tuple)
# São imutáveis, ordenadas e permitem elementos duplicados.
minha_tupla = (1, 2, 3, 4, 5)
print("Tupla:", minha_tupla)

# Dicionários (Dict)
# São mutáveis, desordenados (até Python 3.6), mas a partir do Python 3.7 mantêm a ordem de inserção.
meu_dict = {"nome": "Alice", "idade": 25}
meu_dict["cidade"] = "São Paulo"  # Adicionando um novo par chave-valor
print("Dicionário:", meu_dict)

# Conjuntos (Set)
# São mutáveis, não ordenados e não permitem elementos duplicados.
meu_set = {1, 2, 3, 4, 4, 5}
meu_set.add(6)
print("Conjunto:", meu_set)

# Fila (Queue) usando deque
# FIFO (First In, First Out)
minha_fila = deque([1, 2, 3])
minha_fila.append(4)  # Adicionando no final
minha_fila.popleft()  # Removendo do início
print("Fila (Queue):", minha_fila)

# Pilha (Stack) usando lista
# LIFO (Last In, First Out)
minha_pilha = [1, 2, 3]
minha_pilha.append(4)  # Adicionando no topo
minha_pilha.pop()  # Removendo do topo
print("Pilha (Stack):", minha_pilha)

# Arrays
# São mais eficientes em termos de memória do que listas para grandes volumes de dados numéricos.
meu_array = array.array('i', [1, 2, 3, 4, 5])
meu_array.append(6)
print("Array:", meu_array)

# Named Tuples (Tuplas Nomeadas)
# São como tuplas, mas com campos nomeados, tornando-as mais legíveis.
Pessoa = namedtuple("Pessoa", "nome idade")
pessoa1 = Pessoa(nome="Alice", idade=25)
print("Named Tuple:", pessoa1)

# DefaultDict
# É semelhante ao dicionário, mas fornece um valor padrão para chaves inexistentes.
meu_defaultdict = defaultdict(int)
meu_defaultdict["contador"] += 1
print("DefaultDict:", meu_defaultdict)

# Counter
# Conta a frequência de elementos em um iterável.
minha_lista_contagem = [1, 2, 2, 3, 3, 3]
contagem = Counter(minha_lista_contagem)
print("Counter:", contagem)

# Deque
# Deque (Double-ended Queue) permite inserção e remoção de ambos os lados.
meu_deque = deque([1, 2, 3, 4])
meu_deque.appendleft(0)  # Adicionando à esquerda
meu_deque.pop()  # Removendo da direita
print("Deque:", meu_deque)
