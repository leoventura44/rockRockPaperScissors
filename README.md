# rockRockPaperScissors

Nesse projeto, criei um programa que joga Pedra, Papel e Tesoura com o usuário.

Lembrando que o link para o repositório no GitHub estará no final desta publicação.

A funcionalidade é bem simples, o usuário digita a letra equivalente a Pedra, Papel e Tesoura (P, A e T respectivamente) e dependendo da letra escolhida pelo computador ele irá avisar se o jogador ganhou, perdeu ou se deu empate.

A codificação foi dessa maneira:
- importei o módulo RANDOM da biblioteca do Python;
- criei uma função JOGO onde será pedido a letra P, A ou T para o usuário, e a função RANDOM.CHOICE() para a escolha do computador;
- em seguida implantei o argumento IF para os resultados de empate, vitória e derrota;
- e por ultimo criei a função VITÓRIA para estipular quais as condições de vitória seguindo a regra do jogo Pedra, Papel e Tesoura e o RETURN TRUE caso seja alcançado este resultado.
