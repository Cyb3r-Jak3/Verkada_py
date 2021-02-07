.PHONY: clean clean-build clean-pyc test docs

clean: clean-build clean-pyc

full-test: lint test

ifeq ($(OS),Windows_NT)
    RM = del //Q //F
    RRM = rmdir //Q //S
else
    RM = rm -f
    RRM = rm -f -r
endif

clean-build:
	$(RM) -r build/
	$(RM) -r dist/
	$(RM) -r *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec $(RM) {} +
	find . -name '*.pyo' -exec $(RM) {} +
	find . -name '*~' -exec $(RM) {} +

docs:
	sphinx-apidoc -f -o docs/ verkada_py
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

lint:
	black --check verkada_py
	pylint --disable=W0511  verkada_py
	flake8 --statistics --show-source --count verkada_py
	bandit -r verkada_py

test:
	py.test --cov verkada_py tests/ -vv