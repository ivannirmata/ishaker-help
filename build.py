#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор статичного сайта iShaker Help (RU + EN) — 30 тем, полный текст.
Запуск: python3 build.py  → генерирует index.html, ru/*.html, en/*.html, assets/style.css
Черновик для внутреннего ревью перед публикацией на публичной вики.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

STYLE = """body{font-family:-apple-system,'Segoe UI',Roboto,sans-serif;background:#fff;color:#1a1a1a;margin:0;}
.wrap{max-width:840px;margin:0 auto;padding:32px 24px 96px;}
.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;font-size:15px;}
.home{color:#1a73e8;text-decoration:none;font-weight:600;}
.lang{color:#1a56b0;background:#e8f0fe;border-radius:12px;padding:4px 12px;text-decoration:none;font-weight:600;}
h1{font-size:34px;line-height:1.18;margin:0 0 16px;}
h2{font-size:23px;margin:34px 0 12px;border-bottom:2px solid #eee;padding-bottom:6px;}
p,li{font-size:17px;line-height:1.65;}
ol li,ul li{margin-bottom:8px;}
figure{margin:24px 0;text-align:center;}
figure img{max-width:100%;height:auto;border:1px solid #e5e5e5;border-radius:8px;}
figcaption{font-size:14px;color:#777;margin-top:8px;}
.note{background:#fff8e1;border-left:4px solid #f4b400;padding:12px 16px;font-size:15px;color:#6b5900;border-radius:0 8px 8px 0;margin:20px 0;}
.badge{display:inline-block;background:#e8f0fe;color:#1a56b0;font-size:13px;padding:3px 10px;border-radius:12px;margin-bottom:16px;}
.foot{color:#999;font-size:13px;margin-top:20px;}
hr{border:none;border-top:1px solid #eee;margin:40px 0 0;}
a{color:#1a73e8;}
.subtitle{font-size:18px;color:#555;margin:0 0 8px;line-height:1.5;}
.prio{font-size:22px;margin:34px 0 6px;}
.arts{list-style:none;padding:0;margin:0;}
.arts li{display:flex;justify-content:space-between;gap:16px;padding:11px 0;border-bottom:1px solid #f0f0f0;font-size:17px;align-items:baseline;}
.arts .t{flex:1;}
.arts .links{white-space:nowrap;}
.arts .links a{margin-left:10px;font-weight:600;}
"""

def page(lang, title, body, other_href):
    other = "EN" if lang == "ru" else "RU"
    switch = '<a class="lang" href="%s">%s</a>' % (other_href, other)
    return """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — iShaker Help</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<div class="wrap">
<div class="topbar"><a class="home" href="../index.html">← iShaker Help</a>%s</div>
<h1>%s</h1>
%s
<hr>
<p class="foot">Draft / черновик — для внутреннего ревью перед публикацией. iShaker USA.</p>
</div>
</body>
</html>""" % (lang, title, switch, title, body)

def rootpage(title, body, badge=""):
    return """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s — iShaker Help</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">
<div class="topbar"><a class="home" href="index.html">← iShaker Help</a></div>
%s<h1>%s</h1>
%s
<hr>
<p class="foot">iShaker USA — внутренний гайд для авторов.</p>
</div>
</body>
</html>""" % (title, badge, title, body)

ARTICLES = [
# ---------------------- Приоритет 1 ----------------------
{"num":1,"prio":1,"slug":"01-machine-offline-wifi",
 "ru_title":"Машина офлайн / WiFi отваливается","en_title":"Machine offline / WiFi keeps disconnecting",
 "ru":"""<p>Если вверху панели телеметрии появилась жёлтая полоса или значок «?», машина <strong>не на связи с сервером</strong>. Важно: продажи при этом обычно продолжаются — оплата картой идёт по своей линии (Nayax), а продажи копятся локально и подгружаются позже. <strong>Офлайн ≠ остановка продаж.</strong></p>
<h2>Почему пропадает связь</h2>
<p>Чаще всего — слабый или перегруженный WiFi, перезагрузка роутера, смена пароля сети или большое расстояние до точки.</p>
<h2>Что проверить</h2>
<ol>
<li>Убедитесь, что интернет работает — откройте любой сайт на телефоне, подключённом к той же сети.</li>
<li>Перезагрузите роутер и подождите 2–3 минуты.</li>
<li>На машине откройте виджет «Интернет» / WiFi и переподключитесь к сети (пароль сохранён, но иногда нужно выбрать сеть заново).</li>
<li>Если есть возможность — подключите машину кабелем Ethernet: проводное соединение обычно стабильнее WiFi.</li>
</ol>
<div class="note">На Touch 2 меню WiFi открывается поверх витрины и как будто «закрывает экран» — это нормально. После подключения вернитесь назад.</div>
<p>Обычно этого достаточно. Если после перезапуска роутера и переподключения машина всё ещё офлайн — пришлите нам фото экрана статуса, и мы подскажем следующий шаг.</p>""",
 "en":"""<p>A yellow bar or a “?” icon at the top of the telemetry dashboard means the machine is <strong>not connected to the server</strong>. Note: sales usually keep working — card payments run on their own line (Nayax) and sales are stored locally and uploaded later. <strong>Offline does not mean sales are stopped.</strong></p>
<h2>Why the connection drops</h2>
<p>Most often it is a weak or overloaded WiFi, a router reboot, a changed WiFi password, or too much distance to the access point.</p>
<h2>What to check</h2>
<ol>
<li>Confirm the internet works — open any website on a phone connected to the same network.</li>
<li>Restart the router and wait 2–3 minutes.</li>
<li>On the machine, open the “Internet” / WiFi widget and reconnect to the network (the password is saved, but sometimes you need to pick the network again).</li>
<li>If possible, connect the machine with an Ethernet cable — a wired link is usually more stable than WiFi.</li>
</ol>
<div class="note">On Touch 2 the WiFi menu opens over the storefront and seems to “cover the screen” — that is normal. Go back after connecting.</div>
<p>This is usually enough. If the machine is still offline after restarting the router and reconnecting, send us a photo of the status screen and we will guide you through the next step.</p>"""},
{"num":2,"prio":1,"slug":"02-add-your-own-flavor",
 "ru_title":"Как завести свой порошок / вкус","en_title":"Adding your own powder / flavor",
 "ru":"""<p>Часть шагов вы делаете сами, а регистрацию совсем нового продукта — через нас.</p>
<h2>Что вы делаете сами</h2>
<p>Если нужный вкус уже есть в каталоге машины: назначаете его на слот, задаёте цену и дозировку, калибруете слот. Как назначать вкус — см. «Новый вкус не появился после Update Database»; как калибровать — см. «Доза порошка неверная / калибровка».</p>
<h2>Что присылаете нам</h2>
<p>Если продукта или бренда в системе ещё нет — мы его регистрируем и добавляем иконку/название. Пришлите:</p>
<ul>
<li>фото лицевой стороны банки;</li>
<li>фото панели состава (supplement / nutrition facts);</li>
<li>бренд и точное название вкуса.</li>
</ul>
<p>После регистрации продукт появится у вас в каталоге, и его можно будет назначить на слот.</p>
<h2>После добавления — на машине</h2>
<ol>
<li>Service Mode → Configurator → Change Drinks → <strong>Update Database From Server</strong>.</li>
<li>Назначьте вкус на нужный слот → Save.</li>
<li>Controller Reboot.</li>
<li>Откалибруйте слот (см. страницу про калибровку).</li>
</ol>
<div class="note">Если после этого вкус показан как «taste.xxx» или белым квадратом — иконка/название ещё не подтянулись. Напишите нам, поправим; обычно помогает повторный Update Database после нашей правки.</div>""",
 "en":"""<p>You do some steps yourself; registering a brand-new product goes through us.</p>
<h2>What you do yourself</h2>
<p>If the flavor is already in the machine catalog: assign it to a slot, set the price and dosage, and calibrate the slot. To assign a flavor see “New flavor doesn’t appear after Update Database”; to calibrate see “Powder dose is wrong / calibration”.</p>
<h2>What you send us</h2>
<p>If the product or brand is not in the system yet, we register it and add the icon/name. Please send:</p>
<ul>
<li>a photo of the front of the container;</li>
<li>a photo of the supplement / nutrition facts panel;</li>
<li>the brand and the exact flavor name.</li>
</ul>
<p>After we register it, the product appears in your catalog and you can assign it to a slot.</p>
<h2>After it is added — on the machine</h2>
<ol>
<li>Service Mode → Configurator → Change Drinks → <strong>Update Database From Server</strong>.</li>
<li>Assign the flavor to the slot → Save.</li>
<li>Controller Reboot.</li>
<li>Calibrate the slot (see the calibration page).</li>
</ol>
<div class="note">If the flavor shows as “taste.xxx” or a white square, the icon/name hasn’t synced yet. Message us and we’ll fix it; a second Update Database after our fix usually resolves it.</div>""",
 "img":"update-database.jpg","cap_ru":"Экран Controller Configuration: бренд, продукт и вкус по слотам.","cap_en":"Controller Configuration screen: brand, product and taste per slot."},
{"num":3,"prio":1,"slug":"03-flavor-not-showing-after-update",
 "ru_title":"Новый вкус не появился после «Update Database»","en_title":"New flavor doesn’t appear after “Update Database”",
 "ru":"""<h2>Полный путь синхронизации</h2>
<ol>
<li>Service Mode → Configurator → <strong>Change Drinks</strong>.</li>
<li>Нажмите <strong>Update Database From Server</strong> и дождитесь загрузки.</li>
<li>Назначьте вкус на нужный слот → <strong>Save</strong>.</li>
<li><strong>Controller Reboot</strong>.</li>
</ol>
<h2>Почему вкус может не появиться</h2>
<ul>
<li>Не нажали <strong>Update Database From Server</strong> — без этого локальный каталог не обновляется.</li>
<li>Не сделали Controller Reboot после Save.</li>
<li>Продукт ещё не зарегистрирован у нас — пришлите фото банки и состава (см. «Как завести свой порошок / вкус»).</li>
<li>Не совпала категория/вид напитка — проверьте, что выбрана правильная категория.</li>
</ul>
<div class="note">Если после Update Database и перезагрузки вкус всё равно не виден или показан как «taste.xxx» / белым квадратом — напишите нам, поправим на своей стороне.</div>""",
 "en":"""<h2>Full sync path</h2>
<ol>
<li>Service Mode → Configurator → <strong>Change Drinks</strong>.</li>
<li>Tap <strong>Update Database From Server</strong> and wait for it to finish.</li>
<li>Assign the flavor to the slot → <strong>Save</strong>.</li>
<li><strong>Controller Reboot</strong>.</li>
</ol>
<h2>Why a flavor may not appear</h2>
<ul>
<li>“Update Database From Server” wasn’t tapped — the local catalog won’t refresh without it.</li>
<li>No Controller Reboot after Save.</li>
<li>The product isn’t registered on our side yet — send a photo of the container and facts panel (see “Adding your own powder / flavor”).</li>
<li>The drink category/type doesn’t match — check that the correct category is selected.</li>
</ul>
<div class="note">If after Update Database and a reboot the flavor still doesn’t show, or shows as “taste.xxx” / a white square, message us and we’ll fix it on our side.</div>""",
 "img":"update-database.jpg","cap_ru":"Кнопка «Update DataBase From Server» на экране конфигурации.","cap_en":"The “Update DataBase From Server” button on the configuration screen."},
{"num":4,"prio":1,"slug":"04-powder-dose-calibration",
 "ru_title":"Доза порошка неверная (ставлю 30 г — выходит 15 г)","en_title":"Powder dose is wrong (set 30 g, get 15 g)",
 "ru":"""<p>Если вы задаёте одну дозу порошка, а по факту выходит меньше (или шейк слишком жидкий) — почти всегда дело в калибровке и в правиле рецепта.</p>
<h2>Почему в калибровке норма, а в продаже меньше</h2>
<p>В режиме калибровки и в обычной продаже подача порошка может немного отличаться (взаимная синхронизация насоса и шнека, время пролива). Поэтому калибровку всегда проверяйте в обычном режиме продажи, а не только в калибровочном.</p>
<h2>Правило рецепта</h2>
<ul>
<li>Объём напитка должен быть <strong>≥ вода + порошок</strong>.</li>
<li>Соотношение вода : порошок примерно <strong>1 : 5</strong> — рабочая зона.</li>
<li>Слишком мало воды → перелив или машина игнорирует настройку.</li>
</ul>
<h2>Калибровка кухонными весами</h2>
<ol>
<li>Запустите выдачу порошка в стакан на весах.</li>
<li>Взвесьте фактическую выдачу.</li>
<li>Введите фактическое значение в Service Mode и сохраните.</li>
<li>Повторите 2–3 раза, пока не окажетесь в пределах <strong>±1.5 г</strong> от цели (для воды — ±10 мл).</li>
</ol>
<h2>Когда калибровать заново</h2>
<p>При загрузке нового порошка или смене бренда — да. При простой смене вкуса того же типа — обычно не требуется.</p>
<div class="note"><strong>Безопасность.</strong> Для энергетиков, преворкаутов, EAA и креатина не превышайте суточную норму с упаковки. Если вкус кажется слабым — снижайте воду, а не повышайте порошок.</div>
<p>Если после калибровки выдача в продаже всё равно занижена — напишите нам, посмотрим; иногда требуется настройка на нашей стороне.</p>""",
 "en":"""<p>If you set one powder dose but get less in the cup (or the shake is too watery), it’s almost always about calibration and the recipe rule.</p>
<h2>Why calibration looks right but purchase gives less</h2>
<p>Powder delivery can differ slightly between calibration mode and a normal purchase (how the pump and auger sync, and the pour time). Always verify a calibration with a normal purchase, not only in calibration mode.</p>
<h2>Recipe rule</h2>
<ul>
<li>Drink volume must be <strong>≥ water + powder</strong>.</li>
<li>Water : powder around <strong>1 : 5</strong> is the working zone.</li>
<li>Too little water → overflow or the machine ignores the setting.</li>
</ul>
<h2>Calibrating with a kitchen scale</h2>
<ol>
<li>Dispense powder into a cup on the scale.</li>
<li>Weigh the actual delivery.</li>
<li>Enter the actual value in Service Mode and save.</li>
<li>Repeat 2–3 times until within <strong>±1.5 g</strong> of the target (for water, ±10 ml).</li>
</ol>
<h2>When to re-calibrate</h2>
<p>When loading a new powder or switching brands — yes. For a simple flavor swap of the same type — usually not needed.</p>
<div class="note"><strong>Safety.</strong> For energy, pre-workout, EAA and creatine, never exceed the daily serving on the label. If a flavor seems weak, reduce water — do not increase powder.</div>
<p>If purchase delivery is still low after calibration, message us — sometimes a tweak is needed on our side.</p>"""},
{"num":5,"prio":1,"slug":"05-after-update-checklist",
 "ru_title":"Что проверить после обновления ПО","en_title":"What to check after a software update",
 "ru":"""<p>После того как ПО машины обновили удалённо, пробегитесь по этому короткому чек-листу.</p>
<h2>Проверьте эти 5 вещей</h2>
<ol>
<li><strong>Цены.</strong> Иногда сбрасываются на значение по умолчанию (например $100). Проверьте цену каждого напитка.</li>
<li><strong>Уровень воды.</strong> Может показать «∞» или сброситься — введите текущий уровень (см. «Вода показывает ∞ / долив»).</li>
<li><strong>Остатки порошка.</strong> Могут обнулиться — введите текущие остатки при ближайшем пополнении.</li>
<li><strong>Дозировки.</strong> Проверьте, что дозы напитков на месте и корректны.</li>
<li><strong>Режим.</strong> Убедитесь, что машина вышла из сервисного режима (жёлтая полоса убрана) и стоит на витрине.</li>
</ol>
<div class="note">Если что-то выглядит не так после обновления — пришлите фото, поправим.</div>""",
 "en":"""<p>After the machine’s software is updated remotely, run through this short checklist.</p>
<h2>Check these 5 things</h2>
<ol>
<li><strong>Prices.</strong> They sometimes reset to a default (e.g. $100). Check the price of every drink.</li>
<li><strong>Water level.</strong> May show “∞” or reset — enter the current level (see “Water shows ∞ / refilling”).</li>
<li><strong>Powder inventory.</strong> May reset to zero — enter the current amounts at the next refill.</li>
<li><strong>Dosages.</strong> Confirm the drink doses are present and correct.</li>
<li><strong>Mode.</strong> Make sure the machine left service mode (no yellow bar) and is back on the storefront.</li>
</ol>
<div class="note">If something looks off after an update, send a photo and we’ll fix it.</div>"""},
{"num":6,"prio":1,"slug":"06-water-refill-reset-gauge",
 "ru_title":"Вода показывает ∞ / долив и сброс уровня после замены бутыли","en_title":"Water shows ∞ / refilling and resetting the gauge after a bottle swap",
 "ru":"""<h2>После замены бутыли вода не идёт</h2>
<p>Скорее всего в линии воздух. Выгоните его: Service Menu → <strong>Pumping water</strong> (прокачка), пока вода не пойдёт ровно. Перезагружать машину для этого не нужно.</p>
<h2>Значок воды показывает «∞»</h2>
<p>После обновления счётчик остатка воды мог не перенестись — задайте значение вручную.</p>
<ul>
<li><strong>Shaker S:</strong> в Service Menu иконки уровня (бутыль / стаканы / порошок) кликабельны — нажмите на иконку воды и задайте текущий уровень.</li>
<li><strong>Другие модели:</strong> через раздел остатков (Inventory / Remains).</li>
</ul>
<div class="note">Машина считает только расход — фактический остаток вводится вручную при пополнении. Если после ввода значение снова «плывёт» — напишите нам.</div>""",
 "en":"""<h2>No water after replacing the bottle</h2>
<p>There’s likely air in the line. Purge it: Service Menu → <strong>Pumping water</strong> until water flows steadily. You don’t need to reboot the machine for this.</p>
<h2>The water icon shows “∞”</h2>
<p>After an update the water level counter may not have carried over — set the value manually.</p>
<ul>
<li><strong>Shaker S:</strong> in the Service Menu the level icons (bottle / cups / powder) are tappable — tap the water icon and set the current level.</li>
<li><strong>Other models:</strong> via the Inventory / Remains section.</li>
</ul>
<div class="note">The machine only counts consumption — the actual remaining amount is entered manually at refill. If the value keeps drifting after you set it, message us.</div>""",
 "img":"service-pumping-water.jpg","cap_ru":"Сервисное меню: кнопка «Pumping water»; уровень воды здесь показан как ∞.","cap_en":"Service menu: the “Pumping water” button; the water level here shows as ∞."},
{"num":7,"prio":1,"slug":"07-screen-frozen-recovery",
 "ru_title":"Экран завис / застрял на 100% / не реагирует","en_title":"Screen frozen / stuck at 100% / not responding",
 "ru":"""<p>Если экран завис, застрял на «100%» при приготовлении или не реагирует на касания — вот что можно сделать самому, безопасно.</p>
<h2>Шаги восстановления</h2>
<ol>
<li>Подождите 2–3 минуты — иногда машина доготавливает и отвисает сама.</li>
<li>Выключите машину тумблером сзади примерно на 60 секунд, затем включите. Дайте 2–3 минуты на полную загрузку.</li>
<li>Если касания не работают, но нужно закрыть зависшее приложение — подключите USB-клавиатуру и нажмите <strong>Alt+F4</strong>, затем дайте машине загрузиться.</li>
</ol>
<div class="note">Не выдёргивайте питание во время приготовления без необходимости. Дайте машине полностью загрузиться перед проверкой (2–3 минуты).</div>
<p>Если зависания повторяются регулярно — пришлите нам фото/видео и примерное время, когда это происходит, и мы посмотрим причину.</p>""",
 "en":"""<p>If the screen freezes, gets stuck at “100%” while making a drink, or doesn’t respond to touch — here’s what you can safely do yourself.</p>
<h2>Recovery steps</h2>
<ol>
<li>Wait 2–3 minutes — the machine sometimes finishes and recovers on its own.</li>
<li>Switch the machine off with the rear switch for about 60 seconds, then on. Allow 2–3 minutes to fully boot.</li>
<li>If touch doesn’t work but you need to close a frozen app — connect a USB keyboard and press <strong>Alt+F4</strong>, then let the machine boot.</li>
</ol>
<div class="note">Avoid pulling power during a drink unless necessary. Let the machine boot fully before checking (2–3 minutes).</div>
<p>If freezes keep happening, send us a photo/video and roughly when it occurs, and we’ll look into the cause.</p>"""},
{"num":8,"prio":1,"slug":"08-first-time-setup",
 "ru_title":"Чек-лист первого запуска — от доставки до первой продажи","en_title":"First-time setup checklist — from delivery to first sale",
 "ru":"""<p>Короткий порядок действий при установке новой машины. По каждому пункту есть отдельная страница со деталями.</p>
<ol>
<li><strong>Распаковка и питание.</strong> Включите машину тумблером сзади, дождитесь загрузки.</li>
<li><strong>Серийный номер.</strong> Найдите S/N (на двери сзади) — понадобится для поддержки и регистрации.</li>
<li><strong>Интернет.</strong> Подключите WiFi или Ethernet (см. «Машина офлайн / WiFi»).</li>
<li><strong>Регистрация в телеметрии.</strong> Пройдите по ссылке, которую мы пришлём. Сначала интернет, потом код.</li>
<li><strong>Стаканы.</strong> Загрузите стаканы и проверьте выдачу.</li>
<li><strong>Вода.</strong> Выберите источник (бутыль или водопровод) и прокачайте линию (см. «Вода / долив»).</li>
<li><strong>Nayax.</strong> Подключите и настройте платёжный терминал.</li>
<li><strong>Напитки.</strong> Проверьте каталог, цены и дозы; откалибруйте слоты (см. «Калибровка»).</li>
</ol>
<div class="note">Если на любом шаге что-то идёт не так — пришлите фото экрана, подскажем.</div>""",
 "en":"""<p>A short order of steps when installing a new machine. Each item has its own detailed page.</p>
<ol>
<li><strong>Unpack and power on.</strong> Turn the machine on with the rear switch and wait for it to boot.</li>
<li><strong>Serial number.</strong> Find the S/N (on the rear of the door) — you’ll need it for support and registration.</li>
<li><strong>Internet.</strong> Connect WiFi or Ethernet (see “Machine offline / WiFi”).</li>
<li><strong>Telemetry registration.</strong> Follow the link we send. Internet first, then the code.</li>
<li><strong>Cups.</strong> Load cups and test dispensing.</li>
<li><strong>Water.</strong> Choose the source (bottle or mains) and prime the line (see “Water / refilling”).</li>
<li><strong>Nayax.</strong> Connect and configure the payment terminal.</li>
<li><strong>Drinks.</strong> Check the catalog, prices and doses; calibrate the slots (see “Calibration”).</li>
</ol>
<div class="note">If anything goes wrong at any step, send a photo of the screen and we’ll help.</div>"""},
{"num":9,"prio":1,"slug":"09-nayax-cashless-out-of-order",
 "ru_title":"Nayax «Cashless Out of Order» (M00 / V00 / V01)","en_title":"Nayax “Cashless Out of Order” (M00 / V00 / V01)",
 "ru":"""<p>Если платёжный терминал Nayax пишет «Cashless Out of Order» с кодом M00, V00 или V01 — обычно это потеря связи между терминалом и машиной по MDB-кабелю, а не поломка самого Nayax.</p>
<h2>Что проверить</h2>
<ol>
<li>Перезапустите <strong>только платёжный терминал</strong> (не выключая машину) — часто восстанавливает связь.</li>
<li>Проверьте MDB-кабель терминала: плотно ли он вставлен, и есть ли на терминале питание.</li>
<li>Проверьте, что у машины есть интернет — для онлайн-функций терминала.</li>
<li>Если у машины при этом ошибка воды или приготовления — терминал может уходить в ошибку заодно; сначала устраните основную проблему.</li>
</ol>
<div class="note">Настройка терминала (подключение к MDB) описана на странице «Machine settings for the NAYAX terminal» — эта страница про восстановление связи, а не про первичную настройку.</div>
<p>Если связь не поднимается — сообщите нам серийный номер ридера, посмотрим на стороне Nayax.</p>""",
 "en":"""<p>If the Nayax terminal shows “Cashless Out of Order” with code M00, V00 or V01, it’s usually a lost link between the terminal and the machine over the MDB cable — not a failure of the Nayax unit itself.</p>
<h2>What to check</h2>
<ol>
<li>Restart <strong>only the payment terminal</strong> (without turning the machine off) — this often restores the link.</li>
<li>Check the terminal’s MDB cable: is it seated firmly, and does the terminal have power?</li>
<li>Confirm the machine has internet — for the terminal’s online functions.</li>
<li>If the machine also has a water or brewing error, the terminal may fault along with it; fix the main problem first.</li>
</ol>
<div class="note">Terminal configuration (MDB connection) is on the “Machine settings for the NAYAX terminal” page — this page is about restoring the link, not the initial setup.</div>
<p>If the link won’t come back, send us the reader’s serial number and we’ll check on the Nayax side.</p>"""},
{"num":10,"prio":1,"slug":"10-service-menu-touch-2",
 "ru_title":"Сервисное меню — Touch 2","en_title":"Service menu — Touch 2",
 "ru":"""<p>Как войти в сервисное меню Touch 2, где что находится и как безопасно выйти. Пути ниже — общий ориентир; точные названия вкладок и скриншоты добавим по факту с машины.</p>
<h2>Вход</h2>
<p>Вход в сервисный режим — через сервисную авторизацию (QR / сервисный доступ). После входа доступны основные разделы управления.</p>
<h2>Основные разделы</h2>
<ul>
<li><strong>Change Drinks / ассортимент</strong> — какие вкусы на каких слотах; здесь же <strong>Update Database From Server</strong>.</li>
<li><strong>Dosages / дозировки</strong> — дозы воды и порошка по напиткам.</li>
<li><strong>Configurator / настройки</strong> — конфигурация машины.</li>
<li><strong>Wash / мойка</strong> — промывка миксера.</li>
</ul>
<h2>Перед уходом</h2>
<div class="note">Обязательно выйдите из сервисного режима перед тем, как оставить машину. Если этого не сделать, на дашборде будет жёлтая полоса (сервисный режим), и продажи будут стоять.</div>
<p>[Скриншоты вкладок будут добавлены с реальной Touch 2.]</p>""",
 "en":"""<p>How to enter the Touch 2 service menu, where things are, and how to exit safely. The paths below are a general guide; exact tab names and screenshots will be added from the machine.</p>
<h2>Entry</h2>
<p>Enter service mode via service authorization (QR / service access). Once in, the main management sections are available.</p>
<h2>Main sections</h2>
<ul>
<li><strong>Change Drinks / assortment</strong> — which flavors are on which slots; also <strong>Update Database From Server</strong>.</li>
<li><strong>Dosages</strong> — water and powder doses per drink.</li>
<li><strong>Configurator</strong> — machine configuration.</li>
<li><strong>Wash</strong> — mixer rinse.</li>
</ul>
<h2>Before you leave</h2>
<div class="note">Always exit service mode before leaving the machine. If you don’t, the dashboard shows a yellow bar (service mode) and sales are paused.</div>
<p>[Tab screenshots will be added from an actual Touch 2.]</p>"""},
# ---------------------- Приоритет 2 ----------------------
{"num":11,"prio":2,"slug":"11-telemetry-dashboard",
 "ru_title":"Как читать дашборд телеметрии","en_title":"Reading the telemetry dashboard",
 "ru":"""<p>Дашборд показывает статус машины и продажи. Ниже — как его читать, чтобы не путать «нет связи» с «нет продаж».</p>
<h2>Иконки статуса</h2>
<p>Вверху — состояние по каналам: <strong>WiFi</strong> (связь с сервером), <strong>MDB</strong> (платёжный терминал), <strong>Hardware</strong> (машина). Зелёный — норма, жёлтый/красный — проблема по этому каналу.</p>
<h2>WiFi off ≠ нет продаж</h2>
<p>Даже без связи с сервером оплата картой обычно идёт (Nayax по своей линии), а продажи копятся локально и подгружаются позже. Ноль продаж на дашборде при живой машине — смотрите отдельно MDB / экран / сервисный режим.</p>
<h2>Downtime и проценты</h2>
<p>Downtime и большие проценты — это <strong>сумма за период</strong> (по умолчанию неделя), а не «прямо сейчас». Скачок процента — накопленное за окно, не текущее состояние.</p>
<div class="note">Жёлтая полоса = машина в сервисном режиме (продажи стоят). Прочерк вместо названия вкуса в продажах = продажа прошла офлайн; детализация может подтянуться позже или быть недоступна.</div>""",
 "en":"""<p>The dashboard shows machine status and sales. Here’s how to read it so you don’t confuse “no connection” with “no sales”.</p>
<h2>Status icons</h2>
<p>At the top are the channels: <strong>WiFi</strong> (server link), <strong>MDB</strong> (payment terminal), <strong>Hardware</strong> (machine). Green is fine; yellow/red means a problem on that channel.</p>
<h2>WiFi off ≠ no sales</h2>
<p>Even without a server link, card payments usually work (Nayax on its own line) and sales accumulate locally and upload later. Zero sales with a live machine — check MDB / the screen / service mode separately.</p>
<h2>Downtime and percentages</h2>
<p>Downtime and big percentages are a <strong>total for the period</strong> (a week by default), not “right now”. A percentage spike is what accumulated over the window, not the current state.</p>
<div class="note">A yellow bar = the machine is in service mode (sales paused). A dash instead of a flavor name in sales = an offline sale; details may sync later or be unavailable.</div>"""},
{"num":12,"prio":2,"slug":"12-service-menu-shaker-s",
 "ru_title":"Сервисное меню — Shaker S","en_title":"Service menu — Shaker S",
 "ru":"""<p>Как войти в сервисное меню Shaker S, где основные разделы и как безопасно выйти. Скриншоты добавим с реальной Shaker S.</p>
<h2>Вход</h2>
<p>Вход — через сервисный доступ. После входа открываются разделы управления машиной.</p>
<h2>Основные разделы</h2>
<ul>
<li><strong>Drinks</strong> — список напитков.</li>
<li><strong>Configurator</strong> — здесь <strong>Change Drinks</strong> и <strong>Update Database From Server</strong>.</li>
<li><strong>Inventory / Remains</strong> — остатки воды и порошков.</li>
<li><strong>Dosages</strong> — дозы напитков.</li>
</ul>
<h2>Иконки уровня кликабельны</h2>
<p>Иконки бутыли / стаканов / порошка в сервисном меню Shaker S нажимаются — клик задаёт текущий уровень (удобно после долива).</p>
<div class="note">Перед уходом обязательно выйдите из сервисного режима — иначе на дашборде жёлтая полоса и продажи стоят.</div>""",
 "en":"""<p>How to enter the Shaker S service menu, the main sections, and how to exit safely. Screenshots will be added from an actual Shaker S.</p>
<h2>Entry</h2>
<p>Enter via service access. Once in, the machine management sections open.</p>
<h2>Main sections</h2>
<ul>
<li><strong>Drinks</strong> — the drink list.</li>
<li><strong>Configurator</strong> — this is where <strong>Change Drinks</strong> and <strong>Update Database From Server</strong> are.</li>
<li><strong>Inventory / Remains</strong> — water and powder levels.</li>
<li><strong>Dosages</strong> — drink doses.</li>
</ul>
<h2>Level icons are tappable</h2>
<p>The bottle / cups / powder icons in the Shaker S service menu are tappable — a tap sets the current level (handy after a refill).</p>
<div class="note">Always exit service mode before leaving — otherwise the dashboard shows a yellow bar and sales are paused.</div>"""},
{"num":13,"prio":2,"slug":"13-stimulant-safety",
 "ru_title":"Безопасность: не превышать суточную дозу стимуляторов","en_title":"Safety: don’t exceed the daily stimulant dose",
 "ru":"""<p>Для стимулирующих продуктов доза — это вопрос безопасности и ответственности, а не только вкуса.</p>
<h2>Правило</h2>
<ul>
<li>Для энергетиков, преворкаутов, EAA и креатина <strong>не превышайте суточную норму</strong> с упаковки продукта.</li>
<li>Если вкус кажется слабым — <strong>снижайте воду</strong>, а не повышайте порошок.</li>
<li>Пищевая ценность на экране считается от реальной дозы — держите дозу в пределах порции с этикетки.</li>
</ul>
<div class="note">Это важно и по здоровью посетителей, и юридически. При сомнениях по конкретному продукту — напишите нам, подскажем безопасную дозу.</div>""",
 "en":"""<p>For stimulant products the dose is a matter of safety and liability, not just taste.</p>
<h2>The rule</h2>
<ul>
<li>For energy, pre-workout, EAA and creatine, <strong>do not exceed the daily serving</strong> on the product label.</li>
<li>If a flavor seems weak, <strong>lower the water</strong> — do not increase the powder.</li>
<li>The on-screen nutrition facts reflect the actual dose — keep it within the label’s serving.</li>
</ul>
<div class="note">This matters both for customer health and legally. If you’re unsure about a specific product, message us and we’ll suggest a safe dose.</div>"""},
{"num":14,"prio":2,"slug":"14-preventing-powder-clogging",
 "ru_title":"Профилактика слёживания / засора порошка","en_title":"Preventing powder clogging / caking",
 "ru":"""<p>Слёжанный порошок комкуется, забивает шнек и портит выдачу. Чаще всего причина — влажность.</p>
<h2>Что помогает</h2>
<ul>
<li>Использовать свободнотекучие порошки (с anti-caking).</li>
<li>Плотно закрывать крышку контейнера; можно положить рядом пакетик силикагеля.</li>
<li>Меньше держать порошок открытым на воздухе, особенно во влажном помещении.</li>
<li>При плотном потоке продаж — периодически очищать белый лоток / воронку между выдачами.</li>
</ul>
<div class="note">Если порошок уже слежался и забил шнек — остановите слот, просушите и очистите контейнер, при необходимости напишите нам.</div>""",
 "en":"""<p>Caked powder clumps, jams the auger and ruins delivery. The usual cause is humidity.</p>
<h2>What helps</h2>
<ul>
<li>Use free-flowing powders (with anti-caking).</li>
<li>Seal the container lid tightly; a silica-gel packet nearby helps.</li>
<li>Keep powder exposed to air as little as possible, especially in a humid room.</li>
<li>Under heavy sales, clear the white tray / funnel between dispenses.</li>
</ul>
<div class="note">If powder has already caked and jammed the auger, stop the slot, dry and clean the container, and message us if needed.</div>"""},
{"num":15,"prio":2,"slug":"15-error-code-index",
 "ru_title":"Единый индекс кодов ошибок","en_title":"Error code index",
 "ru":"""<p>Короткий справочник по кодам ошибок. По каждой ошибке на основном сайте есть отдельная страница с шагами.</p>
<h2>Известные коды</h2>
<ul>
<li><strong>Error 1</strong> — нет воды (проверьте источник, бутыль, прокачку).</li>
<li><strong>Error 5</strong> — нет стакана (загрузка стаканов, датчик).</li>
<li><strong>Error 9</strong> — манипулятор.</li>
<li><strong>Error 11</strong> — шторка окна выдачи. В телеметрии может показываться как «no cups».</li>
<li><strong>Error 18</strong> — неправильный рецепт (объём меньше воды+порошка).</li>
<li><strong>Error 19</strong> — бак полон (нужно опорожнить).</li>
</ul>
<div class="note">Если видите код, которого нет в списке — пришлите фото экрана, подскажем, что это и что делать.</div>""",
 "en":"""<p>A short reference for error codes. Each error has its own step-by-step page on the main site.</p>
<h2>Known codes</h2>
<ul>
<li><strong>Error 1</strong> — no water (check the source, bottle, priming).</li>
<li><strong>Error 5</strong> — no cup (cup loading, sensor).</li>
<li><strong>Error 9</strong> — manipulator.</li>
<li><strong>Error 11</strong> — dispensing window shutter. May show as “no cups” in telemetry.</li>
<li><strong>Error 18</strong> — wrong recipe (volume less than water + powder).</li>
<li><strong>Error 19</strong> — bucket full (needs emptying).</li>
</ul>
<div class="note">If you see a code that isn’t listed, send a photo of the screen and we’ll tell you what it is and what to do.</div>"""},
{"num":16,"prio":2,"slug":"16-mixing-powders-creatine",
 "ru_title":"Микс нескольких порошков + добавка креатина","en_title":"Mixing multiple powders + creatine add-on",
 "ru":"""<p>В одном напитке можно совмещать несколько порошков — например протеин + креатин + BCAA.</p>
<h2>Как это работает</h2>
<ul>
<li>Мультислотовый рецепт: напиток берёт порошок с нескольких слотов.</li>
<li>Добавку (например креатин) можно оформить как опцию с отдельной ценой.</li>
<li>Стакан не переполнится: объём напитка учитывает все компоненты.</li>
</ul>
<div class="note">Опции появляются после Update Database и нужной конфигурации. Если нужной опции (например добавить креатин) нет — напишите нам, настроим.</div>""",
 "en":"""<p>A single drink can combine several powders — for example protein + creatine + BCAA.</p>
<h2>How it works</h2>
<ul>
<li>A multi-slot recipe pulls powder from several slots.</li>
<li>An add-on (e.g. creatine) can be set up as an option with its own price.</li>
<li>The cup won’t overflow: the drink volume accounts for all components.</li>
</ul>
<div class="note">Options appear after Update Database and the right configuration. If an option you need (e.g. add creatine) is missing, message us and we’ll set it up.</div>"""},
{"num":17,"prio":2,"slug":"17-water-priming-air-lock",
 "ru_title":"Прокачка воды / воздушная пробка — насос работает, воды нет","en_title":"Water priming / air lock — pump runs but no water",
 "ru":"""<p>Насос слышно, а воды нет — почти всегда это воздушная пробка в линии.</p>
<h2>Что сделать</h2>
<ol>
<li>Прогоните прокачку: Service Menu → <strong>Pumping water</strong>, пока вода не пойдёт ровно.</li>
<li>Если не помогает — снимите/продуйте трубку, чтобы выгнать воздух, и поставьте обратно.</li>
<li>Проверьте, что шланг нигде не пережат.</li>
<li>Проверьте соединения у бака/чиллера — там может подсасывать воздух.</li>
</ol>
<div class="note">Это про уже подключённую воду. Про монтаж и первое подключение — см. страницы подключения воды.</div>""",
 "en":"""<p>You can hear the pump but no water comes out — this is almost always an air lock in the line.</p>
<h2>What to do</h2>
<ol>
<li>Run priming: Service Menu → <strong>Pumping water</strong> until water flows steadily.</li>
<li>If that doesn’t help, remove/blow through the tube to clear the air, then reconnect it.</li>
<li>Check the hose isn’t pinched anywhere.</li>
<li>Check the connections at the tank/chiller — air can be drawn in there.</li>
</ol>
<div class="note">This is for water that’s already connected. For installation and first connection, see the water-connection pages.</div>"""},
{"num":18,"prio":2,"slug":"18-water-source-bottle-vs-mains",
 "ru_title":"Выбор / переключение источника воды: бутыль vs водопровод","en_title":"Water source: bottle vs mains, and switching",
 "ru":"""<h2>Только бутыль</h2>
<p>Машина может работать от внутренней бутыли без подключения к водопроводу. В этом случае линию водопровода не подключают.</p>
<h2>Переключение на водопровод</h2>
<ol>
<li>Подключите линию водопровода.</li>
<li>Отрегулируйте давление (винтом на узле).</li>
<li>Выберите правильный источник в ПО машины.</li>
</ol>
<div class="note">Неверно выбранный источник в ПО даёт ложную ошибку «нет воды» (например режим водопровода при работе от бутыли). Часть удалённых настроек проще делать на бутыли — при сомнениях напишите нам.</div>""",
 "en":"""<h2>Bottle only</h2>
<p>The machine can run from the internal bottle without a mains connection. In that case the mains line isn’t connected.</p>
<h2>Switching to mains</h2>
<ol>
<li>Connect the mains water line.</li>
<li>Adjust the pressure (screw on the unit).</li>
<li>Select the correct source in the machine software.</li>
</ol>
<div class="note">The wrong source in software causes a false “no water” error (e.g. mains mode while running on the bottle). Some remote settings are easier on the bottle — if unsure, message us.</div>"""},
{"num":19,"prio":2,"slug":"19-cups-only-mode",
 "ru_title":"Режим «только стаканы» (отключить чужой шейкер)","en_title":"Cups-only mode (disable bring-your-own-shaker)",
 "ru":"""<p>Если посетители ставят свои шейкеры и крупные заклинивают механику, можно перевести машину в режим выдачи только своего стакана.</p>
<h2>Что делает режим</h2>
<ul>
<li>Машина всегда наливает в свой стакан, чужой шейкер не принимается — механика защищена.</li>
<li>Включается/выключается в настройках.</li>
</ul>
<div class="note">Обратная сторона: не отключите случайно саму выдачу стаканов — иначе появится «поставьте свой стакан». После изменения проверьте выдачу. Если нужно — напишите нам, поможем настроить.</div>""",
 "en":"""<p>If customers put in their own shakers and oversized ones jam the mechanics, you can set the machine to dispense only its own cup.</p>
<h2>What the mode does</h2>
<ul>
<li>The machine always pours into its own cup and won’t accept an outside shaker — the mechanics are protected.</li>
<li>It’s turned on/off in the settings.</li>
</ul>
<div class="note">The flip side: don’t accidentally disable cup dispensing itself — otherwise you get “insert your own cup”. Test dispensing after the change. If needed, message us and we’ll help configure it.</div>"""},
# ---------------------- Приоритет 3 ----------------------
{"num":20,"prio":3,"slug":"20-loyalty-cards-points",
 "ru_title":"Лояльность: как работают карты и баллы","en_title":"Loyalty cards and points",
 "ru":"""<h2>Как это работает для покупателя</h2>
<ul>
<li>Покупатель прикладывает карту или сканирует QR — баллы начисляются за покупку.</li>
<li>Накопленные баллы тратятся при оплате.</li>
<li>Карта или QR — всё, что нужно; отдельное приложение не обязательно.</li>
</ul>
<div class="note">Кнопки лояльности на экране могут выглядеть серыми, но они работают. Если нужно настроить программу лояльности под вашу точку — напишите нам.</div>""",
 "en":"""<h2>How it works for the customer</h2>
<ul>
<li>The customer taps a card or scans a QR — points are earned on the purchase.</li>
<li>Accumulated points are spent at payment.</li>
<li>A card or QR is all that’s needed; a separate app isn’t required.</li>
</ul>
<div class="note">The loyalty buttons on screen may look grey but they work. If you want the loyalty program configured for your location, message us.</div>"""},
{"num":21,"prio":3,"slug":"21-cup-detection-compatibility",
 "ru_title":"Тёмные / красные стаканы не распознаются","en_title":"Dark / red cups not detected",
 "ru":"""<p>Датчик стакана — оптический. Тёмные и красные стаканы он может «не видеть».</p>
<h2>Что делать</h2>
<ul>
<li>Используйте светлые стаканы (наши стандартные).</li>
<li>Держите датчик в чистоте — после мойки протрите зону датчика.</li>
</ul>
<div class="note">Если машина пишет «no cups», а стаканы есть — это датчик или застрявший стакан, а не пустой лоток. Проверьте загрузку и чистоту датчика; при необходимости — Controller Reboot.</div>""",
 "en":"""<p>The cup sensor is optical. It may “not see” dark and red cups.</p>
<h2>What to do</h2>
<ul>
<li>Use light-colored cups (our standard ones).</li>
<li>Keep the sensor clean — wipe the sensor area after cleaning.</li>
</ul>
<div class="note">If the machine says “no cups” but cups are present, it’s the sensor or a stuck cup, not an empty tray. Check loading and sensor cleanliness; do a Controller Reboot if needed.</div>"""},
{"num":22,"prio":3,"slug":"22-displayed-volume-vs-actual",
 "ru_title":"Надпись объёма vs реальная доза (oz / ml)","en_title":"Displayed volume vs actual dose (oz / ml)",
 "ru":"""<p>Надпись объёма на экране (например «12 oz») — это <strong>только подпись</strong>, а не реальная доза напитка.</p>
<h2>Что важно знать</h2>
<ul>
<li>Реальная доза задаётся в дозировках/калибровке, а не в подписи.</li>
<li>Подпись можно поменять (oz / ml) отдельно от рецепта.</li>
<li>После Update Database надпись может вернуться к прежней — задайте заново.</li>
</ul>
<div class="note">Если хотите, чтобы на экране был один объём, а реальная выдача — другая, это нормально: меняем подпись, дозу оставляем как откалибровано.</div>""",
 "en":"""<p>The volume label on screen (e.g. “12 oz”) is <strong>just a label</strong>, not the actual drink dose.</p>
<h2>What to know</h2>
<ul>
<li>The real dose is set in dosages/calibration, not in the label.</li>
<li>The label (oz / ml) can be changed separately from the recipe.</li>
<li>After Update Database the label may revert — set it again.</li>
</ul>
<div class="note">If you want one volume shown on screen and a different actual pour, that’s fine: we change the label and leave the dose as calibrated.</div>"""},
{"num":23,"prio":3,"slug":"23-screen-orientation",
 "ru_title":"Экран перевёрнут / обрезан — ориентация (Touch)","en_title":"Screen upside-down / cut-off — orientation (Touch)",
 "ru":"""<p>После перезагрузки или сервисной сессии экран Touch иногда оказывается перевёрнутым или показан частями.</p>
<h2>Что делать</h2>
<ol>
<li>Дайте машине полностью загрузиться — 2–3 минуты. Часто ориентация выправляется сама.</li>
<li>Если не выправилось — пришлите нам фото, поправим удалённо.</li>
</ol>
<div class="note">Не пытайтесь крутить настройки экрана вслепую — просто дайте догрузиться и напишите нам, если осталось.</div>""",
 "en":"""<p>After a reboot or a service session, the Touch screen is sometimes upside-down or shown in parts.</p>
<h2>What to do</h2>
<ol>
<li>Let the machine boot fully — 2–3 minutes. The orientation often corrects itself.</li>
<li>If it doesn’t, send us a photo and we’ll fix it remotely.</li>
</ol>
<div class="note">Don’t change display settings blindly — just let it finish booting and message us if it remains.</div>"""},
{"num":24,"prio":3,"slug":"24-idle-video-not-playing",
 "ru_title":"Idle / attract-видео не проигрывается","en_title":"Idle / attract video not playing",
 "ru":"""<p>Заставка (idle / attract-видео) иногда перестаёт проигрываться — чаще после обновления.</p>
<h2>Безопасные шаги</h2>
<ol>
<li>Сделайте Controller Reboot.</li>
<li>Если не помогло — выключите/включите машину тумблером сзади (крайнее средство), дайте загрузиться.</li>
</ol>
<div class="note">Если видео не вернулось — напишите нам, восстановим/заменим медиа. Настройка своей заставки/логотипа делается через нас.</div>""",
 "en":"""<p>The attract / idle video sometimes stops playing — usually after an update.</p>
<h2>Safe steps</h2>
<ol>
<li>Do a Controller Reboot.</li>
<li>If that doesn’t help, switch the machine off/on with the rear switch (last resort) and let it boot.</li>
</ol>
<div class="note">If the video doesn’t come back, message us and we’ll restore/replace the media. Setting a custom attract video/logo is done through us.</div>"""},
{"num":25,"prio":3,"slug":"25-drip-tray-fills-with-water",
 "ru_title":"Поддон / воронка наполняется водой в простое — это норма","en_title":"Drip tray / funnel fills with water when idle — normal",
 "ru":"""<p>Нижний поддон (там, где стоит стакан) со временем набирает воду — это нормально.</p>
<h2>Почему так</h2>
<ul>
<li>Поддон собирает капли и воду от промывки миксера.</li>
<li>Слива у поддона нет — его опорожняют вручную.</li>
</ul>
<div class="note">Это не протечка. Просто периодически сливайте поддон. Если воды в поддоне подозрительно много — напишите нам, посмотрим.</div>""",
 "en":"""<p>The lower tray (where the cup sits) collects water over time — this is normal.</p>
<h2>Why</h2>
<ul>
<li>The tray catches drips and mixer-rinse water.</li>
<li>The tray has no drain — you empty it manually.</li>
</ul>
<div class="note">This is not a leak. Just empty the tray periodically. If there’s an unusual amount of water, message us and we’ll take a look.</div>"""},
{"num":26,"prio":3,"slug":"26-water-wont-stop-calibration",
 "ru_title":"Вода льётся без остановки при калибровке — аварийный стоп","en_title":"Water won’t stop during calibration — emergency stop",
 "ru":"""<p>Иногда во время калибровки воды поток не останавливается вовремя.</p>
<h2>Как остановить</h2>
<ol>
<li>Выйдите из режима калибровки.</li>
<li>Если не реагирует — сделайте Controller Reboot, чтобы прекратить подачу.</li>
<li>После — перепроверьте калибровку воды заново.</li>
</ol>
<div class="note">Если это повторяется — напишите нам с деталями (модель, когда происходит), посмотрим причину. Не оставляйте машину в таком состоянии без присмотра.</div>""",
 "en":"""<p>Sometimes during water calibration the flow doesn’t stop on time.</p>
<h2>How to stop it</h2>
<ol>
<li>Exit calibration mode.</li>
<li>If it doesn’t respond, do a Controller Reboot to cut the flow.</li>
<li>Afterwards, re-check the water calibration.</li>
</ol>
<div class="note">If this repeats, message us with details (model, when it happens) and we’ll look into the cause. Don’t leave the machine unattended in this state.</div>"""},
{"num":27,"prio":3,"slug":"27-requesting-spare-keys",
 "ru_title":"Запрос дополнительных / запасных ключей","en_title":"Requesting additional / spare keys",
 "ru":"""<p>Физические ключи к машине — кастомные, произвольно они не дублируются.</p>
<h2>Как заказать</h2>
<ul>
<li>Пришлите нам серийный номер машины — по нему подготовим доп/замену.</li>
<li>Как альтернатива физическому ключу — QR-доступ к двери (открытие по QR без ключа).</li>
</ul>
<div class="note">Сроки и стоимость уточняйте у нас отдельно.</div>""",
 "en":"""<p>The machine’s physical keys are custom-cut and not duplicated arbitrarily.</p>
<h2>How to order</h2>
<ul>
<li>Send us the machine serial number — we’ll prepare an extra/replacement from it.</li>
<li>As an alternative to a physical key — QR door access (open by QR without a key).</li>
</ul>
<div class="note">Ask us separately about timing and cost.</div>"""},
{"num":28,"prio":3,"slug":"28-chiller-cooling",
 "ru_title":"Чиллер / охлаждение — включение и температура","en_title":"Chiller / cooling — turning on and temperature",
 "ru":"""<p>Как включить охлаждение и что находится на задней панели.</p>
<h2>Охлаждение</h2>
<p>Включите охлаждение и дайте ему выйти на режим — шейк станет холодным не сразу. Регулировка температуры — на узле охладителя.</p>
<h2>Задняя панель Touch 2 — две розетки</h2>
<ul>
<li><strong>Верхняя розетка (C14)</strong> — вход питания 220В самой машины.</li>
<li><strong>Нижняя розетка (C14)</strong> — выход для опционального компрессорного чиллера (на замену штатному охладителю).</li>
</ul>
<div class="note">Не меняйте эти две розетки местами. Если шейк недостаточно холодный — проверьте, включено ли охлаждение и дайте время; если не помогает — напишите нам.</div>""",
 "en":"""<p>How to turn on cooling and what’s on the back panel.</p>
<h2>Cooling</h2>
<p>Turn cooling on and give it time to reach temperature — the shake won’t be cold immediately. Temperature is adjusted on the cooler unit.</p>
<h2>Touch 2 back panel — two outlets</h2>
<ul>
<li><strong>Top outlet (C14)</strong> — 220V power input for the machine itself.</li>
<li><strong>Bottom outlet (C14)</strong> — output for an optional compressor chiller (replacing the built-in cooler).</li>
</ul>
<div class="note">Don’t swap these two outlets. If the shake isn’t cold enough, check that cooling is on and give it time; if it doesn’t help, message us.</div>"""},
{"num":29,"prio":3,"slug":"29-auto-wash-schedule",
 "ru_title":"Авто-мойка / ополаскивание миксера — расписание","en_title":"Auto-wash / mixer rinse — schedule",
 "ru":"""<p>Машина может сама ополаскивать миксер — это снижает налёт и запах.</p>
<h2>Настройка</h2>
<ul>
<li>Авто-мойку можно настроить по расписанию (например раз в час) или после каждого шейка.</li>
<li>Включается в сервисном меню (раздел Wash / мойка).</li>
</ul>
<div class="note">AutoClean снижает налёт, но не заменяет периодическую ручную чистку узлов. Если не уверены в настройке для вашей проходимости — напишите нам, подскажем интервал.</div>""",
 "en":"""<p>The machine can rinse the mixer on its own — this reduces buildup and odor.</p>
<h2>Setup</h2>
<ul>
<li>Auto-wash can be scheduled (e.g. hourly) or run after each shake.</li>
<li>It’s enabled in the service menu (Wash section).</li>
</ul>
<div class="note">AutoClean reduces buildup but doesn’t replace periodic manual cleaning. If you’re unsure what interval fits your traffic, message us and we’ll suggest one.</div>""",
 "img":"service-wash-mixer.jpg","cap_ru":"Сервисное меню: «Wash Mixer» — запуск ополаскивания миксера.","cap_en":"Service menu: “Wash Mixer” — start the mixer rinse."},
{"num":30,"prio":3,"slug":"30-third-party-mdb-terminals",
 "ru_title":"Сторонние MDB-терминалы — совместимость","en_title":"Third-party MDB terminals — compatibility",
 "ru":"""<p>Машина общается с платёжными устройствами по протоколу <strong>MDB (уровень 3)</strong> — тот же разъём, что у любого MDB-терминала.</p>
<h2>Что это значит</h2>
<ul>
<li>В теории машина совместима с MDB-совместимыми cashless-устройствами, не только Nayax.</li>
<li>У поставщика терминала запрашивайте поддержку <strong>MDB Level 3</strong>.</li>
</ul>
<div class="note">Прежде чем ставить неподтверждённый терминал — уточните у нас. Не каждое устройство мы проверяли, и поддержку по непроверенным терминалам гарантировать не можем.</div>""",
 "en":"""<p>The machine talks to payment devices over the <strong>MDB (level 3)</strong> protocol — the same connector any MDB terminal uses.</p>
<h2>What this means</h2>
<ul>
<li>In theory the machine is compatible with MDB-compliant cashless devices, not only Nayax.</li>
<li>From the terminal supplier, ask for <strong>MDB Level 3</strong> support.</li>
</ul>
<div class="note">Before installing an unverified terminal, check with us. We haven’t tested every device and can’t guarantee support for unverified terminals.</div>"""},
]

def w(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)

w("assets/style.css", STYLE)

def fig(src, cap):
    return '<figure><img src="../assets/img/%s" alt=""><figcaption>%s</figcaption></figure>' % (src, cap)

for a in ARTICLES:
    ru_body = a["ru"] + (fig(a["img"], a["cap_ru"]) if a.get("img") else "")
    en_body = a["en"] + (fig(a["img"], a["cap_en"]) if a.get("img") else "")
    w("ru/%s.html" % a["slug"], page("ru", a["ru_title"], ru_body, "../en/%s.html" % a["slug"]))
    w("en/%s.html" % a["slug"], page("en", a["en_title"], en_body, "../ru/%s.html" % a["slug"]))

def index_rows(prio):
    rows = []
    for a in ARTICLES:
        if a["prio"] != prio:
            continue
        rows.append('<li><span class="t">%d. %s</span><span class="links"><a href="ru/%s.html">RU</a><a href="en/%s.html">EN</a></span></li>'
                    % (a["num"], a["ru_title"], a["slug"], a["slug"]))
    return "\n".join(rows)

index_html = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>iShaker Help</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">
<span class="badge">Draft / черновик</span>
<h1>iShaker Help</h1>
<p class="subtitle">Справочные страницы для операторов iShaker — русский и английский. Черновик для внутреннего ревью перед публикацией.</p>
<p style="margin:0 0 28px"><a href="guide.html"><strong>📝 Как писать статьи — гайд для авторов →</strong></a></p>
<h2 class="prio">🔴 Приоритет 1</h2>
<ul class="arts">
%s
</ul>
<h2 class="prio">🟡 Приоритет 2</h2>
<ul class="arts">
%s
</ul>
<h2 class="prio">🟢 Приоритет 3</h2>
<ul class="arts">
%s
</ul>
</div>
</body>
</html>""" % (index_rows(1), index_rows(2), index_rows(3))

w("index.html", index_html)

# ---------------- guide page (для авторов) ----------------
GUIDE_BODY = """<p class="subtitle">Гайд для того, кто наполняет этот справочник: о чём писать, где брать материал и изображения, каким тоном, чего не публиковать и как это технически собрать.</p>

<h2>1. О чём статья</h2>
<ul>
<li><strong>Одна страница = одна тема, один вопрос оператора.</strong> Не сваливать всё в простыню.</li>
<li>Только два типа контента: <strong>(a)</strong> что оператор делает сам на своей машине; <strong>(b)</strong> объяснение «как/почему это работает».</li>
<li>Заголовок — как формулирует оператор (симптом/вопрос), а не наш технический термин. «Машина офлайн / WiFi отваливается», а не «Диагностика сетевого подключения».</li>
</ul>

<h2>2. Откуда брать темы</h2>
<ul>
<li><strong>Реальные повторяющиеся вопросы операторов</strong> — самый сильный сигнал.</li>
<li>Приоритетный список тем — в этом справочнике (индекс, приоритеты 1/2/3).</li>
<li>Если оператор не понял то, что нам кажется очевидным — это кандидат в новую страницу.</li>
</ul>

<h2>3. Где искать материал</h2>
<ul>
<li><strong>Заводская вика (RU)</strong> — базовые штатные процедуры (вода, ошибки, сервисное меню). Это <em>источник</em>, а не готовый текст: адаптировать под оператора, не копировать дословно и не тащить сервисный/внутренний уровень.</li>
<li><strong>Существующие страницы info.ishakerusa.com</strong> — образец тона и структуры на EN.</li>
<li><strong>Реальная машина</strong> — проверять точные названия кнопок и снимать скриншоты. Не восстанавливать формулировки по памяти.</li>
<li><strong>Команда/поддержка</strong> — по тому, что нельзя проверить самому. Лучше спросить, чем выдумать: неверная инструкция дороже отсутствующей.</li>
</ul>

<h2>4. Структура страницы</h2>
<ol>
<li><strong>Лид</strong> — 1–2 строки: что за ситуация.</li>
<li><strong>«Почему так»</strong> — если помогает понять причину.</li>
<li><strong>Шаги</strong> — что проверить/сделать, нумерованным списком.</li>
<li><strong>Note</strong> (жёлтый блок) — предупреждение или важный нюанс.</li>
<li><strong>Финал</strong> — «если не помогло / нестандартно — напишите нам».</li>
</ol>
<p>Каждая тема — на <strong>двух языках (RU + EN)</strong>. EN базовый, дальше при необходимости другие языки.</p>

<h2>5. Изображения</h2>
<ul>
<li>Скриншоты снимать на <strong>реальной машине той же модели</strong> (по возможности того же билда) — интерфейс между моделями отличается.</li>
<li>Для EN-страниц снимать UI на <strong>английской локали</strong>.</li>
<li>Класть в <code>assets/img/</code>, вставлять <code>&lt;figure&gt;</code> с подписью. Нужную кнопку выделять рамкой (см. готовые примеры в <code>assets/img/</code>).</li>
<li><strong>Нельзя в кадре:</strong> реальные серийные номера, имена/контакты клиентов, фото разборки, плат и проводки. Если серийник попал — замазать.</li>
</ul>

<h2>6. Тон</h2>
<ul>
<li><strong>Не обещать результат.</strong> «usually / in most cases / based on what we see now» — норма, а не слабость.</li>
<li>Избегать «reconnects on its own», «no laptop needed», «that's all you need», «это точно починит». Не сбудется — потеряется доверие.</li>
<li>От лица <strong>«our team / we»</strong>, без имён отдельных сотрудников.</li>
<li>Уверенно, но честно: где не уверены — «if it doesn't pick up, we'll guide you through the next step».</li>
</ul>

<h2>7. Чего не публикуем</h2>
<ul>
<li>Любые пароли, доступы, служебные команды, названия внутренних инструментов.</li>
<li>Как оператору самому получить удалённый доступ к машине (доступ выдаём по запросу).</li>
<li>Наши сроки/SLA/описание внутренних процессов — создаёт обязательства.</li>
<li>Темы, по которым ещё нет решения команды — сверяться перед публикацией.</li>
</ul>
<div class="note"><strong>Проверка:</strong> страница = (a) что оператор делает сам, или (b) объяснение как/почему? Если это (c) описание нашей внутренней кухни — не публикуем.</div>

<h2>8. Термины</h2>
<ul>
<li>Названия кнопок и пунктов меню — <strong>байт-в-байт как на машине</strong> (не угадывать регистр и раздельность).</li>
<li>RU-источник ≠ дословный перевод: сверять формулировки со скриншотом EN-локали.</li>
<li>Перед «на EN этого нет» — проверить, нет ли уже EN-эквивалента под другим названием.</li>
</ul>

<h2>9. Технически (этот репозиторий)</h2>
<ul>
<li>Весь контент — в <code>build.py</code>, список <code>ARTICLES</code>. Поля: <code>num</code>, <code>prio</code>, <code>slug</code>, <code>ru_title</code>, <code>en_title</code>, <code>ru</code>, <code>en</code>; опционально <code>img</code> + <code>cap_ru</code>/<code>cap_en</code>.</li>
<li>Правка → <code>python3 build.py</code> → пересобираются <code>index.html</code>, <code>ru/*.html</code>, <code>en/*.html</code>, эта страница.</li>
<li>Слаг одинаковый в <code>ru/</code> и <code>en/</code>. <code>prio</code> (1/2/3) — группировка в индексе. Картинки — <code>assets/img/</code>.</li>
<li>Предпросмотр — открыть <code>index.html</code> или задеплоить (GitHub Pages / Vercel).</li>
</ul>

<h2>10. Чек-лист перед публикацией</h2>
<ul>
<li>☐ Заголовок — с точки зрения оператора.</li>
<li>☐ Есть RU и EN.</li>
<li>☐ Шаги проверены на реальной машине.</li>
<li>☐ Скриншоты без серийников и внутренностей.</li>
<li>☐ Тон без обещаний результата, от «our team».</li>
<li>☐ Нет паролей/доступов/внутренней кухни.</li>
<li>☐ Термины сверены с машиной.</li>
</ul>"""

w("guide.html", rootpage("Как писать статьи", GUIDE_BODY, '<span class="badge">Для авторов</span>'))

print("Built: index + guide + %d articles x2 langs + style" % len(ARTICLES))
