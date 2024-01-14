#!/bin/bash
set -e
mkdir /home
echo creating user: maximilian_de_junious
getent passwd maximilian_de_junious > /dev/null && echo 'User maximilian_de_junious already exists. Aborting.' && exit 1 || true
groupadd de_junious
useradd -d /home/de_junious -c de_junious -m -g de_junious -G student,2CN -s /bin/bash maximilian_de_junious
echo maximilian_de_junious:i@ws[~VZvn\`\ | chpasswd
echo creating user: ramon_nunez_gomez
getent passwd ramon_nunez_gomez > /dev/null && echo 'User ramon_nunez_gomez already exists. Aborting.' && exit 1 || true
groupadd nunez_gomez
useradd -d /home/nunez_gomez -c nunez_gomez -m -g nunez_gomez -G student,3BN -s /bin/bash ramon_nunez_gomez
echo ramon_nunez_gomez:i0,?%3h@@w@B | chpasswd
echo creating user: ulku_omer_ullagoss
getent passwd ulku_omer_ullagoss > /dev/null && echo 'User ulku_omer_ullagoss already exists. Aborting.' && exit 1 || true
groupadd ullagoss
useradd -d /home/ullagoss -c ullagoss -m -g ullagoss -G student,1AN -s /bin/bash ulku_omer_ullagoss
echo ulku_omer_ullagoss:h*/l7jCIll,o | chpasswd
echo creating user: isis_lanpher
getent passwd isis_lanpher > /dev/null && echo 'User isis_lanpher already exists. Aborting.' && exit 1 || true
groupadd lanpher
useradd -d /home/lanpher -c lanpher -m -g lanpher -G student,4CN -s /bin/bash isis_lanpher
echo isis_lanpher:pOf:7xJ06|q# | chpasswd
echo creating user: maximilian_galvin
getent passwd maximilian_galvin > /dev/null && echo 'User maximilian_galvin already exists. Aborting.' && exit 1 || true
groupadd galvin
useradd -d /home/galvin -c galvin -m -g galvin -G student,2AN -s /bin/bash maximilian_galvin
echo maximilian_galvin:8K\`7f\!qLEpC | chpasswd
echo creating user: jannette_laspina
getent passwd jannette_laspina > /dev/null && echo 'User jannette_laspina already exists. Aborting.' && exit 1 || true
groupadd laspina
useradd -d /home/laspina -c laspina -m -g laspina -G student,4CN -s /bin/bash jannette_laspina
echo jannette_laspina:%;ls=jr=|kv\' | chpasswd
echo creating user: marg_dodich
getent passwd marg_dodich > /dev/null && echo 'User marg_dodich already exists. Aborting.' && exit 1 || true
groupadd dodich
useradd -d /home/dodich -c dodich -m -g dodich -G student,3CN -s /bin/bash marg_dodich
echo marg_dodich:tKcVvZ.3K}H* | chpasswd
echo creating user: carisa_bannowsky
getent passwd carisa_bannowsky > /dev/null && echo 'User carisa_bannowsky already exists. Aborting.' && exit 1 || true
groupadd bannowsky
useradd -d /home/bannowsky -c bannowsky -m -g bannowsky -G student,2AN -s /bin/bash carisa_bannowsky
echo carisa_bannowsky:T+0[;},KO_{m | chpasswd
echo creating user: david_waisath
getent passwd david_waisath > /dev/null && echo 'User david_waisath already exists. Aborting.' && exit 1 || true
groupadd waisath
useradd -d /home/waisath -c waisath -m -g waisath -G student,4CN -s /bin/bash david_waisath
echo david_waisath:wc\'bYQ?*@L{{ | chpasswd
echo creating user: paulette_von_reddigpiette
getent passwd paulette_von_reddigpiette > /dev/null && echo 'User paulette_von_reddigpiette already exists. Aborting.' && exit 1 || true
groupadd von_reddigpiette
useradd -d /home/von_reddigpiette -c von_reddigpiette -m -g von_reddigpiette -G student,2CN -s /bin/bash paulette_von_reddigpiette
echo paulette_von_reddigpiette:ly1xLQdPf6v\' | chpasswd
echo creating user: kirby_latona
getent passwd kirby_latona > /dev/null && echo 'User kirby_latona already exists. Aborting.' && exit 1 || true
groupadd latona
useradd -d /home/latona -c latona -m -g latona -G student,2AN -s /bin/bash kirby_latona
echo kirby_latona:C22+Lq&pdc#d | chpasswd
echo creating user: reed_homewood
getent passwd reed_homewood > /dev/null && echo 'User reed_homewood already exists. Aborting.' && exit 1 || true
groupadd homewood
useradd -d /home/homewood -c homewood -m -g homewood -G student,2BN -s /bin/bash reed_homewood
echo reed_homewood:SRe5Ojw8eaG[ | chpasswd
echo creating user: blair_pallaforzedian
getent passwd blair_pallaforzedian > /dev/null && echo 'User blair_pallaforzedian already exists. Aborting.' && exit 1 || true
groupadd pallaforzedian
useradd -d /home/pallaforzedian -c pallaforzedian -m -g pallaforzedian -G student,5CN -s /bin/bash blair_pallaforzedian
echo blair_pallaforzedian:krTw#M5?#Las | chpasswd
echo creating user: lon_senemounnaratquillian
getent passwd lon_senemounnaratquillian > /dev/null && echo 'User lon_senemounnaratquillian already exists. Aborting.' && exit 1 || true
groupadd senemounnaratquillian
useradd -d /home/senemounnaratquillian -c senemounnaratquillian -m -g senemounnaratquillian -G student,2CN -s /bin/bash lon_senemounnaratquillian
echo lon_senemounnaratquillian:_R1[\`2B9XD@o | chpasswd
echo creating user: vada_isaac
getent passwd vada_isaac > /dev/null && echo 'User vada_isaac already exists. Aborting.' && exit 1 || true
groupadd isaac
useradd -d /home/isaac -c isaac -m -g isaac -G student,2BN -s /bin/bash vada_isaac
echo vada_isaac:_Z]#D5JD<LGC | chpasswd
echo creating user: jeanett_plancarte
getent passwd jeanett_plancarte > /dev/null && echo 'User jeanett_plancarte already exists. Aborting.' && exit 1 || true
groupadd plancarte
useradd -d /home/plancarte -c plancarte -m -g plancarte -G student,4BN -s /bin/bash jeanett_plancarte
echo jeanett_plancarte:Kg;Gu/N?HB0C | chpasswd
echo creating user: alex_berteottistirn
getent passwd alex_berteottistirn > /dev/null && echo 'User alex_berteottistirn already exists. Aborting.' && exit 1 || true
groupadd berteottistirn
useradd -d /home/berteottistirn -c berteottistirn -m -g berteottistirn -G teacher,None -s /bin/bash alex_berteottistirn
echo alex_berteottistirn:Aqzt>^aS3~/o | chpasswd
echo creating user: robyn_strycker
getent passwd robyn_strycker > /dev/null && echo 'User robyn_strycker already exists. Aborting.' && exit 1 || true
groupadd strycker
useradd -d /home/strycker -c strycker -m -g strycker -G student,3AN -s /bin/bash robyn_strycker
echo robyn_strycker:0(TNBsj>R3\_ | chpasswd
echo creating user: camille_von_verrill
getent passwd camille_von_verrill > /dev/null && echo 'User camille_von_verrill already exists. Aborting.' && exit 1 || true
groupadd von_verrill
useradd -d /home/von_verrill -c von_verrill -m -g von_verrill -G student,3BN -s /bin/bash camille_von_verrill
echo camille_von_verrill::\"j3h<S#kXc2 | chpasswd
echo creating user: franz_michael_leopold_deschner
getent passwd franz_michael_leopold_deschner > /dev/null && echo 'User franz_michael_leopold_deschner already exists. Aborting.' && exit 1 || true
groupadd deschner
useradd -d /home/deschner -c deschner -m -g deschner -G student,4CN -s /bin/bash franz_michael_leopold_deschner
echo franz_michael_leopold_deschner:ordiC)ksvb?g | chpasswd
echo creating user: veola_franzi
getent passwd veola_franzi > /dev/null && echo 'User veola_franzi already exists. Aborting.' && exit 1 || true
groupadd franzi
useradd -d /home/franzi -c franzi -m -g franzi -G teacher,None -s /bin/bash veola_franzi
echo veola_franzi:%{OR\"P)+AU{e | chpasswd
echo creating user: chantelle_cringle
getent passwd chantelle_cringle > /dev/null && echo 'User chantelle_cringle already exists. Aborting.' && exit 1 || true
groupadd cringle
useradd -d /home/cringle -c cringle -m -g cringle -G student,3CN -s /bin/bash chantelle_cringle
echo chantelle_cringle:$}NwWIrRQvFR | chpasswd
echo creating user: britney_kosh
getent passwd britney_kosh > /dev/null && echo 'User britney_kosh already exists. Aborting.' && exit 1 || true
groupadd kosh
useradd -d /home/kosh -c kosh -m -g kosh -G student,5BN -s /bin/bash britney_kosh
echo britney_kosh:-FG54y<!~c\Z | chpasswd
echo creating user: clayton_derouchie
getent passwd clayton_derouchie > /dev/null && echo 'User clayton_derouchie already exists. Aborting.' && exit 1 || true
groupadd derouchie
useradd -d /home/derouchie -c derouchie -m -g derouchie -G student,4BN -s /bin/bash clayton_derouchie
echo clayton_derouchie:ACPjtfXaQK)Z | chpasswd
echo creating user: beverlee_doutt
getent passwd beverlee_doutt > /dev/null && echo 'User beverlee_doutt already exists. Aborting.' && exit 1 || true
groupadd doutt
useradd -d /home/doutt -c doutt -m -g doutt -G student,5BN -s /bin/bash beverlee_doutt
echo beverlee_doutt:@TuE0Y/;#9\`y | chpasswd
echo creating user: alma_munley
getent passwd alma_munley > /dev/null && echo 'User alma_munley already exists. Aborting.' && exit 1 || true
groupadd munley
useradd -d /home/munley -c munley -m -g munley -G student,1BN -s /bin/bash alma_munley
echo alma_munley:{V<s2<xF\')tU | chpasswd
echo creating user: thad_dornbos
getent passwd thad_dornbos > /dev/null && echo 'User thad_dornbos already exists. Aborting.' && exit 1 || true
groupadd dornbos
useradd -d /home/dornbos -c dornbos -m -g dornbos -G student,5AN -s /bin/bash thad_dornbos
echo thad_dornbos:8yu+}5rTR#s~ | chpasswd
echo creating user: arvilla_mahala
getent passwd arvilla_mahala > /dev/null && echo 'User arvilla_mahala already exists. Aborting.' && exit 1 || true
groupadd mahala
useradd -d /home/mahala -c mahala -m -g mahala -G student,2CN -s /bin/bash arvilla_mahala
echo arvilla_mahala:~O<guRY\'5\`\6 | chpasswd
echo creating user: mirza_ellingwood
getent passwd mirza_ellingwood > /dev/null && echo 'User mirza_ellingwood already exists. Aborting.' && exit 1 || true
groupadd ellingwood
useradd -d /home/ellingwood -c ellingwood -m -g ellingwood -G teacher,None -s /bin/bash mirza_ellingwood
echo mirza_ellingwood:~H&~\`T3\\`Vcv | chpasswd
echo creating user: francie_de_cardinallisciola
getent passwd francie_de_cardinallisciola > /dev/null && echo 'User francie_de_cardinallisciola already exists. Aborting.' && exit 1 || true
groupadd de_cardinallisciola
useradd -d /home/de_cardinallisciola -c de_cardinallisciola -m -g de_cardinallisciola -G student,3AN -s /bin/bash francie_de_cardinallisciola
echo francie_de_cardinallisciola:(Jk-=:=?diVS | chpasswd
echo creating user: irenee_gundry
getent passwd irenee_gundry > /dev/null && echo 'User irenee_gundry already exists. Aborting.' && exit 1 || true
groupadd gundry
useradd -d /home/gundry -c gundry -m -g gundry -G teacher,None -s /bin/bash irenee_gundry
echo irenee_gundry:/V=mC8$iUJQ0 | chpasswd
echo creating user: irenee_pinedo
getent passwd irenee_pinedo > /dev/null && echo 'User irenee_pinedo already exists. Aborting.' && exit 1 || true
groupadd pinedo
useradd -d /home/pinedo -c pinedo -m -g pinedo -G student,3CN -s /bin/bash irenee_pinedo
echo irenee_pinedo:y\'Yv29U/fU\`t | chpasswd
echo creating user: chelah_faivre
getent passwd chelah_faivre > /dev/null && echo 'User chelah_faivre already exists. Aborting.' && exit 1 || true
groupadd faivre
useradd -d /home/faivre -c faivre -m -g faivre -G student,2CN -s /bin/bash chelah_faivre
echo chelah_faivre:65Il%]!aRCky | chpasswd
echo creating user: mirza_pinsky
getent passwd mirza_pinsky > /dev/null && echo 'User mirza_pinsky already exists. Aborting.' && exit 1 || true
groupadd pinsky
useradd -d /home/pinsky -c pinsky -m -g pinsky -G student,1BN -s /bin/bash mirza_pinsky
echo mirza_pinsky:L\"0L<qBB59W\" | chpasswd
echo creating user: francie_pinsky1
getent passwd francie_pinsky1 > /dev/null && echo 'User francie_pinsky1 already exists. Aborting.' && exit 1 || true
groupadd pinsky1
useradd -d /home/pinsky1 -c pinsky1 -m -g pinsky1 -G student,1BN -s /bin/bash francie_pinsky1
echo francie_pinsky1:CIFD,oDqx}Wz | chpasswd
echo creating user: goldie_pinsky2
getent passwd goldie_pinsky2 > /dev/null && echo 'User goldie_pinsky2 already exists. Aborting.' && exit 1 || true
groupadd pinsky2
useradd -d /home/pinsky2 -c pinsky2 -m -g pinsky2 -G student,1BN -s /bin/bash goldie_pinsky2
echo goldie_pinsky2:@e;Zqd,Yavlh | chpasswd
echo creating user: another_pinsky3
getent passwd another_pinsky3 > /dev/null && echo 'User another_pinsky3 already exists. Aborting.' && exit 1 || true
groupadd pinsky3
useradd -d /home/pinsky3 -c pinsky3 -m -g pinsky3 -G student,1BN -s /bin/bash another_pinsky3
echo another_pinsky3:=G=>VNgKI=zo | chpasswd
echo creating user: andromede_norlien
getent passwd andromede_norlien > /dev/null && echo 'User andromede_norlien already exists. Aborting.' && exit 1 || true
groupadd norlien
useradd -d /home/norlien -c norlien -m -g norlien -G student,2AN -s /bin/bash andromede_norlien
echo andromede_norlien:6A~]<$ErK4wo | chpasswd
echo creating user: helaah_preato
getent passwd helaah_preato > /dev/null && echo 'User helaah_preato already exists. Aborting.' && exit 1 || true
groupadd preato
useradd -d /home/preato -c preato -m -g preato -G student,1BN -s /bin/bash helaah_preato
echo helaah_preato:K1rgPZ\"w$\"0# | chpasswd
