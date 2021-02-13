<form method="post">  
SAYİ GİRİNİZ: <input type="text" name="input"><br><br>  
<input type="submit" name="submit" value="submit">  
</form> 

<?php
$input=$_POST['input'];
 
$asal=0; $i=2;
 
do
{
	if ($input % $i == 0)
	{
		$asal = 1;
	}
	$i++;
}
while($i<$input);
 
if ($asal != 1)
{
	echo 'Sayi '.$input . ' Asaldir.';
}
else
{
	echo 'Sayi '.$input . ' Asal Degildir.';
}
 
?>


