# CCCV Coffee Price Scraper

Este projeto é um web scraper automatizado que coleta cotações de café do site da CCCV (Conselho dos Exportadores de Café do Brasil) e atualiza essas informações em um banco de dados SQL Server.

## 📋 Funcionalidades

- **Web Scraping**: Extrai cotações de café (Arábica Dura, Arábica Rio e Conilon) do site da CCCV
- **Agendamento**: Executa automaticamente em horários pré-definidos
- **Banco de Dados**: Atualiza as cotações em um banco SQL Server
- **Monitoramento**: Log de execução para acompanhar o funcionamento

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **requests**: Para requisições HTTP
- **BeautifulSoup**: Para parsing HTML
- **pymssql**: Para conexão com SQL Server
- **schedule**: Para agendamento de tarefas

## 📦 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Acesso ao banco de dados SQL Server configurado
- Conexão com a internet

### Passo 1: Clone o repositório

```bash
git clone <url-do-repositorio>
cd job.cccv
```

### Passo 2: Crie um ambiente virtual (recomendado)

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
# venv\Scripts\activate
```

### Passo 3: Instale as dependências

```bash
pip install requests beautifulsoup4 pymssql schedule
```

**Ou**

pip install -r requirements.txt
```

### Passo 4: Configuração do Banco de Dados

1. **Configure as credenciais do banco** no arquivo `job_cccv.py`:

```python
# Informações de conexão (linha ~35)
server = 'SEU_SERVIDOR'
database = 'SEU_BANCO'
username = 'SEU_USUARIO'
password = 'SUA_SENHA'
```

2. **Estrutura da tabela necessária**:

```sql
CREATE TABLE dbo.cotacao_cafes (
    id INT PRIMARY KEY,
    data_vigencia VARCHAR(50),
    periodo VARCHAR(20),
    nome VARCHAR(100),
    valor VARCHAR(50),
    updated_at DATETIME
);



## 🚀 Como Usar

### Execução Manual

```bash
# Ativar ambiente virtual (se não estiver ativo)
source venv/bin/activate

# Executar o script
python job_cccv.py
```


## 📁 Estrutura do Projeto

```
job.cccv/
├── job_cccv.py          # Script principal
├── README.md            # Este arquivo
└── requirements.txt     # Dependências (opcional)
```

## 🔧 Configuração Avançada

### Alterar Horários de Execução

Edite as linhas no final do arquivo `job_cccv.py`:

```python
schedule.every().day.at("HH:MM").do(main)
```

### Personalizar User-Agent

Altere o header na linha ~9:

```python
headers = {"User-Agent": "SEU_USER_AGENT_PERSONALIZADO"}
```


**Desenvolvido para Gap Café** 🏢# WebScraping_Cotacao_CCCV
