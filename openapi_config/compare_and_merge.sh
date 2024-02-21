#! /bin/bash
set -e

cd "$(dirname "$0")"

TMP='./tmp_public-openapi.yml'
CURR='./current_public-openapi.yml'
PREV='./previous_public-openapi.yml'
MERGED='./merged_pyrolific-openapi.yml'

wget https://docs.prolific.com/docs/api-docs/public-openapi -O $TMP
if cmp -s $TMP $CURR; then
    echo "$TMP matches $CURR, removing tmp and exiting"
    rm $TMP
    exit
else
    mv $CURR $PREV
    mv $TMP $CURR
fi

echo "git merge-file $MERGED $PREV $CURR"
git merge-file $MERGED $PREV $CURR
echo "git add $MERGED $PREV $CUR"
git add $MERGED $PREV $CURR

git commit -m "Downloaded new openapi spec, rotated current to previous spec files and merged pyrolific specific changes"
