# 🚀 Docs Manager

> Gestão inteligente de documentos: controle sobre arquivos com uma camada colaborativa de comentários e gestão de privilégios de acesso

<div align="center">
    <img width=200px src="docs_manager\static\img\logotipo_fundo.svg"/>
</div>

<p align="center">Figura 1: Logo da Aplicação.</p>

## 📋 Sobre o Projeto

O projeto é construído sobre uma **arquitetura monolítica modular do Django**, permitindo gerenciar de forma eficiente o ciclo de vida de documentos e comentários. Ele oferece uma interface intuitiva e controle de acesso diferenciado para diferentes perfis de usuários.

Você pode conferir a aplicação em produção [clicando aqui](https://occasional-christin-caioduart3-2bee5def.koyeb.app/) (hospedado no Koyeb).


### Funcionalidades Principais

* **Gestão de Acesso:** Autenticação para Superusuários e Usuários Comuns com restrições de permissões baseadas em perfil.
* **Painel Administrativo:** Interface de gerenciamento de usuários exclusiva para Superusuários.
* **Módulo de Documentos:** Listagem, upload, download, remoção e buscador integrado de arquivos.
* **Interatividade:** Sistema de criação e listagem de comentários em documentos.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12** (Back-end)
* **Django 6.0.2** (Framework Back-end)
* **Supabase** (Postgresql em nuvem)
* **HTML5, CSS3 e JavaScript** (Front-end)

---

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente de desenvolvimento em sua máquina.

### 1. Clonar o Repositório

```bash
git clone https://github.com/CaioDuart3/docs_manager
cd docs_manager

```

### 2. Configurar o Ambiente Virtual

```bash
# Criar o ambiente
python -m venv venv

# Ativar o ambiente (Windows)
venv\Scripts\activate

# Ativar o ambiente (Linux/macOS)
source venv/bin/activate

```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt

```

### 4. Configurações Iniciais (.env)

Crie um arquivo `.env` na raiz do projeto seguindo o modelo abaixo:

```env
# Chave secreta do Django
# Substitua pelo valor gerado com a execução:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY=sua-secret-key-aqui

# Ativa ou desativa o modo de debug
# True para desenvolvimento (mostra erros detalhados)
# False para produção (não mostra erros e aumenta a segurança)
DEBUG=True

# Hosts permitidos para acessar o site
# Separe múltiplos hosts por vírgula
# Em produção, adicione o domínio real do seu site
ALLOWED_HOSTS=localhost,127.0.0.1,www.seudominio.com

# Configurações do banco de dados PostgreSQL (Supabase)
# Nome do banco de dados criado no Supabase
DB_NAME=nome_do_banco_de_dados

# Usuário do banco de dados
# Normalmente 'postgres' no Supabase
DB_USER=usuario_do_banco

# Senha do banco de dados
# A senha que você definiu ao criar o projeto no Supabase
DB_PASSWORD=minha_senha

# Host do banco de dados
DB_HOST=host_do_banco

# Porta do banco de dados
# Normalmente 5432 para PostgreSQL
DB_PORT=porta_do_banco

```
> ⚠️ **Dica:** Para rodar localmente, você pode usar PostgreSQL instalado na sua máquina. Para produção, configure as variáveis fornecidas pelo Supabase.

### 5. Migrações e Superusuário

```bash
# Criar as tabelas no banco de dados
python manage.py migrate

# Criar administrador para gerenciar o sistema
python manage.py createsuperuser

```

### 6. Iniciar o Servidor

```bash
python manage.py runserver

```

O projeto estará disponível em `http://127.0.0.1:8000`.

---

## 📂 Estrutura de Pastas

```text
└─ docs_manager          // Raiz do projeto
    ├─ apps              // Módulos da aplicação
    │  ├─ documents      // Gestão de documentos e comentários
    │  │  ├─ static      // Assets específicos do app
    │  │  └─ templates   // Telas de documentos
    │  └─ users          // Gestão de usuários e autenticação
    │     └─ templates   // Tela de login
    ├─ docs_manager      // Configurações centrais do Django (Settings)
    └─ static            // Estilização e assets globais
        ├─ css
        └─ img

```

---


## 👁️ Observações Relevantes

Ao criar super usuários, eles terão acesso a todas as funcionalidades, incluindo:
- Criação e gerenciamento de usuários;
- Upload, visualização, download e exclusão de qualquer documento;
- Visualização e adição de comentários em qualquer documento.

Usuários comuns possuem acesso mais limitado. Eles podem:

- Apagar apenas seus próprios documentos;
- Upload, visualização e download de documentos;
- Visualizar e adicionar comentários em qualquer documento.

---

⚠️ Atenção: Este site foi para produção com ferramentas 100% gratuitas, como Koyeb e Supabase. Por isso, o desempenho pode ser limitado devido às restrições de hardware dos planos gratuitos. Agradeço sua paciência e compreensão!

---


> Desenvolvido com ☕ por **Caio Duarte**
