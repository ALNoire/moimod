label label_day_4:
    $ persistent.sprite_time = "day"
    $ backdrop = "days" 
    $ new_chapter(3, u"Лето с Женей: День 3") 
    $ renpy.pause(2)
    $ renpy.block_rollback()

    play music music_list["memories"] fadein 2
    scene bg dom with dissolve

    "День начался очень даже неплохо."
    "Я выспался."
    "Приятные воспоминания о вчерашнем вечере еще грели мою дущу."
    "Тот странный пионер подтвердил мою догадку. Все дело в автобусе."
    "Но вместо томительного ожидания неизвестного я решил полностью отдаться тому, что происходит здесь и сейчас."
    "В конце концов, это самое увлекательное приключение в моей скучной и несчастной жизни."
    "Если подумать, в той реальности меня ничего не держало. Ни друзей, ни семьи, ни возлюбленной."
    "Родители жили отдельно и мы почти не общались. Ни у меня, ни у них не было к этому стремления. Мы были едва ли не чужими людьми с тех пор, как я закончил учебу и навсегда оставил их."
    "Все остальное для меня превратилось в один бесконечно повторяющийся цикл. Бессмысленное существование во имя утоления базовых потребностей."
    "Даже не жизнь, а так... Существование."
    "За время, которое я провел здесь, случилось столько удивительных событий, сколько не наберется за последний год в моей реальности."
    "И где же тогда эта реальность? Пустая, серая обыденность без цели и радостей? Или яркие, живые образы? Люди, в чьих лицах есть жизнь, а не презрение ко всему сущему."
    "Я наконец чувствовал что-то. Не был ходячим трупом."
    "Кто бы и зачем сюда меня не отправил, я как минимум рад, что этот неведомый добродетель показал мне другой мир."
    "Показал, что жить можно не вопреки, а наслаждаться. Теплотой солнца, прохладным ветром, другими людями." 
    "Жалею только о том, что не сразу осознал этого."
    "Лето, лагерь и детская беззаботность. Чего еще я мог желать?"
    "Временные парадоксы, параллельные миры, какая разница?"
    "Проблемы надо решать по мере поступления, а сейчас я хочу жить и радоваться."
    stop music fadeout 2
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_houses_day with dissolve
    "Самому удивительно с какой радостью я встречаю новый день в лагере."
    "Линейки, различная самодеятельность, которые я ненавидел в детстве и юности, теперь кажутся чем-то приятным и вдохновляющим."
    "Даже не самим фактом наличия, как помогают общей атмосфере."
    "Сегодня мне хотелось провести день в ярких эмоциях."
    "Утренний ветер приятно пробежал по коже, наполнил легкие чистым, свежим воздухом."
    "Я взглянул на мирно плывущие облака и медленным шагом пошел на площадь."
    scene bg ext_square_day with dissolve
    "Сегодня даже не опоздал."
    show mt normal pioneer far at center with dissolve
    mt "Все в сборе."
    mt "Сегодня планируется лагерный чемпионат по волейболу."
    mt "Никаких отказов и безответственных попыток улизнуть от участия можете даже не пробовать."
    mt "Участвовать будут все, кто не занят другими обязанностями."
    show mt angry pioneer far
    mt "А кто чем занимается у меня записано. Особенно некоторых это касается."
    "Вожатая явно имела в виду меня."
    "Что-то поспешил я с жизнерадостными выводами."
    "Ни в каких соревнованиях я участвовать не собирался."
    "Как бы теперь найти возможность затеряться до конца мероприятий."
    "Имелась одна идея, но мне даже сложно представить что из этого выйдет."
    "Вожатая тем временем закончила с раздачей указаний, но распустила не всех."
    mt "А ты и Алиса останьтесь, пожалуйста."
    show dv guilty pioneer close at right with dissolve
    "Алиса выглядела печально."
    "Я все еще не знал причин, но в груди все сжалось."
    "Рыжая снова втянула меня в какую-то пакость, в этом сомнений не оставалось."
    play music music_list["scarytale"] fadein 5
    show mt angry pioneer close at left with dissolve
    mt "Двачевская, ты уже поняла в чем дело?"
    show dv guilty pioneer close at right
    dv "Я ничего не делала."
    mt "Поздно невиновную из себя строить."
    mt "Выворачивайте карманы, оба."
    "Вот черт!"
    "Я же даже не выложил эту пачку."
    "Еще и телефон заметят, будут с вопросами приставать."
    "Выбора нет, придется доставать сигареты."
    "Я стыдливо вытащил пачку, сминая в руках до хруста картона."
    mt "Так я и знала! Что молчишь? Скажешь что-то в свое оправдание?"

    menu:
        "Взять вину на себя":
            ya "Виноват, оправданий не имею."
            show mt normal pioneer close at left
            mt "Хоть честно признался. В наказание будешь заниматься уборкой весь сегодняшний вечер."
            "Ольга Дмитриевна ловким движением руки вырвала у меня из рук пачку."
            mt "И не думай, что этим все огранчится. Твое вопиющее поведение переходит все границы."
            "Рыжая, ну ты меня и подставила."
            ya "Справедливо, заслужил."
            "Я сказал это больше в насмешку для Алисы, нежели ради ответа."
            "Как бы мне не хотелось поступить иначе - я не мог. Я согласился помочь и просто не имел права предать ее."
            show mt rage pioneer close
            mt "Ладно, разберемся с этим позже, нужно все подготовить к чемпионату и только посмейте куда-то убежать!"
            hide mt with dissolve
            stop music fadeout 2
            show dv smile pioneer close with dspr
            dv "Спасибо. Я знала что ты прикроешь. И это... Ну... Извини в общем."
            ya "Толку от твоих извинений? Не тебе же весь вечер уборку делать. А у меня, может, планы были?"
            dv "Не расстраивайся, может чего успеем придумать. Я своих не бросаю, тем более ты меня прикрыл, может и я тебя однажды прикрою."
            dv "Жаль, что вожатая все забрала."
            ya "А вот тут ты не права."
            "Перед тем, как вытащить пачку, я смог высыпать несколько штук в карман."
            ya "Держи."
            "Я отдал ей все, что утаил при изъятии."
            show dv smile pioneer close at center
            "Алиса заметно воспряла духом."
            show dv surprise pioneer close with dspr
            dv "У меня просто слов нет. Как ты это делаешь? Я не в смысле... А, ты просто великолепный!"
            ya "Вспоминай об этом почаще, пока я буду мыть полы до полуночи."
            show dv normal pioneer close
            dv "Я же сказала. Что-то придумаю. Не волнуйся об этом."
            ya "С тобой все понятно, а как я попал под подозрение?"
            dv "Кто-то нас сдал."
            show dv rage pioneer close with dspr
            dv "Найду - убью на месте!"
            hide dv with dissolve
            $ alis1 = True
            jump day_3_1

        "Сдать Алису":
            ya "Алиса мне вчера отдала. Попросила спрятать, это не мое."
            show dv rage pioneer close
            show mt angry pioneer close
            "Вожатая забрала у меня сигареты."
            mt "Двачевская! Мало того, что сама пакостишь, теперь вообще банду собрать решила?"
            dv "Да врет он все! Подставить меня хочет, чтоб не ему одному прилетело."
            mt "А это уже не важно. Кто лидер, а кто соучастник. Оба вечером будете заниматься уборкой!"
            mt "Эх, разберусь я с вами. Только не сейчас. Надо к чемпионату все подготовить. Но вы меня поняли! Уборка!"
            hide mt with dissolve
            "Не знаю зачем я сделал это. Глупо было надеяться, что смогу избежать наказания. Теперь еще и от Алисы попадет."
            show dv angry pioneer close
            dv "Вот ты как значит? Предать меня решил? Зачем тогда помочь соглашался, чтобы потом подставить?"
            ya "Я согласился подержать их у себя, а не отдуваться за тебя. Это разные вещи, поняла?"
            dv "Поняла, что доверять тебе не стоило, гад. Знала бы, ни в жизни с тобой не связалась."
            hide dv with dissolve
            play sound sfx_punch_medium
            with hpunch
            "Уходя с площади, рыжая толкнула меня напоследок."
            stop music fadeout 2
            jump day_3_1

label day_3_1:
    $ renpy.block_rollback()
    "Отлично! Теперь еще и уборка добавилась."
    "Двачевская, знал же, что дружба с тобой мне боком выйдет." 
    "Да только поздно что-то делать."
    "Пойду на завтрак."
    play ambience ambience_dining_hall_full
    scene bg int_dining_hall_people_day with dissolve
    "Поесть спокойно не дали."
    "Ко мне сразу же подошла Славя."
    show sl smile pioneer close at right with dissolve
    sl "Доброе утро. Ты вчера так и не вернулся. Почему?"
    ya "Не смог уговорить Женю. Одну ее тоже оставлять не хотелось, мне она показалась расстроенной."
    sl "Разве? Когда она пришла в наш домик, то выглядела очень даже радостной. Мы соседки."
    show sl normal pioneer close
    sl "Чем это вы там занимались вместе?"
    "Какое тебе дело?"
    ya "Сидели, говорили о всяком, ничего такого."
    show sl smile pioneer close
    sl "Ну... Ладно. Думаю, она тоже иногда нуждается в общении, как бы она этого не отрицала."
    ya "Похоже на то. Как раз собираюсь заглянуть к ней, сдать книги."
    show un normal pioneer close at left with dissolve
    un "Привет ребята. Алису не видели?"
    ya "Видел ее на площади, но она уже ушла."
    ya "Куда направилась не знаю. А зачем она тебе?"
    un "Мы с ней кое о чем договаривались. Ладно, извините, пойду ее искать."
    hide un with dissolve
    "Подозрительно."
    sl "Что это ты на нее так смотришь?"
    ya "Чего-то здесь не чисто."
    sl "Наверняка какая-нибудь мелочь. Лена во всяких сомнительных Алисиных авантюрах не участвует."
    ya "В тихом омуте, знаешь как дальше?"
    sl "Все бы тебе в черных красках видеть. Уверена, что Лена ничего плохого не совершила, я ее хорошо знаю."
    ya "Буду рад ошибиться."
    sl "Ладно, до встречи."
    hide sl with dissolve
    "Самое время забрать книги и пойти в библиотеку, пока еще что-нибудь не случилось."
    stop ambience fadeout 1
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_library_day with dissolve
    "Если от вечерней уборки, судя по всему не отвертеться, то пропустить спортивные соревнования у меня еще была надежда."
    "Не без помощи Жени, само собой."
    "У библиотеки как обычно никого не было."
    "Сердитая библиотекарша отпугивала потенциальных читателей не хуже злой собаки, охраняющей деревенское хозяйство."
    stop ambience fadeout 1
    play ambience ambience_library_day fadein 1
    play sound sfx_open_door_1
    scene bg spitzh with dissolve
    "Вид спящей девушки вызывал во мне умиление."
    "Вечерами она гуляла по лагерю допозна, а днем отсыпалась в библиотеке."
    "Такая спокойная, безобидная и вовсе не сердитая, даже будить не хотелось."
    "Я решил не мешать ее отдыху и сам разыскать нужную полку."
    hide bg spitzh
    scene bg int_library_day
    with dissolve
    "Это раздел с коммунистической литературой, не сюда."
    "Этот тоже про какую-то совковую хрень."
    "Тут вообще всего подряд натыкано."
    "Здесь не помешает инвентаризация."
    play sound sfx_table_hit
    with vpunch
    $ renpy.pause (0.1)
    play sound sfx_table_hit
    with vpunch
    $ renpy.pause (0.1)
    play sound sfx_table_hit
    with vpunch
    "Одним неудачным движением я случайно смахнул одну из книг с верхней полки, а за ней посыпались еще несколько, устраивая громкий переполох."
    "Женя тут же проснулась и со скоростью молнии подскочила к месту бедствия."
    show zh angry glasses pioneer at center
    mz "Ты чего тут шаришься как у себя дома?"
    ya "Не хотел прерывать твой сон."
    mz "А что ты прямо сейчас сделал?"
    ya "Хотел сдать вчерашние книги."
    mz "Прочитал уже? Быстрый какой."
    ya "Узнал все необходимое."
    mz "Молодец, что сдал, но бардак, который ты учинил в храме знаний - за это ты поплатишься!"
    play sound sfx_open_door_1
    "Хлопнула входная дверь."
    "Я увидел, что в библиотеку зашла Ольга Дмитриевна. Она была в крайнем бешенстве и вероятно искала меня."
    ya "Женя, пожалуйста прикрой меня от нее."
    "Я перешел на шепот."
    show zh angry glasses pioneer close with dissolve
    mz "Еще чего!"
    ya "Не оставляй пионера в беде, прошу тебя."
    mt "Женя, ты у себя?"
    mt "Мне сказали, что этот злодей к тебе пошел, он все еще здесь?"
    "Женя вышла из книжных рядов, навстречу вожатой."
    hide zh with dissolve
    "Ну все, пропала моя надежда..."
    mz "Был вот только что. Ушел минуту назад."
    mt "Эх, не успела. Ну ничего, поймаю я его, за все ответит. А то повадился от лагерных мероприятий отлынивать."
    play sound sfx_open_door_1
    show zh normal glasses pioneer far at center with dissolve
    mz "Вылезай, она ушла."
    "Эх, Женя. До последнего не верил в нее, а она меня не выдала."
    ya "Знаешь, все говорят, что ты злая бессердечная билиотекарша, но я вижу, что это неправда."
    show zh normal glasses pioneer close with dissolve
    mz "Кто-то же должен убирать весь этот учиненный тобой беспорядок. Так что я руководствовалась лишь практической целью."
    "Ну конечно."
    ya "Это единственная причина?"
    mz "Приступай уборке, пока я не передумала. А я за чаем схожу."
    ya "Будет сделано, товарищ заведующий."
    "Я приложил ладонь к виску, пародируя отдачу воинской чести."
    hide zh with dissolve
    "Когда Женя ушла мне пришлось возвращать книги на место."
    "Попутно я смахивал пыль и выравнивал книжные ряды, чтобы не допустить повторных обрушений."
    "И как такая компактная девушка вообще сюда достает достает."
    "Она даже на стуле не дотянулась бы до верхник полок."
    "Может, у нее где-то была лестница?"
    "Спустя каких-то полчаса работа была сделана."
    "Не считая некоторых малопопулярных разделов в библиотеке был порядок."
    "И мне не пришлось разбирать библиотеку целиком."
    "Я вышел к столу, дабы сообщить о завершении своей работы."
    show zh normal glasses pioneer close with dissolve
    play music bybd3 fadein 2
    mz "Садись, угощайся чаем, труженник."
    ya "Ага, партия выражает благодарность."
    mz "Вот партию не трогай! Хотя, лично я благодарона за помощь. Не зря грех на душу взяла перед вожатой."

    if prosmotr == True:
        "Я отхлебнул горячего ароматного чая."
        mz "Тебе правда интересно о чем я пишу?"
        ya "Иначе бы я не стал смотреть."
        mz "Ты ведь даже не спросил разрешения."
        ya "Можно подумать, ты бы позволила."
        show zh normal glasses pioneer close
        mz "Нет, но хотя бы из вежливости."
        ya "Еще не поздно спросить?"
        show zh confused glasses pioneer close
        mz "Если правда интересно, то возьми."
        "Женя протянула мне свою драгоценную тетрадь."
        $ set_mode_nvl()
        "Грузовой отсек космического крейсера Союз."
        "Тихий гул потрепанной посудины слегка действовал на нервы. Высадка все откладывалась и откладывалась. Скука и отсутствие каких-либо внятных инструкций начинали серьезно раздражать."
        "Капитан Смирнов уже думал завалиться вздремнуть на пассажирских сиденьях челнока, пока это возможно, когда в отсек спустился один из штабистов — обыкновенный представитель многопоколенной военной династии с отменной выправкой и лощеной рожей, но без намека на реальный опыт в бою или хотя бы за картой."
        "— Капитан Смирнов? — обратился он к взводу, глядя на толпу и явно в упор не замечая самого капитана."
        "— Я Смирнов и погоны вроде не снимал, — только и оставалось ответить."
        "— Оставьте свои замечания для подчиненных. Генерал Ульянов, капитан Симонов и лейтенанты Ким и Венедов на связи в конференц-зале и требуют вас для инструктажа."
        "Смирнов молча поднялся и проследовал за штабистом. Цели его присутствия на корабле остались для капитана загадкой. Похоже, Ульянов хотел либо отделаться от него, либо иметь лишние глаза и уши поближе к советскому космофлоту и десантной группе. Другое дело — что он рассчитывал услышать или увидеть? Люди Смирнова еще ни разу не показали себя трусами."
        nvl clear 
        "Штабист бодрым шагом проводил Смирнова до конференц-зала, пропустил к точке связи и встал за спиной, что ощутимо раздражало. Он включил приемник. Переговоры, очевидно, уже шли вовсю, но дожидаться, пока на капитана обратят внимание, было как минимум не по уставу."
        "— Товарищ генерал, капитан Смирнов на связи."
        "— А, Смирнов, ваши первоначальные инструкции немного меняются. Сколько у вас боеспособных людей?"
        "— После прошлого боя осталось девятнадцать бойцов, товарищ генерал. Двое убиты, четверо ранены. Какова наша задача?"
        "— Симонов, введите его в курс дела."
        "Симонов, судя по мундиру, был флотский, а лейтенанты — из пехоты."
        "— Капитан Смирнов, колония Новая Сибирь почти полностью захвачена. В жилых секторах действуют организованные группы лейтенанта Кима и лейтенанта Венедова, еще часть выживших разбросаны по колонии, но мы не можем контролировать ситуацию. Для восстановления преимущества нам необходимо закрепиться в нескольких опорных точках. Вам как десанту доверят точку, наиболее отдаленную от основного поселения. А именно укрепленную базу при иридиевом руднике..."
        $ set_mode_adv()
        nvl clear
        "Выглядело очень многообещающе. Прямо звездные войны с красным оттенком."
        ya "Это бесподобно. Лучшее, что я читал на тему, честно говоря."
        mz "Неправда."
        ya "От чистого сердца говорю. У тебя огромный талант."
        show zh shy glasses pioneer close with dissolve
        mz "Льстец, подлиза."
        ya "Может все таки дурак?"
        mz "Ну уж нет."
        show zh smile glasses pioneer close
        ya "В общем, мне очень нравится."
        mz "Ой, сахар совсем забыла с тобой, сейчас принесу."
        hide zh with dissolve
        jump day_3_2
    else:
        "Я отхлебнул горячего ароматного чая."
        mz "Признавайся, чего натворил, что тебя по всему лагерю Ольга Дмитриевна разыскивает."
        ya "С сигаретами попался, но они были не мои. Глупая ситуация."
        mz "Курил небось?"
        ya "Ни в жизни."
        mz "Так я тебе и поверила."
        ya "С тобой я всегда честен."
        show zh confused glasses pioneer close with dissolve
        mz "Ладно, так и быть. Доверюсь."
        mz "Заговорилась тут с тобой, сахар принести забыла."
        hide zh with dissolve
        jump day_3_2

label day_3_2:
    "Женя убежала в кладовую."
    "Чай уже закончился, а она за сахаром собралась."
    show zh fun pioneer close at center with dissolve
    mz "Хочешь еще налью?"
    "Она посмотрела на мою опустевшую кружку."
    ya "Спасибо, не надо. Чай наверное дефицитный, а так и весь могу выпить."
    mz "Будь оно так, ни капельки бы тебе не налила."
    ya "Не надоело тебе ругаться?"
    show zh sad pioneer close
    mz "Сам сказал, что я злая бессердечная билиотекарша."
    ya "Я сказал, что убедился в обратном."
    mz "С чего вдруг? Прикрыла я тебя не из доброты."
    ya "И чаем тоже из корыстных побуждений напоила?"
    show zh shy pioneer close
    mz "Ну... Не знаю..."
    ya "Хорошо тут у тебя, тихо. Понимаю, почему ты сюда напросилась."
    show zh normal pioneer close
    mz "И ничего я не напрашивалась. Желающих особоенно не было."
    ya "Но ты ведь тут добровольно."
    ya "Днем спишь, вечерами гуляешь, когда народу поменьше."
    mz "Ночь - прекрасное время."
    ya "Согласен. Я часто гулял ночами у себя в городе. Мог до самого утра бродить, думать о всяком. А над головой луна и звезды, да уличные фонари озаряют мой путь."
    mz "Звучит романтично. Меня вот ночью родители не пускают. В лагере с этим не так строго, хотя если сильно задержусь - начнут искать."
    mz "Стараюсь не опаздывать, а то подумают чего, расспросы начнутся."
    ya "А тебе есть что скрывать?"
    show zh angry pioneer close
    mz "В чем это ты меня подозреваешь?"
    ya "Лишь пытаюсь узнать тебя получше."
    mz "Зачем?"
    ya "Ты интересная личность."
    show zh confused pioneer close
    mz "Ну, ты скажешь тоже..."
    ya "Ничего кроме правды."
    mz "Обед скоро, надо собираться."
    ya "Женя, слушай. Может сходим к пляжу. Сегодня все равно большая часть пионеров на волейболе до вечера."
    mz "Жарко там да и в песке валяться не очень хочется."
    ya "Можем и просто где-то посидеть. Не надоело еще в библиотеке скучать?"
    mz "Ладно, раз ты так просишь. После обеда на лодочной станции."
    ya "Договорились."

    show black with dissolve
    stop music fadeout 2
    stop ambience
    $ renpy.pause (1, hard = True)
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day
    hide black 
    with dissolve

    "Обед - дело важное, тем более когда вечер обещает быть трудным и длительным."
    "Очень надеюсь, что здесь меня не перехватит вожатая и не отправить на принудительные работы."
    "Все же, я Жене пообещал прийти."
    "Пришлось оглядываться каждые пару секунд."
    "Хотя, не знаю как бы это помогло, если Ольга Дмитриевна решила бы заглянуть в этот момент."
    "Разве только в окно прыгнуть."
    "Но, к счастью, все обошлось."
    "Закончив со всеми тремя блюдами, я поспешил к причалу."

    show black with dissolve
    stop ambience fadeout 1
    $ renpy.pause (1, hard = True)
    play ambience ambience_lake_shore_evening fadein 1
    scene bg ext_boathouse_day
    show zh normal glasses pioneer close at center
    hide black 
    with dissolve

    ya "Ты уже здесь. Как только успела раньше меня?"
    mz "Может, это ты не торопился."
    ya "Я спешил сюда как только мог."
    mz "Зачем позвал меня?"
    mz "Мог бы и один сходить, если на свежий воздух захотелось."
    ya "А тебе лишь бы взаперти сидеть, вон уже бледная какая стала."
    show zh angry glasses pioneer close
    mz "Тебе-то что?"
    ya "Для всего ли нужна причина?"
    mz "Да, представь себе."
    show zh normal glasses pioneer close
    ya "Нельзя просто наслаждаться видами? Я думал, тебе это нравится."
    mz "Это не лишено смысла."
    scene bg lodki with dissolve
    ya "Расскажи еще о себе."
    mz "Что ты хочешь узнать?"
    ya "Хочу знать о тебе все."
    mz "Это еще зачем?"
    ya "Таков мой интерес."
    mz "Больше на допрос похоже, но ладно. Расскажу."
    mz "Я из далеких краев..."
    "Она говорила. Долго и подробно."
    "Про детство и учебу, немного про свои интересы, хотя и не спешила раскрывать о себе подробностей."
    "А я даже не вдавался в детали, мне просто нравилась слушать ее милый, приятный голос, ощущать ее рядом."
    "Хотелось обнять, крепко прижать к груди."
    "Ведь она тоже живой человек, ей наверняка, как и всем, хочется простых радостей, влюбленности. Быть нужной и особенной в чьих-то глазах."
    "Я чувствую в ней это, несмотря на все попытки скрыть за пеленой отторжения и грубости."
    "Такой чудесной и в то же время такой непростой и противоречивой девушки я не встречал прежде."
    "Думаю, что и ее саму в глубине души одолевали чудовищной силы страсти. Борьба между тем, чтобы быть собой и страхом быть непонятой, отверженной."
    "За образом сердитой, нелюдимой и вечно недовольной девочки скрывалась другая Женя."
    "Чувственая и нежная, добрая и заботливая, но ей никогда не давали шанса раскрыть себя."
    "Быть может, ее не приняли настоящей и она закрылась от остальных?"
    "Стала такой, какой все теперь ее знают."
    "Но мне хотелось сломать эту защиту, добраться до самого сердца. Чтобы хоть одним глазком увидеть ту, что спрятана. Чтобы она явила истинную себя, хотя бы для меня одного."
    scene bg ext_boathouse_day with dissolve
    show zh angry glasses pioneer close at center
    mz "Ты меня слушаешь вообще?" 
    mz "Сам просил рассказать."
    ya "Слушаю."
    "Конечно, я соврал."
    show zh hope glasses pioneer close
    mz "Я не понимаю зачем все это."
    mz "Целый день ходишь за мной, тащишь сюда комаров кормить."
    mz "Скажи уже прямо, что тебе от меня нужно?" 
    
    menu:
        "Признаться ей":
            ya "Ты мне нравишься."
            show zh shyangry glasses pioneer close
            mz "Дурак!"
            hide zh with dspr
            play sound sfx_slavya_run
            "Женя бросилась бежать прочь от меня."
            $ priz = True
            "Я всякое мог ожидать, но точно не такой реакции."
            "Не долго думая, я отправился в погоню."
            play sound sfx_slavya_run
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            $ renpy.pause (1)
            scene ext_square_day with dspr
            play sound sfx_slavya_run
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            with vpunch
            $ renpy.pause (1)
            scene ext_library_day with dspr
            "Женя забежала в библиотеку и закрылась изнутри."
            play sound sfx_knocking_door_outside
            ya "Женя, открой пожалуйста. Давай поговорим."
            ya "Я знаю, что ты там."
            play sound sfx_knocking_door_outside
            "В ответ была только тишина."
            ya "Женя, ты не можешь прятаться там вечно. Неужели я не заслуживаю внятного ответа?"
            ya "Тебя обидели мои слова?"
            "Все еще тишина."
            ya "Черт! Не заставляй меня выбивать двери и окна. Пожалуйста, скажи мне, что случилось."
            mt "Вот ты где!"
            play sound sfx_knocking_door_outside
            "Нет! только не сейчас!"
            show mt angry pioneer far at right with dissolve
            mt "Мне казалось, утром ты был достаточно наказан, но судя по всему ты все еще ничего не понял."
            ya "Можно не сейчас? Когда угодно позже, но не сейчас!"
            "Я сорвался на крик."
            mt "Быстро за мной! Уборка ждет? иначе мигом вылетишь из лагеря."
            show mt rage pioneer close at center with dissolve
            "Ну почему так все совпало. Как все несправедливо."
            "Мне не оставалось ничего, кроме как подчиниться."
            "Женя не стала говорить со мной и вряд ли я бы смог что-то с этим сделать при всем желании."
            jump day_3_3

        "Не признаваться сейчас":
            ya "Ничего, просто так. Ты ведь не хуже других."   
            "Господи, что за чушь я сейчас сказал...."
            show zh sad glasses pioneer close at center with dissolve
            mz "Понятно."
            mz "Мне уже пора, спасибо за прогулку."
            show zh cry glasses pioneer close
            ya "Подожди, я не это хотел сказать."
            hide zh with dissolve
            "Какой же я идиот..."
            "Хотелось пойти за ней, догнать, объяснить все, но сейчас в этом не было смысла."
            "Она и слушать меня не станет."
            "Стоит дать ей немного времени и потом попробовать снова."
            "Все равно этот вечер я бы провел на уборке столовой."
            jump day_3_3

label day_3_3:
    $ renpy.block_rollback()
    $ persistent.sprite_time = "night"

    show black
    stop ambience fadeout 1
    $ renpy.pause (1, hard = True)
    play ambience ambience_dining_hall_empty fadein 1
    scene bg int_dining_hall_night
    hide black 
    with dissolve

    "Ужин прошел без происшествий, аппетита совсем не было."
    "А еще эта уборка." 
    "Черт бы побрал Алису с ее сигаретами."

    if alis1 == True:
        "Как за помощью обратиться, так она первая, а я за нее получать должен."
        "Уже жалею, что прикрыл ее тогда."
        "Взяв тряпку в руки, я начал мыть пол."
        "Мерзкий, грязный, изорванный, видавший не одну смену, кусок ткани едва не рассыпался в моих руках от старости."
        "Вода становилась черной уже после пары ополаскиваний."
        show dv normal pioneer2 close at center with dissolve
        ya "А вот и виновница торжества. Ну? Что придумала?"
        dv "Ничего не вышло. Но и оставить все так я тоже не могла. Пришла помочь тебе с этим, ты за меня вступился и я ценю это."
        ya "Неужели я слышу в тебе голос совести?"
        show dv guilty pioneer2 close with dissolve
        dv "Просто хочу отдать долг."
        ya "Ну вперед, чего стоишь без дела. Уборка сама себя не сделает."
        show dv smile pioneer2 close
        dv "Получается, мир?"
        ya "Вот приберемся, тогда и руки пожмем, а то сейчас не очень гигиенично."
        jump night_3_1
    else:
        "Еще больше меня смущал факт того, что придется делать с ней уборку после того, как я ее подставил."
        "Не уверен даже был ли смысл извиняться, но стоило попробовать."
        show dv angry pioneer2 close at center with dissolve
        ya "Прости, что сдал тебя вожатой."
        ya "Наверное, просто испугался в тот момент."
        ya "Я сожалею о содеянном."
        show dv sad pioneer2 close
        dv "Я сама виновата, что поверила тебе."
        dv "Почему-то подумала, что ты нормальный парень, надежный. Не трус."
        ya "Если хочешь, я сейчас пойду и скажу Ольге Дмитриевне, что это были мои сигареты?"
        show dv normal pioneer2 close at left with dissolve
        dv "Раньше надо было думать. Теперь вон тряпку бери и вперед."
        ya "Как мне заработать твое прощение?"
        dv "Никак, работай давай, хватит языком чесать."
        jump night_3_1

label night_3_1:
    show black with dissolve
    $ renpy.pause (1)
    play sound sfx_broken_dish
    scene bg int_dining_hall_night
    hide black 
    with dissolve

    "После долгой и выматывающей уборки мы с Алисой наконец присели на пару минут отдохнуть."
    "Большая часть посуды не пострадала, хотя были и жертвы."
    "В следующий раз будут думать кого отправлять на такую ответственную работу."
    "Уж явно не двух самых безответственных пионеров лагеря."
    "До отбоя оставалось совсем немного."

    if priz == True:
        "Попытать ли счастье снова, попытавшись разыскать Женю и объяснить ей все?"
        "Лучше дам ей ночь подумать, а завтра попробую снова. И снова, если будет нужно."
        "За такую девушку и побороться стоило."
        "Вот только на сегодня мои силы уже иссякли. А завтра самое время, чтобы взять штурмом библиотеку, если придется."
        "Для любой битвы нужно много сил. И завтра они мне действительно пригодятся."
        stop ambience fadeout 1
        jump night_3_2
    else:
        stop ambience fadeout 1
        "И я бы не смог уснуть, не попытавшись исправить собственную глупость."
        play ambience ambience_ext_road_night fadein 1
        scene bg domzh with dissolve
        "Я подошел к домику Жени и Слави."
        "Повезло, что Славя как раз собиралась зайти и я смог перехватить ее."
        show sl normal pioneer far at right with dissolve
        ya "Привет Славя. Мне нужна твоя помощь."
        sl "Что у вас случилось? Женя пол дня слезами заливается."
        ya "Я сказал очень обидную глупость, не со зла. И Женя не стала слушать моих оправданий."
        sl "Ничего удивительного. И чем же я могу помочь тебе? Да и стоит ли, раз ты так поступил с Женей."
        ya "Я хочу исправить все и извиниться. Она меня слушать не станет. Ты же ее знаешь. Просто вымани ее на улицу, а дальше я разберусь."
        show sl normal pioneer close at right
        sl "Ой, не нравится мне это."
        ya "Пожалуйста! Если я не попрошу прощения, то сам не усну сегодня."
        sl "Ладно, я позову ее, а ты побудь тут."
        hide sl with dissolve
        "Славя выманила Женю на улицу."
        "Едва завидев меня, Женя попробовала забежать обратно, но соседка держала дверь, не желая пускать ее, пока мы не поговорим."
        "Осознав неизбежность, девушка все таки вышла ко мне."
        show zh angry glasses pioneer close at center with dissolve
        mz "Зачем пришел? Сказал уже достаточно сегодня."
        mz "Что я не хуже остальных, да? Но и не лучше. Что-то среднее."
        mz "Можно прийти ко мне, чтобы я тебя чаем поила, от вожатой прикрывала, да?"
        ya "Слова действительно здесь не помогут."
        "Ну, была не была!"
        window hide
        scene bg posl with dissolve
        $ renpy.pause (2)
        scene bg posl2 with dissolve
        $ renpy.pause (2)
        scene black with dspr
        play sound sfx_punch_medium
        window show
        hide zh
        scene bg domzh with dissolve
        play sound sfx_punch_medium
        with hpunch
        "Женя выдала мне звонкую пощечину, после чего забежала в домик."
        "Меня пробило на истерический смех."
        "Все таки дама с характером, этого у нее не отнять."
        "Но я все равно был счастлив, потому что в этот самый момент почувствовал тот отклик в ее сердце, как бы она не показывала обратное."
        "А это значит - я на верном пути."
        jump night_3_2

label night_3_2:
    scene bg dom with dissolve
    play sound sfx_open_door_1
    "Абсолютно сумасшедший день, который выдавил меня до капли."
    "Я едва смог добраться до собственной постели и почти сразу уснул."
    show blink
    $renpy.pause (2)
    scene black
    jump label_day_5