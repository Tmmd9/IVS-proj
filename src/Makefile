# IVS Team1 Makefile

.PHONY: pack packfolder clean test doc run apt all

all: apt run

apt:
	sudo apt install python3-pip
	pip3 install PyQt5
	export PATH="$HOME/.local/bin:$PATH"
	sudo apt-get install libxcb-xinerama0

pack: doc packfolder IVS-proj/xkovac49_xmedve04_xvacla31_xverev00.zip
IVS-proj/xkovac49_xmedve04_xvacla31_xverev00.zip:
	rm -rf ../../xkovac49_xmedve04_xvacla31_xverev00/repo/doc
	cd ../.. && zip -r $@ xkovac49_xmedve04_xvacla31_xverev00

packfolder:
	mkdir -p ../../xkovac49_xmedve04_xvacla31_xverev00/repo
	mkdir ../../xkovac49_xmedve04_xvacla31_xverev00/installer
	mkdir ../../xkovac49_xmedve04_xvacla31_xverev00/doc
	cp -a ../../IVS-proj/. ../../xkovac49_xmedve04_xvacla31_xverev00/repo/
	cp -a ../doc ../../xkovac49_xmedve04_xvacla31_xverev00/doc/
	cp -a ../kalkulacka_pkg.deb ../../xkovac49_xmedve04_xvacla31_xverev00/installer

clean:
	rm -rf ../../xkovac49_xmedve04_xvacla31_xverev00 ../doc
	rm -rf __pycache__

test: mathlib_test.py
	cd .. && python3 -m src.mathlib_test

doc: Doxyfile
	sudo apt install doxygen
	cd .. && rm -rf doc
	cd .. && mkdir doc && cd doc && doxygen ../src/$^

run: main.py
	python3 main.py

