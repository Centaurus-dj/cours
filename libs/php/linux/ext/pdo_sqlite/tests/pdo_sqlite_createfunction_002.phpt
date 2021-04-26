--TEST--
PDO_sqlite: Testing sqliteCreateFunction() produces warning when
un-callable function passed
--CREDITS--
Chris MacPherson chris@kombine.co.uk
--SKIPIF--
<?php if (!extension_loaded('pdo_sqlite')) print 'skip not loaded'; ?>
--FILE--
<?php

$db = new PDO( 'sqlite::memory:');

try {
    $db->sqliteCreateFunction('bar-alias', 'bar');
} catch (\TypeError $e) {
    echo $e->getMessage() . \PHP_EOL;
}

?>
--EXPECT--
PDO::sqliteCreateFunction(): Argument #2 ($callback) must be a valid callback, function "bar" not found or invalid function name
