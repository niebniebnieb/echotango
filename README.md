# Virtual Gallery     :art:
### Features
* Artists' registration with optional registration fee.
* Artists' Info Upload
    * Headshot
    * Featured Image
    * Contact Info
* Gallery Images Upload
    * Artwork Info (price, dimensions)
* Bulk Image File Resizing
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
#### 2.) Artist to be "Published" instead of "Draft"
edit 
	- wp-content/themes/astra/functions.php
```
add_filter('cf7_2_post_status_artists', 'publish_by_default', 10,1);
function publish_by_default($status){
  return 'publish';
}
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
rename files to IN_IMG
#### 2.) Admin Resizes Images
Resies files in IN_IMG by running
```
python to-jpg.py # in ADD mode
```
Files go to OUT_IMG
Some files names have to be cleaned manually.
#### 3.) Admin Upload Legacy Images Files to Media Library
Dashboard > Media > Add New > Select Files > OUT_IMG > Upload

#### 4.) Artist Registers via Form
Can be via UPDATE or NEW

#### 5.) Admin Links Artist to Media Library Image
For every artist who registered, set artist name and run for featured artwork and headshot if supplied.
Can also do: Dashboard > Artists > <artist> > Featured Image > Search > ...

```
update_artists.sql
```

### New Artist Image Upload
#### 1.) Artist uses Registration Page to Upload Images
Files go to upload/img
#### 2.) Admin Resizes Images
Downloads files to ADD_IN_IMG
and runs
```
python to-jpg.py # in ADD mode
```
Files go to ADD_OUT_IMG
#### 3.) Admin Imports Images to Media Library
As above but from ADD_OUT_IMG dir.
Delete files from uploads/img

#### 4.) Admin Links Artist to Media Library Image
For every artist who registered, set artist name and run for featured artwork and headshot if supplied.
Can also do: Dashboard > Artists > <artist> > Featured Image > Search > ...
(same as 5. above)
```
python update_artist
```

### Artwork/Product Registration
Gravity Forms + Custom Post Type
Alt: Upload from Google Sheet.

http://www.evelindi.com/


