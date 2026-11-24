#!/bin/bash
# Recria o ambiente de producao. Rode uma vez no inicio da sessao: bash _rotina/setup.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /root/.fonts /home/claude/ig_week/src /home/claude/ig_week/car /home/claude/ig_week/stories /home/claude/lp/site/assets
cp "$HERE"/fonts/*.ttf /root/.fonts/ && fc-cache -f >/dev/null 2>&1 || true
cp "$HERE"/assets/src/*.png /home/claude/ig_week/src/
cp "$HERE"/assets/kanban_anon.png /home/claude/ig_week/
cp "$HERE"/assets/shots/*.webp /home/claude/lp/site/assets/
cp "$HERE"/scripts/*.py /home/claude/ig_week/
python3 -c "import playwright, numpy, PIL" 2>/dev/null || pip install --break-system-packages playwright numpy pillow
echo "ok: scripts em /home/claude/ig_week"
