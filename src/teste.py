import os
import matplotlib.pyplot as plt

velocidade_desejada = 100
kps = [0.1, 0.3, 0.6, 0.9]
passos = 20

for kp in kps:
    velocidade = 0
    velocidades = []

    for _ in range(passos):
        erro = velocidade_desejada - velocidade
        controle = kp * erro
        velocidade += controle
        velocidades.append(velocidade)

    plt.plot(velocidades, label=f"kp = {kp}")

plt.legend()
plt.xlabel("Iterações (tempo)")
plt.ylabel("Velocidade")
plt.title("Resposta do Sistema com Controle Proporcional (P)")
base_dir = os.path.dirname(__file__)
images_dir = os.path.join(base_dir, "..", "images")
os.makedirs(images_dir, exist_ok=True)
plt.savefig(os.path.join(images_dir, "resposta_kp.png"))
plt.show()
plt.show()
