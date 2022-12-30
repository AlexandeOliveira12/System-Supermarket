use Compras;

create database Compras;

select * from HistoricoCompras;

drop table HistoricoCompras; 

drop database Compras;

create table HistoricoCompras (
	ID int NOT NULL UNIQUE AUTO_INCREMENT, 
    Horario datetime,
    item varchar(255),
    valor float,
    CC boolean,
    CD boolean,
    D boolean
)
