# Write your MySQL query statement below
SELECT firstName, lastName, city, state from Person LEFT JOIN Address ON Person.personID = Address.personID;