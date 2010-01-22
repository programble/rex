# Rex installation Makefile

all: 
	@echo "Run 'make install' to install Rex"

install:
	mkdir -p /usr/share/rex
	cp -v * /usr/share/rex/
	cp rex /usr/bin/

remove: uninstall

uninstall:
	rm -vf /usr/bin/rex
	rm -vrf /usr/share/rex
