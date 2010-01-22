# Rex installation Makefile

PREFIX=/usr
INSTALL_DIR=$(PREFIX)/share/rex
BIN_DIR=$(PREFIX)/bin

all: 
	@echo "Run 'make install' as root to install Rex"

install: info
	mkdir -p $(INSTALL_DIR)
	cp -fv * $(INSTALL_DIR)
	chmod +x $(INSTALL_DIR)/rex.py
	ln -fs $(INSTALL_DIR)/rex.py $(BIN_DIR)/rex

info:
	@echo "Installing data to:"
	@echo "    $(INSTALL_DIR)"
	@echo "Installing binary to:"
	@echo "    $(BIN_DIR)"
	@echo

remove: uninstall

uninstall:
	rm -vf $(BIN_DIR)/rex
	rm -vrf $(INSTALL_DIR)
