#!/usr/bin/env python
# coding: utf-8

# # Exercícios
# 
# ## 1. Faturamento do Melhor e do Pior Mês do Ano
# 
# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?

# In[28]:


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
print(maior_valor)
print(menor_valor)
print(vendas_1sem)


# ## 2. Continuação
# 
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# 
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
# 
# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista

# In[13]:


i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)

print('O melhor mês do ano foi {} com {} vendas'.format(meses[i_maior_valor], maior_valor))
print('O pior mês do ano foi {} com {} vendas'.format(meses[i_menor_valor], menor_valor))

fat_total = sum(vendas_1sem)
print('Faturamento Total: R${:,}'.format(fat_total))

percentual = maior_valor / fat_total
print('O melhor mês representou {:.1%} das vendas do ano todo'.format(percentual))


# ## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")
# 
# Dica: o método remove retira um item da lista.

# In[29]:


top3 = []

print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)

vendas_1sem.remove(maior_valor)

maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)

