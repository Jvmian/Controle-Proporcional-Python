# Controle Proporcional (P) em Python

Este projeto consiste em uma simulação simples de um **controlador proporcional (P)** aplicado a um sistema dinâmico, com o objetivo de analisar o impacto do ganho proporcional (Kp) na resposta do sistema.

## 🎯 Objetivo
Compreender como diferentes valores de **Kp** influenciam:
- velocidade de resposta
- estabilidade do sistema
- comportamento ao longo do tempo

Esse tipo de análise é fundamental em áreas como **automação, robótica, controle industrial e mecatrônica**.

## ⚙️ Funcionamento
O sistema tenta atingir uma **velocidade desejada (setpoint = 100)**.  
A cada iteração:
- calcula-se o erro
- aplica-se o controle proporcional
- atualiza-se a velocidade do sistema

A simulação é repetida para diferentes valores de Kp.

## 📊 Resultados
A imagem abaixo mostra a resposta do sistema para diferentes ganhos proporcionais:

![Resposta do Controle Proporcional](images/resposta_kp.png)

Observações:
- Kp baixo → resposta lenta
- Kp alto → resposta mais rápida, porém mais agressiva

## 🛠️ Tecnologias Utilizadas
- Python
- NumPy
- Matplotlib

## 🚀 Próximos Passos
- Evoluir para controle PI
- Tornar a simulação interativa
- Aplicar o conceito em hardware real (Arduino / ESP32)
