<?php
header("Content-Type: text/html");

$a = $_GET['a'] ?? 1;
$b = $_GET['b'] ?? 1;
$c = $_GET['c'] ?? 1;

$command = escapeshellcmd("python3 /var/www/html/calculate.py a=$a b=$b c=$c");
$output = shell_exec($command);

echo $output;
?>