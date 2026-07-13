#!/bin/sh

printf "Content-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\n\r\n"

QUERY_STRING="${QUERY_STRING:-}"
Q=$(printf '%s' "$QUERY_STRING" | sed -n 's/.*q=\([^&]*\).*/\1/p' | sed 's/+/ /g;s/%\([0-9A-Fa-f][0-9A-Fa-f]\)/\\x\1/g' | xargs -0 printf '%b' 2>/dev/null)

if [ -z "$Q" ]; then
  printf '[]'
  exit 0
fi

printf '['
FIRST=1
find /srv/data -iname "*${Q}*" -maxdepth 10 2>/dev/null | head -500 | while IFS= read -r FULLPATH; do
  REL="${FULLPATH#/srv/data}"
  [ -z "$REL" ] && continue

  if [ -d "$FULLPATH" ]; then
    TYPE="directory"
    SIZE=0
  else
    TYPE="file"
    SIZE=$(stat -c '%s' "$FULLPATH" 2>/dev/null || echo 0)
  fi
  MTIME=$(stat -c '%Y' "$FULLPATH" 2>/dev/null || echo 0)
  MTIME_ISO=$(date -u -d "@$MTIME" '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "1970-01-01T00:00:00Z")

  NAME=$(basename "$FULLPATH")
  DIR=$(dirname "$REL")

  if [ "$FIRST" = "1" ]; then
    FIRST=0
  else
    printf ','
  fi
  printf '{"name":"%s","path":"%s","dir":"%s","type":"%s","size":%s,"mtime":"%s"}' \
    "$NAME" "$REL" "$DIR" "$TYPE" "$SIZE" "$MTIME_ISO"
done
printf ']'
