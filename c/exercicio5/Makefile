.PHONY: build

BUILDDIR = ../build/exercicio5

build: $(BUILDDIR)/exercicio5

$(BUILDDIR)/exercicio5 : exercicio5.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<