# ⚙️ API de Gerenciamento de Consultas Médicas - Backend

Este repositório contém o código-fonte da API REST desenvolvida em **Python** e **Django** para o ecossistema de gerenciamento e agendamento de consultas médicas. Esta API foi projetada especificamente para ser consumida pelo aplicativo mobile desenvolvido em **React Native** e **Expo**, fornecendo toda a infraestrutura de dados, persistência e segurança necessárias. O projeto segue boas práticas de arquitetura em camadas, código limpo, segurança e isolamento de ambiente.

---

## 🚀 Tecnologias Utilizadas

O ecossistema do backend foi projetado utilizando as seguintes tecnologias e bibliotecas:

* **Python (v3+):** Linguagem core de desenvolvimento.
* **Django & Django REST Framework (DRF):** Framework base para construção e roteamento da API RESTful de alto desempenho.
* **Simple JWT:** Mecanismo de autenticação baseado em JSON Web Tokens (Access e Refresh Tokens).
* **Django Filter:** Mecanismo para criação de filtros relacionais dinâmicos diretamente na URL.
* **Docker & Docker Compose:** Ferramentas de conteinerização para garantir paridade total entre ambientes de desenvolvimento e produção.
* **SQLite:** Banco de dados relacional leve utilizado para persistência rápida de dados locais.

---

## 📦 Como Instalar o Projeto

Existem duas formas de preparar o ambiente: via Docker (Recomendado) ou em ambiente Python local.

### Opção 1: Via Docker (Recomendado)
Certifique-se de ter o **Docker** e o **Docker Compose** instalados em sua máquina. Nenhuma instalação local de Python é necessária nesta opção.

### Opção 2: Via Ambiente Python Local
Caso prefira rodar sem Docker, isole o ambiente com uma ferramenta de ambiente virtual:

```bash
# 1. Clonar o repositório
git clone https://github.com/alvaro-miguel/Desafio-Tecnico-Back-end-Django.git
cd Desafio-Tecnico-Back-end-Django

# 2. Criar e ativar o ambiente virtual (Virtualenv)
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 3. Instalar as dependências necessárias
pip install -r requirements.txt
```

## ⚙️ Como Executar o Projeto

### 🐳 Rodando com Docker (Orquestração Completa)

Na raiz do projeto (onde está localizado o arquivo `docker-compose.yml`), execute os comandos abaixo no terminal:

```bash
# 1. Subir os contêineres em segundo plano
docker compose up -d

# 2. Executar as migrações para estruturar as tabelas do banco de dados
docker compose exec api python manage.py migrate

# 3. Criar o usuário administrador do sistema (Django Admin)
docker compose exec api python manage.py createsuperuser
```

O servidor da API estará ativo e respondendo no endereço local:

```text
http://localhost:8000/
```

---

### 💻 Rodando Localmente (Sem Docker)

Caso tenha instalado as dependências via ambiente virtual, execute:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🧪 Como Testar a API

### 🔑 Endpoint Crítico: Autenticação (Simple JWT)

A API possui rotas protegidas que exigem um token Bearer válido para manipulação dos dados de consultas.

#### URL de geração do token

```http
POST http://localhost:8000/api/token/
```

#### Corpo da requisição (JSON)

```json
{
  "username": "seu_usuario_admin",
  "password": "sua_senha_cadastrada"
}
```

#### Resposta esperada

Você receberá um objeto contendo o `access token`. Copie este valor para utilizar nas próximas requisições através do cabeçalho:

```http
Authorization: Bearer <seu_token_access>
```

---

## 🔄 Endpoints do CRUD de Consultas (`/api/consultas/`)

| Método | Endpoint | Protegido? | Descrição |
|---|---|---|---|
| GET | `/api/consultas/` | Sim | Lista todas as consultas cadastradas |
| GET | `/api/consultas/<id>/` | Sim | Retorna os detalhes de uma consulta específica |
| POST | `/api/consultas/` | Sim | Cadastra uma nova consulta médica |
| PUT | `/api/consultas/<id>/` | Sim | Atualiza todos os dados de uma consulta existente |
| PATCH | `/api/consultas/<id>/` | Sim | Atualiza dados parciais de uma consulta existente |
| DELETE | `/api/consultas/<id>/` | Sim | Remove uma consulta do banco de dados |

---

## 🔍 Filtros Dinâmicos Disponíveis (Diferencial)

Você pode aplicar parâmetros diretamente na URL do método `GET` para refinar as buscas.

### Filtrar por especialista

```http
GET http://localhost:8000/api/consultas/?medico=NomeDoMedico
```

### Filtrar por data específica

```http
GET http://localhost:8000/api/consultas/?data=2026-05-20
```

---

## 🛡️ Regras de Negócio e Validações de Backend

Se tentar cadastrar uma consulta (via `POST`) com data retroativa ou fora do horário comercial permitido, a camada isolada de serviços (`services.py`) interceptará a requisição e retornará um erro HTTP `400 Bad Request`, detalhando a infração de negócio.