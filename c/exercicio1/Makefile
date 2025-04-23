.PHONY: build

BUILDDIR = ../build/exercicio1

build: $(BUILDDIR)/exercicio1

$(BUILDDIR)/exercicio1 : exercicio1.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<