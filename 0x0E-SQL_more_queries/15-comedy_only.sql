-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres t ON tv_shows.id = t.show_id
INNER JOIN tv_genres g ON t.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY tv_shows.title ASC;
