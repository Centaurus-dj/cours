#-*- UTF-8 -*-

import os

print(os.system('"libs/php/Win_php/php.exe" "cours/Nsi/Php/pages/index.php"'))
open("test-log.txt", "w").write(str(os.system('"libs/php/Win_php/php.exe" "cours/Nsi/Php/pages/index.php"')))
