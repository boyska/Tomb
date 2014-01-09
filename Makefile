PROG = tomb
PREFIX ?= /usr/local
MANDIR ?= /usr/share/man

all:
	@echo "Tomb is a script and does not need compilation, it can be simply executed."
	@echo "To install it in /usr/local together with its manpage use 'make install'."

install:
	@install -Dm755 ${PROG} ${DESTDIR}${PREFIX}/bin/${PROG}
	@install -Dm666 doc/${PROG}.1 ${DESTDIR}${MANDIR}/man1/${PROG}.1

test:
	make -C extras/test

deb:
	ln -fs doc/tomb.1 tomb.1
	equivs-build  extras/equivs-tomb

clean:
	rm -f tomb.1
	rm -f tomb_*.deb
