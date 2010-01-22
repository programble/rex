# Rex installation Makefile

PREFIX=/usr
INSTALL_DIR=$(PREFIX)/share/rex
BIN_DIR=$(PREFIX)/bin

all: 
	@echo "Run 'make install' as root to install Rex"

install:
	mkdir -p $(INSTALL_DIR)
	cp -v * $(INSTALL_DIR)
    chmod +x $(INSTALL_DIR)/rex.py
	ln -s $(INSTALL_DIR)/rex.py $(BIN_DIR)/rex

remove: uninstall

uninstall:
	rm -vf $(BIN_DIR)/rex
	rm -vrf $(INSTALL_DIR)
