set /a n = %1
:loop
set /a "b = n & 1, n >>= 1" 
<nul set /p "=%b%"
if %n% gtr 0 goto :loop
