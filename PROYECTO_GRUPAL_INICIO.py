from datetime import date, datetime
import re
import requests
import holidays
import random

''': Un ciudadano necesita mantenerse informado si está apto para sufragar y 
también saber si es miembro de mesa. Multas puestas por el CNE por incumplir la asistencia a 
la mesa electoral.
'''


'''REGLAMENTO A LA LEY DE ELECCIONES.

Resolución Tribunal Supremo Electoral No. 1. RO/ Sup 39 de 20 de Marzo del 2000.

EL REGLAMENTO GENERAL A LA LEY DE ELECCIONES

Título Primero

DE LA ORGANIZACION ELECTORAL

Capítulo I

DEL DERECHO AL SUFRAGIO
Art. 1.- El sufragio es derecho y deber de los ecuatorianos en goce de los derechos políticos. Por medio de él se hace efectiva su participación en la vida del Estado.

El voto es universal, igual y directo. Su ejercicio es personal, obligatorio y secreto. Para los ecuatorianos mayores de sesenta y cinco años y para los analfabetos el voto es facultativo.

Es elector todo ecuatoriano, mayor de dieciocho años, que se halle en goce de los derechos políticos, calidad que se acredita con la cédula de ciudadanía.

Art. 2.- Solo en los casos señalados por la Constitución y la Ley de Elecciones, el goce de los derechos políticos se suspenderá.

En consecuencia, aún aquellos ecuatorianos cuyas cédulas de identidad y ciudadanía hubieren caducado, tendrán el derecho y la obligación de sufragar.

No pueden votar quienes no consten en los padrones electorales, los miembros de la Fuerza Pública en servicio activo, y los que no tengan cédula de ciudadanía.

Art. 3.- La participación equitativa de hombres y mujeres como candidatos en los procesos de elección popular así como el ejercicio del derecho al voto queda garantizado en condiciones de igualdad según la Constitución y la Ley.

Art. 4.- Exclusivamente, en las elecciones de Presidente y Vicepresidente de la República, los ecuatorianos domiciliados en el exterior podrán ejercer su derecho al voto, de acuerdo a lo estipulado en la Ley.

Art. 5.- La Ley y este Reglamento garantiza la legitimación activa y pasiva de los derechos políticos, por tanto, la calidad de elector habilita para:

a) Elegir a los dignatarios de elección popular; y,

b) Ser elegido para desempeñar funciones de elección popular con los requisitos y prohibiciones establecidas en la Constitución y en la Ley;

c) Desempeñar empleos y funciones públicas; y,

d) Para ejercer el derecho al voto en las Consultas Populares y en los procesos de Revocatoria del Mandato.

Capítulo II

DE LOS ORGANISMOS ELECTORALES
Art. 6.- Son causas de excusa para el ejercicio de las funciones de miembros de los organismos electorales determinados en el Art. 9 de la Ley, las siguientes:

a) Imposibilidad física debidamente comprobada y certificada por un médico que ejerza funciones públicas;

b) Haber ejercido funciones en los organismos electorales durante dos períodos consecutivos anteriores, lo cual se probará con las designaciones correspondientes o mediante certificación del Secretario del correspondiente Tribunal Electoral;

c) Ser mayor de sesenta y cinco años de edad:

d) Ostentar una dignidad directiva en una organización política, lo cual se probará con el registro de inscripción de directivas de las organizaciones políticas que reposan en los Tribunales Electorales;

e) Participar como candidato para una dignidad de elección popular; y,

f) La calamidad doméstica debidamente justificada y sólo constituirá excusa de carácter temporal.

Art. 7.- No podrán ser vocales de los Tribunales Supremo y Provinciales Electorales, los funcionarios de libre nombramiento y remoción de la Función Ejecutiva.

No podrán ser funcionarios y empleados de los Tribunales Supremo y Provinciales Electorales quienes formen parte de las directivas de las organizaciones políticas legalmente inscritas, lo cual se probará con el registro correspondiente; tampoco, podrán intervenir en las campañas electorales con ocasión de los procesos de elección convocados por los organismos electorales competentes, caso contrario, serán sancionados con la pena prescrita en el Art. 150 de la Ley de Elecciones.

Art. 8.- Los vocales del Tribunal Supremo Electoral durarán cuatro años en sus funciones y los vocales de los Tribunales Provinciales Electorales dos años, pudiendo ser reelegidos.

Para elegir Presidente y Vicepresidente de los Tribunales Supremo y Provinciales Electorales, el primer vocal elegido por el H. Congreso Nacional y por el Tribunal Supremo Electoral, según el caso, convocará por escrito, a la sesión inaugural, que se realizará en la Sala de Sesiones del organismo electoral correspondiente, salvo que todos los vocales elegidos, acuerden por unanimidad, el lugar, día y hora de la sesión inaugural.

Art. 9.- Los vocales y los dignatarios anteriores sólo podrán ser sustituidos o reemplazados, por renuncia del titular o en caso de reorganización parcial o total, por parte del Tribunal Supremo Electoral.

En caso de falta temporal o definitiva del Presidente le subrogará el Vicepresidente. A falta del Vicepresidente, el Tribunal Electoral correspondiente designará al Vocal que ha de ejercer las funciones de Presidente, en forma ocasional, mientras dure la ausencia; o definitivamente, si es del caso.

Art. 10.- Caducarán los nombramientos de los Vocales de los Tribunales Provinciales Electorales si no se hubieren posesionado dentro del plazo determinado en el Art. 143 de la Ley, previa certificación del Secretario del Tribunal de que no se ha posesionado desde la fecha de notificación del nombramiento respectivo.

Los vocales suplentes de los Tribunales Provinciales Electorales, podrán excusarse del ejercicio de sus funciones, por las causas establecidas en la Ley, en cualquier momento, ante el Tribunal Supremo Electoral, siempre y cuando no se hubieren principalizado en forma definitiva.

Art. 11.- El Secretario General y el Prosecretario General del Tribunal Supremo Electoral, los Secretarios de los Tribunales Provinciales Electorales, los Directores, Asesores y los Coordinadores Electorales de las Vocalias del Tribunal Supremo Electoral, son de libre nombramiento y remoción del respectivo Organismo.

Art. 12.- El quórum para las sesiones de los Tribunales Supremo y Provinciales Electorales será de cuatro de sus miembros. Las decisiones de los organismos electorales se adoptarán con el voto válido de cuatro de sus miembros.

Art. 13.- El Tribunal Supremo Electoral y los Tribunales Provinciales Electorales, de entre sus miembros, constituirán al inicio de sus funciones, las comisiones permanentes Jurídica, Económica y Técnica, que estarán constituidas por tres Vocales. Igualmente, podrán constituir, comisiones especiales.

Art. 14.- Para llamar a que se integre a un Vocal Suplente, en forma ocasional, bastará la comunicación del principal dirigida al Presidente del Tribunal, caso contrario se aplicará el Art. 144 de la Ley, siempre y cuando no justifique su inasistencia a tres sesiones consecutivas.

Art. 15.- Los Secretarios de los Tribunales Provinciales Electorales ejercen además de las funciones contempladas en la Ley, las determinadas en el Reglamento Orgánico Funcional, en el Reglamento Interno y otros Reglamentos y Resoluciones, entre las que expresamente se detallan a continuación:

a) Ejercer las funciones de Jefe Administrativo en cada uno de los organismos electorales;

b) Dar fe de los actos de los Tribunales Provinciales Electorales;

c) Receptar documentación, impugnaciones y recursos de apelación y de queja presentados ante los organismos electorales;

d) Llevar el archivo de documentos, resoluciones y actas de las sesiones de los Tribunales Provinciales;

e) Notificar con las resoluciones dictadas por el Presidente y el Pleno de los organismos electorales;

f) Les está prohibido negarse a recibir: cualesquier petición, de la naturaleza que fuere; inscripciones de candidaturas; impugnaciones; quejas o recursos de apelación; y,

g) Las demás contempladas en la Ley y este Reglamento.

Art. 16.- El Tribunal Supremo Electoral y los Tribunales Provinciales Electorales, de acuerdo con las facultades que, en materia presupuestaria, le concede la Ley y con cargo a las partidas presupuestarias correspondientes, dispondrán los egresos relacionados con los actos del proceso electoral y con el funcionamiento y organización de los organismos electorales. Tales egresos se realizarán por resolución del Pleno de los Tribunales o por disposición del Presidente, según la capacidad como ordenadores de gasto aprobada por el Tribunal Supremo Electoral, de conformidad con la ley y con la intervención del funcionario del área financiera competente, quienes tendrán que rendir caución, la misma que será fijada por el organismo electoral correspondiente.

Art. 17.- Los Organismos Electorales contarán con el apoyo de la Fuerza Pública para la estricta aplicación de las disposiciones de la Ley y este Reglamento. Para ello, lo solicitarán, en el caso del Tribunal Supremo Electoral, a los Ministros de Gobierno y de Defensa Nacional; y, para el de los Tribunales Provinciales Electorales, al Gobernador de la Provincia.

Art. 18.- Para que los organismos electorales puedan gozar de la franquicia postal, desde la fecha de la convocatoria hasta treinta días después de las elecciones, el Tribunal Supremo Electoral solicitará dicha franquicia al Director Nacional de Correos, el que deberá concederla en un plazo máximo de ocho días de presentada la solicitud. La franquicia se referirá al correo nacional interno y para cualquier asunto oficial que envíen los organismos electorales.

Para elecciones en una provincia o cantón, la franquicia se referirá sólo para el Tribunal Supremo Electoral y para el Tribunal Provincial Electoral respectivo dentro de su jurisdicción.

Capítulo III

DE LOS PADRONES ELECTORALES
Art. 19.- Los ecuatorianos en goce de sus derechos políticos, que consten o no en los padrones electorales, podrán actualizar sus datos y cambiar su domicilio electoral durante todo el año, en los Tribunales Provinciales Electorales, salvo en el período eleccionario en el que podrán hacerlo en los Centros de Información Electoral hasta antes de la convocatoria a la elección correspondiente, durante el período de funcionamiento de estos Centros.

En caso de que no se actualice los datos ni se registre el cambio de domicilio electoral, el ciudadano deberá votar en el lugar que conste en el padrón electoral.

Los cambios de domicilio y actualización de datos, establecidos en la Ley de Elecciones, se realizarán, en forma escrita y personalmente, presentando la cédula de ciudadanía.

Los Tribunales Provinciales Electorales, facilitarán los medios necesarios para que los ciudadanos puedan comunicar los cambios de domicilio antes de la convocatoria a elecciones.

Los cambios de domicilio o actualización de datos que se efectuaren después de la convocatoria a elecciones se registrarán en el padrón electoral para el próximo proceso electoral.

Todas las actualizaciones y cambios de domicilio electoral se guardarán en archivos magnéticos de soporte.

Art. 20.- La difusión del padrón electoral, en donde consten el domicilio del elector se realizará a través de los Centros de Información Electoral, en el tiempo, modalidad y sistema que resuelva el Tribunal Supremo Electoral.

Los Tribunales Provinciales Electorales, informarán públicamente desde sesenta días antes de la votación, la nómina de los electores cedulados que constan en los padrones, a través de los Centros de Información Electoral, según el cronograma de funcionamiento aprobado en cada provincia, determinando previamente los sitios de instalación necesarios.

Los ciudadanos deberán informarse sobre su empadronamiento, en los Centros de Información Electoral o en los Tribunales Provinciales Electorales o en el Tribunal Supremo Electoral. También se podrá requerir esta información por medio del sistema telefónico.

Art. 21.- Los Centros de Información Electoral funcionarán durante ocho días, como mínimo. En caso de ser necesario que funcionen en un lapso mayor, los Tribunales Provinciales Electorales solicitarán la respectiva autorización del Tribunal Supremo Electoral.

Art. 22.- El padrón definitivo, con indicación de la parroquia y junta electoral donde debe votar quien este en goce de los derechos políticos, será difundido públicamente a través del sistema que resuelva adoptar el Tribunal Supremo Electoral.

Capítulo IV

DE LAS ELECCIONES

Art. 23.- La primera vuelta electoral se realizará el tercer domingo de octubre de cada cuatro años, para elegir las siguientes dignidades: Presidente y Vicepresidente de la República; representantes al Parlamento Andino; Diputados al Congreso Nacional; y, minorías de los Concejos Municipales de conformidad con la ley.

La segunda vuelta electoral deberá efectuarse el último domingo de noviembre del año en que corresponda elegir al Presidente y Vicepresidente de la República.

No habrá doble vuelta electoral para elegir Presidente y Vicepresidente de la República, si en la primera uno de los binomios hubiese obtenido una votación que supere el 50% de los votos válidos o, en el caso de que el binomio con la votación más alta, hubiere alcanzado más del 40% de los votos válidos, siempre y cuando obtenga una diferencia de por lo menos, diez puntos porcentuales sobre el binomio que le siguió en votación.

Art. 24.- El tercer domingo de mayo de cada cuatro años, deberá elegirse las siguientes dignidades: Prefectos Provinciales, Alcaldes Municipales, Consejeros Provinciales de elección directa; mayorías de Concejos Municipales; y, Juntas Parroquiales Rurales, de conformidad con la ley.

Capítulo V

DE LAS CANDIDATURAS

Art. 25.- No podrán participar en calidad de candidatos para dignidades de elección popular, los que se encuentren incursos en las prohibiciones constantes en la Constitución Política del Estado, en la Ley de Elecciones y en cualquier otra disposición legal vigente.

Art. 26.- Constituyen inhabilidades para ser candidatos a cualquier dignidad de elección popular las siguientes:

a) Quienes, dentro de juicio penal por delitos sancionados con reclusión en el Código Penal, hayan recibido sentencia condenatoria ejecutoriada o hayan sido llamados a la etapa plenaria, salvo que en este último caso se hubiere dictado sentencia absolutoria, antes de la fecha de cierre de la inscripción de las candidaturas;

b) Los funcionarios públicos de libre nombramiento y remoción, y los de período fijo, a menos que hayan renunciado un día antes a la fecha de inscripción de su candidatura;

c) Los magistrados y jueces de la Función Judicial, salvo que hubieren renunciado a sus funciones con seis meses de anticipación a la fecha de inscripción de la candidatura;

d) Los que hayan ejercido autoridad ejecutiva en gobiernos de facto;

e) Los miembros de la fuerza pública, en servicio activo;

f) Los que tengan contratos con el Estado, como personas naturales o como representantes o apoderados de personas jurídicas, nacionales o extranjeras, siempre y cuando el contrato se hubiere celebrado para la ejecución de obra pública, prestación de servicio público o para la explotación de recursos naturales, a través de concesiones, contrato de asociación o participación y en cualquier otra modalidad contractual; y,

g) Los culpados, contra quienes dentro del juicio penal, se hubiere dictado sentencia condenatoria, en los delitos tipificados en el Art. 257 del Código Penal; en este único caso, quedan inhabilitados de por vida.

Art. 27.- Los servidores públicos que no sean de libre nombramiento y remoción podrán ser candidatos y gozarán de licencia sin sueldo, que se concederá automáticamente, desde la fecha de inscripción de su candidatura hasta la proclamación de resultados; y, en el caso de ser electos, mientras dure el ejercicio de las funciones.

Los docentes universitarios no requerirán de licencia para ser candidatos ni para ejercer la dignidad para la cual resultaren elegidos.

Art. 28.- Son funcionarios de período fijo, aquellos que deban cumplir un período determinado, por designación o nombramiento consagrado en la Constitución Política de la República o en leyes especiales; y, los que tengan contrato a plazo determinado.

Ejercicio de la autoridad ejecutiva se entiende por la potestad y capacidad de adoptar decisiones de carácter general y obligatorio, facultado por ley, en el ámbito de la Función Ejecutiva y según lo determina el Art. 164 de la Constitución.

Art. 29.- Los requisitos para ser candidatos a Presidente y Vicepresidente de la República son ser ecuatoriano por nacimiento, gozar de los derechos políticos y tener treinta y cinco años de edad, a la fecha de inscripción de la candidatura.

Son inhabilidades, además de las consagradas en el artículo 24 del presente Reglamento, ser cónyuge, padre, hijo o hermano del Presidente de la República en ejercicio de sus funciones; y, ser Vicepresidente de la República o Ministro de Estado, a menos que renuncien hasta un día antes a la fecha de cierre de inscripción de las candidaturas, en concordancia con lo dispuesto en el artículo 47 de la Ley de Elecciones.

Art. 30.- Para ser candidatos a Diputado del Congreso Nacional se requiere ser ecuatoriano por nacimiento, gozar de los derechos políticos y tener veinte y cinco años de edad, por lo menos, a la fecha de inscripción de la candidatura; y, haber nacido en la provincia o tener su residencia en ella, de modo ininterrumpido, al menos, durante tres años inmediatamente anteriores a la fecha de las elecciones.

Son inhabilidades las contempladas en el artículo 24 de este Reglamento.

Art. 31.- Los requisitos para ser candidatos a Prefecto Provincial o Alcalde Municipal son ser ecuatoriano; gozar de los derechos políticos; tener treinta años de edad, por lo menos, a la fecha de inscripción de la candidatura; haber nacido en la provincia o cantón, según el caso, o haber tenido su domicilio civil principal en la jurisdicción política administrativa de que se trate, sin interrupción, durante dos años, al menos, antes de la fecha de las elecciones.
Son inhabilidades, además de las consagradas en el artículo 24 del presente Reglamento, las determinadas en el artículo 47 numeral 2 de la Ley de Elecciones.

Art. 32.- Son requisitos e inhabilidades para ser candidatos a Consejero Provincial o Concejal Municipal, los determinados en el artículo anterior, con excepción de la edad que se requerirá tener veinte y cinco y veinte años de edad, respectivamente, a la fecha de inscripción de la candidatura.

Art. 33.- Para optar por la candidatura a miembro de Junta Parroquial Rural se requiere ser ecuatoriano; gozar de los derechos políticos; tener dieciocho años de edad, por lo menos, a la fecha de inscripción de la candidatura; haber mantenido su domicilio electoral en la parroquia, en los dos últimos años o haber nacido en ella, lo cual podrá probarse con el padrón electoral y con la inscripción del nacimiento o la fe de bautismo, respectivamente, de ser el caso.

Son inhabilidades las consagradas en el artículo 47 numeral 2 de la Ley de Elecciones y en el Art. 24 del presente Reglamento.

Art. 34.- Sin perjuicio de lo manifestado anteriormente, para efectos de calificar las candidaturas, se observarán las siguientes normas:

a) La inhabilidad para quien tenga contratos con el Estado sea como persona natural o como representante legal o apoderado de compañía nacionales o extranjeras, en los casos y modalidades señaladas en la Constitución y en la Ley, se referirá al momento de la inscripción de la candidatura;

b) La determinación de la edad, para la inscripción y calificación de la candidatura, se contabilizará a la fecha de inscripción de su candidatura;

c) Las personas que deben renunciar a sus funciones, por disposición constitucional o legal, lo harán un día antes de la fecha de inscripción de la candidatura, con excepción de los casos determinados en él literal c) del artículo 26 del presente Reglamento, quienes deberán hacerlo seis meses antes de la fecha de inscripción de su candidatura;

d) Los dignatarios de elección popular en ejercicio de sus funciones que presenten e inscriban su candidatura para una dignidad distinta de la que ostentan, deberán renunciar a su cargo, un día antes de la fecha de inscripción de la misma;

e) Para la determinación de la mora de los deudores de los organismos seccionales, se considerará la misma a la fecha de inscripción de su candidatura y bastará la certificación del Tesorero de la entidad correspondiente, de que el deudor está en mora; salvo que, antes del momento de calificar su candidatura, presente los justificativos del pago correspondiente;

f) Si al momento de la inscripción de la candidatura, hubiere resciliado, rescindido, resuelto o revocado, por causas legales, los contratos con el Estado, en los Casos determinados por la Constitución, cesará dicha prohibición legal. Bastará para justificar la copia certificada otorgada por el funcionario competente de dicha situación; y,

g) Las personas que tuvieren pendientes reclamaciones administrativas, juicios contenciosos administrativos o tributarios por deudas con el fisco, consejos provinciales y concejos municipales, si pueden ser candidatos, mientras no exista resolución en firme.

Art. 35.- No podrán ser candidatos a Prefectos Provinciales, Consejeros Provinciales, Alcaldes, Concejales Municipales y miembros de las Juntas Parroquiales Rurales, los que directa o indirectamente, como personas naturales o como representantes de personas jurídicas, tengan contratos con el organismo seccional autónomo correspondiente, al menos, treinta días antes de la fecha de inscripción de su candidatura.

Art. 36.- Los Diputados, Consejeros Provinciales o Concejales Municipales, suplentes, que no se hayan principalizado en forma definitiva, podrán ser candidatos a la misma dignidad u otra, sin necesidad de renunciar a sus funciones.

Art. 37.- El servicio civil ecuatoriano, comprende a los ecuatorianos en goce del derecho político de desempeñar empleo o función pública remuneradas, en dependencias fiscales o en instituciones de derecho público.

Art. 38.- Para computar los plazos sobre el tiempo de renuncias, se tomará en consideración desde la fecha de presentación de la renuncia del cargo en la respectiva entidad.

Art. 39.- Cuando en la Ley de Elecciones o en otras leyes, se utilicen las palabras "se requiere para ser electos" o "para ser elegidos", se entenderá que los requisitos deben cumplirse a la fecha de inscripción de las candidaturas; y, cuando se utilicen los términos "al momento de la elección", "anteriores a la elección" o "antes de la elección", se entenderá que se refiere al día de las elecciones.

Art. 40.- Las candidaturas pluripersonales deberán presentarse con, al menos, el 30% de mujeres entre los principales y el 30% entre los suplentes.

La alternabilidad y secuencia en la presentación de listas deberá seguir el orden par o impar.

Alternabilidad es la distribución en la lista en forma sucesiva, entre hombres y mujeres.

Secuencia es la serie de combinaciones que pueden realizarse en la lista, saltando los lugares de inscripción de la lista, al tratarse de representaciones de 3 a 5 dignidades, saltando uno o dos puestos; de 6 dignidades en adelante, pasando entre dos y tres puestos y así sucesivamente.

Art. 41.- La fórmula de representación, de la igualdad de género, en el proceso de inscripción de candidaturas será el siguiente:

En elecciones que se elijan tres representantes deberá inscribirse, al menos, una candidata mujer como principal y una como suplente; en elecciones de cuatro a seis representantes por lo menos, dos serán candidatas mujeres principales y dos suplentes, la alternancia comenzará dependiendo de la inscripción de la candidata; en elecciones de siete a nueve dignidades, al menos, tres candidatas mujeres como principales y tres como suplentes, siguiendo el procedimiento de alternabilidad anterior; en elecciones de diez a doce representantes, cuatro candidatas mujeres mínimo como principales y suplentes, respectivamente; y, así de manera sucesiva.

En elecciones donde deban elegirse dos representantes, uno de los candidatos preferentemente será mujer, de igual forma en el caso de los suplentes.

Art. 42.- Exclusivamente quienes participen como candidatos a Alcalde Municipal, Prefecto Provincial o Diputado, conjuntamente con el formulario de inscripción de su candidatura, están obligados a presentar el plan de trabajo, el que deberá reunir los requisitos mínimos que a continuación se indican:

- La determinación de los objetivos de carácter general y específicos.
- El programa de trabajo que contendrá las acciones básicas que ejecutará, en el caso de ser elegido.
- Una propuesta en la que incluya el diagnóstico de la circunscripción política que representará y las soluciones que pretende implementar a la problemática del Consejo Provincial, Concejo Cantonal o del Congreso Nacional.
- Deberá declarar que se sujeta al ordenamiento jurídico ecuatoriano.
Este Plan de Trabajo debe ser otorgado ante Notario Público con la formalidad que exige la ley para estos casos.

Art. 43.- Los Tribunales Provinciales Electorales llevarán el Registro Provincial de Planes de Trabajo, ordenados en forma numérica y secuencial, conforme a la fecha de su presentación.

Capítulo VI

DE LA REELECCION

Art. 44.- En los casos permitidos por la Constitución y la Ley, quienes opten por la reelección, tienen derecho a licencia sin sueldo desde la fecha de inscripción de la candidatura hasta la proclamación de resultados, sin necesidad de petición expresa; y, si se presentaren a una dignidad distinta, deberán renunciar a su cargo, previamente a la fecha de inscripción de la candidatura.

Esta disposición no es aplicable para los dignatarios de elección popular alternos que, al momento de la inscripción de las candidaturas, no se encuentren en ejercicio de sus funciones; y no podrán principalizarse durante el proceso electoral; por lo que, ipso iure, perderán su condición de alternos, en el caso de ser electos.

Se entenderá por reelección según lo determina la Ley, si algún dignatario que habiendo sido electo para una dignidad ha subrogado definitivamente, por mandato de la ley, en otra dignidad de elección popular, siempre y cuando tal subrogación se haya producido un año de antes a la fecha de inscripción de la candidatura, por lo menos.

Capítulo VII

DE LA INSCRIPCION Y CALIFICACION

DE LAS CANDIDATURAS

Art. 45.- La inscripción de candidaturas nacionales, provinciales, cantonales y parroquiales serán presentadas por el Director Nacional o Provincial del correspondiente partido político, según el caso, o por quien lo subrogue estatutariamente. Igual procedimiento se utilizará en el caso de que un partido político patrocine la candidatura de un ciudadano independiente.

Los candidatos independientes, estarán representados directamente por el propio candidato o por un apoderado especial, en elecciones unipersonales; y, en el caso de candidaturas pluripersonales serán representados por los propios candidatos mediante la designación de un apoderado especial, sea que se trate de elecciones nacionales, provinciales, cantonales y parroquiales, según el caso.

En el caso de las alianzas en las elecciones, la inscripción de candidaturas serán presentadas por los Directores de los Partidos y representantes de las organizaciones de independientes, según el caso.

Art. 46.- La designación del apoderado especial se realizará mediante poder especial otorgado ante un Notario Público y en el se expresará lo siguiente:

a) La jurisdicción electoral en la que actuará, debiendo determinar con claridad si se trata de una nacional, provincial, cantonal o parroquial;

b) El ámbito de acción del mandatario y sus facultades, entre las que se incluirán las que contemplen la Ley de Elecciones y este Reglamento; y,

c) El organismo electoral ante quien hará valer los derechos de la representación.

Art. 47.- Los candidatos que no estén afiliados o patrocinados por un partido político, deberán acompañar a la correspondiente inscripción, un respaldo de firmas equivalentes al uno por ciento de los electores empadronados, en la correspondiente circunscripción, exceptuándose los movimientos políticos independientes, que habiendo participado en las dos últimas elecciones pluripersonales, obtuvieron el porcentaje de representatividad del 5% de los votos válidos, de conformidad con la ley; organizaciones que tendrán derecho a participar con la misma simbología y el número asignado en el proceso electoral anterior.
Art. 48.- Para la inscripción se utilizarán los formularios diseñados, aprobados y proporcionados por el Tribunal Supremo Electoral, a través de los organismos electorales inferiores.

En las candidaturas unipersonales o bipersonales deberá acompañarse las fotografías de los candidatos, preferiblemente a todo color.

Todos los candidatos tendrán la obligación de adjuntar las fotocopias de las respectivas cédulas de ciudadanía con el formulario de inscripción.

Para la inscripción de candidaturas no es necesario la presencia de los candidatos.

La solicitud de inscripción de candidaturas podrá ser presentada desde el día siguiente a la convocatoria hasta las dieciocho horas del sexagésimo primer día anterior al de la elección.

El lugar, día y hora de la presentación de la solicitud de inscripción será certificado por los Secretarios de los Tribunales Electorales competentes.

Art. 49.- La asignación de número, aprobación de la simbología, reserva y derecho del nombre de las organizaciones de independientes, sea que participen en las elecciones, con alcance nacional, provincial, cantonal o parroquial, si es presentada antes de la fecha de inscripción de las candidaturas, se lo realizará ante el Tribunal Supremo Electoral; y si fuere después, se lo realizará ante el Tribunal Electoral que deba calificar las candidaturas, siguiendo la numeración secuencial y de acuerdo con el orden de su presentación. Esta petición lo presentará el apoderado especial o los propios candidatos.

En el caso de que una misma organización de independientes inscribiera candidaturas a nivel nacional, provincial, cantonal o parroquial, éstas inscripciones recibirán un mismo número y se utilizará la misma simbología aprobada.

Art. 50.- El uno por ciento de firmas de los ciudadanos empadronados que respalden la inscripción de las candidaturas constará en los formularios aprobados por el Tribunal Supremo Electoral, sea ésta para Presidente y Vicepresidente de la República; o para Diputados Provinciales, Prefectos y Consejeros Provinciales, en caso de las provincias; o para Alcaldes Municipales, Concejales Municipales y miembros de las Juntas Parroquiales, en caso de los cantones y parroquias rurales.

Este respaldo de firmas, en caso de elecciones pluripersonales no será para cada uno de los integrantes de la lista, sino para todos en su conjunto.

Si no se cumple con el número de firmas de respaldo exigido por la Ley, se rechazará la inscripción de la o las candidaturas, en forma definitiva.

Art. 51.- Una vez presentadas las candidaturas, los Tribunales Electorales Supremo y Provinciales, según el caso, antes de calificarlas, notificarán con la nómina de las mismas a las demás organizaciones políticas, al día siguiente de la presentación, y tratándose de los candidatos independientes, se les notificará mediante carteles que se exhibirán públicamente en los Tribunales Provinciales o en casilleros electorales asignados para el efecto. Art. 52.- Las organizaciones políticas o los independientes, por intermedio de su representante legal nacional o provincial, según el caso, o los candidatos, podrán presentar impugnaciones a las candidaturas, adjuntando las pruebas y documentos justificativos, dentro del plazo de tres días contados a partir de la notificación de las candidaturas. El escrito de impugnación será presentado en original, anexando las copias necesarias para las notificaciones.

Si no se presentaren impugnaciones en el plazo de tres días, el Tribunal procederá a calificar las candidaturas.

Art. 53.- Terminado el plazo determinado en el artículo anterior, de existir impugnaciones a las candidaturas, al siguiente día se correrá traslado con las mismas a los candidatos impugnados y a las organizaciones políticas a las que pertenecen, las mismas deberán ser contestadas en el plazo de un día.

Con la contestación o en rebeldía, el Tribunal Electoral procederá a resolver las impugnaciones y calificar las candidaturas en el plazo de cuatro días.

Art. 54.- Los Tribunales Electorales negarán, de oficio o a petición de parte, la inscripción de listas de candidaturas pluripersonales que no incluyan un mínimo de 30% de mujeres como candidatas principales y el mismo porcentaje en los suplentes, según la representación, alternancia y secuencia prevista en la Constitución, en la Ley y este Reglamento.

Art. 55.- Al momento de calificar las candidaturas, los Tribunales Electorales solo podrán rechazar las candidaturas, de oficio y con las pruebas constantes en el expediente, en los siguientes casos:

a) Por incumplir con los requisitos de edad exigidos;

b) Si no se cumpliere con la fórmula de representación de la igualdad de género prevista en la Ley;

c) Si no se presentare el Plan de Trabajo, en el caso de las elecciones de Diputados, Prefectos Provinciales y Alcaldes Municipales;

d) Por incumplimiento de las formalidades que se exigen para la presentación de la inscripción de candidaturas;

e) Por falta de firmas de respaldo en el caso de candidaturas de las organizaciones de independientes; y,

f) Si no se inscribieren con el 30% de candidatas mujeres como principales e igual porcentaje en el caso de los suplentes.

Puede el partido presentar nuevos candidatos, en el plazo de tres días contados desde la notificación.

En el caso de candidatos independientes se podrá presentar nuevos candidatos previa la autorización escrita del resto de integrantes de la lista, en el mismo plazo señalado en el inciso anterior. Art. 56.- Presentados los nuevos candidatos, el Tribunal procederá de acuerdo al trámite establecido en este Reglamento. Art. 57.- En caso de que los nuevos candidatos tengan inhabilidades comprobadas, el Tribunal Electoral competente rechazará la lista; pudiendo los afectados presentar el recurso de apelación, en el plazo de dos días, contados a partir de la notificación de la resolución de negativa de inscripción de la candidatura unipersonal o pluripersonal. La resolución del Tribunal Supremo Electoral causará ejecutoria.

Art. 58.- El recurso de apelación puede ser presentado ante el respectivo Tribunal Provincial, por los representantes a nivel nacional, provincial o cantonal o por los propios candidatos.

El Tribunal Provincial enviará al Tribunal Supremo Electoral, el expediente que contendrá entre otros los siguientes documentos:

a) Formulario original de la inscripción de la candidatura, debiendo dejarse copia certificada en el organismo inferior;

b) Resolución del Tribunal Electoral competente negando la inscripción;

c) Las impugnaciones, pruebas y documentos, así como también los escritos presentados por las partes, debidamente foliados y rubricados por el Secretario;

d) La documentación que se haya presentado sobre la

candidatura; y,
e) Resolución del Tribunal concediendo el recurso.

Si el organismo electoral inferior no remitiere la documentación antes indicada será amonestado o sancionado de conformidad con la Ley, según la gravedad de la falta.

Art. 59.- Las organizaciones políticas, los candidatos o sus apoderados especiales, podrán también apelar de la calificación de las candidaturas, por parte de los Tribunales Provinciales Electorales, en el plazo de dos días de notificados con la resolución.

Para este caso, el Tribunal enviará la misma documentación indicada en el artículo anterior, excepto lo contemplado en la letra b), y enviará la resolución del Tribunal aceptando las candidaturas.

Para los casos de apelación, las organizaciones políticas, los candidatos o sus representantes no requieren adjuntar en su escrito de apelación ninguna documentación, pero sí deberán fundamentar las causas por las que apela conforme a la ley. Puede apelar quien presentó la impugnación o cualquiera otro legalmente autorizado, así no hubiere impugnado.

Art. 60.- Las organizaciones políticas y los candidatos independientes podrán cambiar los candidatos, por una sola vez, y serán sustituidos por aquellos que han sido rechazados por el Tribunal Electoral correspondiente.

Si se superaren las causas que motivaron el rechazo de una candidatura, la organización política, o los candidatos o sus representantes, podrán presentarla nuevamente y con esta solicitud se entenderá se ha ejercido el derecho contemplado en el inciso anterior de este artículo.

Art. 61.- Si el Tribunal Supremo Electoral al momento de resolver un recurso de apelación interpuesto, rechazare las candidaturas, las organizaciones políticas, los candidatos o los representantes afectados podrán presentar otras, siempre y cuando no hayan hecho uso del derecho establecido en el artículo anterior.

La nueva lista deberá ser presentada en el plazo de tres días, contados a partir de la notificación de la resolución del Tribunal Supremo Electoral, en el Tribunal Provincial respectivo. Para su calificación se deberá seguir el trámite establecido en este Reglamento.

Art. 62.- Las causas subidas en grado, por apelación ante el Tribunal Supremo Electoral, serán falladas en mérito de los autos.

No se admitirá prueba alguna en esta instancia.

Art. 63.- La inhabilidad física, mental o legal de un candidato deberá ser acreditada suficientemente ante un Juez de Derecho y calificada y comprobada por los Tribunales respectivos, adjuntando esta justificación la organización política, los candidatos o sus representantes podrán solicitar al Tribunal el cambio de candidaturas y reemplazarlos por una sola vez, en el plazo de tres días de recibida la notificación.

Tratándose de los candidatos independientes, se requerirá la autorización escrita del resto de integrantes de la lista.

Art. 64.- Las inhabilidades constitucionales y legales serán calificadas por los Tribunales Provinciales Electorales cuando sobre las mismas se planteare la respectiva impugnación o recurso de apelación, salvo los casos determinados en el Art. 55 del presente Reglamento que pueden ser impugnados, de oficio o a petición de parte y, a través de la interposición del recurso de apelación correspondiente.

Art. 65.- Cuando un ciudadano figure como candidato en dos o más listas, el Tribunal negará la inscripción de su nombre en todas ellas. En este caso, la organización política, el candidato o sus representantes afectados podrán reemplazar el nombre con el de otro ciudadano, sujetándose al trámite para la inscripción previsto en la Ley de Elecciones y en este Reglamento.

Art. 66.- Las organizaciones políticas, el resto de candidatos o sus representantes podrán cambiar el nombre de una candidatura antes de su calificación en el Tribunal Electoral correspondiente, pero una vez inscrita y calificada ésta no puede ser cambiada sino por causa de muerte, imposibilidad física, mental o legal de las que habla la ley y el presente reglamento.

No se podrá presentar listas incompletas de candidatos principales ni de suplentes.

Art. 67.- El Tribunal Supremo Electoral y los Tribunales Provinciales Electorales notificarán cualquier resolución sobre rechazo por causas de oficio, impugnaciones, aceptación o negativa de inscripción de candidaturas, dentro del plazo máximo de un día, siempre que no exista un plazo diferente determinado en la Ley o en este Reglamento.

Capítulo VIII

DE LAS JUNTAS RECEPTORAS DE VOTO

Art. 68.- Las ternas de los ciudadanos que envíen las organizaciones políticas para la conformación de las Juntas Receptoras del Voto, deberán contener los nombres y apellidos de los ciudadanos, números de cédulas de ciudadanía, direciones domiciliarias y de trabajo.

Art. 69.- Los miembros de las Juntas Receptoras del Voto tiene la obligación de asistir a los cursos o seminarios de capacitación electoral, que serán dictados por los Tribunales Provinciales Electorales.

Art. 70.- Los Tribunales Provinciales Electorales conformarán las Juntas Receptoras del Voto, de entre los ciudadanos en goce de los derechos políticos que tenga su domicilio electoral en la jurisdicción donde deba votar, con personas de comprobada capacidad e idoneidad, estudiantes que sean mayores de edad o que cumplan los 18 años un día antes de las elecciones o con miembros de las organizaciones políticas, que hubieren remitido los listados, con sesenta días de anticipación al día fijado para una elección. Pasado este plazo, el Tribunal no aceptará ternas presentadas por las organizaciones políticas, los candidatos o sus representantes, y designará las Juntas con los ciudadanos constantes en el Padrón Electoral, de conformidad con la Ley.

Las ternas que envíen los candidatos independientes, integrarán las juntas que correspondan a la circunscripción de sus candidaturas. Art. 71.- La notificación que se efectúa para los miembros integrantes de las Juntas Receptoras del Voto, tendrá plena validez al ser publicada por la prensa o notificada por cualquier otro medio que decida el correspondiente Tribunal Provincial Electoral.

Art. 72.- Los Vocales designados para las Juntas Receptoras del Voto, no podrán excusarse sino por las causales determinadas en el artículo 6 del presente Reglamento.

Los Tribunales recibirán por escrito las excusas debidamente justificadas, después de tres días de realizada la publicación o la notificación. Quienes no cumplan con sus funciones, serán sancionados con la multa de dos salarios mínimos vitales y, en caso de reincidencia con el doble de la multa.

Art. 73.- Las Juntas Receptoras del Voto extenderán por triplicado el acta de instalación y por cuadriplicado las actas de escrutinio de resultados electorales, en los formularios numerados y seriados que para el efecto entregará el Tribunal Electoral competente y, en la que constarán:

a) El lugar, día y hora de instalación de la Junta;

b) Los nombres y apellidos de los Vocales principales y suplentes que actúen;

c) Nombres, apellidos y sus respectivas firmas y rúbricas, de los delegados de cada organización política, concurrentes al acto eleccionario;

d) Las firmas y rúbricas del Presidente y Secretario de la Junta Receptora del Voto;

e) Los resultados numéricos, en letras y números, obtenidos por cada organización política o candidatos, según el caso; y,

f) Las demás constantes en la Ley y este Reglamento.

Art. 74.- Cada uno de los vocales integrantes de las Juntas Receptoras del Voto, percibirán un estipendio en la cantidad que determine el Tribunal Supremo Electoral.

Art. 75.- Las Juntas Receptoras del Voto están en la obligación de aceptar a los delegados de las organizaciones políticas y de los candidatos para su asistencia a las mismas, los que deberán portar sus respectivas credenciales, firmadas por el Director o Secretario de la organización política, del candidato o de sus representantes. Art. 76.- Las Juntas Receptoras del Voto tendrán, entre otros, los siguientes deberes y atribuciones:

a) Levantar por triplicado el acta de instalación y por cuadriplicado las de escrutinio de la Junta Receptora del Voto;

b) Entregar al votante las papeletas de votación y el certificado de votación;

c) Efectuar todos los escrutinios una vez concluido el sufragio;

d) Entregar o remitir a los Tribunales Provinciales Electorales las urnas, paquetes y sobres que contienen la primera copia del acta de instalación y escrutinios bajo la protección de la Fuerza Pública. Esta copia será colocada dentro de la urna;

e) Entregar directamente al coordinador el segundo ejemplar del acta de instalación y de escrutinios en sobre debidamente cerrado y firmado por el Presidente y Secretario de la Junta, para que se entregue en el Tribunal Provincial Electoral;

f) Obtener la firma del coordinador en el recibo de entrega del acta que se indica en la letra anterior;

g) Fijar un ejemplar del acta en el lugar visible donde funcionó la Junta Receptora del Voto;

h) Entregar el cuarto ejemplar al Coordinador de la Fuerza Pública, en los casos de transmisión inmediata de resultados;

i) Cuidar que las actas de instalación y de escrutinios lleven las firmas del Presidente y del Secretario, así como que sean firmados por los mismos funcionarios los sobres que contengan dichas actas, los votos válidos, los emitidos en blanco y los anulados;

j) Entregar las copias certificadas del resumen del acta a las organizaciones políticas y a los candidatos independientes que lo solicitaren a través de sus delegados debidamente acreditados;

k) Prohibir que se haga propaganda partidista en el recinto electoral del sufragio; y,

l) Vigilar que el acto electoral se realice con normalidad y en orden.

Art. 77.- El Tribunal Supremo Electoral al aprobar la cartilla electoral y los instructivos sobre el procedimiento de votación deberá determinar los mecanismos más idóneos para garantizar la accesibilidad de las personas con discapacidad para el ejercicio del sufragio, según el sistema que se emplee.

Título Segundo

DE LA VOTACION

Art. 78.- Si el nombre del elector no consta en el padrón de la parroquia de su domicilio, no se aceptará su voto. Se dejará constancia de este hecho en el acta en observaciones y se le entregará un certificado de haberse presentado. Si el nombre consta en el padrón de otra Junta Receptora de Voto de otra parroquia, sufragará en ella. Art. 79.- Tanto en la recepción de votos cuanto en los escrutinios de Junta Receptora del Voto y en el Escrutinio Provincial, los organismos electorales utilizarán métodos y técnicas de administración y mecánica electoral que permitan obtener información estadística desagregada por sexo, garantizando que no se viole el principio del secreto del voto.

Art. 80.- La presentación de la cédula de ciudadanía debidamente confrontada con el padrón electoral, da derecho al sufragio. Por ningún motivo los miembros de la Junta Receptora del Voto impedirán sufragar al elector que conste en el padrón, ni exigirán otras condiciones o requisitos par el libre ejercicio del sufragio.

Si el último número de la cédula de ciudadanía, dígito verificador, no coincide con el último número del padrón se le permitirá votar al elector.

Art. 81.- Llegadas las diecisiete horas las personas que se encuentran en la fila de sufragantes no podrán votar; pero la Junta Receptora del Voto les entregará un certificado provisional de presentación, a fin de no ser sancionados y de que puedan ejercer sus derechos ante el Tribunal Provincial Electoral correspondiente. Art. 82.- Si un ciudadano se presentare a votar en una junta receptora del voto y no constare en el padrón electoral de esa junta y habiendo recibido de la misma un certificado provisional de presentación, el Tribunal Provincial verificara si se encuentra empadronado en otro sitio, y en este caso será sancionado de acuerdo con la Ley.

Art. 83.- Las organizaciones políticas y los candidatos independientes pueden realizar alianzas entre si, en listas unipersonales y pluripersonales y, en este caso, deberán declarar expresamente al organismo electoral correspondiente, el casillero donde constarán en la papeleta electoral, hasta antes de que la resolución de calificación de la candidatura quede en firme. Título III

DE LOS ESCRUTINIOS Y DE LA ADJUDICACION

Capítulo I

DEL ESCRUTINIO DE LA JUNTA RECEPTORA

DEL VOTO

Art. 84.- La Junta Receptora del Voto una vez que ha procedido a la separación de las papeletas válidas, nulas, en blanco y no utilizadas, guardará en sobres cerrados las papeletas no utilizadas y las emitidas en blanco, previo el conteo correspondiente y de inmediato procederá al escrutinio de los votos válidos, blancos y nulos.

En todas las actas de escrutinio deberá, obligatoriamente colocarse la lámina autoadhesiva transparente de seguridad. Art. 85.- El segundo ejemplar del acta de instalación y de escrutinios de la Junta Receptora del Voto será entregada al Coordinador Electoral, en sobre cerrado y firmado por el Presidente y Secretario de la Junta en la parte posterior, y de esta entrega se dejará constancia en el recibo correspondiente. El Secretario del Tribunal Provincial sentará razón de la recepción del sobre con las observaciones que fueren del caso.

El Coordinador realizará la entrega de todas las actas de las Juntas Receptoras del Voto que le hubieran sido asignadas por el Tribunal Provincial Electoral.

No será causa de nulidad de las actas la falta de firma del Presidente y Secretario de la Junta en los sobres que las contienen. Art. 86.- El tercer ejemplar del acta será fijado en la parte más visible del recinto electoral en donde funcionó la Junta Receptora del Voto, aunque su falta de fijación no será causa de nulidad. El incumplimiento de lo anterior será motivo de la sanción establecida en la Ley:

El cuarto ejemplar del acta será entregado al coordinador del operativo para la transmisión inmediata de resultados, en las dignidades donde se vaya a implementar este Sistema.

Art. 87.- Los tres ejemplares de las actas de instalación y cuatro de los escrutinios de las Juntas Receptoras del Voto, llevarán las firmas auténticas y originales del Presidente y Secretario. Además, podrán firmar los Vocales de la Junta y los Delegados o Representantes de las organizaciones políticas o de los candidatos debidamente acreditados. No será causa de nulidad del acta la falta de firma del Presidente o del Secretario de la Junta, en caso de incumplimiento serán sancionados de conformidad con la Ley.

A los partidos políticos y a los candidatos independientes se les entregará copia del resumen del acta, en formularios que contendrán los resultados de la Junta, firmados por el Presidente y el Secretario.

La Junta Receptora del Voto no podrá, por ningún motivo, dejar de entregar la copia del acta resumen al delegado de la organización política o candidato independiente que lo solicitare y que porte la respectiva credencial.

Art. 88.- Los Tribunales Provinciales Electorales designarán los Coordinadores Electorales que estimen necesarios para el desarrollo del proceso electoral y para el cumplimiento de las disposiciones legales. Dichos Coordinadores deberán reunir para su elección, los mismos requisitos establecidos en la Ley para los Vocales de las Juntas Receptoras del Voto y sujetarse a las prohibiciones legales establecidas para los mismos.

Capítulo II

DEL ESCRUTINIO PROVINCIAL

Art. 89.- El escrutinio provincial que realizará el Tribunal Provincial Electoral, se realizará en una sola fase. El Tribunal examinará las actas y sumará el número de votos válidos obtenidos por los candidatos y constantes en las actas de las Juntas Receptoras del Voto entregadas al Tribunal Provincial, que se instalará a partir de las veinte y un horas del día de las elecciones, en sesión permanente hasta la culminación del escrutinio.

Art. 90.- A la sesión permanente asistirán, obligatoriamente, los Vocales del Tribunal Provincial y el Secretario, y podrán concurrir, los candidatos, los delegados de las organizaciones políticas o de los candidatos independientes, en número no mayor de dos, y los representantes de los medios de comunicación social debidamente acreditados.

Los Tribunales Provinciales Electorales no podrán suspender la sesión permanente por más de doce horas.

Art. 91.- Si un Tribunal Provincial Electoral demorare injustificadamente por más de doce horas, contadas desde la fecha y hora de instalación, el inicio de escrutinios o no lo continuare por inasistencia de sus miembros en el tiempo de que habla el artículo anterior, el Tribunal Supremo Electoral destituirá a los responsables, principalizará a los suplentes e impondrá a los Vocales destituidos la pena de suspensión de los derechos de ciudadanía por un año. De repetirse estos hechos, el Tribunal Supremo Electoral reorganizará el Tribunal Provincial, el mismo que, así reorganizado, se instalará de inmediato en la respectiva sesión.

Estas resoluciones se ejecutarán inmediatamente.

Art. 92.- Si por causa de fuerza mayor o caso fortuito que determinen la inasistencia de los Vocales de un Tribunal, no se llevare a efecto la sesión para el escrutinio en el día y hora fijados para ello, se procederá a un nuevo señalamiento dentro del día siguiente como máximo.

La convocatoria para el nuevo señalamiento lo hará el Presidente o quien lo subrogue, a partir del día en que cesó el hecho que motivó la inasistencia de los Vocales del Tribunal.

Art. 93.- En el escrutinio provincial los delegados o los candidatos podrán objetar las actas que generen duda sobre su validez legal, siempre que tuvieren pruebas documentadas. Dichas actas se considerarán como suspensas.

Art. 94.- En los años en que se realizaren elecciones para Presidente y Vicepresidente de la República y Diputados Nacionales, los Tribunales Provinciales Electorales, escrutarán en primer lugar, las actas donde consten los resultados para tales dignidades, debiendo levantar un acta especial, donde se proclamen los resultados definitivos.

En lo demás, se aplicarán las disposiciones previstas en la Ley de Elecciones y este Reglamento.

Art. 95.- Si los Tribunales Provinciales Electorales, al momento de realizar el escrutinio provincial encontraren que un acta no reúne los requisitos legales, la declararán suspensa para ser analizada su validez al final del escrutinio provincial.

Art. 96.- Concluido el examen de las actas el Tribunal procederá a totalizar el número de votos válidos obtenidos por cada candidato o por cada lista, según los casos. De la resolución de suspensión de actas no habrá reclamo o impugnación de ninguna clase.

Art. 97.- La suma de los resultados constantes en las actas, consistirá en el ingreso de los resultados numéricos al sistema que para el efecto instale el Tribunal Supremo Electoral, en el que se especificarán, entre otras cosas:

a) Código de provincia, cantón, parroquia y mesa;

b) Mesas totales de cada parroquia, cantón o provincia;

c) Mesas escrutadas por parroquias, cantones y provincia;

d) Mesas por escrutarse por parroquia, cantón o provincia;

e) Resultados parciales de votos válidos, en blanco y nulos por parroquia y cantón de cada candidato o lista; y,

f) Resultados totales, por provincia, de cada candidato o lista. Art. 98.- Los delegados podrán constatar o presenciar el ingreso de los datos al sistema de suma que se efectúe durante el escrutinio provincial.

Art. 99.- El Tribunal notificará con los resultados electorales, el mismo día de redactada el acta de conclusión del escrutinio provincial, la que se extenderá por duplicado, dejando constancia de la instalación del Tribunal, de los nombres de los Vocales, candidatos y delegados asistentes y se adjuntarán los resultados numéricos generales. El acta se aprobará en la misma audiencia, debiendo firmar el Presidente y el Secretario del Tribunal. Si los escrutinios duraren más de un día se levantará acta de cada jornada.

Los resultados serán desglosados junta por junta, debiéndose contabilizar también los votos en blanco y los nulos, los que no influirán en el resultado, a excepción de las consultas populares. Art. 100.- Si una organización política o candidato o el apoderado especial no está de acuerdo con los resultados numéricos, podrá impugnarlos dentro de la misma audiencia de escrutinios provinciales.

A estas impugnaciones se adjuntarán las pruebas y documentos justificativos respectivos, que determinen el error numérico en que haya incurrido la información del Tribunal.

Art. 101.- Antes de la proclamación definitiva de los resultados por parte del Tribunal Provincial, debe resolverse previamente sobre:

a) El escrutinio de las actas rezagadas y suspensas; y,

b) Las impugnaciones presentadas.

Art. 102.- La audiencia pública la realizarán los Tribunales hasta diez días después al de las elecciones.

Sino hubiere impugnaciones, actas rezagadas ni actas suspensas, se levantará de inmediato el acta de escrutinios definitivos.

Si las hubiere, se procederá a analizarlas actas rezagadas y se recibirá en la misma audiencia todas las observaciones legales o impugnaciones numéricas, sobre las mismas que el Tribunal resolverá en dicha audiencia.

Se analizarán las actas que fueron declaradas suspensas, respecto a su validez jurídica, y se procederá a sumar los votos, de las que se declaren válidas.

Las organizaciones políticas, los candidatos, o sus apoderados, podrán impugnar en esta audiencia los resultados numéricos de las actas suspensas y podrán observar la validez legal de alguna acta que no fue declarada suspensa.

Las impugnaciones serán verbales y fundamentadas, no pudiendo el candidato o delegado del mismo partido o candidatura, intervenir por más de dos ocasiones por el mismo asunto.

Cada candidato o delegado no podrá intervenir en cada ocasión por más de tres minutos.

Si para sumar el resultado de una junta no hubiere el ejemplar del acta entregada por el coordinador, se la extraerá de la urna correspondiente, procediéndose a su examen legal, para establecer su validez.

De no existir el acta del Coordinador ni la de la urna, el Tribunal podrá escrutar los votos, solo tomando como referencia por lo menos dos copias presentadas por las organizaciones políticas o por los candidatos independientes. De existir diferencias en esas copias; el Tribunal deberá exigir la presentación de otras. Prevalecerán las copias que contengan la firma auténtica del Presidente o Secretario de la Junta.

Art. 103.- El Secretario levantará acta de los escrutinios definitivos y notificará máximo al día siguiente de concluido el escrutinio provincial, a las organizaciones políticas y candidatos. Art. 104.- El recurso de apelación previsto para la nulidad de la votación, procede únicamente cuando el Tribunal la declare antes de concluir el escrutinio.

Art. 105.- Las organizaciones políticas o los candidatos podrán apelar también de la declaratoria de nulidad o de la validez de los escrutinios realizado por el Tribunal Provincial dentro del plazo de dos días de notificada el acta de escrutinios definitivos.

El Tribunal concederá el recurso, de ser procedente, al día siguiente de su presentación, si éste hubiere sido interpuesto dentro del plazo establecido en la Ley, debiendo remitir al día siguiente la documentación para conocimiento del Tribunal Supremo Electoral.

La documentación que deberá enviarse al Tribunal Supremo Electoral será entre otros:

a) Copia certificada del acta de escrutinios definitivos;

b) Copia del escrito de apelación;

c) Copia de la resolución del Tribunal concediendo el recurso; y, d) Todos los documentos que han servido de base para la declaratoria de nulidad o de validez de los escrutinios, como actas de instalación y escrutinios de las Juntas Receptoras del Voto apeladas, paquetes con los correspondientes votos, etc.

Art. 106.- Los recursos de apelación deberán presentarse en el Tribunal Provincial Electoral respectivo, dentro de los plazos previstos en la Ley.

Capítulo III

ESCRUTINIO NACIONAL

Art. 107.- El Tribunal Supremo Electoral realizará el escrutinio nacional y proclamará los resultados de elecciones para Presidente y Vicepresidente de la República y para dignidades de elección nacional así como en los casos de Consulta Popular Nacional.

Para ello se instalará en audiencia pública, previo señalamiento de lugar, día y hora, no antes de cuatro ni después de siete días, contados desde aquél en que se realizaron las elecciones.

La notificación del señalamiento de la audiencia, se hará por medio de los casilleros electorales o carteles y, de estimarlo necesario, en uno de los periódicos de mayor circulación de las provincias de mayor población.

Art. 108.- Los Tribunales Provinciales Electorales remitirán al Tribunal Supremo Electoral, uno de los ejemplares de las actas de escrutinios provinciales, luego de que hubieren notificado a las organizaciones políticas y a los candidatos.

Art. 109.- El Tribunal Supremo Electoral, procederá al escrutinio nacional en la siguiente forma:

a) Resolverá en primer lugar los recursos de apelación que se hubieren interpuesto por la nulidad de la votación y de los escrutinios;

b) Examinará las actas levantadas durante el escrutinio provincial a fin de verificar los resultados y corregir los errores;

c) Resueltos los recursos y examinadas todas las actas el Tribunal Supremo Electoral sumará el número de votos válidos obtenidos por cada candidato o por cada lista, según los casos, y hará la proclamación de los resultados definitivos.

Esta resolución causará ejecutoria;

d) El Tribunal podrá ordenar se realice las verificaciones y comprobaciones que estime necesarias; y,

e) Para el cómputo contabilizará los votos en blanco y nulos, los que no influirán en el resultado de las elecciones ni de la adjudicación de puestos, excepto en las consultas populares. Capítulo IV

ADJUDICACION DE PUESTOS

Art. 110.- Para la adjudicación de puestos se seguirá el procedimiento establecido en la Ley.

Art. 111.- En elecciones pluripersonales se aplicará la fórmula de representación proporcional de reparto de escaños entre las listas, DHont o de divisores continuos, procedimiento de división de los votos recibidos por las organizaciones políticas para una serie de divisores, de cuyo resultado se obtienen cocientes y, en base a éstos los escaños se reparten a los cocientes más altos siguiendo el proceso siguiente:

- La suma total de todos los votos nominales alcanzados por todos los candidatos de cada lista, es la cifra a la que se aplicará la fórmula DHont o de divisores continuos;
- El total de votos obtenidos por cada lista, efectuada la suma indicada en el numeral anterior, se dividirá para 1, 2, 3, 4, 5, etc., hasta que cada lista obtenga un número de cocientes igual al de los candidatos a elegirse como principales;
- Una vez obtenidos los cocientes, se ordenarán de mayor a menor, indicando a la lista que corresponda y se asignará los puestos que le correspondan a cada lista, adjudicando en forma ascendente a descendente, a los cocientes más altos.
- La adjudicación de los escaños dentro de una lista corresponderá a los candidatos con mayor número de votos, hasta completar el número total de representaciones que le correspondan por lista.
En caso de empate por el último escaño, se decidirá por sorteo. Si algún resultado atrojare decimales, se utilizará el entero más próximo, y en caso de mitades iguales, se aproximará a la inmediata superior.

Ejemplos demostrativos se anexan al final de este Reglamento. Art. 112.- En elecciones de dos representantes, el primer escaño se adjudicará al candidato quien obtenga el mayor número de votos y el segundo puesto corresponderá al más votado de la lista que siga en votos, siempre que haya obtenido más del 60% de los votos del primer escaño. Caso contrario, ambos escaños corresponderán a la primera lista.

Art. 113.- La adjudicación de puestos para la elección de Diputados Provinciales, Prefectos Provinciales, Alcaldes Municipales, Consejeros Provinciales, Concejales Cantonales y miembros de las Juntas Parroquiales y Rurales, corresponderá hacer a los Tribunales Provinciales Electorales inmediatamente de que se hayan notificado con los resultados definitivos provinciales, siempre y cuando no exista ninguna apelación pendiente sobre los mismos y la resolución se encuentre ejecutoriada por el ministerio de la ley.

Art. 114.- Si hubiere apelación sobre adjudicación de puestos que hagan los Tribunales Provinciales Electorales, la proclamación de candidatos triunfantes realizará el Tribunal Supremo Electoral, luego de resuelto el recurso.

Art. 115.- Ejecutoriada la resolución de adjudicación de puestos, los Tribunales Provinciales Electorales entregarán las credenciales a los Diputados Provinciales, Prefectos Provinciales, Alcaldes Municipales, Consejeros Provinciales, Concejales Cantonales y miembros de las Juntas Parroquiales Rurales; se dejará constancia en el libro correspondiente, el cual será firmado por el elegido, constituyendo tal hecho la posesión en el desempeño de sus cargos.

Igual procedimiento se seguirá en el Tribunal Supremo Electoral respecto a dignidades de elección nacional.

El Presidente y Vicepresidente de la República, recibirán las respectivas credenciales del Tribunal Supremo Electoral, y prestarán su promesa ante el Congreso Nacional.

Para la entrega de credenciales los Tribunales Electorales notificarán a los candidatos electos mediante los casilleros electorales, o de ser el caso, por escrito o mediante carteles. Capítulo V

DE LA NULIDAD DE LAS

VOTACIONES Y ESCRUTINIOS

Art. 116.- No existirán otras causales de nulidad de las votaciones, que las que determina en forma expresa la Ley.

En general en caso de duda, se estará por la validez de las votaciones.

Art. 117.- La declaración de nulidad del acto de escrutinios realizados por los Tribunales Provinciales, sólo procede en los casos que determina la Ley.

Estas nulidades no se refieren a los que son propios del acto de votación y de nulidad de una acta de la Junta Receptora del Voto. Art. 118.- Si el Tribunal Supremo Electoral, al conocer una apelación, declara la nulidad de los escrutinios definitivos de las elecciones efectuadas en una provincia, realizará de inmediato el nuevo escrutinio en base de las actas de escrutinio de las juntas receptoras del voto.

En este caso, extenderá las credenciales a los candidatos triunfadores.

Art. 119.- Para que el Tribunal Supremo Electoral pueda convocar a una nueva elección en una o más parroquias, por haberse declarado la nulidad de las votaciones, dicha nulidad deberá referirse a la totalidad de las juntas. El término parroquias se refiere tanto a las urbanas como a las rurales.

Las nuevas elecciones se realizarán dentro de diez días de declarada la nulidad y previa convocatoria pública, que se realizará por lo menos tres días antes del día señalado para la nueva votación.
Para el escrutinio se seguirá el trámite establecido en la Ley y este Reglamento.

Art. 120.- La convocatoria para las nuevas elecciones, en las circunscripciones territoriales en las que no hubiere podido verificarse oportunamente una elección, podrá realizarse a través de los medios de comunicación de mayor difusión en el lugar de la votación, cuando menos con tres días de anticipación del fijado para la votación. Las elecciones se realizarán dentro del plazo de diez días contados a partir de la fecha de las elecciones generales o parciales.

Título IV

DEL DERECHO DE IMPUGNACION Y DE LOS

RECURSOS ELECTORALES

Capítulo I

DE LAS IMPUGNACIONES

Art. 121.- Las organizaciones políticas o los candidatos, por intermedio de su representante legal nacional o provincial, tendrán los siguientes derechos y recursos:

a) Derecho de impugnación

b) Recurso de apelación; y,

c) Recurso de queja.

Art. 122.- La impugnación procede en los siguientes casos

a) De candidaturas presentadas para intervenir en las elecciones unipersonales y pluripersonales, por inhabilidades legales; y;

b) Del resultado numérico de los escrutinios electorales. Art. 123.- Las impugnaciones serán presentadas ante el Tribunal Supremo Electoral, por el representante nacional de la organización política, y en los Tribunales Provinciales Electorales, por el representante provincial. Un representante provincial sólo podrá impugnar las candidaturas correspondientes a la provincia de la cual es representante de la organización política. Así mismo los candidatos nacionales sólo pueden impugnar ante el Tribunal Supremo Electoral y los candidatos provinciales, cantonales o parroquiales ante el Tribunal de su domicilio.

Los candidatos independientes, podrán presentar las impugnaciones por sí mismos o a través de sus representantes de acuerdo con la circunscripción de su candidatura, es decir, si la candidatura es a nivel nacional la presentará ante el Tribunal Supremo Electoral, si la candidatura es provincial, cantonal o parroquial, la presentará únicamente al Tribunal de su domicilio.

Capítulo II

DE LOS RECURSOS ELECTORALES

Art. 124.- El recurso de apelación procede en los siguientes casos:

a) De la aceptación o negativa de inscripción de candidatos;

b) De la declaración de nulidad de la votación;

c) De la declaración de nulidad de los escrutinios;

d) De la declaración de validez de los escrutinios; y,

e) De la adjudicación de puestos.

Las organizaciones políticas y los candidatos o sus representantes podrán interponer el recurso de apelación en el plazo de dos días de recibida la notificación.

Declarada la validez de una junta electoral, no procederá ningún recurso.

El Tribunal Provincial, de ser procedente, concederá el recurso dentro del día siguiente de su presentación.

Art. 125.- El Tribunal Supremo Electoral, resolverá las apelaciones interpuestas en el caso de elecciones para Presidente y Vicepresidente de la República, en un plazo de cinco días, contados desde que avocó conocimiento, y no mayor de diez días, desde que recibió la documentación materia de la apelación.

Para las demás dignidades resolverá en el plazo de cinco días desde que avocó conocimiento, debiendo de todas maneras resolver todas las apelaciones, sobre candidaturas, hasta cuarenta y seis días antes de las elecciones.

Se entiende que un Tribunal avoca conocimiento de un asunto, desde el momento que es tratado por el Pleno de un Organismo, aunque no exista resolución de ninguna clase.

Art. 126.- De no existir resolución del Tribunal Supremo Electoral en los plazos indicados, el recurrente, de acuerdo con la Ley, tendrá derecho a presentar su reclamación ante el Tribunal Constitucional.

Art. 127.- El recurso de queja procede en los siguientes casos:

a) Por incumplimiento de la Ley, los reglamentos y las resoluciones de los Tribunales Provinciales Electorales o del Tribunal Supremo Electoral; y,

b) Por infracciones a las leyes, los reglamentos o las resoluciones por parte de los Vocales de los Tribunales Provinciales Electorales o del Tribunal Supremo Electoral.

Las quejas contra los funcionarios y empleados de los Tribunales Provinciales Electorales, se presentarán ante estos mismos organismos. A su vez, las quejas contra los Vocales de los Tribunales Provinciales Electorales, se presentarán ante el Tribunal Supremo Electoral.

Las quejas contra los Vocales del Tribunal Supremo Electoral, se presentarán ante el Tribunal Constitucional.

Art. 128.- Para determinar la fecha de la infracción legal, reglamentaria o administrativa, se tomará en consideración el día de la notificación de la resolución o la fecha en que se cometió la infracción.

Art. 129.- Todas las apelaciones, quejas y denuncias que se presentaren ante el Tribunal Supremo Electoral y los Tribunales Provinciales Electorales, se resolverán previo informe de la Comisión Jurídica, que funcionará en cada uno de dichos organismos y en forma permanente, salvo decisión en contrario adoptada por el Pleno.

Las que interpongan las organizaciones políticas, serán aceptadas a trámite solamente cuando estén suscritas por el representante legal de ellos, nacional o provincial, según el caso, o los candidatos.

Tratándose de candidatos independientes, serán aceptadas al trámite cuando estén suscritas por el candidato o apoderado especial, de acuerdo a la circunscripción de su candidatura.

Las denuncias o reclamaciones de los ciudadanos, serán presentadas previa la exhibición de su correspondiente cédula de ciudadanía.

Título V

CONSULTAS POPULARES

Art. 130.- Si el Presidente de la República convoca a una Consulta Popular, en los casos previstos por la Constitución, la convocatoria la realizará el Tribunal Supremo Electoral en el plazo de quince días contados a partir desde la recepción del correspondiente Decreto Ejecutivo. El Tribunal Supreno Electoral fijará la fecha de la consulta popular, dentro de los cuarenta y cinco días contados a partir de la convocatoria; y, si se encontrare en proceso electoral, se realizará el día de las elecciones, siempre y cuando el Decreto Ejecutivo sea recibido con un plazo de 45 días antes de las elecciones, por lo menos.

El Tribunal Supremo Electoral deberá presupuestar, organizar y dirigir este evento de conformidad con la Constitución y la ley. Art. 131.- Para efectos de la consulta popular se utilizarán los mismos padrones electorales que sirvieron para las últimas elecciones, actualizados hasta treinta días antes de la consulta y, en las juntas electorales actuarán los mismos Vocales que intervinieron en la última elección.

Art. 132.- Los escrutinios de la consulta popular lo efectuarán los Tribunales Provinciales Electorales y enviarán al Tribunal Supremo Electoral siguiendo el procedimiento determinado en la Ley y este Reglamento, incluyendo las impugnaciones numéricas, las apelaciones, en cuanto al tiempo y modo de presentarlos.

Art. 133.- Previo al inicio de los escrutinios nacionales, efectuados por el Tribunal Supremo Electoral, éste resolverá las apelaciones presentadas en los Tribunales Provinciales Electorales. Título VI

DE LAS GARANTIAS DEL SUFRAGIO

Capítulo I

DISPOSICION GENERAL

Art. 134.- El Tribunal Supremo Electoral, los Tribunales Provinciales Electorales y los Vocales de las Juntas Receptoras del Voto, harán cumplir las normas legales sobre las garantías que gozan e impondrán las sanciones que la Ley establece, para el caso de violación o infracción de aquellas.

Capítulo II

DEL PROCEDIMIENTO PARA EL JUZGAMIENTO

Art. 135.- Las autoridades para juzgar y sancionar las infracciones electorales, sin perjuicio de la competencia de los jueces penales, para conocer de los delitos relativos al sufragio incriminados en el Capítulo I del Título II, del Libro Segundo del Código Penal son:

a) La Corte Suprema de Justicia, al tratarse de los miembros del Tribunal Supremo Electoral y de las personas sujetas al fuero de Corte Suprema;

b) El Tribunal Supremo Electoral al tratarse de los Vocales de los Tribunales Provinciales Electorales y de las personas sujetas al fuero de Corte Superior; y,

c) Los Tribunales Provinciales Electorales al tratarse de los miembros de las Juntas Receptoras del Voto y de cualquier otra persona, sin fuero especial.

Art. 136.- Para el juzgamiento de los ciudadanos que no hubieren sufragado, el Presidente del Tribunal Provincial Electoral respectivo, publicará la citación concediendo un plazo de treinta días para que justifique la omisión. El proceso de juzgamiento se iniciará 30 días después de proclamados los resultados electorales.

La citación contendrá un aviso publicado por la prensa o por la radio, advirtiendo a los no sufragantes, que al no presentar las pruebas de descargo por su incumplimiento, serán sancionados con la multa determinada en la Ley.

Para efectos de la aplicación de las multas, el Tribunal Supremo Electoral emitirá el instructivo correspondiente.

El ciudadano podrá presentarse dentro de estos treinta días, al respectivo Tribunal Provincial, para su juzgamiento.

En caso de que no se hubieren emitido los títulos de crédito, deberá cancelar la multa correspondiente en el Tribunal Provincial Electoral de su jurisdicción y, de haber sido emitidos los títulos de crédito, deberá cancelarlos en el Ministerio de Finanzas, debiendo el Tribunal Provincial, con el recibo de pago, emitir el correspondiente certificado.

Art. 137.- Las únicas causales para eximir a una persona de la sanción por no sufragar, son las determinadas en el artículo 128 de la Ley de Elecciones. No se aceptarán otros motivos o justificaciones. Art. 138.- Para que los Tribunales Provinciales Electorales eximan de la sanción, los no sufragantes comprobarán su causal con la siguiente documentación:

a) Los que no puedan votar por mandato legal, presentarán su cédula de identidad o el documento que les acredite como miembros activos de la Fuerza Pública;

b) Los que por impedimento físico o enfermedad no puedan sufragar, justificarán por medio de un certificado otorgado por un médico de Salud Pública o del IESS o la certificación de haber estado hospitalizado el día de las elecciones, conferido por un Centro de Salud.

Si una persona hubiese estado detenida el día de las elecciones, justificará con la certificación correspondiente, otorgada por la autoridad competente;

c) La calamidad doméstica se justificará presentando la partida de defunción de la persona fallecida, o una declaración jurada rendida ante Juez competente, para éstos u otros casos.

En caso de fallecimiento, sólo se aceptará la excusa hasta parientes dentro del cuarto grado de consanguinidad o segundo de afinidad;

d) Los mayores de sesenta y cinco años y los analfabetos presentarán su cédula de ciudadanía o identidad, según los casos; y,

e) Los que no consten en los padrones, sólo requerirán la comprobación por parte del propio Tribunal Electoral.

El Tribunal concederá el certificado de exoneración de la votación sin más trámite, a excepción de las personas mayores de sesenta y cinco años y los analfabetos, quienes sólo presentarán para cualquier trámite a la Autoridad Pública su cédula de ciudadanía o identidad.

Art. 139.- Los estudiantes que vayan a obtener el título de bachiller y no hubieren llegado a esa edad en el día de las elecciones, no requerirán de ninguna certificación o comprobante para el trámite del bachillerato. Para otorgar un nuevo certificado de votación, por pérdida o extravío, el ciudadano deberá cancelar el valor que fije el Tribunal Supremo Electoral, en los Tribunales Provinciales Electorales.

Art. 140.- Si las penas que impusieren los Tribunales Provinciales Electorales fueren de multas que no excedan de dos salarios mínimos vitales, la resolución causará ejecutoria. Si fuere de suspensión de los derechos de ciudadanía, de privación de la libertad o de multas superiores a dos salarios mínimos vitales, se podrá recurrir ante el Tribunal Supremo Electoral.

El recurso deberá ser interpuesto dentro del término de tres días, contados a partir de la fecha de notificación.

Art. 141.- Para el cobro de las multas que establece la Ley, los Tribunales Provinciales Electorales pueden hacerlo por medio del pago directo en el Banco Central para el ingreso en la cuenta especial denominada "Cuenta Multas Tribunal Supremo Electoral", administrada por ese Organismo.

Art. 142.- Transcurrido un año del día de las elecciones, no se exigirá a ningún ciudadano el pago de multas por no haber sufragado, ni se solicitará por parte de los funcionarios públicos el comprobante de votación, excepto en los casos de interrupción de la prescripción.

La prescripción de la acción se interrumpe con la notificación al infractor o por la publicación en la prensa o notificación, en el caso del no sufragante.

Título VII

DE LOS CASILLEROS ELECTORALES

Art. 143.- Todas las notificaciones que deban hacer el Tribunal Supremo Electoral y los Tribunales Provinciales Electorales, desde el momento de la convocatoria a elecciones hasta la adjudicación definitiva de puestos y entrega de credenciales, se realizarán a través de los casilleros electorales que cada organización política tendrá en los diferentes Tribunales, incluyendo el Tribunal Supremo Electoral.

Tratándose de los candidatos independientes, las notificaciones se las realizará mediante carteles que serán fijados en los Tribunales Electorales, o si fuera del caso a través de casilleros electorales debidamente identificados con el correspondiente número, que se les asignará a partir de la inscripción de las candidaturas.

Art. 144.- Los secretarios de los Tribunales pondrán la fe de presentación en cada escrito que presenten las organizaciones políticas o candidatos y que se refieran a asuntos electorales. Formarán el correspondiente expediente debidamente numerado, foliado y rubricado, de cada candidatura o lista.

De cada resolución se dejará constancia en el expediente, con indicación del día y la hora.

Las providencias que dicten los Tribunales, serán firmadas por el Presidente y certificadas por el Secretario.

Los Secretarios llevarán un detalle pormenorizado de todas las providencias que han notificado en el día, a cada partido o candidato. Para las notificaciones, los Secretarios lo harán certificando las respectivas copias.

Art. 145.- El Presidente o el Secretario del Tribunal entregará a cada Director Nacional o Provincial o su representante, según el caso, la llave del correspondiente casillero electoral, quedando bajo la responsabilidad del representante de la organización política, el cuidado y conservación de la misma.

En caso de pérdida, el partido solicitará el cambio de cerradura, a su costo.

Título VIII

DE LOS COLEGIOS ELECTORALES

Capítulo I

Colegios Electorales de Elección Indirecta

de los Consejeros Provinciales

Art. 146.- Las elecciones indirectas se realizarán sesenta días antes de la terminación del mandato de los Consejeros Provinciales que deban cumplir su período a través del procedimiento establecido en la ley.

Art. 147.- La mitad más uno del total de los consejeros que conforman los Consejos Provinciales serán elegidos mediante elecciones populares y directas; y, los restantes serán designados en elecciones indirectas, a través de los Colegios Electorales integrados por todos los Concejos Municipales de la provincia, siguiendo el procedimiento determinado en el artículo siguiente.

Art. 148.- El Tribunal Provincial Electoral, sesenta días antes de que termine el período para el que fueron designados los consejeros provinciales de elección indirecta, convocará al Colegio Electoral integrado por todos los Concejos Municipales de la respectiva provincia para su designación en base al Reglamento que, para el efecto, deberá dictar el Tribunal Supremo Electoral, de conformidad con la ley.

El Colegio Electoral estará representado por todos los Alcaldes y Concejales en funciones.

Para que haya quórum será necesaria la concurrencia de, por lo menos, la mitad más uno de los Alcaldes y la mitad más uno de los Concejales de cada Municipio. El Colegio Electoral se instalará en segunda convocatoria máximo ocho días después, con el número de miembros presentes y estará dirigido por el Pleno del Tribunal Provincial Electoral.

De la resolución de resultados sobre la designación de los Consejeros Provinciales, a través de elecciones indirectas pronunciados en los Colegios Electorales correspondientes y proclamados por los Tribunales Provinciales Electorales, cabe recurso de apelación ante el Tribunal Supremo Electoral, el mismo que deberá ser interpuesto por el representante legal del Concejo Municipal. Art. 149.- Los consejeros provinciales designados por elección indirecta, a través de los Colegios Electorales, deberán pertenecer a cantones diferentes a los de los consejeros provinciales elegidos mediante votación popular y directa, tomando en consideración que el candidato propuesto sea oriundo del cantón o tenga su domicilio principal en el mismo, es decir, que haya residido en ella de modo ininterrumpido, al menos, dos años antes de la elección.

Art. 150.- Para la designación de consejeros mediante elección indirecta, a través de los Colegios Electorales integrados por los Concejos Municipales, se aplicará la fórmula de representación de candidatos consagrada en la Ley de Elecciones, aplicando la igualdad de género, en el porcentaje de, al menos, el 30% de candidatas mujeres como principales y el mismo porcentaje para candidatas mujeres suplentes; porcentaje que se incrementará en cada proceso electoral general, en un 5% adicional hasta llegar a la igualdad en la representación. Se tomará en cuenta la participación étnica cultural. Capítulo II

DE LOS OTROS COLEGIOS

ELECTORALES

Art. 151.- Para la organización y funcionamiento de los Colegios Electorales, Nominadores o Designadores previstos en la Constitución Política de la República, la Ley de Elecciones y otras leyes especiales o reglamentos generales de aplicación de leyes vigentes, el Tribunal Supremo Electoral deberá dictar el Reglamento de Organización, Funcionamiento y Atribuciones del Colegio Electoral correspondiente y las que tenga el organismo electoral competente, según el caso.

Título IX

DE LA POSESION

Art. 152.- El Presidente y el Vicepresidente de la República se posesionarán y ejercerán sus funciones desde el 15 de enero del año siguiente al de su elección, en la forma prescrita en la Constitución y la Ley.

Los Diputados al Congreso Nacional se posesionarán, sin necesidad de convocatoria previa, el 5 de enero del año siguiente al de su elección, de acuerdo con la Constitución y la Ley Orgánica de la Función Legislativa.

Los Prefectos Provinciales, los Alcaldes Municipales, los Consejeros Provinciales, los Concejales Municipales y las Juntas Parroquiales Rurales se posesionarán y entrarán en funciones el 10 de agosto del año de su elección, según las Leyes de Régimen Provincial y Municipal correspondiente.

Los representantes a los que se refieren los incisos segundo y tercero de este artículo que por causa debidamente justificada no se hubieren posesionado en las fechas indicadas, podrán hacerlo posteriormente ante los organismos o autoridades competentes. DISPOSICIONES GENERALES

Art. 153.- Para la determinación del número de consejeros que deba conformar un Consejo Provincial se utilizará las proyecciones del Censo Nacional de Población entregadas por el Instituto Ecuatoriano de Censos y Estadísticas o por el organismo competente que cumpla esta función, y que deberá ser entregado con treinta días de anticipación a la fecha de la convocatoria a elecciones.

Art. 154.- El Tribunal Supremo Electoral dictará reglamentos especiales si se adoptare un sistema de automatización del escrutinio o de inmediata contabilización o similares, el mismo que será publicado en el Registro Oficial.

Art. 155.- Previo al proceso electoral, los vocales de los Tribunales Provinciales Electorales deberán distribuirse la coordinación de cantones y parroquias de una provincia, debiendo coordinar cada vocal un número de recintos, parroquias y cantones, similar y equitativo, procedimiento que se decidirá en una sesión convocada exclusivamente para estos efectos y en la que se tomarán en cuenta los siguientes parámetros:

a) Número de electores totales por provincia, cantones y parroquias;

b) La extensión territorial de la jurisdicción electoral de que se trate;

c) La división política administrativa de la provincia; y

d) Deberá asignarse un número igual de electores y de recintos electorales bajo el control, coordinación y supervisión de los Vocales.

Art. 156.- Los Tribunales Provinciales Electorales convocarán a audiencia pública de sorteo de los Coordinadores de Recinto Electoral designados, asignando mediante esta modalidad el recinto electoral que le corresponde coordinar, sin importar el origen de su designación, garantizando de esta forma el auto control y seguimiento de las actividades de dichos Coordinadores.

Art. 157.- En caso de falta temporal o definitiva del suplente con derecho a ejercer la representación alterna, subrogará al principal el siguiente candidato principal con mayor número de votos y que no obtuvo una representación en las elecciones y así sucesivamente. Los alternos de éstos actuarán exclusivamente si se principaliza en forma definitiva.

Art. 158.- Desde la convocatoria a elecciones y hasta la conclusión del proceso electoral, con la entrega de credenciales, para efectos de los plazos, correrán todos los días, inclusive sábados, domingos y feriados. Por tanto, el Tribunal Supremo Electoral y los Tribunales Provinciales Electorales podrán recibir cualquier inscripción impugnación, apelación o queja o resolver cualquier trámite en cualquier día.

Art. 159.- El horario de atención en la Secretaría de dichos organismos para los días inhábiles, será de nueve horas a doce horas y de quince horas a dieciocho horas.

Se exceptúa el último día en que deba recibirse la inscripción de candidaturas, en el que, si recayere en día feriado, se laborará como día hábil.

Art. 160.- Todos los escritos en período electoral, deberán ser entregados en la Secretaría de los organismos.

Art. 161.- Los Tribunales Electorales, en lo referente a los trámites y procedimientos, estarán a lo que dispone la Ley de Elecciones, este Reglamento, los Reglamentos Especiales o Internos, Instructivos y Manuales que dicte el Tribunal Supremo Electoral. Art. 162.- En el caso de que los Tribunal Supremo y Provinciales Electorales, realicen campañas de capacitación de los electores, de difusión cívica y cualquiera vinculada con el proceso electoral, tendrá en cuenta para su aprobación los principios en que se sustenta el derecho al sufragio así como su eficaz ejercicio y la participación ciudadana con perspectiva de género, para promover la participación equitativa de hombres y mujeres. Se tomará en cuenta la participación étnica cultural.

Art. 163.- Para efectos de organización interna, los Tribunales Supremo Electoral y Provinciales Electorales, llevarán como libros especiales los siguientes:

a) De las organizaciones políticas;

b) De desafiliaciones;

c) De expulsiones;

d) De registro y cambios de directivas nacionales o provinciales; e) De la inscripción y calificación de candidatura;

f) De los dignatarios electos; y

g) De los planes de trabajo

El Tribunal Supremo Electoral dictará los correspondientes instructivos para ese objeto.

Art. 164.- Para efectos de determinación de las desafiliaciones y expulsiones, las primeras deberán ser presentadas en el Tribunal Provincial Electoral del domicilio del interesado, por éste, adjuntando copia de su cédula de ciudadanía y las expulsiones deberán ser notificadas por el partido, al Tribunal Supremo Electoral, adjuntando copia certificada de la resolución tomada por el organismo interno correspondiente.

El Tribunal Supremo Electoral reglamentará internamente el procedimiento de inscripción de expulsiones.

Las notificaciones de desafiliaciones y expulsiones serán hechas por los partidos políticos a los Tribunales correspondientes, en el plazo máximo de treinta días de producidas.

Art. 165.- Definiciones.- Organizaciones Políticas.- Se consideran para los efectos de aplicación de la Ley de Elecciones y de este Reglamento, como organizaciones políticas a los partidos políticos legalmente reconocidos; y, a las organizaciones y movimientos de independientes, nacionales, regionales o locales, sean provinciales (sic), cantonales o parroquiales.

Artículos finales.- Primero.- Queda derogado el Reglamento expedido mediante Decreto Ejecutivo No. 1257-A de 16 de febrero de 1990, publicado en el R.O. No. 379, Suplemento, de la misma fecha, así como todos los reglamentos, resoluciones o instructivos dictados por el Tribunal Supremo Electoral, que se opongan al presente reglamento. Segundo.- El presente reglamento entrará en vigencia a partir de la fecha de su publicación en el Registro Oficial.

Nota: Para ver cuadros, favor remitirse a Imágenes del Registro Oficial, (Inserte su disco compacto y pulse el botón respectivo).'''
#________________________ CLASE PADRE ___________________________________________________________________
class Persona:
    '''Clase padre el cual contiene los metodos o las cualidades de una persona normal.
    
-----
Atributos
-----
- self.nombre: De tipo str. \n
        Son los nombres (2) de la persona.

- apellido: De tipo str.\n
        El cual constiene los apellidos (2) de la persona.\n 
- edad: De tipo fecha (str).\n
        El cual constiene la fecha de nacimiento formato ##/##/####. 
- numCedula: De tipo str.\n
        Por que son 10 numeros y el int no coje a todos. 
        
----
Metodos
-----
- >>> def __init__(self, nombre, apellido, edad ,numCedula): El cual es el constructor el cual constiene los tributos de la clase Persona. 
'''
    def __init__(self, nombre, apellido, edad ,numCedula):
        self.nombre= nombre
        self.apellido = apellido
        self.edad = edad 
        self.numCedula = numCedula

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        """
        Establece el valor del atributo de fecha
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._edad= value

#____________________ CLASE PARA EL CIUDADANO ___________________________________________________________
class Ciudadano(Persona):
    '''
Base legal: https://aceproject.org/ace-es/topics/lf/lfc/lfc24 . 

En este link se evidencia el Reglamento General a la Ley de Elecciones de Ecuador. En el se 
ilustra todo lo que se debe tener en cuenta para poder sufragar y para ser parte de una mesa 
electoral. En el presente proyecto se tomará este Reglamento como base legal. Con esto se evita 
las sanciones puestas por el CNE por no incumplir la asistencia a la mesa electoral (Electorales, 
2022)'''
    def __init__(self,nacionalidad,expedicionCedula,ocupacion ,nombre, apellido, edad, numCedula):
        self.nacionalidad = nacionalidad
        self.expedicionCedula = expedicionCedula
        self.ocupacion=ocupacion = ocupacion
        super().__init__(nombre, apellido, edad, numCedula)

    def ComprobarCiudadano(self):
        '''Utilizar principalmete nacionalidad'''
        return self.nacionalidad =='Ecuatoriana'
        
    def MayorDeEdad(self):
        '''ocupar principalmente edad '''
        fechaActual = datetime.now()
        fechaActual = fechaActual.strftime("%Y-%m-%d")
        fechaActual= datetime.strptime(fechaActual, "%Y-%m-%d")
        diferenciaTiempo= fechaActual.year - self.edad.year
        diferenciaTiempo -= ((fechaActual.month,fechaActual.day)< (self.edad.month, self.edad.day))
        return diferenciaTiempo > 18
    

    def PuedeVotar(self):
        '''utilizar https://aceproject.org/ace-es/topics/lf/lfc/lfc24#:~:text=Art.%2070.%2D%20Los,con%20la%20Ley.'''
        


    def MiembroMesa(self):
        '''utilizar principalmete ocupacion
        Para tomarencuentaesto seconsidera la siguinte paguina. https://www.caib.es/sites/processoselectorals/es/miembros_de_las_mesas_electorales-65461/
        
        Art. 69.- Los miembros de las Juntas Receptoras del Voto tiene la obligación de asistir a los cursos o seminarios de capacitación electoral, que serán dictados por los Tribunales Provinciales Electorales.
Art. 70.- Los Tribunales Provinciales Electorales conformarán las Juntas Receptoras del Voto, de entre los ciudadanos en goce de los derechos políticos que tenga su domicilio electoral en la jurisdicción donde deba votar, con personas de comprobada capacidad e idoneidad, estudiantes que sean mayores de edad o que cumplan los 18 años un día antes de las elecciones o con miembros de las organizaciones políticas, que hubieren remitido los listados, con sesenta días de anticipación al día fijado para una elección. Pasado este plazo, el Tribunal no aceptará ternas presentadas por las organizaciones políticas, los candidatos o sus representantes, y designará las Juntas con los ciudadanos constantes en el Padrón Electoral, de conformidad con la Ley.'''
        
        pass

#  ________________________ MANEJO DE HOLIDAYS DE FECHA DE ACCESO _______________________________________    
class FeriadosTsachilas(holidays.HolidayBase):
    ''' Esta clase se encarga de definir nuevas fiestas personalisadas ante la necesidad de nosotros.\n
        recibe parametros de Holiday base para poder hacer todo lo necesario en esta clase.\n
        ------------------
        Atributos
        -----------------
        - country - el cual lo heredamos de holiday base, el cual da la forma para definir un pais.
        - provincia1 - el cual es una lista definido en la libreria builtins.pyi
        -  '''
    provincia=['EC-SD'] # guia de nuestro paso de dato 
    def __init__(self ,**lista): # será un diccionario con los argumentos ingresados, con ** hace que la función acepte infinitos argumentos, pero hay que aclarar primero el nombre del argumento.
        '''declaramos las funciones necesarias para tener nuestrosferiados a la mano'''
        self.country = 'ECU'
        self.provincia1=lista.pop('prov', 'ON')
        holidays.HolidayBase.__init__(self, **lista)

    def _populate(self, year):
        '''
            La documetacion se puede encontrar en: 
            https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
            - Cantonización de Santo Domingo: domingo 3 de julio (pasa al lunes 4)
            - Provincialización: domingo 6 de noviembre (pasa al lunes 7)
            ---------
            Parametros
            ----------
            El parametro que pasa a este metodo es el --year-- o año el cual servira para declarar nuevas fiestas con años dinamicos.
            '''

        
        self[date(2023, 2, 5)] = "La elección de autoridades seccionales en Ecuador 2023" #  los parametros son año, mes y dia. 
####_____________________________________________________________________________________________________
class Descuento:
    '''
        En esta clase es donde sucede toda la magia para condicionar los descuentos, aqui hacemos las condiciones para aplicar los datos. 
        
        Parametros
        ------------
        atributos
        ----------------
        - dia - la cual pasa el año mes y dia para saber si es feriado.
        - ApiEnLiena - la cual hacemos que pase el valor de la api y poder controlar el el error ValueError
         
         Metodos
         ------------
         - constructor - contine a los atributos.
         - dia - la cual es un decorador property el cual lo que hace es interpretar la lectura, escritura y borrado de atributos.
                 la cual podemos decir que documenta los mismos.\n 
                 Tambien esta el esta el metodo settter para esta funcion, basicamente se encarga de recibir los datos cuando se escriba.
         - __EsFiesta - este comprueba si un dia es feriado o no para poder hacer losen cuentos, en el menu principal. 
                         este es privado. 
         - ImprimirSiNo - el cual me hace es retornar true o falce, true cuando si exite el feriado y false cuando no. 
                 '''
    def __init__ (self, dia, API=False):
        '''
        este el costructor.

        parametros
        ----------
            - dia - fecha ingresada
            - consideramos la API para saver si el feriado esta en los feriados personalizados o no. 
            '''
        self.dia= dia
        self.ApiEnLinea= API

    @property # primero se define el property para envolver en una funcion al atributo con funciones o codigo que tiene el mismo.
    def dia(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._dia 
    @dia.setter ## recibe los datos cuando se escriba
    def dia(self, numValor): 
        ''' metodo para poder dar un valor al atributo dia que esta en el costructor. 
         
         Parametros
         --------------
        numValor - el cual es str 
         
         rotorna una excepcion un mensaje al encontrar el error ValueError
          '''
        try:# en este bloque es donde ejecuteremos nuestro codigo para devolver un mensaje al tener un error, en este caso ValueError.
            if len(numValor)!=10:
                raise ValueError # raice como hacer una excepcion ante este error
            datetime.strptime(numValor, '%Y-%m-%d') # tonces pasa nomas, con lo que estabas. 
        except ValueError: # este bloque se ejecutara si el bloque try nofuncina y sabremos cual es el error. 
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor # pues si no pasa normal 

    def __EsFiesta(self, date, enLinea ):
        ''' esta parte contine las condiciones para ver si hay feriado o no en un fecha indicada.
            
            parametros
            ------------
            tenemos:
            - date - el cual es la fecha que tenemos o ingresamos.
            - enLinea - el cual pasa por defecto false, es para decir que si el feriado es de la API o las personalizadas. 
            -------
            -------
            la API utilizada es:
            - abstractapi el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
            entrar con previo registro. 
            '''
        ano, maso, menos = date.split('-')
        if enLinea: # condicion si es enLinea true
            ''' 
                se importa los datos de la API conocida como abstract api
                el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
                
                (ejemplo de fechas. https://www.youtube.com/watch?v=wSLbMwNyeLs)'''
            response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=91616907df7b4e8282a475d32edfa88a&country=EC&year={ano}&month={maso}&day={menos}")
            # pera utilizar este link utilizamos requests el cual nos ayudara a conectar con la API
            print(response.status_code) # retorna en pantalla un codigo 
            print(response.content)# retorna el contenido de dicha fecha consultada
            if response.content== b'[]':# verifica si el contenido es nulo manda una lista vacia o retorna False.
                return False
            return True # pues si no retorna true
        else: # nos conecta con los feriados personalizados o creados 
            FiestasApi=FeriadosTsachilas(prov='EC-SD') # instencia o crea un objeto de la clases feriadoTschilas con un parametro el cual es la cuadad de Santo Domingo
            return date in FiestasApi # retorna true o false dependiendo si la fecha ingresada 'date' se en cunetra en los feriados creados. 
    def ImprimirSiNo(self): # funcion que decide definitivamente
        '''este metodo llama a los metodos anteriores 
        para saber si si es ferido o no

        Datos importados
        ------
        - tenemos a la fecha - esatributo de este metodo
        - y tenemos la ApiEnLienea la cual es atributo de esta clase descuento. 
        - los datos del metodo __EsFiesta - la segunda mas importante en esta clase. '''
        if self.__EsFiesta(self.dia , self.ApiEnLinea): # retorna true dependiento del metodo __EsFiesta como pregunta este reotorna true.
            return True   
        return False # pues si no nada que ver. 
#____________________________ 