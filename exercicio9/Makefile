.PHONY: build

BUILDDIR = ../build/exercicio9

build: $(BUILDDIR)/exercicio9

$(BUILDDIR)/exercicio9 : exercicio9.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<