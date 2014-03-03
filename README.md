[Public] Python Dropbox Indexer
===============================

First steps:

1. Register a dropbox account
2. Create a folder with name : Public
3. Uploade the style folder to the Public folder.
	/style/style.css

Installation:

1. Create a ./bin directory in your home
	cd ~
	mkdir .bin
	cd ./bin
2. Download the PDI
	wget https://github.com/bor-attila/python-indexer/archive/master.zip
3. Unzip
	unzip master.zip
4. Create a (soft) link in ./bin
	ln -s python-indexer-master/ppdi_vX.X.X/ppdi.py pdi

FAQ:

Run python pdi -h for more help
