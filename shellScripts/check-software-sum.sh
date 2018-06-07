#!/bin/bash

INSTALLER_SHA256SUM='software hash value'
INSTALLER=$(mktemp)
curl -o "$INSTALLER" "software download link"
if echo "${INSTALLER_SHA256SUM} ${INSTALLER}" | /usr/bin/sha256sum --check; then
    chmod +x "$INSTALLER"
    "$INSTALLER"
    echo "Successfully installed software"
    rm "$INSTALLER"
else
    echo "Installer $INSTALLER sha256 checksum incorrect"
    exit 1
fi
