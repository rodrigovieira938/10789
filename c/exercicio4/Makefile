.PHONY: build

BUILDDIR = ../build/exercicio4

build: $(BUILDDIR)/exercicio4

$(BUILDDIR)/exercicio4 : exercicio4.c
	@mkdir -p $(@D)
	@$(CC) $(CFLAGS) -o $@ $<