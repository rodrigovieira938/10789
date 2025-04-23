.PHONY: build

BUILDDIR = ../build/exercicio6

build: $(BUILDDIR)/exercicio6

$(BUILDDIR)/exercicio6 : exercicio6.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<