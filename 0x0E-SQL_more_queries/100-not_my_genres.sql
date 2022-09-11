-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
(
SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id 
AND tv_show_genres.show_id = tv_shows.id 
AND tv_shows.title = 'Dexter'
)
GROUP BY tv_genres.name
ORDER BY tv_genres.name;
