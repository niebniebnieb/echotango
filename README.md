# Virtual Gallery     :art:
### Features
* Artists' registration with optional registration fee.
* Artists' Info Upload
    * Headshot
    * Featured Image
    * Contact Info
* Gallery Images Upload
    * Artwork Info (price, dimensions)
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

### Artist Registration and/or Upload
####1.) Admin Cleans Most Legacy Image File Names

Headshot file format:
lastname-firstname-head.jpg or .tif ...

Featured Image file format:
lastname-firstname-art.jpg or .tif ...
```
python rename.py
```
Some files names have to be cleaned manually.
####2.) Admin Upload Legacy Images Files to Server
Dashboard > Media > Add New > Select Files > Upload

####3.) Artist Registers via Form
Can be via UPDATE or NEW

####4.) Admin Links Images to Artists
Run update_artists.sql

### Artwork/Product Registration and/or Upload
Plan A: Gravity Forms + Custom Post Type?
Plan B: Upload from Google Sheet.

http://www.evelindi.com/


