# 👁️ Visual Inspector

Pipeline de visão computacional construído do zero com OpenCV e NumPy,
desenvolvido como projeto prático da disciplina TEC434 - Computação Visual
(UEFS - Engenharia da Computação).

## 📌 Sobre o projeto

Este projeto transforma dois roteiros de laboratório num sistema organizado
e reutilizável de manipulação de imagens, cobrindo desde conceitos fundamentais
até técnicas avançadas de visão computacional.

## 🛠️ Funcionalidades

- Correção do espaço de cor BGR → RGB
- Manipulação direta de pixels com NumPy
- Binarização manual com limiar ajustável
- Aritmética de imagens (overflow vs saturação)
- Detecção de mudança entre cenas
- Filtro seletivo por cor no espaço HSV
- Efeito Sin City (objeto colorido em cena P&B)

## 📁 Estrutura do projeto

    visual-inspector/
    ├── data/
    │   ├── input/        # Imagens de entrada
    │   └── output/       # Resultados gerados
    ├── notebooks/
    │   ├── aula_01_fundamentos.ipynb
    │   └── aula_02_operacoes_avancadas.ipynb
    ├── src/
    │   └── utils.py      # Funções reutilizáveis
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## 🚀 Como rodar

1. Clone o repositório:
   git clone https://github.com/kevincorges/visual-inspector.git

2. Instale as dependências:
   pip install -r requirements.txt

3. Coloque suas imagens em data/input/

4. Abra os notebooks na ordem:
   - aula_01_fundamentos.ipynb
   - aula_02_operacoes_avancadas.ipynb

## 🧪 Tecnologias

- Python 3.11
- OpenCV
- NumPy
- Matplotlib

## 👤 Autor

Kevin C. Borges

E-mail para contato: kevinborges.estagio@gmail.com

LinkedIn: www.linkedin.com/in/kevin-cordeiro-borges-280aa7218

Engenharia de Computação — UEFS
