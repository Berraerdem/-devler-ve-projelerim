<?php 
  
setlocale(LC_TIME, 'tr_TR');
 
echo strftime('%H:%M').'<br>';


if(strftime('%H:%M') >= strtotime('06:00') && strftime('%H:%M') < strtotime('10:00'))
  echo"gunaydin";

if (strftime('%H:%M') >= strtotime('10:00') && strftime('%H:%M') < strtotime('17:00'))
  echo"iyi gunler";

if (strftime('%H:%M') >= strtotime('17:00') && strftime('%H:%M') < strtotime('20:00'))
  echo"iyi akşamlar"; 

if (strftime('%H:%M') >= strtotime('20:00') && strftime('%H:%M') < strtotime('00:00'))
  echo"iyi geceler"; 

if (strftime('%H:%M') > strtotime('00:00') && strftime('%H:%M') < strtotime('06:00'))
  echo"esenlikler dilerim";    
 
?>