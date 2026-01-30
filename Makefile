install:
	uv sync

VD-games:
	uv run python -m VD_games.scripts.VD_main

build:
	uv build

package-install:
	uv tool install dist/*.whl

