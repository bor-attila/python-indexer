[Public] Python Dropbox Indexer
===============================

First steps:
------------

1. Register a [dropbox][1] account
2. Create a folder with name : <br> <b>Public</b>
3. Uploade the style folder to the Public folder. <br> <b>/style/style.css</b>

Installation:
------------

* Create a ./bin directory in your home
	```
	cd ~
	mkdir .bin
	cd ./bin
	```

* Download the PDI

    ```wget https://github.com/bor-attila/python-indexer/archive/master.zip```
* Unzip

    ```unzip master.zip```

* Create a (soft) link in ./bin

    ```ln -s python-indexer-master/ppdi_vX.X.X/ppdi.py pdi```

First index
-----------
The PDI before the first index, will open your webbrowser and you will need to give perssion to PDI to index your dropbox.
If this permission will be denied the PDI <b>won't</b> index your dropbox.

After the first success index, the PDI will not ask permission again, so you can use with <i>crontab</i>. (Don't forget to use -q for quiet mode, or use > /dev/null)

Arguments
---------
usage: ppdi.py [-h] [-l LANG] [-a] [-d DISABLER] [-s STYLEDIR] [-o] [-q]

optional arguments:

  <b>```-h, --help```</b> 
> shows a help message

  <b>```-l LANG, --lang LANG```</b>
> Selected language in LanguageCode_Country format. <b>eg: en_US</b>

  <b>```-a, --all```</b>
> Indexing of folders.Each folder will appear on the generated HTML page. (Ignoring the disabler.)

  <b>```-d DISABLER, --disabler DISABLER```</b> 
> It sets the prefix of the folders which are to be excluded from indexing. For example if you do not want to share a directory witch exists in Public dir, just rename the directory in that way the first charachter must be the disabler. The dafult disabler is "<b>.</b>" . <b>eg: <i>.mydir</i></b> will not will be excluded from indexing.
  
  <b>```-s STYLEDIR, --styledir STYLEDIR```</b> 
> The style directory in the Dropbox which contains the CSS stylesheet.Also you can put here images,js,css files. The style directory is automatic excluded from indexing
  
  <b>```-o, --openbrowser```</b>
> It automatically opens the index.html from the root directory
  
  <b>```-q, --quiet ```</b>
> No output


FAQ:
---
Run python pdi -h for more help


  [1]: http://dropbox.com
