use supermercado;

create database supermercado;

select * from Produtos;

drop table Produtos; 

drop database supermercado;

CREATE TABLE Produtos ( 
	ID int NOT NULL UNIQUE AUTO_INCREMENT, 
    Nome varchar(255) NOT NULL UNIQUE, 
    Valor float,
    Código int,
    Qntd varchar(255),
    ItemEmEstoque boolean,
    PRIMARY KEY (ID)
);