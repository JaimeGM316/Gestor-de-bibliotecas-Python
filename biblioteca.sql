drop database if exists biblioteca;

create database biblioteca;

use biblioteca; 

create table libro (
   id integer not null,
   titulo varchar(25) not null,
   autor varchar(25) not null,
   editorial varchar(25) not null,
   paginas integer not null,
   copias integer not null,
   constraint id_pk primary key (id)
);

insert into libro values(1,"El pantano", "Pedro Parque", "Marte", 100, 500);