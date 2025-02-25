.PHONY: build

BUILDDIR = ../build/exercicio7

build: $(BUILDDIR)/exercicio7

$(BUILDDIR)/exercicio7 : exercicio7.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<