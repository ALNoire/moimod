label label_day_6:
    $ persistent.sprite_time = "day"
    $ backdrop = "days" 
    $ new_chapter(5, u"Лето с Женей: День 5") 
    $ renpy.pause(2)
    $ renpy.block_rollback()

    play music music_list["door_to_nightmare"] fadein 2
    scene bg darksov
    show prologue_dream
    show pi far
    with dissolve

    pi "Вспоминай."
    ya "О чем ты?"
    pi "Ты и сам знаешь."
    pi "Сколько еще времени тебе нужно, чтобы понять?"
    ya "Я тебя не понимаю."
    pi "Скоро поймешь, но будет слишком поздно."

    show black with dissolve
    stop music fadeout 2
    $ renpy.pause (1, hard = True)
    scene bg dom with dissolve
    hide black
    with dissolve

    "О, боже."
    "Ну и хрень же приснится."
    "Оно и понятно. Столько событий за последние дни."
    "Мозг не справляется с таким количеством информации."
    scene bg ebalo with dspr
    "До сих пор поверить не могу."
    "Мне все это правда не снится."
    "Я действительно снова молодой и нахожусь в пионерском лагере."
    "Любой другой на моем месте уже с ума бы сошел, но только не я."
    "Даже самые фантастические вещи в моей жизни я принимал без удивления."
    "Временами, размышляя о жизни я даже жаждал сбежать подальше от собственной жизни."
    "Куда-то в другой город, страну или даже другой мир."
    "Но меня больше удивлял сам факт случившегося, чем все происходящее."
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_houses_day with dissolve
    "Одно я находил странным."
    "За несколько коротких дней я совершенно позабыл о многих вещах."
    "Будто они вытеснились новыми воспоминаниями."
    "Может, побочный эффект переноса."
    "Хотя, какая разница."
    "Несколько унылых фактов из прошлой жизни, кому она теперь нужна, когда я теперь не там."
    "Если автобус и правда был причиной всех событий, то в конце смены я вернусь домой и все вернется на свои места."
    "Никто даже не заметит моего отсутствия."
    "А вот хочется ли мне обратно? Большой вопрос на который пока нет ответа."
    "При всей моей неприязни к людям, это место вдохнуло в меня любовь к жизни."
    "С другой стороны, можно не садиться в автобус."
    "Остаться в этом мире."
    "Но куда мне пойти? Чем заняться?"
    "Если события будут складываться в правильной исторической последовательности, я бы мог сделать состояние на своих знаниях."
    "Даже если нет, я все равно знаю о будущем достаточно, чтобы как-то применить эти знания."
    "Все же, если история этого мира не сильно отличается от моей реальности, то и прогресс будет идти в похожем ключе."
    "Звучит, как план."
    "Вот только одна загвоздка."
    "Меня никто не знает, у меня нет документов."
    "Мои родители сейчас моложе меня и еще много лет не встретятся."
    "Слишком непростая задача на голодный желудок."
    stop ambience fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "Линейку я пропустил и сразу отправился в столовую."
    "Ольга Дмитриевна даже не пришла отчитывать меня за это."
    "Быть может, придумывает мне очередное наказание или просто смирилась с моей разгильдяйской натурой."
    "В любом случае, я был рад позавтракать в спокойной обстановке."
    "Смешавшись с толпой, я смог утащить пару лишних булок и улизнуть незамеченным."
    "Уж очень они были вкусными."
    "Съем позже или разделю с кем-то."
    stop music fadeout 2
    scene bg ext_square_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 1
    show dv normal pioneer close at center with dissolve
    if alis1 == True:
        dv "Привет, пионер."
        ya "Рад видеть, Алиса."
        show dv smile pioneer with dissolve
        "Я залез в карманы и вытащил пару булок, протянув девушке."
        ya "Стащил парочку, но что-то расхотелось."
        ya "Возьми, если хочешь."
        show dv shy pioneer with dissolve
        "Рыжая осторожно взяла у меня выпечку."
        dv "Они точно не ядовитые?"
        ya "Лично цианид насыпал."
        show dv smile pioneer with dissolve
        dv "Ладно, пока ты меня еще не подводил."
        ya "После всего, что с нами было, следовало бы и правда тебя отравить."
        ya "Но я, пожалуй, сделаю это в другой раз."
        jump day_5_1
    else:
        show dv angry pioneer with dspr
        dv "Чего тебе надо, предатель?"
        "Я залез в карманы и вытащил пару булок, протянув девушке."
        ya "Всего лишь хотел еще раз извиниться за тот случай."
        dv "Думаешь купить у меня прощение за булку?"
        ya "Нет, просто считаю, что виноват перед тобой."
        ya "Можешь не прощать, но булки возьми. Я виноват, должен тебе."
        "Возьми эти чертовы булки и отвали от меня, рыжая стерва."
        show dv normal pioneer with dissolve
        dv "Что это значит? Тебе наплевать на мое прощение? Зачем тогда тут любезничаешь?"
        ya "Я тебя подставил и сожалею об этом. Хочу сделать что-то хорошее и загладить вину."
        ya "Не ради твоего прощения. Хотя, я был бы рад, если ты не будешь держать обиды."
        dv "Странный же ты."
        dv "Ладно, давай сюда."
        "Двачевская ловко выхватила булки из моих рук."
        jump day_5_1

label day_5_1:
    show dv smile pioneer
    ya "Ну, пойду тогда."
    "Я уже собирался уйти, но Алиса окликнула меня."
    dv "Подожди."
    dv "Ты собираешься на пляж сегодня?"
    ya "А должен?"
    show dv angry pioneer with dspr
    dv "Обязан!"
    ya "С тобой спорить себе дороже."
    ya "Приду, раз так нужен."
    hide dv with dissolve
    "И зачем это я ей там понадобился?"
    "Лучше не расслабляться."
    "Не исключаю очередной подставы от рыжухи."
    scene ext_library_day with dissolve
    "Я отправился в библиотеку на поиски Жени."
    "На двери висел замок, хотя время уже приличное."
    "Обычно Женя приходит раньше."
    "Может, хоть сегодня не придется бегать по лесу и искать ее."
    "Хотя, где она еще может быть."
    "Стоит сходить к пляжу, если остальные там, то могут знать где она."
    stop ambience fadeout 2
    play ambience ambience_lake_shore_day fadein 1
    scene bg ext_beach_day with dissolve
    show dv smile swim close at left with dissolve
    dv "Я уже и не надеялась."
    ya "А чего бы не прийти."
    ya "Девчонки в мокрых купальниках - не худшее зрелище."
    dv "Вот только давай без извращенных фантазий."
    ya "Договорились, представляю молча."
    show dv normal swim close with dspr
    dv "Вообще никак нельзя!"
    ya "Я понял, не злись только."
    show dv normal swim close with dspr
    ya "Я Женю искал, не видела ее?"
    dv "Так вон она с остальными плещется."
    dv "И сдалась же она тебе..."
    dv "Женя, по твою душу пришли."
    "Евгения выскочила из воды и подошла к нам."
    show zh fun swimsuit far at right with dissolve
    "В таком виде я даже не сразу узнал ее."
    "Несмотря на самую обычную фигуру и маленький рост, в купальнике она смотрелась просто шикарно."
    "Я не мог отвести взгляда."
    show zh fun swimsuit close at right with dissolve
    mz "Чего так пялишься? Книгой по голове давно не получал?"
    ya "На мое счастье, у тебя ее нет."
    mz "А это легко исправить можно."
    show zh sceptic swimsuit close with dspr
    ya "Не ожидал увидеть тебя тут."
    mz "Считаешь, что я только сплю и книги читаю целыми днями?"
    ya "В основном."
    mz "Погода хорошая, да и..."
    show zh angry swimsuit close with dspr
    mz "А ну брысь отсюда, Двачевская. Чего уши греешь? Не видишь, у нас тут личный разговор."
    show dv grin swim close with dissolve
    dv "Ой, больно надо мне ваши секреты слушать."
    mz "Вот и иди."
    dv "Вот и пойду."
    hide dv with dissolve
    show zh normal swimsuit close with dspr
    mz "На чем мы остановились?"
    ya "С чего это ты вдруг на пляж к остальным пришла."
    show zh shy swimsuit close with dspr
    mz "А вот так."
    mz "Настроение хорошее."
    ya "У меня тоже."
    ya "Хотел предложить тебе кое-чего сегодня."
    show zh sceptic swimsuit close with dspr
    mz "Говори."
    mz "Но учти. Тяжелой книгой я тебя огреть в любой момент могу."
    ya "Всего лишь хотел позвать тебя прогуляться сегодня ночью."
    mz "Почему ночью?"
    ya "Романтичное время. Тишина, звезды светят."
    show zh excitement swimsuit close with dspr
    mz "Даже и не знаю. Страшно ночами бродить, да и кто же нас отпустит."
    ya "А зачем спрашивать?"
    show zh shyangry swimsuit close with dspr
    mz "Это еще что за разговоры такие!"
    mz "Может для тебя это и ничего страшного, но я дорожу своей репутацией и нарушать режим не собираюсь."
    ya "Не будь такой занудой. Мы тихо сбежим. Никто и не заметит."
    mz "Ты ничем не рискуешь, а на мне большая ответственность, которую я не собираюсь обменивать на спонтанные ночные блуждания."
    ya "Почему?"
    show zh angry swimsuit close with dspr
    mz "Потому!"
    ya "Значит, я зайду после отбоя?"
    show zh normal swimsuit close with dspr
    mz "Попробуй."
    "Ну вот. Так бы сразу, а то не хочу, не буду."
    stop ambience fadeout 2
    scene bg ext_square_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 1
    "Я вернулся на площадь."
    "Из головы не выходил этот сон и тот странный пионер."
    "Странно искать в снах какую-то логику."
    "Это ведь просто бред уставшего сознания."
    "А уж тем более в нынешних обстоятельствах."
    "Что я должен вспомнить?"
    "Не знаю почему, но одна вещь все же казалась мне подозрительной."
    "Я совершенно не мог вспомнить имя своей собаки, с которой прожил двенадцать лет."
    "Как бы я не напрягал свой мозг, все было тщетно."
    "За ним выяснилось, что я так же не могу вспонить ни единого однокурсника по своему поганому колледжу."
    "Хотя, я не уверен, что вообще когда-то знал хоть кого-то из них по имени."
    "Но все это казалось малозначимым перед главным вопросом."
    "Когда я сюда попал?"
    "Какой был день?"
    "Телефон уже отрубился без зарядки и посмотреть не представлялось возможным."
    "Если поездку в автобусе еще можно было отнести к загадкам перемещения во времени, то вот события предшествующие этому не должны быть такими непонятными."
    "Только сейчас мне пришло осознание того, что я вообще не помню события последних недель своей жизни до лагеря."
    "Те немногие путанные фрагменты, которые я мог соотнести с датой не проясняли ровным счетом ничего важного."
    "Стоит поискать того пионера и задать ему пару вопросов."
    "Он явно знает больше, чем хочет говорить."
    "Время в абтрактых размышлениях шло незаметно."
    "Так и просидел на площади до обеда."
    "Еще статуя эта дебильная."
    "Не помню такого деятеля. Может, какой-то мелкий партийный чиновник с манией величия?"
    "Или основатель лагеря."
    "Да и какая разница, пора на обед."
    stop ambience fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "Надо же, никаких навязчивых обитателей лагеря не спешат пристать ко мне со своими дурацкими вопросами."
    "Я почти счастлив."
    show us smile sport close at right with dissolve
    "Ну, нет..."
    us "Чего тут один сидишь? Алиса прогнала, за что пристаешь к ней?"
    ya "Тебе что надо, зараза мелкая?"
    us "Какой же ты злобный, чего только все в тебе находят."
    ya "Свалила отсюда, пока я тебе чай на голову не вылил."
    us "Смотри котлетой не подавись."
    ya "Ну все, конец тебе..."
    "Я демонстративно поднялся со стула и схватился за стакан, готовясь выплеснуть чай на эту приставучую дрянь."
    show us fear sport close at right with dissolve
    hide us with dissolve
    "Так-то."
    "В следующий раз подумает как не в свои дела лезть."
    "Я вернулся к еде, но покой продлился не долго."
    show mi smile pioneer far at center with dissolve
    mi "Как дела? Чего к нам в клуб не заходишь? У нас концерт скоро. Мы с Алисой еще играем. Тебе музыка нравится? А какая?"
    ya "А можно помедленнее? Я за ходом твоих мыслей не успеваю."
    mi "Конечно, извини. Мне многие говорят, что я черезчур разговорчива."
    mi "Ничего не могу с собой поделать."
    ya "Давай по порядку. Чего тебе от меня нужно? Не просто же так пришла."
    mi "Пригласить на репетицию. Алиса много о тебе говорила, думаю она тоже будет рада."
    ya "Я бездарен и у меня нет слуха. Играть ни на чем не умею, пою тоже отвратительно." 
    ya "Не будет от меня пользы, да я и сам желанием не горю."
    mi "А ты приходи послушать. Будет весело."
    ya "Загляну, если будет время."
    ya "А теперь, пожалуйста, дай мне спокойно пообедать."
    mi "Конечно, приходи, в любое время ждем тебя."
    hide mi with dissolve
    "Свалила наконец, я уж думал не заткнется."
    "Не знаю почему, но я не мог просто послать Мику куда подальше."
    "Может, тому виной было ее искреннее дружелюбие и неиссякаемая энергия."
    "Хоть меня и раздражали такие гиперактивные и жизнерадостные люди, но обижать ее просто за сам факт такого поведения казалось невероятно плохой идеей."
    "Совсем другое дело - Ульяна."
    "К ней я не питал ни капли жалости или угрызений совести."
    stop ambience fadeout 2
    scene bg ext_houses_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 1
    "После обеда хотелось пройтись и еще раз подумать о чем-то, но лучше не попадаться кому-либо на глаза."
    "Будто каждый в этом лагере только и ждет, как бы достать меня своими разговорами."
    "Пойти прогуляться по лесу?"
    "Слишком велик шанс встретить кого-то, да и тащиться туда мне лень."
    "Еще и солнце жарит, к черту этот лес. Лучше спрячусь в домике."
    "Там-то меня точно никто искать не будет."
    "Но едва я подошел к своему, меня встретила Алиса."
    show dv smile pioneer close at center with dissolve
    ya "Только не говори, что..."
    dv "Мне нужна твоя помощь."
    ya "Именно."
    ya "Чего на этот раз? Бомбу собрать?"
    dv "Нет, просто разобраться с одним делом."
    dv "Мне надо достать одну вещь из медпункта, но мне ее не дадут."
    ya "И ты хочешь, чтобы я снова взял на себя все проблемы?"
    show dv angry  pioneer close
    dv "Отвлеки медсестру и все. Неужели это так сложно?"
    ya "Ладно, пойдем."
    stop ambience fadeout 2
    scene bg ext_aidpost_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 1
    "Алиса разделилась со мной, не доходя до медпункта."
    "Отправилась занимать позицию в ближайших кустах, чтобы потом незаметно проскочить."
    stop ambience fadeout 2
    scene bg int_aidpost_day with dissolve2
    play sound sfx_open_door_1
    play ambience ambience_day_countryside_ambience fadein 1
    "На удивление, медсестры не было на месте. За столом в ее отсутствие сидела Лена, листающая журнал."
    "Она даже не сразу заметила меня."
    show un normal pioneer close at center
    ya "А где медработник?"
    un "Она ушла по какому-то важному делу. Попросила меня посидеть."
    "Так даже проще, не придется разыгрывать сцену с болезнью."
    "С другой стороны, у меня не было ни одной идеи, как и зачем можно выманить ее наружу."
    ya "Слушай, Лена. Мне твой совет нужен."
    un "Мой?"
    "Лена явно удивилась, что кто-то спросил ее мнения."
    ya "Давай выйдем на улицу."
    un "Зачем?"
    ya "Так нужно. Ничего за пару минут не случится."
    stop ambience fadeout 2
    scene bg ext_aidpost_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 1
    play sound sfx_open_door_1
    show un smile pioneer close at center with dissolve
    "Лена на улице, Алиса тут же заскочила внутрь."
    "Мне же предстояло придумать не совсем идиотскую причину по которой я вытащил сюда Лену."
    ya "Кто твоя соседка?"
    un "Мику, а что?"
    ya "Ну, короче, это самое..."
    "Как же я нелепо сейчас выгляжу."
    "Самому за себя стыдно."
    "Алиса, что ты там так долго."
    un "Что?"
    ya "Хотел узнать про нее..."
    ya "Ну, ты понимаешь."
    show un normal pioneer close at center with dissolve
    un "Не очень."
    "Алиса наконец выбралась."
    "Она бесшумно прокралась мимо, прижимая к груди бумажный сверток с награбленным."
    "Солидный запас."
    "Интересно, что там у нее."
    "Мультики без телевизора смотреть?"
    "На целый сезон хватит, а то и на два."
    "Лена ничего не заподозрила."
    "За исключением того, что считает меня идиотом, а еще, вероятно, ей влетит за пропажу."
    "Плевать, это не на моей совести. Я лишь невольный соучастник, в очередной раз доверившийся рыжей преступнице."
    ya "Чего-то зря я пришел, надо было у самой Мику спросить."
    ya "Извини, что потревожил."
    un "Ничего страшного, я пойду."
    hide un with dissolve
    "Все таки, Алисе стоит объясниться."
    "Где ее теперь искать только?"
    "Сама найдет. А я пойду куда планировал. Отдохну утомляющих социальных контактов."

    stop ambience fadeout 2
    scene black with dissolve
    $ renpy.pause (0.3, hard = True)
    show pi smile close at center with dspr
    $ renpy.pause (0.5, hard = True)
    hide pi with dspr
    $ renpy.pause (0.3, hard = True)
    play ambience ambience_day_countryside_ambience fadein 1
    scene bg dom with dissolve
    
    "Странный пионер."
    "Я не видел его на утренних линейках или на площади."
    "Даже в столовой за все эти дни, хотя туда приходят все отряды без исключения."
    "Есть ли смысл спрашивать о нем у кого-то из лагеря?"
    "Это пионер, который выглядит как пионер, который пионер в пионерской форме, то есть вообще кто угодно."
    "Но не может же он не существовать?"
    "Должны быть какие-то списки по отрядам и по лагерю."
    "Еду и остальные ресурсы выделяют на конкретное количество людей. Всякие обходные листы, читательские билеты и прочая бюрократия."
    "У кого может храниться такой список?"
    "Вряд ли вожатая для себя обходные собирала."
    "А другой лагерной администрации я в глаза не видел. Даже не уверен, что она существует."
    play sound sfx_muffled_explosion
    "Какого..."
    "От грохота я слегка испугался."
    stop ambience fadeout 2
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_day_countryside_ambience fadein 1
    play sound sfx_open_door_1
    "Я вышел на улицу, осмотреться."
    "Грохот привлек не только мое внимание."
    "Другие пионеры тоже в недоумении оглядывались, выискивая источник взрыва."
    "Между домиков выскочила Алиса."
    "И почему я не удивлен."
    show dv sad pioneer2 close at center with dspr
    dv "Спрячь меня, срочно!"
    ya "С ума сошла?"
    dv "Срочно!"
    ya "Ладно, заходи."
    "Я пустил ее в свой домик."
    hide dv with dissolve
    "И как ей только удается втягивать меня во все новые и новые проблемы."
    show mt angry pioneer close at center with dissolve
    mt "Где эта бандитка?"
    ya "Вы кого-то конкретного имеете ввиду или..."
    mt "Двачевская."
    ya "Пробегала тут, не знаю куда. А что случилось?"
    show mt normal pioneer close with dissolve
    mt "А ты не слышал этот грохот?"
    ya "Уверены, что это она?"
    mt "Поскольку ты здесь, больше некому."
    ya "Приятно знать, что не я причина всех бед лагеря."
    mt "Ладно, ступай. Мне еще разыскивать эту негодницу."
    hide dv with dissolve
    "Вроде ушла."
    "Надо сообщить Алисе, что угроза миновала."
    stop ambience fadeout 2
    scene bg dom
    show dv smile pioneer2 close at center
    with dissolve
    dv "Ушла?"
    ya "Да, не выдал тебя, как видишь."
    ya "Хоть и мог."

    if alis1 == True:
        dv "Не сомневалась в тебе."
        ya "Повода не давал, вроде."
        jump day_5_2
    else:
        dv "Надо же, в этот раз прикрыл меня."
        ya "Испавляюсь, как видишь."
        jump day_5_2

label day_5_2:
    show dv normal pioneer2 close at center
    dv "В любом случае - спасибо."
    ya "У тебя настоящий талант втягивать меня в неприятности."
    ya "Чего натворила хоть?"
    show dv surprise pioneer2 close at center
    dv "Сделала одну штуку из того, что удалось стащить из медпункта."
    dv "Подменила в клубе энергетиков порошок, они включили свою машину и тут ''бабах''!"
    show dv laugh pioneer2 close at center
    "Алиса громко рассмеялась."
    dv "Видел бы ты их рожи."
    ya "Могу себе представить."
    "Терроризм, вместо производства наркотиков."
    "Алиса умеет удивить."
    ya "Теперь тебе серьезно прилетит от вожатой."
    dv "Просто не буду попадаться ей на глаза, а там она и забудет."
    ya "Такое не забывается."
    dv "Я Ольгу Дмитриевну знаю. Она быстро успокоится."
    ya "Хорошо, если так."
    show dv normal pioneer2 close at left with dspr
    dv "Нам надо держаться вместе."

    if alis1 == True:
        dv "Ты всегда прикроешь, тебе можно довериться."
        dv "Редкая черта."
        ya "А ты всегда втянешь в неприятности."
        ya "Да, мы и правда отличная команда."
        jump day_5_3
    else:
        ya "Еще совсем недавно проклинала меня."
        dv "Ты смог исправиться, надеюсь, не ошиблась, дав тебе второй шанс."
        ya "Постараюсь оправдать доверие."
        jump day_5_3

label day_5_3:
    show dv smile pioneer2 close at left with dspr
    dv "Ты это..."
    dv "Заглядывай, если помощь будет нужна."
    ya "Буду иметь ввиду."
    dv "Тогда до встречи."
    dv "Мне еще от вожатой скрываться до конца дня."
    ya "Желаю удачи."
    hide dv with dissolve
    "Интересно получается."
    "В любой другой ситуации я бы не стал помогать, но в Алисе будто было что-то зловещее, но в то же время притягательное."
    "Хотя, так можно было сказать и про всех остальных."
    "Почти всех..."
    "Загадочное место все же."
    "Даже из такого безразличного разгильдяя вроде меня получился активный участник местных интриг."
    "Пусть это и не выражается в честном пионерском труде. Другие вон тоже не спешат. Я хотя бы социалистическую собственность не взрываю, как некоторые."
    stop ambience fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "Вот так стремительно пролетел очередной день."
    "Едва проснулся, а уже ужин."
    "Все хорошее, что было остается в прошлом, а впереди ждет лишь пугающая неизвестность."
    "Дни идут, а я ни на шаг не продвинулся к разгадке этого странного места."
    "Потратил время на развлечения и другие бессмысленные вещи."
    "Мне не привыкать бездарно растрачивать жизнь."
    "И почему именно сейчас мне в голову лезут эти мысли?"
    "Почему именно в такое прекрасное время я не могу отбросить все рассуждения и просто наслаждаться происходящим?"
    "Сам себе душу терзаю. Думаю о будущем, которое, может, вообще никогда не наступит, вместо того, чтобы жить здесь и сейчас."
    "Ай, да пошло оно все!"
    "Что там Мику говорила? Репетиция?"
    "Отлично."
    stop ambience fadeout 1
    play ambience ambience_ext_road_night fadein 1
    scene bg ext_stage_normal_day with dissolve
    $renpy.pause (2)
    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night with dissolve
    "Я прождал девочек до темноты."
    "Мику объявилась, а вот Алисы пока еще не было."
    "Наверное, попалась Ольге Дмитриевне или скрывается."
    show mi smile pioneer close at center with dissolve
    mi "Как я рада, что ты пришел."
    ya "Долго вы чего-то. И где Алиса?"
    mi "Ждала ее в музыкальном клубе, но не дождалась, решила идти одна."
    mi "Алиса давно уже должна прийти."
    ya "Днем у нее были некоторе сложности. Задерживается, наверное."
    show mi normal pioneer close at left with dissolve
    mi "Можем пока вдвоем попробовать."
    ya "Нет уж, спасибо. Я ни разу в жизни не играл."
    show mi happy pioneer close
    mi "Это не сложно, я научу. Бери гитару и просто повторяй."
    "И кто меня сюда прийти тянул, спрашивается."
    "Придется участвовать."
    scene bg mikusong with dissolve
    play music gitara
    $ renpy.pause (5, hard = True)
    "Мику начала играть приятную мелодию, которая почему-то казалась до боли знакомой."
    "Я был уверен, что уже где-то слышал ее, но никак не мог вспомнить."
    "Может, в каком-то старом фильме или даже в игре."
    "Но попытки напрячь извилины только раздражали и отвлекали меня от и без того неумелых попыток повторить движения."
    "Моим рукам не доставало уверенности и точности, чтобы играть так же, как она."
    "Даже несмотря на то,что мелодия казалось не очень сложной."
    "В какой-то момент Мику увлеклась игрой настолько, что не заметила, как я перестал играть, чтобы не портить звучание."
    stop music fadeout 2
    scene bg ext_stage_normal_night
    show mi normal pioneer close at left
    show dv normal pioneer close at center
    with dissolve
    dv "Ого, не знала, что ты тоже играешь."
    ya "Ну уж нет! С меня хватит позориться."
    show dv smile pioneer close with dissolve
    dv "Поздно заднюю давать. Начинайте, а я послушаю."
    "О, господи..."
    ya "Ладно, выбора у меня нет, но за последствия не ручаюсь."
    scene bg mikusong2 with dissolve
    play music gitara
    $ renpy.pause (5, hard = True)
    "Все пошло заново."
    "На этот раз у меня получалось чуть лучше, хоть далеко не идеально."
    "И мне все еще было стыдно за свою убогую игру."
    "Но Алиса, при всей своей язвительности отнеслась с пониманием."
    stop music fadeout 2
    scene bg ext_stage_normal_night with dissolve
    "Время уже позднее, пора тактично свалить."
    "А то Женя уснет и я ее на улицу не вытащу."
    show dv normal pioneer close at center with dissolve
    show mi normal pioneer close at left with dissolve
    mi "Уже уходишь?"
    ya "Еще дела остались."
    mi "Вот как..."
    show mi smile pioneer close at left with dissolve
    mi "Было весело."
    show dv normal pioneer close at center with dissolve
    dv "Ага, особенно твоя бесподобная игра на гитаре."
    ya "Да, спасибо за поддержку."
    dv "А ты как хотел? Сразу мастерски отыграть?"
    ya "Я вообще никак не хотел, это твоя идея была."
    dv "Ну и что."
    ya "Удачного вечера, девочки."
    mi "И тебе."
    scene bg domzh with dissolve
    ya "Женя, спишь?"
    "Я старался сказать это негромко, чтобы не разбудить остальных, но достаточно, чтобы она могла услышать."
    mz "Тихо ты! Сейчас весь лагерь проснется."
    "Донесся ее голос из приоткрытого окна."
    play sound sfx_open_door_1
    show zh normal pioneer glasses close at left with dspr
    ya "Идем?"
    mz "Куда ты меня затащить собрался среди ночи?"
    ya "Не знаю, прогуляемся где-нибудь."
    show zh fun pioneer glasses close at center
    mz "Странный же ты."
    ya "Когда еще такой шанс представится?"
    ya "Безоблачная ночь, полная луна и звездное небо."
    ya "Только ты и я. Никто не потревожит."
    show zh shy pioneer glasses close at left with dspr
    mz "Ну хватит речи тут зачитывать, не на партсобрании."
    mz "Я ведь уже согласилась."
    mz "Веди."
    scene bg ext_houses_night
    show zh normal pioneer glasses close at left with dspr
    mz "Кто это там?"
    show dv smile pioneer close at right with dissolve
    ya "Алиса?"
    dv "Куда это вы собрались среди ночи?"
    show zh angry pioneer glasses close at left with dspr
    mz "Не твое дело, Двачевская."
    ya "Прогуляться решили, ничего криминального."
    dv "Тогда пойду с вами."
    mz "Никуда ты с нами не пойдешь!"
    show dv angry pioneer close at right
    dv "А чего это ты решать вздумала?"

    menu:
        "Пойти с Алисой":
            ya "Не ругайтесь. Пусть Алиса пойдет с нами."
            mz "Мы так не договаривались. Пусть уходит."
            ya "Не будь такой вредной, что плохого, если Алиса пойдет?"
            show zh sad pioneer glasses close at left
            show dv smile pioneer close at right
            mz "Ладно."
            "Идея, мягко говоря, не внушала оптимизма."
            "Хорошо если эти двое не подерутся в процессе, в чем я сомневался с каждым нашим шагом."
            scene bg genda with dissolve
            show zh angry pioneer glasses close at left
            show dv angry pioneer close at right
            mz "Все, иди домой!"
            dv "Сама иди, детское время кончилось."
            mz "Он меня позвал, а ты навязалась. Уж если кому-то и стоит уйти, то явно не мне."
            dv "Зато со мной он весь день был, пока ты занималась неизвестно чем и неизвестно с кем."
            show zh rage pioneer glasses close at center
            mz "Я перед тобой отчитываться не собираюсь. Алиса - вечная проблема."
            show dv rage pioneer close at right
            dv "Расскажи ему зачем к тебе Электроник приходил утром. Думала, я не видела?"
            mz "Хватит совать нос в чужие дела!"
            dv "Ага, задела тебя за больное?"
            dv "Вот, посмотри с кем ты связался."
            dv "Книжки она читает, порядочная, как же."
            mz "Ты на себя посмотри."
            "Ситуация начала выходить из под контроля."
            ya "Успокойтесь обе!"
            ya "Вы чего тут устроили?"
            show zh normal pioneer glasses close at left
            show dv normal pioneer close at right
            mz "Она первая начала, зачем ты вообще ее позвал?"
            mz "Я думала, это наш с тобой вечер."
            dv "Может, я тоже хочу? С чего ты себе его присвоила?"
            mz "Он сам сказал мне об этом."
            show dv smile pioneer close at right
            dv "Да чтобы кто-то на тебя засмотрелся? Не смеши."
            show zh angry pioneer glasses close at center
            mz "Представь себе, не всем нравятся твои выходки."
            ya "Я же сказал вам! Хватит!"
            show dv sad pioneer close at right with dissolve
            dv "Раз тебе инетресней с этой зазнавшейся дурой, так тому и быть."
            dv "Желаю вам счастья."
            hide dv with dissolve
            ya "Алиса, стой."
            "Двачевская убежала, не оборачиваясь."
            show zh normal pioneer glasses close at center
            mz "Наконец-то ушла."
            mz "Сил никаких нету ее слушать."
            ya "Ну зачем ты так. Неужели нельзя было без скандала?"
            show zh bukal pioneer glasses close at left
            mz "В следующий раз подумает прежде чем лезть в чужие дела."
            ya "Добром это не кончится."
            ya "Только сейчас что-то объяснять уже бессмысленно."
            ya "Возвращаемся к прогулке. Алиса пусть до утра успокоится."
            jump day_5_4

        "Прогнать Алису":
            ya "Алиса, не обижайся, но мы хотели отправиться вдвоем."
            dv "Тогда я расскажу Ольге Дмитриевне, что вы ушли гулять ночью."
            mz "Только посмей!"
            ya "Вот ты как? После всего, что я сделал?"
            show dv rage pioneer close at right
            dv "Да идите вы оба... Куда хотите."
            dv "А еще пусть расскажет что она утром с Электроником делала."
            hide dv with dissolve
            show zh sad pioneer glasses close at center with dissolve
            ya "Никому она не пожалуется. Ей от вожатей в первую очередь попадет за сегодняшнее."
            jump day_5_4

label day_5_4:
    scene bg ext_polyana_night
    show zh normal pioneer glasses close at left with dissolve
    ya "Так что там с Электроником?"
    mz "Ничего. Пришел этот полоумный ко мне с утра, начал про чувства свои говорить."
    ya "А ты?"
    mz "А что я? Прогнала его, сказала чтоб больше на порог мне не являлся."
    mz "Мне больше интересно что там у вас с Алисой."
    ya "Ничего."
    show zh bukal pioneer glasses close at left with dissolve
    mz "А чего она тогда вокруг тебя бегает постоянно?"
    ya "Вот и спросила бы у нее сама."
    show zh sad pioneer glasses close at left with dissolve
    mz "Мне и так все предельно понятно."
    mz "Нашел кого получше, а мне прямо сказать уже смелости не хватает."
    ya "Все совсем не так."
    show zh cry pioneer glasses close at left with dissolve
    ya "Я тебя ни в чем не обманул, все, что я говорил, было правдой."
    ya "И от своих слов я не отказываюсь."
    mz "Не верю я тебе."
    ya "Да почему все так сложно с тобой?"
    mz "Вот и нечего себя утруждать."
    ya "Замолчи, Женя."
    mz "И не поду..."
    scene bg posl3 with dspr
    $ renpy.pause (5, hard = True)
    scene bg ext_polyana_night 
    show zh shyangry pioneer glasses close at left 
    with dissolve
    if priz == True:
        mz "Ты чего это такое делаешь?"
        ya "Ну а как еще мне тебе объяснить."
        mz "Не знаю."
    else: 
        mz "И все-то ты целоваться лезешь."
        mz "Подлец."
        ya "Не знаю, как объяснить тебе иначе."

    ya "Женя, поверь мне."
    ya "Я был серьезен тогда и моя убежденность никуда не делась."
    ya "Ты одна мне нужна. Никто другой."
    show zh shy pioneer glasses close at left with dissolve
    mz "Хорошо, верю."
    "Женя взглянула в небо."
    scene bg zvezdi with dissolve
    play music bybd3 fadein 2
    mz "Красиво."
    ya "И не говори."
    mz "О чем думаешь?"
    ya "А надо? Просто наслаждаюсь видом."
    ya "И тому, что ты рядом."
    mz "Ну ладно тебе, скажешь тоже."
    mz "Чего же во мне такого особенного?"
    ya "Что-то есть. Сам не знаю, но чувствую это."
    mz "Не знаешь, дурак."
    ya "Если без этого нельзя, пусть буду дураком."
    mz "Чего же в этом хорошего?"
    ya "Много думать - вредно."
    ya "Вот так задумаешься однажды и чего-нибудь нехорошее придумаешь."
    mz "Хитро ты все заворачиваешь."
    ya "Есть такое."
    mz "Но в одном ты прав. Сейчас думать - это лишнее."
    mz "Когда еще так спокойно посидеть удастся."
    mz "Скоро конец смены, а там учеба, экзамены и взрослая жизнь. И с тобой, скорее всего мы тоже больше никогда не увидимся."
    ya "А вот это ты точно зря начинаешь."
    mz "Стараюсь не думать."
    ya "Вот и я..."
    stop music fadeout 2
    scene bg ext_house_of_dv_night with dissolve
    "Мы пробыли на нашей поляне еще какое-то время, после чего вернулись в лагерь."
    "Теперь надо не привлекая внимания вернуться домой."
    show zh normal pioneer glasses close at left with dissolve
    show us sad sport close at right with dissolve
    mz "Почему не в кровати еще, на часы смотрела?"
    us "Я не могу одна. А Алиса так и не пришла. Вы ее не видели?"
    "Этого только не хватало."
    "Я посмотрел на Женю неодобрительным взглядом."
    ya "И где теперь ее искать?"
    mz "Иди к себе, Ульяна. Мы поищем Алису."
    us "Вы ее точно найдете?"
    mz "Найдем, куда она денется."
    "Мне бы твою уверенность."
    hide us with dissolve
    ya "Ну и где нам ее искать?"
    ya "Лагерь большой, а пойти она могла куда угодно."
    mz "Есть у меня одна догадка. Идем."
    scene bg ext_boathouse_night with dissolve
    show zh normal pioneer glasses close at left with dissolve
    ya "Одной лодки не хватает."
    mz "Значит, мы на верном пути."
    ya "Уплыла куда-то?"
    mz "Да, на остров. Они часто туда с Леной уплывали, уж не знаю зачем."
    ya "Может, я один за ней схожу?"
    mz "Попробуй."
    stop ambience fadeout 2
    play ambience ambience_boat_station_night fadein 1
    scene bg boat with dissolve
    $ renpy.pause (5, hard = True)
    "Надеюсь, у Алисы хватило ума не совершить какую-нибудь глупость."
    "Мне льстило внимание сразу двух девушек, но проблем от таких симпатий оказалось больше, чем хотелось."
    "Еще и Женя злится."
    "Что Алиса, что Женя - девушки крайне темпераментные. За словом в карман не полезут и насилием не побрезгуют."
    scene bg ext_island_night with dissolve
    show dv sad pioneer close at center with dissolve
    dv "Ты откуда тут? Как нашел меня?"
    ya "Не одна ты такая хитрая."
    dv "Чего надо?"
    ya "Пока мы все еще сохраняем самообладание, я скажу."
    ya "Алиса, мы все за тебя переживаем."
    dv "А зачем?"
    dv "Какое вам дело до вечно мешающей всем злодейки. Которая только и жаждет сотворить какую-то гадость."
    dv "Пропадет и ладно, всем только лучше станет."
    show dv cry pioneer close at center with dspr
    ya "Не говори глупостей. Мы с тобой отлично ладили. Что случилось?"
    dv "Будто ты не знаешь. Не строй из себя идиота."
    ya "Если тебе нужно побыть одной, это понятное чувство. Я просто хотел убедиться, что с тобой все хорошо. Ульяна тебя искала."
    show dv sad pioneer close with dspr
    dv "Ничего со мной не случится. Побуду тут и вернусь обратно."
    ya "Алиса, послушай..."
    dv "Ничего не говори. Со мной все будет нормально. Оставьте меня одну."

    scene black with dissolve
    stop ambience fadeout 2
    $ renpy.pause (2, hard = True)
    scene bg dom with dissolve
    
    "Просто сумасшедший день."
    "Мы попрощались с Женей и я незамедлительно отправился к себе в домик."
    "Сил оставалось только лечь и закрыть глаза."
    show blink
    $renpy.pause (2)
    scene black
    th "Продолжение следует."