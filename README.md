# ⚙️ API de Gerenciamento de Consultas Médicas — Backend

Este repositório contém uma API RESTful desenvolvida em **Python** com **Django REST Framework (DRF)**, responsável pelo gerenciamento e agendamento de consultas médicas.

A API foi projetada para servir como backend de um aplicativo mobile desenvolvido em **React Native / Expo**, oferecendo:

- persistência relacional de dados;
- autenticação segura baseada em JWT;
- regras de negócio centralizadas;
- isolamento de ambiente com Docker;
- arquitetura modular e escalável.

---

# 🚀 Tecnologias Utilizadas

O backend foi estruturado utilizando ferramentas modernas do ecossistema Python:

| Tecnologia | Finalidade |
|---|---|
| **Python 3.11+** | Linguagem principal do projeto |
| **Django** | Framework web principal |
| **Django REST Framework (DRF)** | Construção da API REST |
| **Simple JWT** | Autenticação baseada em tokens JWT |
| **Django Filter** | Filtros dinâmicos via Query Parameters |
| **Docker & Docker Compose** | Conteinerização e padronização de ambiente |
| **PostgreSQL / SQLite** | Bancos de dados relacionais suportados |

---

# 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular baseada no padrão do Django, separando responsabilidades de configuração, regras de negócio, serialização e controle das requisições.

```text
├── core/                         # Configurações globais do projeto
│   ├── __init__.py
│   ├── settings.py              # Configurações centrais e variáveis de ambiente
│   ├── urls.py                  # Rotas globais da aplicação
│   └── wsgi.py
│
├── consultas/                          # Aplicação principal da API
│   ├── migrations/              # Histórico de migrações do banco
│   ├── admin.py                 # Configurações do Django Admin
│   ├── apps.py
│   ├── models.py                # Modelos relacionais
│   ├── serializers.py           # Serializadores e validações
│   ├── services.py              # Regras de negócio
│   ├── urls.py                  # Rotas locais da API
│   └── views.py                 # ViewSets e controladores REST
```
# 🎯 Recursos Implementados

## 👑 1. Painel Administrativo com Django Admin

O sistema utiliza o **Django Admin** como painel operacional principal.

A interface administrativa permite:

- cadastro de médicos especialistas;
- gerenciamento de especialidades;
- controle de horários disponíveis;
- auditoria completa de consultas agendadas.

### Funcionalidades disponíveis

- filtros por data;
- exclusão em lote;
- edição rápida de registros;
- gerenciamento direto do banco de dados.

---

## 🔐 2. Autenticação com JWT

A autenticação da API utiliza **JSON Web Tokens (JWT)** por meio da biblioteca **Simple JWT**.

Ao realizar login, o usuário recebe:

- `Access Token`
- `Refresh Token`

### Exemplo de autenticação

```http
Authorization: Bearer <token>
```

Os endpoints protegidos exigem autenticação válida para acesso.

---

## 🧠 3. Camada de Serviços (`services.py`)

Toda a lógica de negócio foi isolada na camada de serviços para evitar:

- models excessivamente complexos;
- controllers inflados;
- repetição de regras de validação.

### Regras implementadas

#### 📅 Validação de Datas

O sistema impede agendamentos com datas retroativas.

#### ⏰ Controle de Horário Comercial

A API bloqueia consultas fora do horário operacional definido pela clínica.

### Resposta de erro

```http
400 Bad Request
```

---

## 🔄 4. Serializadores Avançados

Os serializadores possuem responsabilidades de:

### ✍️ Escrita (POST / PUT / PATCH)

- validação de dados;
- integridade relacional;
- parsing de tipos.

### 📖 Leitura (GET)

Os endpoints retornam objetos detalhados contendo:

- nome do médico;
- especialidade;
- horário formatado;
- informações completas da consulta.

Isso reduz chamadas adicionais no aplicativo mobile.

---

# 🛣️ Endpoints da API

| Método | Endpoint | Autenticação | Descrição |
|---|---|---|---|
| `POST` | `/api/token/` | ❌ Não | Gera Access Token e Refresh Token |
| `POST` | `/api/token/refresh/` | ❌ Não | Renova o Access Token |
| `GET` | `/api/consultas/` | ✅ JWT | Lista consultas do usuário |
| `POST` | `/api/consultas/` | ✅ JWT | Cria uma nova consulta |
| `GET` | `/api/consultas/<id>/` | ✅ JWT | Retorna detalhes de uma consulta |
| `PUT` | `/api/consultas/<id>/` | ✅ JWT | Atualiza completamente uma consulta |
| `PATCH` | `/api/consultas/<id>/` | ✅ JWT | Atualização parcial |
| `DELETE` | `/api/consultas/<id>/` | ✅ JWT | Remove uma consulta |

---

# 🔍 Filtros Dinâmicos

O endpoint:

```http
GET /api/consultas/
```

suporta filtros dinâmicos via Query Parameters.

## Filtrar por Médico

```http
/api/consultas/?medico=NomeDoEspecialista
```

## Filtrar por Data

```http
/api/consultas/?data=2026-05-20
```

---

# 📦 Instalação e Execução Local

## 🐳 Opção 1 — Docker (Recomendado)

### Pré-requisitos

- Docker
- Docker Compose

### Executar o projeto

```bash
docker-compose up --build
```

O Docker irá:

- baixar as dependências;
- criar os containers;
- executar as migrações;
- iniciar a aplicação na porta `8000`.

---

## 💻 Opção 2 — Ambiente Python Local

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### Windows

```bash
.\venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Executar migrações

```bash
python manage.py migrate
```

---

### 4️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

---

### 5️⃣ Iniciar servidor

```bash
python manage.py runserver 0.0.0.0:8000
```

---

# 🌐 Ambiente de Produção

O backend encontra-se hospedado na plataforma Railway com integração contínua via GitHub.

## 🔗 URL Base da API

```text
https://desafio-tecnico-back-end-django-production.up.railway.app/api/docs/
```

## 🔗 Painel Administrativo

```text
https://desafio-tecnico-back-end-django-production.up.railway.app/admin/
```

---

# 🔑 Credenciais de Demonstração

Para facilitar testes e validações da aplicação:

| Campo | Valor |
|---|---|
| **Usuário** | `user_admin` |
| **Senha** | `senha2026` |

---

# 📌 Observações Técnicas

- O projeto foi desenvolvido seguindo princípios de separação de responsabilidades.
- A API está preparada para ambientes escaláveis e conteinerizados.
- Toda a estrutura foi organizada visando manutenção, legibilidade e expansão futura do sistema.
