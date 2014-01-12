
PREFIX ?= /usr/local

all: hexencode tomb-kdb-pbkdf2 tomb-kdb-pbkdf2-getiter tomb-kdb-pbkdf2-gensalt

tomb-kdb-pbkdf2: pbkdf2.o
	gcc ${LDFLAGS} -o tomb-kdb-pbkdf2 pbkdf2.o -lgcrypt
tomb-kdb-pbkdf2-getiter: benchmark.o
	gcc ${LDFLAGS} -o tomb-kdb-pbkdf2-getiter benchmark.o -lgcrypt
tomb-kdb-pbkdf2-gensalt: gen_salt.o
	gcc ${LDFLAGS} -o tomb-kdb-pbkdf2-gensalt gen_salt.o -lgcrypt
hexencode: hexencode.o
	gcc ${LDFLAGS} -o hexencode hexencode.c

%.o:%.c
	    $(CC) ${CFLAGS} ${CPPFLAGS} ${LDFLAGS} -c -o $@ $<


clean:
	rm -f tomb-kdb-pbkdf2 tomb-kdb-pbkdf2-getiter tomb-kdb-pbkdf2-gensalt hexencode *.deb *.o

install:
	install -Dm755 tomb-kdb-pbkdf2 ${DESTDIR}${PREFIX}/bin/tomb-kdb-pbkdf2
	install -Dm755 tomb-kdb-pbkdf2-getiter ${DESTDIR}${PREFIX}/bin/tomb-kdb-pbkdf2-getiter
	install -Dm755 tomb-kdb-pbkdf2-gensalt ${DESTDIR}${PREFIX}/bin/tomb-kdb-pbkdf2-gensalt
	install -Dm755 hexencode ${DESTDIR}${PREFIX}/bin/hexencode
	@echo "Tomb-kdb auxiliary binaries installed in ${PREFIX}"
