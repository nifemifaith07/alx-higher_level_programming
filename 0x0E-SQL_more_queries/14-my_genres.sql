-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres g ON tv_genres.id = g.genre_id
INNER JOIN tv_shows s ON g.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY tv_genres.name ASC;
