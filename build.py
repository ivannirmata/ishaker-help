#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генератор статичного черновика iShaker Help (RU + EN).
P1 (1-10) — полный текст. P2/P3 (11-30) — каркас (scope + источник).
Запуск: python3 build.py  → генерирует index.html, ru/*.html, en/*.html, assets/style.css
Черновик для внутреннего ревью команды перед публикацией на info.ishakerusa.com.
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
.note{background:#fff8e1;border-left:4px solid #f4b400;padding:12px 16px;font-size:15px;color:#6b5900;border-radius:0 8px 8px 0;margin:20px 0;}
.badge{display:inline-block;background:#e8f0fe;color:#1a56b0;font-size:13px;padding:3px 10px;border-radius:12px;margin-bottom:16px;}
.badge.draft{background:#fdecea;color:#b3261e;}
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
.tag{font-size:12px;color:#b3261e;background:#fdecea;border-radius:10px;padding:2px 8px;margin-left:8px;}
"""

def page(lang, title, body, other_href, badge=""):
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
%s<h1>%s</h1>
%s
<hr>
<p class="foot">Draft / черновик — для внутреннего ревью перед публикацией. iShaker USA.</p>
</div>
</body>
</html>""" % (lang, title, switch, badge, title, body)

DRAFT_RU = '<span class="badge draft">🚧 Каркас — заполнить</span>'
DRAFT_EN = '<span class="badge draft">🚧 Draft — to be written</span>'

# ======================================================================
# P1 — полный текст (RU + EN)
# ======================================================================
P1 = [
{
 "num": 1, "slug": "01-machine-offline-wifi",
 "ru_title": "Машина офлайн / WiFi отваливается",
 "en_title": "Machine offline / WiFi keeps disconnecting",
 "ru": """<p>Если вверху панели телеметрии появилась жёлтая полоса или значок «?», машина <strong>не на связи с сервером</strong>. Важно: продажи при этом обычно продолжаются — оплата картой идёт по своей линии (Nayax), а продажи копятся локально и подгружаются позже. <strong>Офлайн ≠ остановка продаж.</strong></p>
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
 "en": """<p>A yellow bar or a “?” icon at the top of the telemetry dashboard means the machine is <strong>not connected to the server</strong>. Note: sales usually keep working — card payments run on their own line (Nayax) and sales are stored locally and uploaded later. <strong>Offline does not mean sales are stopped.</strong></p>
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
<p>This is usually enough. If the machine is still offline after restarting the router and reconnecting, send us a photo of the status screen and we will guide you through the next step.</p>""",
},
{
 "num": 2, "slug": "02-add-your-own-flavor",
 "ru_title": "Как завести свой порошок / вкус",
 "en_title": "Adding your own powder / flavor",
 "ru": """<p>Часть шагов вы делаете сами, а регистрацию совсем нового продукта — через нас.</p>
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
 "en": """<p>You do some steps yourself; registering a brand-new product goes through us.</p>
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
},
{
 "num": 3, "slug": "03-flavor-not-showing-after-update",
 "ru_title": "Новый вкус не появился после «Update Database»",
 "en_title": "New flavor doesn’t appear after “Update Database”",
 "ru": """<h2>Полный путь синхронизации</h2>
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
 "en": """<h2>Full sync path</h2>
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
},
{
 "num": 4, "slug": "04-powder-dose-calibration",
 "ru_title": "Доза порошка неверная (ставлю 30 г — выходит 15 г)",
 "en_title": "Powder dose is wrong (set 30 g, get 15 g)",
 "ru": """<p>Если вы задаёте одну дозу порошка, а по факту выходит меньше (или шейк слишком жидкий) — почти всегда дело в калибровке и в правиле рецепта.</p>
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
 "en": """<p>If you set one powder dose but get less in the cup (or the shake is too watery), it’s almost always about calibration and the recipe rule.</p>
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
<p>If purchase delivery is still low after calibration, message us — sometimes a tweak is needed on our side.</p>""",
},
{
 "num": 5, "slug": "05-after-update-checklist",
 "ru_title": "Что проверить после обновления ПО",
 "en_title": "What to check after a software update",
 "ru": """<p>После того как ПО машины обновили удалённо, пробегитесь по этому короткому чек-листу.</p>
<h2>Проверьте эти 5 вещей</h2>
<ol>
<li><strong>Цены.</strong> Иногда сбрасываются на значение по умолчанию (например $100). Проверьте цену каждого напитка.</li>
<li><strong>Уровень воды.</strong> Может показать «∞» или сброситься — введите текущий уровень (см. «Вода показывает ∞ / долив»).</li>
<li><strong>Остатки порошка.</strong> Могут обнулиться — введите текущие остатки при ближайшем пополнении.</li>
<li><strong>Дозировки.</strong> Проверьте, что дозы напитков на месте и корректны.</li>
<li><strong>Режим.</strong> Убедитесь, что машина вышла из сервисного режима (жёлтая полоса убрана) и стоит на витрине.</li>
</ol>
<div class="note">Если что-то выглядит не так после обновления — пришлите фото, поправим.</div>""",
 "en": """<p>After the machine’s software is updated remotely, run through this short checklist.</p>
<h2>Check these 5 things</h2>
<ol>
<li><strong>Prices.</strong> They sometimes reset to a default (e.g. $100). Check the price of every drink.</li>
<li><strong>Water level.</strong> May show “∞” or reset — enter the current level (see “Water shows ∞ / refilling”).</li>
<li><strong>Powder inventory.</strong> May reset to zero — enter the current amounts at the next refill.</li>
<li><strong>Dosages.</strong> Confirm the drink doses are present and correct.</li>
<li><strong>Mode.</strong> Make sure the machine left service mode (no yellow bar) and is back on the storefront.</li>
</ol>
<div class="note">If something looks off after an update, send a photo and we’ll fix it.</div>""",
},
{
 "num": 6, "slug": "06-water-refill-reset-gauge",
 "ru_title": "Вода показывает ∞ / долив и сброс уровня после замены бутыли",
 "en_title": "Water shows ∞ / refilling and resetting the gauge after a bottle swap",
 "ru": """<h2>После замены бутыли вода не идёт</h2>
<p>Скорее всего в линии воздух. Выгоните его: Service Menu → <strong>Pumping water</strong> (прокачка), пока вода не пойдёт ровно. Перезагружать машину для этого не нужно.</p>
<h2>Значок воды показывает «∞»</h2>
<p>После обновления счётчик остатка воды мог не перенестись — задайте значение вручную.</p>
<ul>
<li><strong>Shaker S:</strong> в Service Menu иконки уровня (бутыль / стаканы / порошок) кликабельны — нажмите на иконку воды и задайте текущий уровень.</li>
<li><strong>Другие модели:</strong> через раздел остатков (Inventory / Remains).</li>
</ul>
<div class="note">Машина считает только расход — фактический остаток вводится вручную при пополнении. Если после ввода значение снова «плывёт» — напишите нам.</div>""",
 "en": """<h2>No water after replacing the bottle</h2>
<p>There’s likely air in the line. Purge it: Service Menu → <strong>Pumping water</strong> until water flows steadily. You don’t need to reboot the machine for this.</p>
<h2>The water icon shows “∞”</h2>
<p>After an update the water level counter may not have carried over — set the value manually.</p>
<ul>
<li><strong>Shaker S:</strong> in the Service Menu the level icons (bottle / cups / powder) are tappable — tap the water icon and set the current level.</li>
<li><strong>Other models:</strong> via the Inventory / Remains section.</li>
</ul>
<div class="note">The machine only counts consumption — the actual remaining amount is entered manually at refill. If the value keeps drifting after you set it, message us.</div>""",
},
{
 "num": 7, "slug": "07-screen-frozen-recovery",
 "ru_title": "Экран завис / застрял на 100% / не реагирует",
 "en_title": "Screen frozen / stuck at 100% / not responding",
 "ru": """<p>Если экран завис, застрял на «100%» при приготовлении или не реагирует на касания — вот что можно сделать самому, безопасно.</p>
<h2>Шаги восстановления</h2>
<ol>
<li>Подождите 2–3 минуты — иногда машина доготавливает и отвисает сама.</li>
<li>Выключите машину тумблером сзади примерно на 60 секунд, затем включите. Дайте 2–3 минуты на полную загрузку.</li>
<li>Если касания не работают, но нужно закрыть зависшее приложение — подключите USB-клавиатуру и нажмите <strong>Alt+F4</strong>, затем дайте машине загрузиться.</li>
</ol>
<div class="note">Не выдёргивайте питание во время приготовления без необходимости. Дайте машине полностью загрузиться перед проверкой (2–3 минуты).</div>
<p>Если зависания повторяются регулярно — пришлите нам фото/видео и примерное время, когда это происходит, и мы посмотрим причину.</p>""",
 "en": """<p>If the screen freezes, gets stuck at “100%” while making a drink, or doesn’t respond to touch — here’s what you can safely do yourself.</p>
<h2>Recovery steps</h2>
<ol>
<li>Wait 2–3 minutes — the machine sometimes finishes and recovers on its own.</li>
<li>Switch the machine off with the rear switch for about 60 seconds, then on. Allow 2–3 minutes to fully boot.</li>
<li>If touch doesn’t work but you need to close a frozen app — connect a USB keyboard and press <strong>Alt+F4</strong>, then let the machine boot.</li>
</ol>
<div class="note">Avoid pulling power during a drink unless necessary. Let the machine boot fully before checking (2–3 minutes).</div>
<p>If freezes keep happening, send us a photo/video and roughly when it occurs, and we’ll look into the cause.</p>""",
},
{
 "num": 8, "slug": "08-first-time-setup",
 "ru_title": "Чек-лист первого запуска — от доставки до первой продажи",
 "en_title": "First-time setup checklist — from delivery to first sale",
 "ru": """<p>Короткий порядок действий при установке новой машины. По каждому пункту есть отдельная страница со деталями.</p>
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
 "en": """<p>A short order of steps when installing a new machine. Each item has its own detailed page.</p>
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
<div class="note">If anything goes wrong at any step, send a photo of the screen and we’ll help.</div>""",
},
{
 "num": 9, "slug": "09-nayax-cashless-out-of-order",
 "ru_title": "Nayax «Cashless Out of Order» (M00 / V00 / V01)",
 "en_title": "Nayax “Cashless Out of Order” (M00 / V00 / V01)",
 "ru": """<p>Если платёжный терминал Nayax пишет «Cashless Out of Order» с кодом M00, V00 или V01 — обычно это потеря связи между терминалом и машиной по MDB-кабелю, а не поломка самого Nayax.</p>
<h2>Что проверить</h2>
<ol>
<li>Перезапустите <strong>только платёжный терминал</strong> (не выключая машину) — часто восстанавливает связь.</li>
<li>Проверьте MDB-кабель терминала: плотно ли он вставлен, и есть ли на терминале питание.</li>
<li>Проверьте, что у машины есть интернет — для онлайн-функций терминала.</li>
<li>Если у машины при этом ошибка воды или приготовления — терминал может уходить в ошибку заодно; сначала устраните основную проблему.</li>
</ol>
<div class="note">Настройка терминала (подключение к MDB) описана на странице «Machine settings for the NAYAX terminal» — эта страница про восстановление связи, а не про первичную настройку.</div>
<p>Если связь не поднимается — сообщите нам серийный номер ридера, посмотрим на стороне Nayax.</p>""",
 "en": """<p>If the Nayax terminal shows “Cashless Out of Order” with code M00, V00 or V01, it’s usually a lost link between the terminal and the machine over the MDB cable — not a failure of the Nayax unit itself.</p>
<h2>What to check</h2>
<ol>
<li>Restart <strong>only the payment terminal</strong> (without turning the machine off) — this often restores the link.</li>
<li>Check the terminal’s MDB cable: is it seated firmly, and does the terminal have power?</li>
<li>Confirm the machine has internet — for the terminal’s online functions.</li>
<li>If the machine also has a water or brewing error, the terminal may fault along with it; fix the main problem first.</li>
</ol>
<div class="note">Terminal configuration (MDB connection) is on the “Machine settings for the NAYAX terminal” page — this page is about restoring the link, not the initial setup.</div>
<p>If the link won’t come back, send us the reader’s serial number and we’ll check on the Nayax side.</p>""",
},
{
 "num": 10, "slug": "10-service-menu-touch-2",
 "ru_title": "Сервисное меню — Touch 2",
 "en_title": "Service menu — Touch 2",
 "ru": """<p>Как войти в сервисное меню Touch 2, где что находится и как безопасно выйти. Пути ниже — общий ориентир; точные названия вкладок и скриншоты добавим по факту с машины.</p>
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
 "en": """<p>How to enter the Touch 2 service menu, where things are, and how to exit safely. The paths below are a general guide; exact tab names and screenshots will be added from the machine.</p>
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
<p>[Tab screenshots will be added from an actual Touch 2.]</p>""",
},
]

# ======================================================================
# P2 / P3 — каркас (scope + источник)
# ======================================================================
SKELETONS = [
{"num":11,"slug":"11-telemetry-dashboard","prio":2,
 "ru_title":"Как читать дашборд телеметрии","en_title":"Reading the telemetry dashboard",
 "scope_ru":["Что значат иконки WiFi / MDB / Hardware (зелёный / красный / жёлтый).","Почему WiFi off ≠ нет продаж (оплата и продажи идут локально).","Downtime = сумма за период, а не «сейчас».","Жёлтая полоса = сервисный режим.","Прочерк вместо названия вкуса = офлайн-продажа."],
 "scope_en":["What the WiFi / MDB / Hardware icons mean (green / red / yellow).","Why WiFi off does not mean no sales.","Downtime = total for the period, not right now.","Yellow bar = service mode.","A dash instead of a flavor = an offline sale."],
 "src":"Дополнить существующую страницу «Authorization & control in iShaker telemetry»."},
{"num":12,"slug":"12-service-menu-shaker-s","prio":2,
 "ru_title":"Сервисное меню — Shaker S","en_title":"Service menu — Shaker S",
 "scope_ru":["Вход в Service Mode.","Разделы: Drinks / Configurator / Inventory (Remains) / Dosages.","Где Change Drinks и Update Database.","Кликабельные иконки уровня (бутыль / стаканы / порошок).","Выход из сервисного режима перед уходом."],
 "scope_en":["Entering Service Mode.","Sections: Drinks / Configurator / Inventory (Remains) / Dosages.","Where Change Drinks and Update Database are.","Tappable level icons (bottle / cups / powder).","Exiting service mode before leaving."],
 "src":"Адаптировать заводскую страницу сервисного меню Milkshaker S под Shaker S; скриншоты — с Shaker S."},
{"num":13,"slug":"13-stimulant-safety","prio":2,
 "ru_title":"Безопасность: не превышать суточную дозу стимуляторов","en_title":"Safety: don’t exceed the daily stimulant dose",
 "scope_ru":["Для energy / preworkout / EAA / креатина — не превышать суточную норму с упаковки.","Слабый вкус → снижать воду, а не повышать порошок.","Пищевая ценность считается от реальной дозы."],
 "scope_en":["For energy / pre-workout / EAA / creatine — do not exceed the label’s daily serving.","Weak flavor → lower water, not more powder.","Nutrition facts reflect the actual dose."],
 "src":"Наши правила дозирования (dosing safety). Юридически важно."},
{"num":14,"slug":"14-preventing-powder-clogging","prio":2,
 "ru_title":"Профилактика слёживания / засора порошка","en_title":"Preventing powder clogging / caking",
 "scope_ru":["Влажность и слёживание — почему порошок комкуется.","Свободнотекучие порошки, плотная крышка, силикагель.","Меньше воздуха при пополнении; очищать белый лоток между выдачами."],
 "scope_en":["Humidity and caking — why powder clumps.","Free-flowing powders, tight lid seal, silica gel.","Minimize air on refill; clear the white tray between dispenses."],
 "src":"Практика поддержки."},
{"num":15,"slug":"15-error-code-index","prio":2,
 "ru_title":"Единый индекс кодов ошибок (все модели)","en_title":"Error code index (all models)",
 "scope_ru":["Список Error 1 / 5 / 7 / 9 / 11 / 18 / 19 / 603 → однострочное значение + ссылка на страницу.","Заметка: Error 11 в телеметрии показывается как «no cups».","Нормальные EN-ссылки на Error 9 / 11 (сейчас под RU-slug)."],
 "scope_en":["List Error 1 / 5 / 7 / 9 / 11 / 18 / 19 / 603 → one-line meaning + link.","Note: Error 11 shows as “no cups” in telemetry.","Proper EN links for Error 9 / 11 (currently under RU slugs)."],
 "src":"Индекс существующих страниц ошибок info.ishakerusa.com."},
{"num":16,"slug":"16-mixing-powders-creatine","prio":2,
 "ru_title":"Микс нескольких порошков + добавка креатина","en_title":"Mixing multiple powders + creatine add-on",
 "scope_ru":["Мультислотовые рецепты (протеин + креатин + BCAA).","Добавка креатина и её цена.","Почему стакан не переполняется (объём учтён)."],
 "scope_en":["Multi-slot recipes (protein + creatine + BCAA).","Creatine add-on and its pricing.","Why the cup doesn’t overflow (volume is accounted for)."],
 "src":"Наш процесс заведения микс-рецептов."},
{"num":17,"slug":"17-water-priming-air-lock","prio":2,
 "ru_title":"Прокачка воды / воздушная пробка — насос работает, воды нет","en_title":"Water priming / air lock — pump runs but no water",
 "scope_ru":["Насос шумит, но воды нет — как продуть трубку и выгнать воздух.","Проверить перегиб дренажного шланга.","Отличие от первичного подключения воды."],
 "scope_en":["Pump makes noise but no water — how to clear air from the tube.","Check for a pinched drain hose.","How this differs from initial water connection."],
 "src":"Заводская страница «Диагностика» (Shaker S / Milkshaker) — публикуемая часть."},
{"num":18,"slug":"18-water-source-bottle-vs-mains","prio":2,
 "ru_title":"Выбор / переключение источника воды: бутыль vs водопровод","en_title":"Water source: bottle vs mains, and switching",
 "scope_ru":["Можно ли работать только на бутыли без водопровода.","Переключение на водопровод (регулировка давления винтом).","Что удалённо настраивается только на бутыли."],
 "scope_en":["Can you run bottle-only with no plumbing.","Switching to mains (pressure adjust screw).","What can be adjusted remotely only on bottle."],
 "src":"Sibling к существующим страницам подключения воды."},
{"num":19,"slug":"19-cups-only-mode","prio":2,
 "ru_title":"Режим «только стаканы» (отключить чужой шейкер)","en_title":"Cups-only mode (disable bring-your-own-shaker)",
 "scope_ru":["Как включить режим «только стаканы» (защита механики от чужих шейкеров).","Обратная сторона: не отключить выдачу стаканов случайно.","Проверка после изменения."],
 "scope_en":["How to enable cups-only mode (protects the mechanics from oversized shakers).","The flip side: don’t accidentally disable cup dispensing.","Verify after the change."],
 "src":"Практика поддержки."},
{"num":20,"slug":"20-loyalty-cards-points","prio":3,
 "ru_title":"Лояльность: как работают карты и баллы","en_title":"Loyalty cards and points",
 "scope_ru":["Как копить и тратить баллы.","Карта / QR = всё, что нужно покупателю.","Серые, но рабочие кнопки лояльности."],
 "scope_en":["How to earn and spend points.","A card / QR is all the customer needs.","Loyalty buttons look grey but work."],
 "src":"Заводская страница «Система лояльности» — публикуемая, перевести/адаптировать."},
{"num":21,"slug":"21-cup-detection-compatibility","prio":3,
 "ru_title":"Тёмные / красные стаканы не распознаются","en_title":"Dark / red cups not detected",
 "scope_ru":["Тёмные и красные стаканы могут не читаться сенсором.","Используйте светлые стаканы.","Держите датчик в чистоте (после мойки)."],
 "scope_en":["Dark and red cups may not be read by the sensor.","Use light-colored cups.","Keep the sensor clean (after cleaning)."],
 "src":"Дополняет существующие страницы Error 5."},
{"num":22,"slug":"22-displayed-volume-vs-actual","prio":3,
 "ru_title":"Надпись объёма vs реальная доза (oz / ml)","en_title":"Displayed volume vs actual dose (oz / ml)",
 "scope_ru":["Как поменять надпись объёма (oz / ml) без изменения рецепта.","Метка ≠ реальная доза.","Надпись может вернуться после Update Database."],
 "scope_en":["How to change the volume label (oz / ml) without changing the recipe.","The label is not the real dose.","The label may revert after Update Database."],
 "src":"Практика."},
{"num":23,"slug":"23-screen-orientation","prio":3,
 "ru_title":"Экран перевёрнут / обрезан — ориентация (Touch)","en_title":"Screen upside-down / cut-off — orientation (Touch)",
 "scope_ru":["Экран перевёрнут или показан частями после перезагрузки/сессии.","Дать полностью загрузиться (2–3 минуты).","Если не исправилось — в поддержку."],
 "scope_en":["Screen rotated or shown in parts after a reboot/session.","Let it boot fully (2–3 minutes).","If not fixed — contact support."],
 "src":"Практика (Touch)."},
{"num":24,"slug":"24-idle-video-not-playing","prio":3,
 "ru_title":"Idle / attract-видео не проигрывается","en_title":"Idle / attract video not playing",
 "scope_ru":["Idle-видео может не стартовать после обновления.","Безопасные шаги (перезагрузка контроллера; rear switch крайнее средство).","Когда обращаться в поддержку."],
 "scope_en":["The idle video may not start after an update.","Safe steps (controller reboot; rear switch as last resort).","When to contact support."],
 "src":"Практика."},
{"num":25,"slug":"25-drip-tray-fills-with-water","prio":3,
 "ru_title":"Поддон / воронка наполняется водой в простое — это норма","en_title":"Drip tray / funnel fills with water when idle — normal",
 "scope_ru":["Нижний поддон собирает капли и промывку, слива нет.","Опорожнять вручную.","Это не протечка."],
 "scope_en":["The drip tray collects drips and rinse water; there’s no drain.","Empty it manually.","This is not a leak."],
 "src":"Практика."},
{"num":26,"slug":"26-water-wont-stop-calibration","prio":3,
 "ru_title":"Вода льётся без остановки при калибровке — аварийный стоп","en_title":"Water won’t stop during calibration — emergency stop",
 "scope_ru":["Вода не останавливается во время калибровки.","Безопасный способ остановить.","Почему так бывает; связка с калибровкой."],
 "scope_en":["Water doesn’t stop during calibration.","How to stop it safely.","Why it happens; ties to calibration."],
 "src":"Практика / калибровка."},
{"num":27,"slug":"27-requesting-spare-keys","prio":3,
 "ru_title":"Запрос дополнительных / запасных ключей","en_title":"Requesting additional / spare keys",
 "scope_ru":["Ключи кастомные, произвольно не дублируются.","Пришлите серийный номер машины.","Альтернатива — QR-доступ."],
 "scope_en":["Keys are custom-cut and not duplicated arbitrarily.","Send the machine serial number.","Alternative — QR access."],
 "src":"Без логистики и цен (это зона владельца)."},
{"num":28,"slug":"28-chiller-cooling","prio":3,
 "ru_title":"Чиллер / охлаждение — включение и температура","en_title":"Chiller / cooling — turning on and temperature",
 "scope_ru":["Как включить охлаждение и отрегулировать температуру.","Задняя панель Touch 2: две розетки C14 (верх = вход 220В, низ = выход для опц. чиллера).","Что не трогать на задней панели."],
 "scope_en":["How to turn on cooling and adjust the temperature.","Touch 2 back panel: two C14 outlets (top = 220V input, bottom = output for an optional chiller).","What not to touch on the back panel."],
 "src":"Заводская страница «Компрессорный охладитель» + подтверждение по задней панели Touch 2."},
{"num":29,"slug":"29-auto-wash-schedule","prio":3,
 "ru_title":"Авто-мойка / ополаскивание миксера — расписание","en_title":"Auto-wash / mixer rinse — schedule",
 "scope_ru":["Настройка авто-мойки (по времени / после каждого шейка).","Достаточно ли AutoClean vs ручная чистка.","Связь с профилактикой засора."],
 "scope_en":["Configuring auto-wash (by time / after each shake).","Is AutoClean enough vs manual cleaning.","Ties to clog prevention."],
 "src":"Дополнить существующие страницы обслуживания (SMS / Touch 1)."},
{"num":30,"slug":"30-third-party-mdb-terminals","prio":3,
 "ru_title":"Сторонние MDB-терминалы — совместимость","en_title":"Third-party MDB terminals — compatibility",
 "scope_ru":["Совместимость с MDB Level 3 устройствами (не только Nayax).","Что запросить у поставщика.","Аккуратно про «одобренность» — не обещать поддержку неподтверждённых терминалов."],
 "scope_en":["Compatibility with MDB Level 3 devices (beyond Nayax).","What to request from the supplier.","Careful about “approved” — don’t promise support for unverified terminals."],
 "src":"MDB-заметки по протоколу."},
]

def skel_body(scope, source, lang):
    head = "Что должна содержать" if lang == "ru" else "What this page should cover"
    srch = "Источник" if lang == "ru" else "Source"
    items = "\n".join("<li>%s</li>" % s for s in scope)
    return "<h2>%s</h2>\n<ul>\n%s\n</ul>\n<h2>%s</h2>\n<p>%s</p>" % (head, items, srch, source)

# ---------------- write files ----------------
def w(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)

w("assets/style.css", STYLE)

for a in P1:
    w("ru/%s.html" % a["slug"], page("ru", a["ru_title"], a["ru"], "../en/%s.html" % a["slug"]))
    w("en/%s.html" % a["slug"], page("en", a["en_title"], a["en"], "../ru/%s.html" % a["slug"]))

for s in SKELETONS:
    ru_src = s["src"]
    en_src = "See the Russian version — source: " + s["src"]
    w("ru/%s.html" % s["slug"], page("ru", s["ru_title"], skel_body(s["scope_ru"], ru_src, "ru"), "../en/%s.html" % s["slug"], DRAFT_RU))
    w("en/%s.html" % s["slug"], page("en", s["en_title"], skel_body(s["scope_en"], en_src, "en"), "../ru/%s.html" % s["slug"], DRAFT_EN))

# ---------------- index ----------------
def index_rows(items, is_skel):
    rows = []
    for it in items:
        tag = ' <span class="tag">🚧 каркас</span>' if is_skel else ""
        rows.append(
            '<li><span class="t">%d. %s%s</span><span class="links"><a href="ru/%s.html">RU</a><a href="en/%s.html">EN</a></span></li>'
            % (it["num"], it["ru_title"], tag, it["slug"], it["slug"]))
    return "\n".join(rows)

p1_rows = index_rows(P1, False)
p2_rows = index_rows([s for s in SKELETONS if s["prio"] == 2], True)
p3_rows = index_rows([s for s in SKELETONS if s["prio"] == 3], True)

index_html = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>iShaker Help — черновик</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">
<span class="badge">Draft / черновик</span>
<h1>iShaker Help</h1>
<p class="subtitle">Черновик справочных страниц для операторов. 10 приоритетных — с полным текстом (RU + EN); остальные — каркас (что писать + источник). Для внутреннего ревью перед публикацией.</p>
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
</html>""" % (p1_rows, p2_rows, p3_rows)

w("index.html", index_html)

print("Built: index.html + %d P1 pages + %d skeleton pages (x2 langs) + style" % (len(P1), len(SKELETONS)))
