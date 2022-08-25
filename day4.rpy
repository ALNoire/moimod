label label_day_5:
    $ persistent.sprite_time = "day"
    $ backdrop = "days" 
    $ new_chapter(4, u"Лето с Женей: День 4") 
    $ renpy.pause(2)
    $ renpy.block_rollback()

    play music music_list["memories"] fadein 2
    scene bg dom with dissolve
    "Эх, Женя. Заставляешь же ты меня волноваться."
    "Даже утром я все еще пребывал в шоковом состоянии от произошедшего."
    "Пол ночи я придумывал извинения или хотя бы те слова, которые заставят ее выслушать меня."
    "Наверное, я был слишком резок в своих действиях."
    "Ну, правильно!"
    "О чем я вообще думал?"
    "Что она бросится в мои объятия?"
    "К человеку, с которым знакома всего пару дней?"
    "Ей нужен особый подход, следовало быть осторожнее и сдержаннее."
    "Она не привыкла так открыто выражать чувства и я, судя по всему, заставил ее сильно волноваться."
    "Сегодня отличный способ исправить ситуацию."
    "Надеюсь, еще не поздно."
    stop music fadeout 2
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_houses_day with dissolve
    "По дороге я в сотый раз думал о том, что скажу ей."
    "Волнение накатывало с каждым шагом."
    "Вчера я был смелее."
    "Сегодня сердце дрожит от одной мысли о ее недобром взгляде."
    "Может быть от чувства вины или из-за страха быть отвергнутым."
    "Прошлым днем я был полностью уверен в своих силах, но сейчас от моей убежденности не осталось и следа."
    "С трудом перебирая ногами, я шел в сторону площади."
    scene bg ext_square_day with dissolve
    "Среди пионеров Жени не было."
    "Наверное, осталась дома или в библиотеке, не желая видеть меня."
    "Вожатая, как и всякий день проводила утренний инструктаж. Раздавала указания на текущий день."
    "Я не слушал ее, голова была занята совсем другой вещью."
    "Единственное, чего я сейчас хотел, так это скорейшего завершения линейки, чтобы я смог отправиться на поиски Жени."
    "На этот раз вожатая не спешила требовать от меня каких-то действий или объяснений."
    "Никаких поручений или наказаний."
    "Ольга Дмитриевна наконец поняла, что мне не стоит поручать вообще ничего и решила не тратить силы на дальнейшие попытки меня вразумить."
    "Когда нам разрешили разойтись, я пробежал всю площадь в поисках девушки, но ее действитльно нигде не было."
    "Только этот дурацкий памятник очередному советскому деятелю."
    "Унылый, мрачный монумент ушедшей державы."
    "Даже если в этом мире совок еще не развалился."
    "Если представиться случай, стоито спросить об этом персонаже у Жени. Заодно могла бы объяснить мне чем ей так нравится советский строй."
    "Все ее поведение характеризует резкое неприятие общественных норм и контрастирует с образом советского человека."
    "В ней куда больше индивидуалистического, чем в любом из представителей свободного капиталистического мира."
    stop ambience fadeout 1
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "Не успел я поесть, как появилась Славя."
    show sl serious pioneer close at left with dissolve
    sl "Привет. Женю не видел? Вы вчера целый день вместе были."
    ya "Вы же с ней соседки. Я как раз хотел узнать о ней у тебя."
    sl "С раннего утра она куда-то пропала."
    sl "На утренней линейке ее не было, завтракать тоже не приходила. Я волнуюсь."
    ya "Не одна ты."
    show sl normal pioneer close
    sl "Вы были вместе. Алиса сказала, что видела, как она убегала от тебя в слезах."
    ya "Алиса, везде-то ей надо подглядеть."
    sl "Ты меня тут не заговаривай. Обидел девочку, а еще на других жалуешься."
    ya "За вчерашнее вины с себя не снимаю. Напротив, хочу помириться с ней, но не знаю как."
    ya "Теперь ее еще и найти надо. В библиотеке смотрели?"
    sl "Тебе стоит помириться с ней самому."
    ya "Попробую."
    sl "Возьми ей немного еды, она ведь не завтракала."
    hide sl with dissolve
    "Славя оставила мне пару булок, завернутых в плотный бумажный сверток."
    stop ambience fadeout 1
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_library_day with dissolve
    "Я отправился в библиотеку, но здесь Жени тоже не было."
    "Свет внутри не горел, а на двери висел массивный железный замок."
    "Очевидно, она не могла сбежать за пределы лагеря, так что осталось лишь осмотреть его целиком."
    "Где бы эта своевольная девушка не пряталась, я был просто обязан ее найти."
    "Я пытался прикинуть в голове возможные места ее пребывания, но угадать было невозможно."
    "Лагерь большой она может быть вообще где угодно."
    "Если рассуждать логически."
    "Дома ее не было, в столовой, в библиотеке и на площади она тоже не появляась."
    "Это значительно сокращало зону поиска, но побродить еще придется."
    $ disable_all_zones()
    $ set_zone("boat_station","boat_4")
    $ set_zone("camp_entrance","camp_4")
    $ set_zone("forest","forest_4")
    $ set_zone("clubs","clubs_4")
    $ show_map()

label boat_4:
    stop ambience fadeout 1
    play ambience ambience_lake_shore_evening fadein 1
    scene bg ext_boathouse_day with dissolve
    "На лодочной станции никого не было."
    "На ее месте было бы глупо приходить сюда после вчерашнего."
    "Но я должен был проверить это место."
    "Лишь сейчас я почувствовал где стоит искать в первую очередь."
    stop ambience fadeout 1
    jump forest_4

label camp_4:
    scene bg ext_no_bus with dissolve
    "Неплохой вариант, чтобы уйти подальше от любопытных глаз."
    "Но ее тут не оказалось."
    "Лишь сейчас я почувствовал где стоит искать в первую очередь."
    stop ambience fadeout 1
    jump forest_4

label clubs_4:
    scene bg ext_clubs_day with dissolve
    "И с чего я вообще решил, что она может быть тут?"
    "Одно из худших мест для побега."
    "Двое этих идиотов сдали бы ее в два счета."
    "Лишь сейчас я почувствовал где стоит искать в первую очередь."
    stop ambience fadeout 1
    jump forest_4

label forest_4:
    stop ambience fadeout 1
    play ambience ambience_forest_day fadein 1
    scene bg les with dissolve
    "Не знаю почему, но я был уверен, что иду в правильном направлении."
    "Будто чья-то невидимая воля направляла меня сейчас."
    "Двигаясь по тропинке, я заглядывал под каждый куст, безуспешно пытался разглядеть следы."
    "Можно подумать, я бы отличил их среди сотен других на вытоптанной земле."
    "И все таки я шел дальше, пока не вышел к живописной поляне."
    scene bg ext_polyana_day with dissolve
    "Тут и пряталась Женя."
    "Завидев меня, она попыталась пройти мимо и избежать встречи, но я остановил ее."
    show zh sad glasses pioneer close at center with dissolve
    play music bybd3 fadein 1

    if priz == True:
        ya "Привет, Женя."
        mz "Уходи. Зачем пришел?"
        ya "Ребята в лагере волнуются о тебе. Я тоже волновался."
        mz "Со мной все хорошо. Не надо ходить за мной. Забудем все, что вчера случилось."
        ya "Нет уж! Ничего я забывать не собираюсь. Я был полностью серьезен и могу повторить это сейчас. Ты мне нравишься, Женя."
        show zh sceptic glasses pioneer close with dissolve
        mz "Точно, дурак."
        ya "Если нужно быть дураком, чтобы быть рядом, то я буду."
        show zh shyangry pioneer close
        mz "Ты говоришь глупости, не надо. Давай все забудем, пожалуйста."
        ya "Почему? Назови хотя бы причину? Я так плох для тебя?"
        mz "Нет, не в этом дело..."
        ya "Скажи в чем."
        show zh confused glasses pioneer close
        mz "В том, что я боюсь. Понятно?"
        ya "Чего ты боишься? Меня? Себя?"
        mz "Боюсь, что будет теперь с нами."
        mz "Я никогда и никому не хотела довериться так сильно, как тебе."
        mz "Никто не мог понять меня так хорошо, как ты за эти дни."
        mz "Что, если в один день ты поймешь, что совершил ошибку?"
        mz "Или тебе просто надоест возиться с сердитой девочкой из библиотеки?"
        ya "Это невозможно."
        show zh normal glasses pioneer close
        mz "Откуда ты это знаешь?"
        ya "Потому, что я верю в это и чувствую себя живым рядом с тобой."
        ya "Это чувство я никогда и ни на что не променяю."
        mz "Ты поступаешь очень глупо. Не терзай мне душу, прошу тебя."
        ya "Я от своего не отступлюсь. И прошу тебя поверить мне."
        mz "Ты тоже нравишься мне, но я не знаю как мне быть... Мне правда страшно."
        ya "Без доверия ничего не получится. Дай мне шанс и ты не пожалеешь."
        show zh shy glasses pioneer close
        mz "Я попробую."
        jump day_4_1

    else:
        ya "Привет, Женя."
        mz "Уходи. Зачем пришел?"
        ya "Волновался о тебе."
        show zh angry glasses pioneer close with dissolve
        mz "После того, что ты вчера сделал, я не хочу тебя видеть!"
        mz "Даже не подходи ко мне, подлец!"
        ya "Я виноват перед тобой. Не стоило так делать, но я поддался эмоциям, прости."
        mz "Каким еще чувствам. Ты просто решил, что можно использовать меня и мои чувства."
        mz "Я тебя ненавижу!"
        ya "Ты так не думаешь. Вчера я почувствовал, что тебе не все равно. В тот самый момент."
        show zh rage glasses pioneer close
        mz "Неправда. Ты подлец и обманщик! И ничего я к тебе не чувствую."
        ya "И кто же из нас сейчас врет? Точно не я."
        mz "Вчера днем ты ясно дал мне все понять."
        ya "И я очень жалею о сказанном. Выразить чувства бывает непросто."
        mz "Не стоит тратить время на ту, кто не хуже и не лучше других. Вот что я тебе скажу."
        ya "Я сказал глупость вчера, а потом сделал глупость, но последнюю я готов повторить, даже если ты снова меня ударишь."
        ya "Ты мне нравишься, Женя. Прости, что не сказал этого вчера. Я не смог, испугался."
        show zh normal pioneer close
        mz "Чтобы признаться не нужно иметь много смелости."
        ya "Значит, я трус. Но теперь я нашел силы сказать тебе о своих чувствах."
        mz "И что же это было вечером?"
        ya "Ты про поцелуй? Это то, что я не смог выразить словами."
        show zh sad glasses pioneer close
        mz "Мне хочется поверить тебе, но я не могу."
        ya "Сама же сказала, что много смелости для признания не нужно."
        show zh shyangry glasses pioneer close
        mz "Дурак! Это совсем другое."
        ya "Я прошу всего лишь шанс, чтобы доказать тебе серьезность моих намерений."
        ya "Ты никогда не пожалеешь об этом. Обещаю."
        show zh confused glasses pioneer close
        mz "Хорошо, я попробую."
        mz "Но это вовсе не значит, что у тебя есть право делать то, что ты сделал вчерашним вечером!."
        jump day_4_1

label day_4_1:

    ya "Тогда побудем здесь еще немного?"
    ya "Славя просила передать тебе."
    "Я отдал ей сверток с булками."
    ya "Ты ведь не завтракала. Наверное, голодна."
    mz "Спасибо."
    scene bg zhenya with dissolve
    "Женя оценила мою идею."
    "Мы улеглись в тени большого дерева."
    "Так тихо."
    "Спокойствие и умиротворение."
    "Мне так не хватало этого чувства все последние годы."
    "Наконец, Женя обрела душевный покой и приняла мои чувства."
    "Ну, а я?"
    "Я просто был рад, что она рядом."
    stop music fadeout 2
    stop ambience fadeout 2
    scene black with dissolve
    $ renpy.pause (1, hard = True)
    play sound sfx_thunder_crack
    play music dojd fadein 1
    scene bg lesrain
    hide black 
    with dissolve
    "Нам было так хорошо вместе, что мы не заметили как на небе сгустились тучи и начался сильнейший ливень."
    "Я взял Женю за руку и мы побежали в сторону лагеря."
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    $ renpy.pause (1)
    scene bg squarerain
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    $ renpy.pause (1)
    scene bg librain
    $ renpy.pause (1)
    stop music fadeout 2
    play music dojdvdome fadein 2
    play sound sfx_open_door_1
    scene bg int_library_day with dissolve
    "Женя промерзла до костей и отправилась в кладовую переодеваться."
    "Я, с ее позволения, поставил кипятильник."
    "Пока вода в стаканах нагревалась, я засматривался в запотевшие окна, за которыми продолжался холодный проливной дождь."
    "А мы были здесь, в безопасноти и тепле."
    "Трудно представить себе более уютную обстановку, чем горячий чай, приятную компанию и бурю за окном."
    show zh fun glasses pullover close at center with dissolve
    mz "А вот и я."
    ya "Теперь согреешься."
    mz "Чай поможет."
    ya "Чем займемся после чаепития?"
    show zh fun glasses pullover close
    mz "Какие сегодня задания от Ольги Дмитриевны? Ты был на линейке?."
    ya "Я был занят составлением пламенной речи, ничего не услышал."
    show zh normal glasses pullover close
    mz "Эх, прибить бы тебя книгой за такое разгильдяйство. Да жалко."
    ya "Это обнадеживает."
    mz "Вот пойдешь и узнаешь, как только дождь закончится."
    ya "Будет сделано, товарищ Женя."
    show zh sceptic glasses pullover close
    mz "Ехидство в библиотеке запрещено."
    ya "Ну вот, а чем же мне тогда заниматься большую часть времени?"
    mz "Делом займись, книжки почитай."
    mz "Может, чего умного узнаешь."
    ya "Все-то тебе за книгами сидеть. Так всю жизнь и просидишь."
    show zh shyangry glasses pullover close
    mz "Поговори мне тут, бездельник и подлый соблазнитель."  
    "Вопреки моему желанию побыть в библиотеке подольше, дождь закончился так же стремитель, как и начался."
    "Я незамедлительно был отправлен за расписанием к вожатой."
    stop music fadeout 2
    play ambience ambience_ext_road_day fadein 1
    scene bg libafrain with dissolve
    "Воздух ощущался свежим и прохладным."
    "Это хорошо чувствовалось на фоне последних, довольно теплых дней в лагере."
    "Из-за облаков снова начали показываться лучи солнца."
    "Думаю, к вечеру все уже высохнет и ни следа этой маленькой бури не останется."
    "Переодеваться тоже решил не идти."
    "Само пройдет."
    scene bg ext_square_day with dissolve
    "На площади я встретил Лену."
    show un normal pioneer far at center with dissolve
    ya "Привет, Лена. Куда направляешься?"
    un "В библиотеку, книжку сдать."
    ya "Ты ведь была на утренней линейке. Какие мероприятия на сегодня?"
    show un smile pioneer close with dissolve
    un "Сегодня вечер танцев. Хорошо, что дождь так быстро закончился."
    "Ага, Женя будет в восторге."
    ya "Раз все равно идешь в библиотеку, то передай эту информацию Жене. Ее не было утром, она просила узнать."
    un "Хорошо."
    hide un with dissolve
    "Скоро обед, а потом начнется подготовка к праздничному вечеру."
    "Очень хотелось соскочить с подготовки."
    "Ведь припахают же на какое-нибудь дело."
    "Да и танцор из меня так себе. На счет Жени не уверен."
    play ambience ambience_dining_hall_full fadein 1
    scene bg int_dining_hall_people_day with dissolve
    "Обед начинался хорошо."
    "Я смог пристроиться между двумя парнями в очереди и вдвое сократить время ожидания."
    "Однако, как только я сел за обед, в дверях появилась Ольга Дмитриевна."
    show mt normal pioneer close at center with dspr
    mt "Вот ты где, бездельник."
    "Я едва не подавился котлетой."
    ya "Оль-гх-гха Дмитриевна."
    mt "Не говори с набитым ртом. Слушай указания."
    mt "Лена и Мику будут ждать тебя на улице."
    mt "Поможешь им принести украшения для праздника."
    ya "Я бы и рад, но Женя..."
    mt "Ничего с ней не случится за пару часов, как раз встретитесь на празднике."
    hide mt with dissolve
    "Слушать она меня как всегда не стала. Придется помогать."
    stop ambience fadeout 1
    play ambience ambience_ext_road_day fadein 1
    scene bg ext_dining_hall_near_day
    show mi normal pioneer close at left
    show un normal pioneer close at right
    with dissolve
    ya "Привет трудовому народу."
    mi "Шутишь? Хи-хи."
    un "Я сказала Жене про праздничный вечер."
    ya "Спасибо."
    ya "Только надо мне было самому идти."
    "Может быть, не отправили с вами фонарики эти дурацкие вешать."
    mi "Не переживай, мы быстро управимся. Будет весело."
    "Ага, не сомневаюсь."

    show black with dissolve
    stop ambience fadeout 1
    $ renpy.pause (1, hard = True)
    $ persistent.sprite_time = "night"
    play ambience ambience_ext_road_evening fadein 3
    scene bg ext_square_night_party
    hide black
    with dissolve
    
    "Мы трудились до темноты."
    "Весело не было, Мику обманула меня."
    "По крайней мере мне."
    "Площадь заливал красивый искусственный свет."
    "Постепенно набирался народ."
    show un smile dress far at fleft with dissolve
    show sl smile dress far at center with dissolve
    show us smile dress far at left with dissolve
    "Но Жени все не было."
    "Как бы чего не случилось."
    stop ambience fadeout 1
    play ambience ambience_ext_road_night fadein 1
    scene bg libnight with dissolve

    if alis1 == True:
        show dv normal pioneer2 close at center with dissolve
        dv "Как дела, пионер?"
        ya "Не очень праздничный вид у тебя."
        dv "А я не и не собираюсь на эти дурацкие танцы. Думала, ты тоже не пойдешь."
        ya "Еще не решил. Я за Женей вообще пришел, а ты чего тут делаешь?"
        show dv smile pioneer2 close
        dv "Решила вернуть один долг. Не бери в голову и наслаждайся весельем."
        hide dv with dissolve
        jump day_4_2
    else:
        "Недалеко от библиотеки я встретил Электроника."
        "Вид у него был серьезный."
        play music music_list["scarytale"] fadein 2
        show el angry pioneer close at center with dspr
        el "Уходи отсюда! И больше не приближайся к Жене!"
        ya "Или что?"
        el "Придется разобраться с тобой."
        menu:
            "Решить вопрос силой":
                play sound sfx_punch_medium
                with vpunch
                show el fingal pioneer close
                el "Стой, не надо. Я все понял."
                ya "Ты чего задумал?"
                el "Ты Женю обижаешь."
                ya "А ты защищать ее пришел? И вообще. С чего ты так решил?"
                el "Алиса сказала мне, что видела, как женя в слезах от тебя вчера убежала, а сегодня ее весь день нет."
                "Вот же мстительная су..."
                ya "За тот случай я извинился. Сейчас все нормально."
                el "Ты обманываешь."
                ya "Я, кажется, понял в чем дело. Не просто так ты пришел."
                el "О чем это ты?"
                ya "Женя сама должна выбрать с кем ей быть, но если ты не согласен, всегда можем разобраться без ее участия."
                el "Ты прав. Извини, я пойду."
                hide el with dissolve
                stop music fadeout 2
                jump day_4_2

            "Решить вопрос словами":
                ya "Ну давай, ударь меня. Может быть Женя оценит такой поступок."
                ya "Покажи ей какой ты подлец и эгоист на самом деле."
                show el serious pioneer close
                el "В каком это смысле?"
                ya "Ты решил прийти и силой разлучить нас, наплевав на ее чувства и мнение."
                ya "Лишь для того, чтобы самому оказаться ближе к ней, а на ее чувства тебе плевать."
                el "Неправда. Алиса сказала мне, что ты ее обижаешь, вот и все."
                ya "Если ты про вчерашнее, то я извинился. А об остальном..."
                ya "Может, надо дать ей право решать с кем ей хочется быть?"
                show el upset pioneer close
                el "Ты прав. Извини, я пойду."
                hide el with dissolve
                stop music fadeout 2
                jump day_4_2

label day_4_2:
    $ renpy.pause (1)
    $ renpy.block_rollback()
    stop ambience fadeout 1
    play ambience ambience_music_club_night fadein 1
    play sound sfx_open_door_1
    scene bg int_library_night with dissolve
    "В библиотеке было тихо и темно."
    "Я огляделся и обнаружил Женю, которая сидела на подоконнике с грустным видом."
    scene bg zhsidit with dissolve
    ya "Ты чего тут одна?"
    mz "Думала тут обо всем, что ты говорил."
    ya "Какие выводы сделала?"
    mz "Не знаю."
    ya "Признайся, тебе просто нравится, что я за тобой всюду бегаю."
    mz "Можешь не бегать."
    ya "Нет, уже не могу."
    mz "Почему?"
    ya "Без тебя не вижу ни в чем смысла."
    mz "Не говори глупости."
    ya "Ты больше боишься того, что придется танцевать на глазах у всего лагеря или дело только во мне?"
    mz "Не знаю."
    ya "Ты прекрасно выглядишь и тебе совершенно нечего стесняться."
    ya "С остальным тоже попробуем как-то разобраться."
    ya "Пойдем, все ждут только нас двоих."

    show black with dissolve
    stop ambience fadeout 1
    $ renpy.pause (1, hard = True)
    play music praznik fadein 2
    scene bg tanetz
    hide black
    with dissolve

    "Дело дошло до танца."
    "Мы оба невероятно смущались."
    "Наши движения казались неуклюжими, но мало кто обращал на это внимание."
    "Я старался не смотреть на остальных, представляя, что мы с Женей тут одни."
    "Помогало слабо, но я сохранял спокойствие."
    ya "Чувствую себя нелепо."
    mz "Я не лучше."
    ya "Постараемся делать вид, что ничего не происходит."
    
    
    $ renpy.pause (5, hard = True)
    show black with dissolve
    $ renpy.pause (1, hard = True)
    play ambience ambience_ext_road_night fadein 1
    stop music fadeout 2
    scene bg ext_square_night_party2
    show zh confused glasses dress close at center
    hide black
    with dissolve

    mz "Это было... Необычно..."
    ya "И не говори."
    mz "Спасибо, что был рядом."
    mz "Тебе точно стоит дать шанс."
    ya "Я счастлив услышать это."
    show zh shy glasses dress close
    mz "Праздник кончился, пора уходить, хотя мне хотелось бы побыть вместе еще."
    ya "И мне. Хоть проводить разрешишь?"
    mz "Пойдем."
    scene bg domzh
    show zh excitement glasses dress close at center
    with dissolve
    mz "Ну вот и все."
    ya "Это был прекрасный день."
    mz "И я с нетерпением буду ждать нового."
    ya "Спокойной ночи, Женя."
    mz "И тебе."
    stop ambience fadeout 1
    play sound sfx_open_door_1
    scene bg dom with dissolve
    "Похоже, сердце юной библиотекарши окончательно растаяло."
    "И это не могло не радовать."
    show blink
    $renpy.pause (2)
    scene black
    jump label_day_6