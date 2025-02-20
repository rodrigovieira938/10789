.PHONY: clean run build tools exercicio1

CC = gcc
CFLAGS = -Wall -Wextra
EXERCICIOS = exercicio1

build: tools exercicio1

tools:
	@cd tools && make build

exercicio1:
	@cd $@ && make build

clean:
	@rm -rf build

run: build
	@for exe in ${EXERCICIOS}; do \
		./build/tools/pretty_print $$exe; \
		build/$$exe/$$exe; \
	done
clean-run: clean
	@make run
