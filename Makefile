lint:
	uv run ruff check gendiff

build:
	uv build

package-install:
	uv tool install --reinstall dist/*.whl

gendiff:
	uv run gendiff data/file1.json data/file2.json

install:
	uv sync	
	
run-plain-json:
	gendiff tests/test_data/input/plain/json/file1.json tests/test_data/input/plain/json/file2.json

run-plain-yaml:
	gendiff tests/test_data/input/plain/yaml/file1.yaml tests/test_data/input/plain/yaml/file2.yaml

run-tree-json:
	gendiff tests/test_data/input/tree/json/file1.json tests/test_data/input/tree/json/file2.json

check: test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

.PHONY: test

