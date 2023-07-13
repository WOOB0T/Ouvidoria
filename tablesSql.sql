/* TABELAS DE PESSOAS */

/* Setor = 1 (Estudantes)*/

create table estudantes(
matricula bigint,
nome varchar(100),
curso varchar(50),
email_inst varchar(70),
primary key (matricula)
); 

/* Setor = 2 (Docentes)*/

create table docentes(
id bigint,
nome varchar(100),
curso varchar (50),
disciplinas varchar(150),
email_inst varchar(70),
primary key (id)
);

/* Setor = 3 (Colaboradores)*/

create table colaboradores(
id bigint,
nome varchar(100),
depart varchar (50),
email_inst varchar(70),
primary key (id)
);

/* TABELAS DE MANIFESTAÇÕES */

/* Lista de Manifestações*/

create table ocorrencias(
protocolo int auto_increment,
tipo int,
titulo varchar(100),
descricao varchar (300),
autor varchar(100),
primary key (protocolo)
);
 
