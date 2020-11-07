TEX := resume.tex
EXE := create_resume.py

build: $(EXE)
	python3 $(EXE)
	latexmk $(TEX)

.PHONY: clean
clean:
	latexmk -C
	rm -f $(TEX)
