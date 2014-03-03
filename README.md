[Public] Python Dropbox Indexer
===============================

First steps:
------------

1. Register a [dropbox][1] account
2. Create a folder with the following name : <br> <b>Public</b>
3. Upload the style folder to the Public folder. <br> <b>/style/style.css</b>

Installation:
------------

* Create a ./bin directory in your home directory
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
The PDI comes before the first index, it will open your webbrowser, and you will need to give permission to the PDI to index your dropbox.
If this permission will be denied the PDI <b>won't</b> index your dropbox.

After the first successful indexing, the PDI will not ask permission again, so you can use it with <i>crontab</i>. (Don't forget to use -q for quiet mode, or use > /dev/null)

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
> It sets the prefix of the folder which is to be excluded from indexing. For example, if you do not want to share a directory from the Public dir, just rename the directory in a way that the first character should be the disabler. The dafult disabler is "<b>.</b>" . <b>eg: <i>.mydir</i></b> will be excluded from indexing. 
  
  <b>```-s STYLEDIR, --styledir STYLEDIR```</b> 
> The style directory in the Dropbox which contains the CSS stylesheet. You can put here images,js,css files as well. The style directory is automatically excluded from indexing.
  
  <b>```-o, --openbrowser```</b>
> It automatically opens the index.html from the root directory
  
  <b>```-q, --quiet ```</b>
> No output


FAQ:
---
Run python pdi -h for more help


  [1]: http://dropbox.com
