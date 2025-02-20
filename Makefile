EXERCICIOS = exercicio1 exercicio2
.PHONY: clean run build tools $(EXERCICIOS)

CC = gcc
CFLAGS = -Wall -Wextra

build: tools $(EXERCICIOS)

tools:
	@cd tools && make build

exercicio1:
	@cd $@ && make build
exercicio2:
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
