# Virtual Gallery - :art:
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
Headshot file format:
lastname-firstname-head.jpg or .tif ...

Featured Image file format:
lastname-firstname-art.jpg or .tif ...

Clean most file names:
```
python rename.py
```
#### Upload Images to Server
For example:

```
ftp
open ftp.sonomacountyarttrails.org
sonomad6
<password>
lcd ~/IMAGE
cd public_html/sebartsvirtual/wp-content/uploads/img
prompt
mput *.jpg
```
#### Convert all files to .jpg at host.
For example:

bluehost > Advanced > Image > Convert

### Artwork/Product Registration and/or Upload
Upload from Google Sheet.

http://www.evelindi.com/

:art:
