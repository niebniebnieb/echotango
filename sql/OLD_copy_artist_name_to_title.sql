-- The Custom Post Title for artists is constant: CF7 2 Post
-- Until Post My CF7 From can update the title with artist name, this will do it:

USE sonomad6_WPBGT;

UPDATE 4BS_posts
INNER JOIN 4BS_postmeta
ON 4BS_posts.ID = 4BS_postmeta.post_id
SET post_title = 4BS_postmeta.meta_value
WHERE post_type = 'artists'
AND 4BS_postmeta.meta_key = 'artist_last_name';

-- AND 4BS_postmeta.meta_key = CONCAT( 'artist_first_name',' ','artist_last_name');


-- To list the results of the title update:

SELECT t1.ID, t1.post_title, t2.meta_value
FROM 4BS_posts as t1 
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t2.meta_key = 'artist_first_name'
ORDER BY t1.ID


-- Update meta_value --- under construction -- ERROR character set conflict

DROP PROCEDURE IF EXISTS GetOfficeByCountry;

DELIMITER //

CREATE PROCEDURE GetOfficeByCountry(
	IN countryName VARCHAR(255)
)
BEGIN
SELECT t1.ID, t1.post_title, t2.meta_value
FROM 4BS_posts as t1 
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t2.meta_key = 'artist_first_name'
AND t2.meta_value = countryName;

END //

DELIMITER ;

