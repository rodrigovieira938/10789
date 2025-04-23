.PHONY: build

BUILDDIR = ../build/exercicio2

build: $(BUILDDIR)/exercicio2

$(BUILDDIR)/exercicio2 : exercicio2.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<