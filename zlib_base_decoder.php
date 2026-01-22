#!/usr/bin/php

<?php
// 1. argument check
if ($argc < 2) {
    echo "Usage: php " . $argv[0] . " <base64_encoded_string>\n";
    exit(1);
}

// 2. get string from argument
$input = $argv[1];

// 3. decode
// base64_decode: decode binary from Base64
// zlib_decode: extract DEFLATE/ZLIB archive
$decoded = zlib_decode(base64_decode($input));

// 4. output result
if ($decoded !== false) {
    echo $decoded . "\n";
} else {
    echo "Error: Could not decode the string. Check if the input is valid.\n";
    exit(1);
}
