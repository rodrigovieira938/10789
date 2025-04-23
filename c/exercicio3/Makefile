.PHONY: build

BUILDDIR = ../build/exercicio3

build: $(BUILDDIR)/exercicio3

$(BUILDDIR)/exercicio3 : exercicio3.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<