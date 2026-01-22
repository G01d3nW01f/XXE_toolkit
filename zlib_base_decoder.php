#!/usr/bin/php

<?php
// 1. 引数のチェック（スクリプト名 + エンコード文字列が必要なので 2 未満をチェック）
if ($argc < 2) {
    echo "Usage: php " . $argv[0] . " <base64_encoded_string>\n";
    exit(1);
}

// 2. 引数から文字列を取得
$input = $argv[1];

// 3. デコード処理
// base64_decode: Base64形式をバイナリに戻す
// zlib_decode: DEFLATE/ZLIB 圧縮を解凍する
$decoded = zlib_decode(base64_decode($input));

// 4. 結果の出力
if ($decoded !== false) {
    echo $decoded . "\n";
} else {
    echo "Error: Could not decode the string. Check if the input is valid.\n";
    exit(1);
}
