-- @Author      : Sukarna Jana
-- @Version     : 0.0.1V
-- @Last Update : 18-09-2023
-- @Brief       : Store some dummy data to test run Software
-- @SQL Version : 8.0.34

-- Cheack SQL Verion 
SELECT VERSION();

-- Access the Database first 
USE heritagehaven; 

-- Dump dummy data
INSERT INTO kaval_master (Kaval_ID,Kaval_Name)
VALUES
(1909, "Sukarna"),
(1109, "Kunal"),
(1000, "UNKNOWN"),
(1001, "UNKNOWN"),
(1002, "UNKNOWN");

-- Debug 
SELECT * FROM kaval_master;