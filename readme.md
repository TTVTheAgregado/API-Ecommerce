# API E‑commerce

Descrição
Uma API RESTful para loja virtual (produtos, categorias, usuários, carrinho, pedidos, autenticação). Projetada para ser simples, escalável e fácil de integrar com front‑end (web/mobile).

Principais funcionalidades

- Autenticação JWT (registro / login / refresh)
- CRUD de produtos e categorias
- Carrinho de compras e checkout
- Gestão de pedidos (status, histórico)
- Pagamentos (integração via provider externa)
- Controle de permissões (usuário vs. administrador)
- Logs e métricas básicas

Stack sugerido

- Backend: Node.js + Express ou Python + FastAPI
- Banco de dados: PostgreSQL (ou MongoDB)
- Autenticação: JWT
- Migrations: Prisma / TypeORM / Alembic
- Testes: Jest / Pytest

Pré‑requisitos

- Node >= 16 ou Python >= 3.9
- Docker (opcional)
- Banco de dados (Postgres)

Instalação (exemplo Node.js)

```bash
git clone <repo-url>
cd repo
npm install
cp .env.example .env
# ajustar variáveis de ambiente
npm run migrate
npm run dev
```

Variáveis de ambiente (exemplo)

```
PORT=3000
DATABASE_URL=postgres://user:pass@localhost:5432/ecommerce
JWT_SECRET=uma_chave_secreta
PAYMENT_PROVIDER_KEY=...
NODE_ENV=development
```

Execução

- Desenvolvimento: npm run dev
- Build/produção: npm run build && npm start
- Docker (exemplo):

```bash
docker compose up --build
```

Endpoints principais (exemplos)

- Autenticação
  - POST /auth/register
  - POST /auth/login
  - POST /auth/refresh
- Usuários
  - GET /users/:id
  - PUT /users/:id
- Produtos
  - GET /products
  - GET /products/:id
  - POST /products (admin)
  - PUT /products/:id (admin)
  - DELETE /products/:id (admin)
- Categorias
  - GET /categories
  - POST /categories (admin)
- Carrinho
  - GET /cart
  - POST /cart/items
  - DELETE /cart/items/:itemId
- Pedidos
  - POST /orders
  - GET /orders/:id
  - GET /orders (admin)

Exemplo de requisição (login)

```bash
curl -X POST https://api.seu-dominio.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"senha"}'
```

Resposta:

```json
{
  "accessToken": "eyJ...",
  "refreshToken": "..."
}
```

Exemplo de criar produto (com token)

```bash
curl -X POST https://api.seu-dominio.com/products \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Camiseta","price":49.9,"stock":100,"categoryId":1}'
```

Boas práticas

- Validar e sanitizar entradas (use bibliotecas de schema)
- Usar paginação, filtros e ordenação em listagens
- Tratar erros com códigos HTTP apropriados e mensagens claras
- Proteger rotas administrativas
- Testes automatizados para fluxos críticos (checkout, auth)

Testes

- Rodar suíte de testes: npm test ou pytest
- Cobertura mínima recomendada: 70%+ em lógica crítica

Contribuição

- Fork -> branch feature/xxx -> PR com descrição e testes
- Siga o padrão de commits e o guia de estilo do projeto

Licença

- Escolha a licença desejada (ex: MIT)

Contato

- Mantenedor: seu-email@exemplo.com

Observações finais
Adapte os exemplos ao framework e às dependências do seu projeto. Posso gerar um README específico para Node/Express ou FastAPI com instruções detalhadas se quiser.
