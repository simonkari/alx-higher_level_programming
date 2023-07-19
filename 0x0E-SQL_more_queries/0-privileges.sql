-- 0x0E. SQL - More queries, task 0. My privileges!
-- Lists all priviledges for users `user_0d_1` and `user_0d_2`
SELECT * FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');
