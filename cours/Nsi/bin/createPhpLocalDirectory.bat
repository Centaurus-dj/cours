echo off

:: create the base dir needed
mkdir "Travail-PHP-Alexis-Opolka-1G02"

:: travel to the base folder
cd "Travail-PHP-Alexis-Opolka-1G02"

:: create main subdirs
mkdir css
mkdir pages
mkdir js

:: create sub-subdirs
cd pages
mkdir qcm
mkdir test
cd ../

:: create files at base directory
curl https://gitlab.com/CentaurusDJ/import-cours/-/raw/main/cours/Nsi/Php/index.html > index.html

:: create a uninstall execution file to destroy the dir when not needed | optional
echo echo off> Delete-Directory.bat
echo echo Deleting directory...>> Delete-Directory.bat
echo del index.html>> Delete-Directory.bat
echo cd css>> Delete-Directory.bat
echo del master.css>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo cd js>> Delete-Directory.bat
echo del main.js>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo cd pages>> Delete-Directory.bat
echo del index.php>> Delete-Directory.bat
echo cd qcm>> Delete-Directory.bat
echo del index.php>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo cd test>> Delete-Directory.bat
echo del php-example-2.php>> Delete-Directory.bat
echo del php-example-3.php>> Delete-Directory.bat
echo del php-example-4-HTML.html>> Delete-Directory.bat
echo del php-example-4-PHP.php>> Delete-Directory.bat
echo del php-exercise-2.php>> Delete-Directory.bat
echo del php-exercise-3.php>> Delete-Directory.bat
echo del php-exercise-4.php>> Delete-Directory.bat
echo del php-exercise-4-part2.php>> Delete-Directory.bat
echo del php-exercise-5-sender.php>> Delete-Directory.bat
echo del php-exercise-5-receiver.php>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo rmdir test>> Delete-Directory.bat
echo rmdir qcm>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo rmdir css>> Delete-Directory.bat
echo rmdir js>> Delete-Directory.bat
echo rmdir pages>> Delete-Directory.bat
echo del Delete-Directory.bat>> Delete-Directory.bat
echo cd ../>> Delete-Directory.bat
echo rmdir "Travail-PHP-Alexis-Opolka-1G02">> Delete-Directory.bat
echo echo Directory deleted!>> Delete-Directory.bat
echo pause>> Delete-Directory.bat


:: travel to css directory and import page style
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Javascript/css/master.css > css/master.css
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/index.php > pages/index.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/qcm/index.php > pages/qcm/index.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-example-2.php > pages/test/php-example-2.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-example-3.php > pages/test/php-example-3.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-example-4-HTML.hmtl > pages/test/php-example-4-HTML.html
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-example-4-PHP.php > pages/test/php-example-4-PHP.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-2.php > pages/test/php-exercise-2.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-3.php > pages/test/php-exercise-3.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-4.php > pages/test/php-exercise-4.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-4-part2.php > pages/test/php-exercise-4-part2.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-5-sender.php > pages/test/php-exercise-5-sender.php
curl https://gitlab.com/CentaurusDj/import-cours/-/raw/main/cours/Nsi/Php/pages/test/php-exercise-5-receiver.php > pages/test/php-exercise-5-receiver.php
pause