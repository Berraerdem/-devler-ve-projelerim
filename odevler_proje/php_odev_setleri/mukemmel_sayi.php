<form method="post">  
SAYİ GİRİNİZ: <input type="text" name="input"><br><br>  
<input type="submit" name="submit" value="submit">  
</form> 

<?php 

$input=$_POST['input'];

function isPerfectNumber($input) 
{ 
    $sum = 0; 
       
    
    for ($i = 1; $i < $input; $i++) 
    { 
        if ($input % $i == 0) 
        { 
            $sum = $sum + $i; 
        }       
    } 
    return $sum == $input; 
} 
   
function function_alert($message) { 
      
  
    echo "<script>alert('$message');</script>"; 
} 

  
if (isPerfectNumber($input)) 
    function_alert('Sayi '.$input . ' Mukemmel Sayidir.'); 
else
    function_alert('Sayi '.$input . ' Mukemmel Sayi Degildir.');
?> 

