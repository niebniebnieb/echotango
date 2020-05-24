-- After an artist has registered under the Registration form's "Update" menu option
-- update all missing fields.
-- Do first for one artist named tom1:
-- Update brief_description with value of 'brief v2' for tom1 -- needs last name
-- (Implement either with sproc after character set fix or generate statements below from csv via Python.)

SET @first = 'susan';
SET @last = 'bradford';

SET @postid = (SELECT t3.ID FROM
(
    SELECT t1.ID
    FROM 4BS_posts as t1
    INNER JOIN 4BS_postmeta as t2
    ON t1.ID = t2.post_id
    WHERE t1.post_type = 'artists'
    AND t1.post_status != 'trash'
    AND t2.meta_key = 'artist_first_name'
    AND t2.meta_value = @first) as t3,
(
    SELECT t1.ID
    FROM 4BS_posts as t1
    INNER JOIN 4BS_postmeta as t2
    ON t1.ID = t2.post_id
    WHERE t1.post_type = 'artists'
    AND t1.post_status != 'trash'
    AND t2.meta_key = 'artist_last_name'
    AND t2.meta_value = @last) as t4
WHERE t3.ID = t4.ID);

SELECT @postid;
SELECT CONCAT( @last, '-', @first, '-art.jpg');

UPDATE 4BS_postmeta
SET meta_value = CONCAT( @last, '-', @first, '-art.jpg')
WHERE meta_key = '_wp_attached_file';
-- AND 4BS_postmeta.post_id = @postid;


SELECT * from 4BS_postmeta where meta_key = '_wp_attached_file';
-- To list the results of the update:

SELECT t1.ID, t2.meta_key, t2.meta_value
FROM 4BS_posts as t1
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t1.ID = @postid
ORDER BY t2.meta_key;

-- UPDATE 4BS_postmeta
-- SET meta_value = 'brief v5'
-- WHERE meta_key = 'brief_description'
-- AND 4BS_postmeta.post_id = @postid;

/*SELECT t1.ID, t1.post_title, t2.meta_key, t2.meta_value
FROM 4BS_posts as t1
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t1.post_status != 'trash'
ORDER BY t1.ID;
*/
-- SELECT * from 4BS_posts WHERE ID = 151
-- SELECT * from 4BS_posts WHERE post_name LIKE '%brad%'
    /*SELECT t2.*
    FROM 4BS_posts as t1
    INNER JOIN 4BS_postmeta as t2
    ON t1.ID = t2.post_id
    WHERE t1.post_type = 'artists'
    AND t1.post_status != 'trash'
    AND t1.ID = 394
    ORDER BY t2.meta_key
    -- AND t2.meta_key = 'artist_last_name'
    -- AND t2.meta_value = 'bradford'*/
-- UPDATE 4BS_postmeta SET meta_value = 436 WHERE meta_id = 3612;