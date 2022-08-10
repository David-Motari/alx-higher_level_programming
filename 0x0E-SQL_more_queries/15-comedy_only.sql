-- lists all Comedy shows in the database hbtn_0d_tvshows.cript that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_shows.title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_shows.id = tv_show_genres.show_id 
AND tv_show_genres.genre_id = tv_genre.id 
AND tv_genre.name = "Comedy"
 ORDER BY tv_show.title;
