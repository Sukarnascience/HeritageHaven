-- @Author      : Sukarna Jana
-- @Version     : 0.0.1V
-- @Last Update : 18-09-2023
-- @Brief       : Create DataBase and Tables by which we can use for setuping everything for Software to run
-- @SQL Version : 8.0.34

-- Cheack SQL Verion 
SELECT VERSION();
-- it it is above 8.0 then it's fine or else u have to change the sintax of AUTO_INCREMENT to AUTOINCREMENT

-- Creating Database
CREATE DATABASE heritagehaven;

-- Start using it
USE heritagehaven;

-- Setup Tables
CREATE TABLE kaval_master (
    SNo INTEGER PRIMARY KEY AUTO_INCREMENT,
    Kaval_ID INT UNSIGNED NOT NULL,
    Kaval_Name VARCHAR(40) NOT NULL,
    UNIQUE(Kaval_ID),
    CHECK(Kaval_ID >= 0 AND Kaval_ID <= 9999)
);

-- Debug 
SELECT * FROM kaval_master;
