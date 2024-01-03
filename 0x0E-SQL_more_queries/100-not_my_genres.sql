-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
    SELECT g.name
    FROM tv_genres g
    INNER JOIN tv_show_genres s ON g.id = s.genre_id
    INNER JOIN tv_shows t ON s.show_id = t.id
    WHERE t.title = 'Dexter'
)
ORDER BY g.name ASC
