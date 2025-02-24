EXERCICIOS = exercicio1 exercicio2 exercicio3 exercicio4 exercicio5 exercicio6 exercicio7 exercicio8 exercicio9 exercicio10
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
exercicio3:
	@cd $@ && make build
exercicio4:
	@cd $@ && make build
exercicio5:
	@cd $@ && make build
exercicio6:
	@cd $@ && make build
exercicio7:
	@cd $@ && make build
exercicio8:
	@cd $@ && make build
exercicio9:
	@cd $@ && make build
exercicio10:
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
