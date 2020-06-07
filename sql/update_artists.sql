-- After an artist has registered under the Registration form's "Update" menu option
-- update all missing fields.
-- Do first for one artist named @first @last:
-- OLD - WAS: Update brief_description with value of 'brief v2' for tom1 -- needs last name
-- NEW - IS: Update featured_artwork
-- (Implement either with sproc or) Generate statements below from csv via Python.
-- TODO: Set @postid once and reuse for all other fields

-- Link given artist with artist's featured image
SET @first = 'Barbara';
SET @first_lower = LOWER(@first);
SET @last = 'Schwartzberg';
SET @last_lower = LOWER(@last);

-- SET @art_or_head = 'head'; -- TODO Do INSERT for headshot if exists in .
SET @postid = (
SELECT t3.ID
    FROM
        (SELECT t1.ID
        FROM 4BS_posts as t1
        INNER JOIN 4BS_postmeta as t2
        ON t1.ID = t2.post_id
        WHERE t1.post_type = 'artists'
        AND t1.post_status != 'trash'
        AND t2.meta_key = 'artist_first_name'
        AND t2.meta_value = @first) as t3,
        (SELECT t1.ID
        FROM 4BS_posts as t1
        INNER JOIN 4BS_postmeta as t2
        ON t1.ID = t2.post_id
        WHERE t1.post_type = 'artists'
        AND t1.post_status != 'trash'
        AND t2.meta_key = 'artist_last_name'
        AND t2.meta_value = @last
        ) as t4
    WHERE t3.ID = t4.ID
);

SELECT @postid;
-- = 774

SET @title = (SELECT CONCAT( @first, ' ', @last));

SELECT @title;

UPDATE 4BS_posts
SET post_title = @title
WHERE ID = @postid;

SET @postid_img_art = (SELECT ID FROM 4BS_posts
WHERE post_type = 'attachment'
AND post_name LIKE CONCAT(@last_lower,'%')
AND post_name LIKE CONCAT('%',@first_lower,'%')
AND post_name LIKE '%-art');


SET @postid_img_head = (SELECT ID FROM 4BS_posts
WHERE post_type = 'attachment'
AND post_name LIKE CONCAT(@last_lower,'%')
AND post_name LIKE CONCAT('%',@first_lower,'%')
AND post_name LIKE '%-head');

SELECT @postid_img_art;
SELECT @postid_img_head;

INSERT INTO 4BS_postmeta (post_id, meta_key, meta_value) VALUES (
@postid, '_thumbnail_id', @postid_img_art);

UPDATE 4BS_postmeta
SET meta_value = @postid_img_art
WHERE meta_key = 'featured_artwork'
AND post_id = @postid;

-- TODO handle null value for missing head -> ''
UPDATE 4BS_postmeta
SET meta_value = @postid_img_head
WHERE meta_key = 'headshot'
AND post_id = @postid;

-- SELECT post_id FROM 4BS_postmeta WHERE meta_key = '_wp_attached_file'
-- AND meta_value = (SELECT CONCAT( @last, '-', @first, '-art.jpg'));
-- _thumbnail_id

-- INSERT INTO 4BS_postmeta (post_id, meta_key, meta_value) VALUES (
    -- @postid, 'post_title', @title
    -- IF(@art_or_head = 'art', 'featured_artwork', 'headshot'),
    -- (SELECT ID FROM 4BS_posts WHERE post_name =
    --    (SELECT CONCAT( @last, '-', @first, '-', @art_or_head))
    -- )
-- );

/*
SELECT @postid;
SET @art_img = (SELECT CONCAT( @last, '-', @first, '-art.jpg'));
SELECT @art_img;
*/
-- TODO find out what this is:
-- SET @img_post_id = (SELECT * FROM 4BS_postmeta WHERE meta_key = '_wp_attached_file' AND meta_value = @art_img);

/*
UPDATE 4BS_postmeta
SET meta_value = @art_img;
WHERE meta_key = '_wp_attached_file';
-- AND 4BS_postmeta.post_id = @postid;
*/
-- To list the results of the update:
-- post_id = Artist, meta_value = image post id
-- SELECT * FROM 4BS_postmeta WHERE meta_key = 'featured_artwork';

/*
SELECT t1.ID, t2.meta_key, t2.meta_value
FROM 4BS_posts as t1
INNER JOIN 4BS_postmeta as t2
ON t1.ID = t2.post_id
WHERE t1.post_type = 'artists'
AND t1.ID = @postid
ORDER BY t2.meta_key;
*/

/*
UPDATE 4BS_postmeta
SET meta_value = 'brief v5'
WHERE meta_key = 'brief_description'
AND 4BS_postmeta.post_id = @postid;
*/
/*
SELECT t1.ID, t1.post_title, t2.meta_key, t2.meta_value
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


-- SELECT * FROM 4BS_postmeta WHERE meta_key = '_wp_attached_file' AND meta_value = 'udell-luann-art.jpg';
-- SELECT * FROM 4BS_postmeta WHERE meta_key = '_wp_attached_file' AND meta_value = 'bradford-susan-art.jpg';
-- SELECT * FROM 4BS_posts WHERE ID IN( 574,575);
-- -- SELECT * FROM 4BS_posts WHERE ID = 129;
-- SELECT * FROM 4BS_postmeta WHERE meta_key IN (574,575);
-- SELECT * FROM 4BS_postmeta WHERE post_id IN (574,575,129,130);
-- SELECT * FROM 4BS_postmeta WHERE meta_value IN (574,575,129,130);
-- SELECT * FROM 4BS_postmeta WHERE meta_id IN (574,575,129,130);

/*SET @firstname = (SELECT meta_value
FROM 4BS_postmeta
WHERE post_id = @postid
AND meta_key = 'artist_first_name');

SET @lastname = (SELECT meta_value
FROM 4BS_postmeta
WHERE post_id = @postid
AND meta_key = 'artist_last_name');
*/
