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
	gendiff tests/fixtures/input/plain/json/file1.json tests/fixtures/input/plain/json/file2.json
	
check: test lint

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml


