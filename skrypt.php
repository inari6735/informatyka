<?php
    $data1 = 'Adam Miałczyński';
    $data2 = 'Adam Miałczyńsky';
    echo hash('md5', $data1);
    echo("\r\n");
    echo hash('md5', $data2);
    echo("\r\n");
    echo hash('sha256', $data2);
    echo("\r\n");
    echo hash('haval256,5', $data2);
?>

