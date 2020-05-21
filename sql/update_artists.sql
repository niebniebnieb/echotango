-- Update all fields of an artist with given name to given value
-- Do first for one artist named tom1:
-- Update brief_description with value of 'brief v2' for tom1 -- needs last name
-- Implement either with sproc or generate statements below from csv via Python.

SET @postid = 
(SELECT post_id
        FROM 4BS_postmeta
        WHERE meta_key = 'artist_first_name'
        AND meta_value = 'tom1');

UPDATE 4BS_postmeta
SET meta_value = 'brief v4'
WHERE meta_key = 'brief_description'
AND 4BS_postmeta.post_id = @postid;

-- To list the results of the update:

SELECT t1.ID, t1.post_title, t2.meta_value
FROM 4BS_posts as t1
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t1.ID = @postid;


/*
UPDATE 4BS_postmeta
SET meta_value = 'brief v2'
WHERE meta_key = 'brief_description'
AND 4BS_postmeta.post_id = (
	SELECT cid FROM (
    	SELECT post_id as cid
        	FROM 4BS_postmeta
            WHERE meta_key = 'artist_first_name'
            AND meta_value = 'tom1'
    ) AS c
)
*/
