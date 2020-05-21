-- This script should be run daily or more often to
-- OBSOLETE: Change all artists Draft Posts to Published (draft to publish function is working)

USE sonomad6_WPBGT;

SET post_status = 'publish'
WHERE post_status = 'draft'
AND post_type = 'artists';

