# 🕹️ Mini-Projeto IP - Chrono Cin

## 🏆 Equipe
- Arthur Torres <atl> - [@github](https://github.com/arthurtdl)
- Ian Cerqueira <idhac> - [@github](https://github.com/Ian-Cerqueira)
- Ítalo Cauã <icbo> - [@github](https://github.com/italo-Barbosa)
- Maycon Otávio <mobs> - [@github](https://github.com/m4yconn)
- Ryan Souza <rss15> - [@github](https://github.com/RyanRss15)
- Thiago Alves <tam6> - [@github](https://github.com/ThAlvesM)

## 🎯 Descrição do Projeto

Este projeto consiste na criação de um sistema interativo 2D em Python no qual o usuário controla um objeto para coletar itens espalhados pela tela. Cada tipo de item coletado será registrado e exibido ao usuário. A arquitetura do projeto será baseada nos princípios da Programação Orientada a Objetos (POO).

## 🏗️ Arquitetura do Projeto

A organização do código segue a estrutura modular e POO:

```
📂 projeto_ip
 ┣ 📂 assets                 # Recursos gráficos
 ┣ 📂 sounds                 # sons do jogo
 ┣ 📂 src                    # Código-fonte do jogo
 ┃ ┣ 📜 classe_Button.py        # Classe do botao inicio
 ┃ ┣ 📜 coletaveis.py           # Classe dos itens coletáveis
 ┃ ┣ 📜 game.py                 # Arquivo principal para execução
 ┃ ┣ 📜 inimigos.py             # Classe dos inimigos primeira fase
 ┃ ┣ 📜 lore.py                 # Contextualização da Historia
 ┃ ┣ 📜 parallex.py             # Tela de Historia
 ┃ ┣ 📜 plataforma.py           # Plataformas primeira fase
 ┃ ┣ 📜 player.py               # Classe do jogador
 ┃ ┣ 📜 primeira_fase.py        # Lógica principal da primeira fase
 ┃ ┣ 📜 space_shooter.py        # Lógica principal da segunda fase
 ┃ ┣ 📜 typing_text.py          # Texto de Historia
📜 README.md        # Documentação do projeto
```

## 🛠️ Ferramentas e Tecnologias

- **Python** - Linguagem principal do projeto
- **PyGame** - Framework para desenvolvimento de jogos 2D
- **GitHub** - Controle de versão e colaboração
- **Notion** - Gerenciamento de tarefas e documentação

### Justificativas

O PyGame foi escolhido por ser uma biblioteca amplamente utilizada para jogos 2D em Python, oferecendo funcionalidades robustas para renderização gráfica, manipulação de eventos e colisões.

## 📦 Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-ip.git
   cd projeto-ip
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o jogo:
   ```bash
   python src/main.py
   ```

## 🎮 Capturas de Tela
<img src="https://exemplo.com/logo.png" alt="Imagem do Jogo">
<img src="https://exemplo.com/logo.png" alt="Imagem do Jogo">
<img src="https://exemplo.com/logo.png" alt="Imagem do Jogo">

## 📌 Divisão de Tarefas

| Membro       | Responsabilidade                                |
| ------------ | ----------------------------------------------- |
| Arthur       | Implementação do jogador e movimento            |
| Ian          | Implementação das mecanicas do jogo e boss      |
| Italo        | Desenvolvimento dos objetos coletáveis          |
| Maycon       | Implementação da interface gráfica               |
| Ryan         | Criação do Mapa e Sprites                       |
| Thiago       | Documentação e organização                      |

## 📚 Conceitos Aplicados

- **Programação Orientada a Objetos (POO)**: Classes para jogador, itens, e lógica do jogo.
- **Manipulação de Eventos**: Captura de entrada do teclado para movimentação.
- **Colisões**: Detecção da coleta de objetos.
- **Gerenciamento de Estado**: Registro e exibição da pontuação.

## 🚀 Desafios e Lições Aprendidas

- **Erro mais impactante:** Problema na detecção de colisão entre o jogador e os objetos coletáveis. **Solução:** Ajuste nas coordenadas e revisão da lógica de colisão.
- **Maior desafio:** Organização da arquitetura POO do jogo. **Solução:** Aplicação de padrões de design e modularização do código.
- **Lições aprendidas:** Importância da colaboração e versionamento de código para projetos em equipe.

## 📑 Apresentação

O grupo preparou uma apresentação do projeto que pode ser acessada pelo link:
[Apresentação do Projeto](https://docs.google.com/presentation/d/1EbtIqT0eTcCLyh2JuYVoYmxZI2saFLZCQdqgh5rBkiI/edit?slide=id.g3429c676cd2_0_100#slide=id.g3429c676cd2_0_100)

---

📩 **Contato:** Para dúvidas ou sugestões, entre em contato com a equipe pelo canal do grupo no Discord/WhatsApp.

