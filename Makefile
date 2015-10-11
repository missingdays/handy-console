
MAINDIR=~/.handy-console
IGNORES=$(MAINDIR)/ignores
BIN=$(MAINDIR)/bin

install: clean init ignores cp
	echo "Installed"

clean: 
	rm -rf $(MAINDIR)

cp:
	rm -f $(BIN)/*
	cp ./src/**/*.py $(BIN)
	for f in $(BIN)/*; do	 ln -s -f $$f ~/bin/"$$(basename "$$f" .py)"; done

init:
	mkdir $(MAINDIR)
	mkdir $(BIN)

ignores:
	git clone https://github.com/github/gitignore.git $(IGNORES)
	mv ~/.handy-console/ignores/Global/* $(IGNORES)
	rm -rf $(IGNORES)/Global

