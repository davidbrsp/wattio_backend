/app
  /models (SQLAlchemy para definicao dos schemas do DB)
  /repository (funcoes relativas a bancos de dados)
  /routers (endpoints da aplicação)
  /schemas (Classes pydantic para validacão de dados de entrada e sáida)
  /services ()
  main.py
docker.compose.yaml
Dockerfile.yaml
.dockerignore
.gitignore
README.md

n FastAPI the convention is to separate out your SQLAlchemy model classes from your Pydantic schemas — the SQLAlchemy classes are used only for defining the DB schema, the schemas are for validating incoming and outgoing data in your crud functions and path operations. (Pydantic schemas are sort of half-way between API serializer classes and dataclasses — which is a very handy hybrid to have.)

Now, it’s true that the creator of FastAPI has created a project, SQLModel, that tries to unify SQLAlchemy models and Pydantic schemas into one entity. But this library seems to be a little behind the curve in terms of keeping up with the latest developments in either SQLAlchemy or Pydantic. In any case, I prefer the pattern of separating the DB classes from the schemas. One reason to want this is to have different schemas for different CRUD operations — e.g. your schema for updates may have more optional types than your schema for reading.

https://medium.com/@tclaitken/setting-up-a-fastapi-app-with-async-sqlalchemy-2-0-pydantic-v2-e6c540be4308
