-- @Author      : Sukarna Jana
-- @Version     : 0.0.1V
-- @Last Update : 18-09-2023
-- @Brief       : To Drop dummy data / or full setup in database
-- @SQL Version : 8.0.34
-- @Note        : you need to Uncomments the line which you want to bring into action [ by removing "--" from front]

-- Cheack SQL Verion 
SELECT VERSION();

-- Delete all dummy/current data
DELETE FROM kaval_master;

-- Drop Table only
-- DROP TABLE kaval_master;

-- Drop Database only
-- DROP DATABASE heritagehaven;