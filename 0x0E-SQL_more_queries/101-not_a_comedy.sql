-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
    SELECT s.title
    FROM tv_shows s
    INNER JOIN tv_show_genres x ON s.id = x.show_id
    INNER JOIN tv_genres g ON x.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
