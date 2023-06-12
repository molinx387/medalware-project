family_dict = [
    {
        "Familia": "Troyano",
        "Definicion": "Un troyano es un tipo de malware que se disfraza de un programa legítimo o atractivo para engañar a los usuarios y obtener acceso no autorizado a su sistema. A diferencia de otros tipos de malware, los troyanos no se replican por sí mismos, sino que requieren que el usuario los ejecute o instale. Los troyanos pueden tener una amplia gama de funcionalidades maliciosas, como robo de información, control remoto del sistema, captura de contraseñas, envío de spam y destrucción de datos, entre otras.",
    },
    {
        "Familia": "Botnet",
        "Definicion": "Un botnet es una red de dispositivos infectados con software malicioso (conocido como bot) que permite a un atacante controlarlos de forma remota. Estos dispositivos comprometidos pueden incluir computadoras, servidores, dispositivos móviles, enrutadores, entre otros. Los bots dentro del botnet son controlados por un servidor centralizado o distribuido, conocido como C&C (Command and Control). El objetivo principal de un botnet es realizar acciones maliciosas, como el envío de spam, ataques DDoS (Denial of Service), robo de información, distribución de malware adicional, entre otros.",
    },
    {
        "Familia": "Keylogger",
        "Definicion": "Un keylogger es un tipo de malware diseñado para registrar y grabar todas las pulsaciones de teclado realizadas en un sistema comprometido, sin el conocimiento ni el consentimiento del usuario afectado. Estos registros pueden incluir contraseñas, información personal, mensajes de correo electrónico y cualquier otra información confidencial introducida a través del teclado. Los keyloggers pueden operar a nivel de software, aprovechando vulnerabilidades en el sistema operativo o aplicaciones, o a nivel de hardware, utilizando dispositivos físicos conectados al teclado o al puerto USB.",
    },
    {
        "Familia": "Loader",
        "Definicion": "Un Loader es un tipo de malware diseñado para cargar y ejecutar otros programas maliciosos en un sistema comprometido. También se conoce como 'dropper' o 'downloader'. El propósito principal de un Loader es proporcionar una puerta de entrada para otros malware en el sistema objetivo, permitiendo su descarga, instalación y ejecución posterior. Los Loaders suelen utilizarse como la primera etapa de un ataque más amplio, ya que su función principal es entregar y activar otro malware, como troyanos, ransomware o spyware.",
    },
    {
        "Familia": "Cryptojacking",
        "Definicion": "El Cryptojacking es una forma de ciberataque en la que los hackers utilizan el poder de procesamiento de una computadora o dispositivo sin el conocimiento o consentimiento del propietario para minar criptomonedas. En lugar de robar datos o dañar el sistema, el objetivo principal del Cryptojacking es utilizar los recursos computacionales para generar criptomonedas de forma ilícita.",
    },
    {
        "Familia": "Adware",
        "Definicion": "Adware, abreviatura de software publicitario, es un tipo de malware diseñado para mostrar anuncios no deseados en dispositivos infectados. A diferencia de otros tipos de malware que buscan dañar o robar información, el adware se enfoca en generar ingresos a través de publicidad intrusiva. Por lo general, se instala sin el consentimiento del usuario junto con otro software gratuito descargado de fuentes no confiables o a través de enlaces maliciosos en Internet.",
    },
    {
        "Familia": "Ransomware",
        "Definicion": "El ransomware es un tipo de malware que cifra los archivos en un sistema infectado y luego exige un rescate, generalmente en forma de criptomoneda, a cambio de restaurar el acceso a los archivos. Es una forma de extorsión digital que busca obtener beneficios económicos de las víctimas. Una vez que el ransomware se infiltra en un sistema, se propaga rápidamente y encripta los archivos, volviéndolos inaccesibles para el propietario legítimo. A menudo, los ciberdelincuentes amenazan con eliminar o publicar los archivos si no se paga el rescate en un tiempo determinado. Los métodos de distribución comunes para el ransomware incluyen correos electrónicos de phishing, descargas de archivos infectados y aprovechamiento de vulnerabilidades en el software.",
    },
    {
        "Familia": "Stealer",
        "Definicion": "Stealer es una familia de malware diseñada para robar información confidencial de los sistemas infectados, como contraseñas, datos de tarjetas de crédito, cookies de navegadores, historial de navegación y otros datos sensibles. Los Stealers suelen operar de manera sigilosa, recopilando la información robada y enviándola a los ciberdelincuentes sin levantar sospechas. Este tipo de malware puede propagarse a través de descargas maliciosas, correos electrónicos de phishing, sitios web comprometidos y otras técnicas de ingeniería social. Los Stealers pueden representar una amenaza significativa para la privacidad y la seguridad de los usuarios y las organizaciones, ya que pueden comprometer datos sensibles y facilitar el robo de identidad y el fraude.",
    },
    {
        "Familia": "Clipper",
        "Definicion": "Los malwares de la familia Clipper especializados en el robo de criptomonedas. Estos programas maliciosos se centran en interceptar y modificar las direcciones de las carteras de criptomonedas en el portapapeles de los usuarios. Cuando los usuarios intentan realizar una transacción copiando y pegando una dirección de cartera, el malware reemplaza la dirección original por la del atacante. Como resultado, las criptomonedas enviadas por el usuario terminan en la cartera del ciberdelincuente en lugar de la dirección de destino prevista.",
    },
    {
        "Familia": "Virus",
        "Definicion": "Un virus es un tipo de malware diseñado para infectar y dañar archivos o programas en un sistema informático. Los virus se replican al adjuntarse a otros archivos ejecutables o programas, y pueden propagarse de una computadora a otra a través de medios como unidades de almacenamiento extraíbles, redes o descargas de Internet. Los virus pueden realizar una variedad de acciones maliciosas, como corromper archivos, robar información, destruir datos o permitir el acceso no autorizado al sistema infectado. Los virus suelen requerir la intervención activa del usuario o la ejecución de un archivo infectado para propagarse.",
    },
    {
        "Familia": "Gusano",
        "Definicion": "Un gusano informático es un tipo de malware que se propaga de forma autónoma a través de redes informáticas, explotando vulnerabilidades en sistemas y dispositivos. A diferencia de los virus, los gusanos no requieren de un programa huésped para replicarse, sino que pueden propagarse por sí mismos. Los gusanos suelen aprovechar fallos de seguridad en software o utilizar técnicas de ingeniería social para engañar a los usuarios y propagarse de manera efectiva.",
    },
    {
        "Familia": "POS",
        "Definicion": "El malware de punto de venta, también conocido como POS malware, es un tipo de software malicioso diseñado para robar información financiera, como números de tarjetas de crédito y débito, en sistemas de punto de venta utilizados en tiendas minoristas y negocios. El malware de POS se instala en el software o hardware de los terminales de punto de venta y tiene como objetivo capturar los datos de las tarjetas durante una transacción, enviándolos a los atacantes. Una vez que los datos son recopilados, los ciberdelincuentes pueden venderlos en el mercado negro o utilizarlos para cometer fraudes financieros. El malware de punto de venta ha sido responsable de varios ataques exitosos a grandes minoristas en todo el mundo.",
    },
]
