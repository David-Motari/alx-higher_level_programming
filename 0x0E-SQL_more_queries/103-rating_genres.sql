--  lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genre.name, SUM(tv_genre.rate) AS rating
  FROM tv_genres 
  INNER JOIN tv_show_genres
  ON tv_show_genres.genre_id = tv_genre.id
  INNER JOIN tv_show_ratings AS r
  ON tv_show_ratings.show_id = tv_show_genres.show_id
  GROUP BY tv_genre.name
  ORDER BY rating DESC;
