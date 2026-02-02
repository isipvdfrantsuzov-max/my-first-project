install:
	uv sync

VD-games:
	uv tool run --from my-first-project vd-games

build:
	uv build

package-install:
	uv tool install dist/*.whl
