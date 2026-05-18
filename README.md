# ⚙️ API de Gerenciamento de Consultas Médicas - Backend

Este repositório contém a API RESTful robusta desenvolvida em **Python** e **Django REST Framework (DRF)** que serve como o motor de dados para o ecossistema de gerenciamento e agendamento de consultas médicas. 

A infraestrutura foi projetada especificamente para alimentar o aplicativo móvel em **React Native / Expo**, fornecendo persistência relacional, isolamento de ambiente, segurança baseada em tokens e regras de negócio centralizadas. O projeto adota uma arquitetura em camadas bem definida, código limpo, conteinerização completa e esteira de deploy contínuo.

---

## 🚀 Tecnologias e Ecossistema Técnico

O ecossistema do backend foi estruturado utilizando ferramentas modernas do mercado de desenvolvimento:

* **Python (v3.11+):** Linguagem principal, estável e fortemente tipada por meio de tipagem estática opcional.
* **Django & Django REST Framework (DRF):** Framework robusto para a construção ágil de APIs RESTful escaláveis, seguras e com injeção automática de filtros.
* **Simple JWT:** Camada de segurança e gerenciamento de sessões baseada em JSON Web Tokens (criptografia assimétrica para Access e Refresh Tokens).
* **Django Filter:** Mecanismo integrado para a criação de filtros relacionais complexos diretamente em parâmetros de URL (`Query Parameters`).
* **Docker & Docker Compose:** Componentes de isolamento em contêineres, garantindo paridade total de ambiente (`development == production`).
* **PostgreSQL / SQLite:** Suporte nativo e transparente para bancos relacionais, estruturado via ORM do Django.

---

## ⚙️ Arquitetura de Pastas e Separação de Conceitos

O projeto segue o padrão de design arquitetural modular do Django, separando explicitamente as responsabilidades de roteamento, serialização de dados, modelos relacionais e painel administrativo:

```text
├── core/                    # Configurações globais do projeto Django
│   ├── __init__.py
│   ├── settings.py          # Arquivo central de configurações (Lê variáveis de ambiente do Railway)
│   ├── urls.py              # Roteamento central da API e endpoints do Swagger/Admin
│   └── wsgi.py
├── api/                     # App modular da API de Consultas Médicas
│   ├── migrations/          # Histórico de evolução e versionamento do Banco de Dados
│   ├── admin.py             # Configurações avançadas do Painel Administrativo Django
│   ├── apps.py
│   ├── models.py            # Modelos Relacionais (Camada de Dados: Consulta, Especialista, Horario)
│   ├── serializers.py       # Serializadores (Validação de payload, parsing e transformação de tipos)
│   ├── services.py          # Camada Isolada de Serviços (Regras de negócio e travas de segurança)
│   ├── urls.py              # Sub-roteamento de endpoints locais da API
│   └── views.py             # ViewSets (Controladores REST que manipulam as requisições HTTP)
├── Dockerfile               # Instruções de compilação da imagem Docker do backend
```
# 🎯 Recursos de Engenharia Implementados

## 1. Painel de Controle Operacional (Django Admin)

O projeto utiliza o poderoso ecossistema **Django Admin** como o painel administrativo principal do sistema.

Ele foi estendido e configurado em `api/admin.py` para funcionar como o centro operacional do ecossistema móvel.

### 👑 Inserção de Especialistas

Através desta interface visual segura, administradores e clínicas podem:

- cadastrar médicos especialistas;
- definir áreas de atuação;
- gerenciar informações médicas.

### 🕒 Gerenciamento de Horários

Permite a triagem e o cadastro prévio da malha de horários disponíveis para consulta no banco de dados.

### 📊 Auditoria de Consultas

O painel oferece uma visão analítica em tempo real de todas as consultas agendadas pelo aplicativo móvel, permitindo:

- filtros por data;
- exclusões em lote;
- alterações de urgência;
- gerenciamento direto no banco de dados.

---

## 2. Autenticação Segura de Duplo Fator (Simple JWT)

A API expõe rotas seguras para geração e renovação de credenciais.

Ao efetuar login, o aplicativo recebe:

- um token de acesso de curta duração;
- um token de atualização.

O acesso aos endpoints protegidos exige o envio do cabeçalho:

```http
Authorization: Bearer <token>
```

Isso protege as informações médicas contra acessos não autorizados.

---

## 3. Camada Isolada de Negócio (`services.py`)

Para evitar modelos inflados ou controladores complexos, toda a lógica operacional fica concentrada na camada de serviços.

### 📅 Validação de Retroatividade

O backend intercepta o payload e impede que consultas sejam agendadas com datas passadas.

### ⏰ Controle de Horário Comercial

Filtros interceptam pedidos de agendamento e barram marcações fora do horário operacional estabelecido pela clínica.

Quando isso ocorre, a API retorna:

```http
400 Bad Request
```

---

## 4. Serializadores Avançados (`serializers.py`)

Os serializadores possuem dupla responsabilidade no ecossistema da aplicação.

### ✍️ Métodos de Escrita (POST/PUT/PATCH)

- validação de IDs relacionais;
- integridade dos dados enviados.

### 📖 Métodos de Leitura (GET)

Os endpoints retornam objetos detalhados contendo:

- nome do médico;
- especialidade;
- horário formatado;
- informações completas da consulta.

Isso reduz chamadas adicionais no aplicativo móvel.

---

# 🛣️ Matriz de Endpoints da API REST

| Método | Endpoint | Autenticação | Descrição |
|---|---|---|---|
| POST | `/api/token/` | Não | Recebe credenciais (`username/password`) e retorna os Tokens JWT |
| POST | `/api/token/refresh/` | Não | Renova o Access Token utilizando o Refresh Token |
| GET | `/api/consultas/` | Sim (JWT) | Lista todas as consultas do usuário autenticado |
| POST | `/api/consultas/` | Sim (JWT) | Cria um novo agendamento validando regras de data/hora |
| GET | `/api/consultas/<id>/` | Sim (JWT) | Retorna os detalhes completos de uma consulta |
| PUT | `/api/consultas/<id>/` | Sim (JWT) | Atualização completa da consulta |
| PATCH | `/api/consultas/<id>/` | Sim (JWT) | Atualização parcial da consulta |
| DELETE | `/api/consultas/<id>/` | Sim (JWT) | Remove permanentemente a consulta |

---

# 🔍 Parâmetros de Busca Dinâmica (Query Filters)

O endpoint:

```http
GET /api/consultas/
```

possui filtros dinâmicos acoplados diretamente via Query Parameters.

## Filtrar por Médico Especialista

```http
/api/consultas/?medico=NomeDoEspecialista
```

## Filtrar por Data Específica

```http
/api/consultas/?data=2026-05-20
```

---

# 📦 Como Instalar e Executar o Projeto Localmente

## Opção 1: Via Docker (Recomendado)

Certifique-se de possuir:

- Docker;
- Docker Compose.

Na raiz do projeto backend execute:

```bash
docker-compose up --build
```

O Docker irá:

- baixar a imagem do Python;
- instalar dependências;
- executar migrações;
- expor o servidor na porta `8000`.

---

## Opção 2: Ambiente Python Local

### 1. Criar e Ativar Ambiente Virtual

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

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

### 3. Executar Migrações do Banco

```bash
python manage.py migrate
```

---

### 4. Criar Superusuário

```bash
python manage.py createsuperuser
```

---

### 5. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver 0.0.0.0:8000
```

---

# 🌐 API em Produção (Live Demo)

O backend está hospedado na plataforma Railway com integração contínua via GitHub.

## 🔗 URL Base da API

```text
https://desafio-tecnico-back-end-django-production.up.railway.app/api/
```

## 🔗 Painel Administrativo (Django Admin)

```text
https://desafio-tecnico-back-end-django-production.up.railway.app/admin/
```

🔑 Credenciais Homologadas para Teste
Para facilitar a avaliação técnica e o mapeamento dos fluxos do ecossistema móvel na live demo, utilize a conta de superusuário configurada abaixo:

Usuário (Username): user_admin

Senha (Password): senha2026
