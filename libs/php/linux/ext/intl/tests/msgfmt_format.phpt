--TEST--
msgfmt_format()
--SKIPIF--
<?php if( !extension_loaded( 'intl' ) ) print 'skip'; ?>
--FILE--
<?php

/*
 * Format a number using misc locales/patterns.
 */


function ut_main()
{
    $locales = array(
        'en_US' => "{0,number,integer} monkeys on {1,number,integer} trees make {2,number} monkeys per tree",
        'ru_UA' => "{0,number,integer} мавп на {1,number,integer} деревах це {2,number} мавпи на кожному деревi",
        'de' => "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum",
        'en_UK' => "{0,number,integer} monkeys on {1,number,integer} trees make {2,number} monkeys per tree",
    'root' => '{0,whatever} would not work!',
    'fr' => "C'est la vie!",
    );

    $str_res = '';
    $m = 4560;
    $t = 123;

    foreach( $locales as $locale => $pattern )
    {
        $str_res .= "\nLocale is: $locale\n";
        $fmt = ut_msgfmt_create( $locale, $pattern );
        if(!$fmt) {
            $str_res .= dump(intl_get_error_message())."\n";
            continue;
        }
        $str_res .= dump( ut_msgfmt_format( $fmt, array($m, $t, $m/$t) ) ) . "\n";
        $str_res .= dump( ut_msgfmt_format_message($locale, $pattern, array($m, $t, $m/$t))) . "\n";
    }
    return $str_res;
}

include_once( 'ut_common.inc' );

// Run the test
ut_run();

?>
--EXPECT--
Locale is: en_US
'4,560 monkeys on 123 trees make 37.073 monkeys per tree'
'4,560 monkeys on 123 trees make 37.073 monkeys per tree'

Locale is: ru_UA
'4 560 мавп на 123 деревах це 37,073 мавпи на кожному деревi'
'4 560 мавп на 123 деревах це 37,073 мавпи на кожному деревi'

Locale is: de
'4.560 Affen über 123 Bäume um 37,073 Affen pro Baum'
'4.560 Affen über 123 Bäume um 37,073 Affen pro Baum'

Locale is: en_UK
'4,560 monkeys on 123 trees make 37.073 monkeys per tree'
'4,560 monkeys on 123 trees make 37.073 monkeys per tree'

Locale is: root
'msgfmt_create: message formatter creation failed: U_ILLEGAL_ARGUMENT_ERROR'

Locale is: fr
'C\'est la vie!'
'C\'est la vie!'
