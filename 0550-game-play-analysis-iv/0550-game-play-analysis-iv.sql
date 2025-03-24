# Write your MySQL query statement below

# First, let's store the first login date of each player.
WITH temp AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity 
    GROUP BY player_id
)

# Calculate the fraction of players who logged in exactly one day after their first login.
SELECT 
    ROUND(
        SUM(DATEDIFF(a.event_date, t.first_login_date) = 1) / COUNT(DISTINCT a.player_id), 2
    ) AS fraction
FROM Activity a
JOIN temp t ON a.player_id = t.player_id;