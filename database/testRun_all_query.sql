-- @Author      : Sukarna Jana
-- @Version     : 0.0.1V
-- @Last Update : 18-09-2023
-- @Brief       : Create DataBase and Tables by which we can use for setuping everything for Software to run

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

INSERT INTO kaval_master (Kaval_ID,Kaval_Name)
VALUES
(1909, "Sukarna"),
(1109, "Kunal"),
(1000, "UNKNOWN"),
(1001, "UNKNOWN"),
(1002, "UNKNOWN");

-- Debug 
SELECT * FROM kaval_master;