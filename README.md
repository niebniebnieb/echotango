# Virtual Gallery     :art:
Virtual online Gallery where artists can publish and sell their artworks.
### Features
* Artists' Registration with Optional Registration Fee
* Artists' Profile + Upload
    * Headshot
    * Featured Image
    * Contact Info
* Gallery Images + Upload
    * Artwork Info (price, dimensions)
* Bulk Image File Resizing and Compression
* Shopping Cart and eCommerce Payment
* Unlimited number of artists and artworks.

### Installation
Install and active there free Wordpress plugins:
* Advanced Custom Fields
* Contact Form 7
* Custom Post Type UI
* Post My CF7 Form
* WooCommerce
* WooCommerce Services
* WooCommerce Stripe Gateway
* Wordpress File Upload

#### 1.) Pincode -> Zipcode
edit
```
wp-content/plugins/cf7-google-map/public/partials/cf7-googlemap.php
```
#### 2.) PHP Updates
edit 
	- wp-content/themes/astra/functions.php
```
// Publish added artists immediately instead of "Draft"
add_filter('cf7_2_post_status_artists', 'publish_by_default', 10,1);
function publish_by_default($status){
  return 'publish';
}

// Link every product to its artist via prod.post_parent
add_action( 'elementor/query/prodquery', function( $query ) {
	$query->set( 'post_parent', get_the_ID() );
} );
```
#### 3.) To increase contrast in Registration Form
Append to: wp-content/plugins/contact-form-7/includes/css/styles.css (requires restart?)
```
.wpcf7
{
 background-color: #ddd;
 border: 20px solid #ddd;
}
```
#### 4.) To Display Products in Artist Profile
Dashboard > Template > Artist Profile Pages > Elementor >
Search = post > Drag-and-drop > Posts (widget) >
Content > Query > Source = Products > Query ID = prodquery > Update

This is used and required by 2.) above: has to match 'prodquery'

### Image File Format
Headshot:
```
lastname-firstname-head.jpg or .tif or .psd ...
```
Featured Image:
```
lastname-firstname-art.jpg or .tif or .psd ...
```
### Bulk Upload of Returning Artists

#### 1.) Admin Cleans Most Legacy Image File Names

```
python rename.py
```
Renamed files go to IN_IMG.
Some file names have to be cleaned manually.
#### 2.) Admin Resizes Images
Resize files in IN_IMG by running
```
python to-jpg.py # in BULK mode
```
Files go to OUT_IMG
#### 3.) Admin Upload Legacy Images Files to Media Library
Dashboard > Media > Add New > Select Files > OUT_IMG > Upload

#### 4.) Artist Registers via Form
Can be via UPDATE or NEW

#### 5.) Admin Links Artist to Media Library Image
For every artist who registered, set artist name and run for featured artwork and headshot if supplied.

```
update_artists.sql
```
Manual alternative: Dashboard > Artists > select artist name > Featured Image > Search > ...
Repeat for Featured Artwork and Headshot if supplied

### New Artist Featured Artwork and Headshot Upload
#### 1.) Admin Resizes, Compresses and Converts Images to .jpg
After on or more artists have uploaded images (to upload/img)
in the Registration page, the admin resizes and compresses
them by running:
```
python to-jpg.py # in ADD mode
```
Files go to ADD_OUT_IMG
#### 2.) Admin Imports Images to Media Library
As above but from ADD_OUT_IMG dir.

#### 3.) Admin Links Artist to Media Library Image
For every artist who registered, set artist name and run for featured artwork and headshot if supplied.
```
python update_artist
```
Manual alternative: Dashboard > Artists > select artist name > Featured Image > Search > ...
Repeat for Featured Artwork and Headshot if supplied
(same as 5. above)

### Artwork/Product Registration
Gravity Forms + Custom Post Type
Alt: Upload from Google Sheet.

http://www.evelindi.com/


