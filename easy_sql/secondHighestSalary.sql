# Write your MySQL query statement below
SELECT ISNULL(SALARY ,'null') AS `SecondHighestSalary` 
FROM Employee WHERE SALARY < (SELECT MAX(SALARY)  FROM Employee)  
ORDER BY SALARY DESC LIMIT 1



-- the following query worked, but was adding "" to values
SELECT
    CASE
        WHEN SALARY IS NULL THEN 'null'
        ELSE SALARY
    END AS SecondHighestSalary
FROM Employee WHERE SALARY < (SELECT MAX(SALARY)  FROM Employee)  
ORDER BY SALARY DESC LIMIT 1

-- 
-- the following query worked, but was adding "" to values
SELECT
    CASE
        WHEN (SELECT count(DISTINCT SALARY) from Employee) <2
        THEN NULL
        ELSE(SELECT Salary FROM Employee 
              ORDER BY Salary DESC LIMIT 1,1) 
    END AS SecondHighestSalary
FROM Employee WHERE SALARY < (SELECT MAX(SALARY)  FROM Employee)  
ORDER BY SALARY DESC LIMIT 1