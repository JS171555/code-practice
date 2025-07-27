# Consulta de CEP: Uma Aplicação Web Eficiente

Este projeto apresenta uma aplicação web robusta e intuitiva desenvolvida em **Flask** para a consulta de endereços brasileiros através da integração com a **API ViaCEP**. Com uma interface de usuário limpa e responsiva, a ferramenta permite que usuários obtenham rapidamente informações detalhadas de endereços ao inserir um Código de Endereçamento Postal (CEP).




## 📊 Visão Geral do Projeto

O `Consulta de CEP` é uma solução prática para a validação e recuperação de dados de endereços. Ele serve como um exemplo claro de como integrar APIs externas em aplicações web, demonstrando boas práticas de desenvolvimento front-end e back-end. A aplicação é projetada para ser facilmente compreendida e estendida, tornando-a ideal para fins educacionais ou como base para projetos maiores que necessitem de funcionalidades de consulta de CEP.




## ✨ Funcionalidades Principais

- **Consulta Rápida e Precisa**: Permite a busca de endereços completos (rua, bairro, cidade, estado) a partir de um CEP válido, utilizando a API ViaCEP.
- **Validação de Entrada**: Implementa validação robusta para garantir que apenas CEPs no formato correto sejam processados.
- **Feedback Visual Aprimorado**: Oferece mensagens de erro claras e estilizadas, além de um *loading spinner* para indicar o processamento da requisição, melhorando a experiência do usuário.
- **Design Responsivo**: A interface se adapta perfeitamente a diferentes tamanhos de tela, garantindo usabilidade em dispositivos móveis e desktops.
- **Localização Completa**: Totalmente desenvolvido em português brasileiro, desde a interface até as mensagens de feedback.




## 📸 Demonstração Visual

Para uma compreensão visual do funcionamento da aplicação, observe a imagem abaixo, que ilustra a interface de usuário e o resultado de uma consulta de CEP bem-sucedida.

<img src="https://i.imgur.com/g8McwMU.jpeg" alt="Demonstração da aplicação Consulta de CEP">




## 🛠️ Tecnologias Utilizadas

O desenvolvimento desta aplicação foi possível graças à combinação das seguintes tecnologias:

- **Python 3.7+**: Linguagem de programação principal para o desenvolvimento do back-end.
- **Flask**: Microframework web para Python, utilizado para construir a API e servir as páginas HTML.
- **HTML5 + CSS3**: Linguagens de marcação e estilo para a estruturação e apresentação do conteúdo web.
- **JavaScript Vanilla**: Utilizado para a lógica de front-end, incluindo a manipulação do DOM e requisições assíncronas.
- **ViaCEP API**: Serviço RESTful público para consulta de endereços a partir de CEPs [1].

### Referências

[1] ViaCEP. Disponível em: [https://viacep.com.br/](https://viacep.com.br/)




## 📂 Estrutura do Projeto

A organização do projeto segue uma estrutura padrão para aplicações Flask, facilitando a navegação e a manutenção do código:

```
consulta_cep/
├── app.py              # Lógica principal da aplicação Flask
├── static/             # Arquivos estáticos (CSS, JavaScript, imagens)
│   └── style.css       # Folha de estilos CSS
└── templates/          # Modelos HTML
    └── index.html      # Página principal da aplicação
```




## 🚀 Como Rodar a Aplicação Localmente

Para executar esta aplicação em seu ambiente de desenvolvimento local, siga os passos abaixo:

### 1. Clonar o Repositório

Abra seu terminal ou prompt de comando e execute:

```bash
git clone https://github.com/seu-usuario/consulta_cep.git
cd consulta_cep
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

É uma boa prática isolar as dependências do projeto. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Para Linux/macOS:
source venv/bin/activate
# Para Windows:
venc\Scripts\activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas Python necessárias:

```bash
pip install flask requests
```

### 4. Executar a Aplicação

Finalmente, inicie o servidor de desenvolvimento do Flask:

```bash
python app.py
```

Após a execução bem-sucedida, a aplicação estará acessível em seu navegador através do endereço: `http://127.0.0.1:5000/`




## 📋 Requisitos do Sistema

Para o correto funcionamento da aplicação, os seguintes requisitos devem ser atendidos:

- **Python 3.7 ou superior**: A aplicação foi desenvolvida e testada com esta versão do Python.
- **Conexão com a Internet**: Essencial para que a aplicação possa se comunicar com a API ViaCEP e realizar as consultas de endereço.




## 🚀 Opções de Deploy

Esta aplicação pode ser facilmente implantada em diversas plataformas de hospedagem web. Algumas sugestões incluem:

- **Render**
- **Railway**
- **Heroku**
- **PythonAnywhere**
- Qualquer provedor de VPS (Virtual Private Server) de sua preferência.




## ⚠️ Observações Importantes

- **Limitação da API ViaCEP**: A API ViaCEP possui um limite de requisições por IP. Recomenda-se cautela durante testes intensivos para evitar bloqueios temporários.
- **Potencial de Expansão**: Este projeto serve como uma base sólida e pode ser estendido com funcionalidades adicionais, tais como:
  - Histórico de consultas de CEP.
  - Integração com serviços de mapas para visualização do endereço.
  - Implementação de autenticação de usuário para funcionalidades avançadas.




## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Para detalhes completos, consulte o arquivo `LICENSE` na raiz do repositório.




## 💡 Créditos

Desenvolvido com dedicação e paixão pela programação. A interface foi inspirada em princípios de UX/UI modernos, buscando oferecer a melhor experiência ao usuário. Os dados de endereço são fornecidos com a confiabilidade da API ViaCEP.



