.PHONY: build

BUILDDIR = ../build/exercicio10

build: $(BUILDDIR)/exercicio10

$(BUILDDIR)/exercicio10 : exercicio10.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<