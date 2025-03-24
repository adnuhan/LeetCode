# Write your MySQL query statement below
# Write your MySQL query statement below
WITH UserRatings AS (
    SELECT u.name, COUNT(mr.movie_id) AS rating_count
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.name
),
MaxUser AS (
    SELECT name
    FROM UserRatings
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
),
MovieRatings AS (
    SELECT m.title, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
),
MaxMovie AS (
    SELECT title
    FROM MovieRatings
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
)
SELECT name AS results FROM MaxUser
UNION ALL
SELECT title AS results FROM MaxMovie;