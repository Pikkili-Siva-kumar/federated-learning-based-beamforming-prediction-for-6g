drop database if exists cyberbullying;
create database cyberbullying;
use cyberbullying;

create table users (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(225),
    age INT,
    email VARCHAR(225), 
    password VARCHAR(225)
    );

-- create table results (
--     id INT PRIMARY KEY AUTO_INCREMENT, 
--     user_name VARCHAR(225),
--     user_email VARCHAR(225),
--     user_age INT,
--     input VARCHAR(225),
--     output VARCHAR(225),
--     probability VARCHAR(225)
--     );

-- create table reviews (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     user_name VARCHAR(225),
--     user_email VARCHAR(225), 
--     user_age INT,
--     rating INT,
--     feedback VARCHAR(1000)
--     );