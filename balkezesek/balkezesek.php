<?php
class BalKezes {
    public $name;
    public $from;
    public $to;
    public $weight;
    public $height;
    public $height_cm;



    function __construct($name, $from, $to, $weight, $height) {
        $this->name = $name;
        $this->from =  DateTime::createFromFormat('!Y-m-d', $from)->getTimestamp();
        $this->to =  DateTime::createFromFormat('!Y-m-d', $to)->getTimestamp();
        $this->weight = $weight;
        $this->height = $height;
        $this->height_cm = intval($height)*2.54;
    }
}

$f = file("balkezesek.csv");
$balkezesek = Array();
for($x = 1;$x < count($f);$x++) {
$i = $f[$x];
$data = Array();
foreach(explode(";", $i) as $l) {
array_push($data, $l);
}
$blb = new BalKezes($data[0], $data[1], $data[2], $data[3], $data[4]);
array_push($balkezesek, $blb);
}

echo("3. feladat " . count($balkezesek) . " Rekord található az állományban");
foreach($balkezesek as $i) {
    if($i->to >= DateTime::createFromFormat('!Y-m-d', "1999-10-01")->getTimestamp() && $i->to <= DateTime::createFromFormat('!Y-m-d', "1999-11-01")->getTimestamp()){
        echo("  ".$i->name."    ".str_replace(".", ",", $i->height_cm) . " cm\n");
    }
}
?>
