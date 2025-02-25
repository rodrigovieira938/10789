.PHONY: build

BUILDDIR = ../build/exercicio8

build: $(BUILDDIR)/exercicio8

$(BUILDDIR)/exercicio8 : exercicio8.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<