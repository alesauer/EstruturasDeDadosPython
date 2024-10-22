# 🗂️ Estruturas de Dados em Python

Este repositório explora diversas estruturas de dados em Python, como **Listas**, **Tuplas**, **Dicionários**, **Conjuntos**, **Filas**, **Pilhas**, **Arrays**, **Named Tuples**, **DefaultDict**, **Counter**, e **Deque**. 

## 📋 Estruturas de Dados
1. [Listas (List)](#listas)
2. [Tuplas (Tuple)](#tuplas)
3. [Dicionários (Dict)](#dicionarios)
4. [Conjuntos (Set)](#conjuntos)
5. [Fila (Queue)](#fila)
6. [Pilha (Stack)](#pilha)
7. [Arrays](#arrays)
8. [Named Tuples (Tuplas Nomeadas)](#named-tuples)
9. [DefaultDict](#defaultdict)
10. [Counter](#counter)
11. [Deque](#deque)

### Listas (List)
As listas são mutáveis e ordenadas. Permitem duplicatas e são amplamente usadas.
```python
minha_lista = [1, 2, 3]
minha_lista.append(4)
```

### Tuplas (Tuple)
Tuplas são imutáveis e ordenadas. Muito úteis para dados que não devem ser alterados.
```python
minha_tupla = (1, 2, 3)
```

### Dicionários (Dict)
Os dicionários são coleções de pares chave-valor. São mutáveis e, a partir do Python 3.7, mantêm a ordem de inserção.
```python
meu_dict = {'nome': 'Alice', 'idade': 25}
meu_dict['cidade'] = 'São Paulo'
```

### Conjuntos (Set)
Conjuntos são mutáveis, não permitem duplicatas e não mantêm ordem.
```python
meu_set = {1, 2, 3}
meu_set.add(4)
```

### Fila (Queue)
Fila (Queue) segue a regra FIFO. Usamos o `deque` para implementar.
```python
minha_fila = deque([1, 2, 3])
minha_fila.append(4)
minha_fila.popleft()
```

### Pilha (Stack)
A pilha segue o princípio LIFO. Podemos usar uma lista para representar.
```python
minha_pilha = [1, 2, 3]
minha_pilha.append(4)
minha_pilha.pop()
```

### Arrays
Arrays são semelhantes às listas, mas mais eficientes para dados numéricos.
```python
import array
meu_array = array.array('i', [1, 2, 3])
```

### Named Tuples
Tuplas Nomeadas permitem acessar os elementos da tupla por nomes ao invés de índices.
```python
from collections import namedtuple
Pessoa = namedtuple('Pessoa', 'nome idade')
pessoa = Pessoa(nome='Alice', idade=25)
```

### DefaultDict
DefaultDict retorna um valor padrão para chaves inexistentes.
```python
from collections import defaultdict
meu_defaultdict = defaultdict(int)
meu_defaultdict['contador'] += 1
```

### Counter
Counter conta a frequência de elementos em uma lista.
```python
from collections import Counter
contagem = Counter([1, 2, 2, 3, 3, 3])
```

### Deque
Deque é uma fila de dois sentidos, onde podemos adicionar ou remover elementos em ambas as extremidades.
```python
from collections import deque
meu_deque = deque([1, 2, 3])
meu_deque.appendleft(0)
meu_deque.pop()
```

## 🏁 Conclusão
Este repositório demonstra o uso de diversas estruturas de dados em Python, cada uma com suas vantagens e desvantagens dependendo do cenário.
