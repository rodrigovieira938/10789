.PHONY: build

BUILDDIR = ../build/tools

build: $(BUILDDIR)/pretty_print

$(BUILDDIR)/pretty_print: pretty_print.c
	@mkdir -p $(@D)
	@gcc -o $@ $<