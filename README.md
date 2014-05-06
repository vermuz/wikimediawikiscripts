wikispacetomediawikiexport
==========================

This is a collection of scripts to aid users in transferring materials from wikispaces to mediawiki.

filename.py

Place it in a folder and execute it. Opens each file. Places its name at the top and ends it with an ENDTITLE Places --ENDPAGE -- at the end of the page

This script will prepare the file to be used with Mediawiki Bulk Uploader.

http://meta.wikimedia.org/wiki/MediaWiki_Bulk_Page_Creator

Wikispaces to Mediawiki Export Procedure
----------------------------------------

- Use the Backup and Export facility in Wikispaces to export an archive of your wikispaces wiki (preferrably
txt format not the html).
- Decompress the archive.
- git clone https://github.com/nanotube/wikispacestomediawiki
- python wikispacetomediawiki/wstomwconverter.py -f file for all files for mediawiki equivalents of the wikispace files.
5- git clone https://github.com/vermuz/wikimediawikiscripts
Apply filename.py to all the converted files so that they can have their names appended to the top of the file
and ENDPAGE appended to the end of the file.
- Apply Sed filters to clean up the files.
- Create a new user in the mediawiki with the role of a "bot"
- Get bulkinsert script from the following url: http://meta.wikimedia.org/wiki/MediaWiki_Bulk_Page_Creator
- Download Snoopy class for your bot.
http://sourceforge.net/projects/snoopy/
- Install mediawiki
- Download extensions
http://www.mediawiki.org/wiki/Extension:WYSIWYG
http://www.mediawiki.org/wiki/Extension:MsUpload
- If you are using a vagrant setup,
Add following line to your vagrant file to be able to upload images later,
 config.vm.synced_folder "./public" , "/var/www/" + project_name + "/", :owner => "www-data", :group => "vagrant"
If you are using XAMPP,
Create a subdirectory, tmp in the images folder.
Allow access to your images folder.
- Add following lines to your LocalSettings.php
```php
## To enable image uploads, make sure the 'images' directory
## is writable, then set this to true:
$wgEnableUploads = true;
$wgUseImageMagick = true;
$wgImageMagickConvertCommand = "/usr/bin/convert";
require_once( "$IP/extensions/WYSIWYG/WYSIWYG.php" );
$wgGroupPermissions['*']['wysiwyg'] = true;

##Start --------------------------------------- MsUpload
$wgMSU_ShowAutoKat = false;     #autocategorisation
$wgMSU_CheckedAutoKat = false;  #checkbox for autocategorisation checked
$wgMSU_debug = false;           #debug mode 
$wgMSU_ImgParams = '400px';     #default max-size for inserted image
$wgMSU_UseDragDrop = true;      #show drag&drop area
require_once "$IP/extensions/MsUpload/msupload.php";
##End  --------------------------------------- MsUpload
```

- Place the bulkinsert.php and snoopy class in your mediawiki folder.
- Add mediawiki url and bot information to the bulkinsert.php script.
- Execute the bulkinsert.php script on all files to be imported into mediawiki.
- Get all images from wikispaces (usually in a folder called files)
- cd /maintanence (Folder is inside mediawiki by default)
- php importImages.php ../YOUR_FOLDER_CONTAINING_IMAGES jpg
- After export - see your wiki for results in Special:Pages -> All Pages section

GoodLuck!
