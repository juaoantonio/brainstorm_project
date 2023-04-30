# Instalação
* Clonar o repositório do projeto
* Acessar a pasta do projeto e criar um ambiente virtual: python -m venv env
* Ativar o ambiente virtual: source env/bin/activate
* Instalar as dependências: pip install -r requirements.txt
* Para instalar as dependências de desenvolvimento, execute: pip install -r requirements-dev.txt
* Criar um arquivo .env baseado no arquivo .env-exemple e definir as variáveis de ambiente.

# Variáveis de Ambiente
O projeto utiliza as seguintes variáveis de ambiente, que devem ser definidas no arquivo .env:

* SECRET_KEY: chave secreta utilizada pelo Django
* MYSQL_CONFIG_FILE: caminho para o arquivo de configuração do MySQL
* DEBUG: booleano que indica se o modo de debug do Django está ativado ou não (para produção, deve-se usar como False)

# Testes com Coverage.py
Para executar os testes do projeto com o coverage.py, siga os seguintes passos:

* Ative o ambiente virtual: source env/bin/activate
* Execute o comando coverage run manage.py test
* Para gerar o relatório de cobertura, execute: coverage report
* O relatório será exibido no terminal, indicando a porcentagem de cobertura dos testes em cada arquivo.
* Caso deseje gerar um relatório em HTML, execute: coverage html. O relatório será gerado na pasta htmlcov, que pode ser acessada em um navegador web.