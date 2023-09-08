# **Кейс по CV отборочного этапа ML-смены Tinkoff в Сириусе 2023**

В этом Readme приведены те части, которые требовались в кейсе, но в целом удобнее сразу смотреть Jupyter ноутбук.

# **Part 0** **To do List**

1. Hide all installations in setup.sh

2. Add the backbone of the WebUI Stable Diffusion interface to fully automate the code

3. Look for additional methods of image preprocessing, since AUTOMATIC1111 already uses SwinIR -- DONE

4. Add tag clustering -- DONE

5. Try Midjourney to get an alien image -- Non - priority 

6. Add an image difference function to generate a sample of the most diverse offers -- Non - priority

# **Часть 1** **TL;DR**


---

> Определимся с уровнем развития инопланетян. Серфинг интернета, даже с ChatGPT, не дал никаких результатов о вероятном облике неземных существ - даже о ближайшей звёздной системе - Альфа Центавра - практически ничего не известно, не говоря уже о поиске пригодных для развития живых организмов планет. Так что будем считать, что инопланетяне нашли нас первыми, и уровень прогресса (а, соответственно, и интеллект тоже) у них гораздо выше. Именно поэтому все инопланетяне жуткие рационалисты.

 > Теперь представьте, что вам доступны все мыслимые и немыслимые технологии, и вы прибываетне на планету, где люди тратят целые часы, чтобы добраться до работы вместо того, чтобы просто телепортироваться в офис. У них даже крыльев нету! Выглядит серо и скучно. Есть один [персонаж](https://shikimori.me/characters/75-ryuk), который на Земле только и борется со скукой. А ещё он всегда носит с собой **несколько тетрадей** (для контактов, наверное) и очень любит **Apple's**, только настоящие - спелые и сочные. Попробуем сгенерировать инопланетян по его образу и подобию.

> Теперь определимся со вкусами инопланетян. Если для нас фантастикой являются киберпанк (как сценарий обозримого, но всё ещё недостижимого будущего) или, скажем, космические полеты с околосветовой скоростью, то для инопланетян настоящей фантастикой является магия. Ну а где можно найти магии больше, чем во вселенной Гарри Поттера? Хотя оригиналу Дж. К . Роулинг они явно предпочтут фанфик Э. Юдковского "Гарри Поттер и методы рационального мышления". Чего только стоит эксперимент с маховиком времени! Инопланетянам **карманные часы** будут явно интересны. Из всех факультетов Слизерин интересен им более всего - для Когтеврана знаний им хватает с лихвой, а храбрость гриффиндорцев и честность пуффендуйцев идут вразрез с неумолимым инопланетным рационализмом. А вот хитрость и находчивость - игры разума как раз под стать инопланетянам. Да и комнаты Слизерина имеют особенный **интерьер** - расположены они **в подземельях**, а не в башнях, как другие факультеты.

 > С обстановкой разобрались, теперь перейдем к действиям - без дела инопланетянам будет совсем скучно. А где не скучно? Правильно! - на празднике. И так совпало что Хогвартс на **Хэллоуин** выглядит просто великолепно!

# **Часть 2** **Изучение датасета**

---



## Тематика и проблематика (feat. ChatGPT)

---

**Image captioning** - это технология, целью которой является описание содержимого изображения в виде текстовой подписи. Технология сочетает методы CV с NLP для анализа визуальных особенностей и создания связного и описательного предложения, которое отражает суть изображения.


---


Image captioning имеет целый **ряд практических применений**. Вот несколько причин, по которым подписи к изображениям являются ценными:

 > 1. **Доступность**: Субтитры к изображениям делают визуальный контент более доступным для людей с нарушениями зрения или тех, кто полагается на программы для чтения с экрана. Предоставляя текстовые описания изображений, люди, которые не могут воспринимать визуальный контент, все равно могут его понимать и взаимодействовать с ним.

 > 2. **Понимание содержания**: Подписи предоставляют дополнительный контекст, детали и информацию об объектах, действиях и сценах, запечатленных на изображении. Это может помочь в лучшем понимании, особенно когда изображение сложное или неоднозначное.

 > 3. **Поиск и извлечение изображений**: Подписи к изображениям обеспечивают лучшую индексацию и удобство поиска. Связывая релевантные и описательные подписи с изображениями, становится проще осуществлять поиск конкретного визуального контента на основе текстовых запросов. Это выгодно таким приложениям, завязанным на управление контентом.

 > 4. **Организация контента и обобщение**: Подписи могут поддерживать организацию контента и обобщение в различных доменах. Их можно использовать для автоматического создания резюме или выделения ключевых аспектов изображений в галереях, новостных статьях, образовательных материалах или публикациях в социальных сетях.

 > 5. **Социальные сети и вовлечение пользователей**: Релевантные хэштеги играют решающую роль в повышении вовлеченности пользователей на платформах социальных сетей. Они придают изображениям дополнительный контекст или элементы повествования, делая их более привлекательными, доступными для обмена и информативными.

 > 6. **Машинное обучение**: Создание подписей к изображениям - это шаг к преодолению разрыва между CV и NLP. Обучая модели генерировать подписи, мы получаем представление о том, как понимать и представлять визуальную информацию в лингвистической форме. Вот тут лучше оставить [ссылку](https://arxiv.org/pdf/2103.00020.pdf) на колоссальную статью про CLIP.


---
**Постановка задачи** Image captioning

1. **Извлечение объектов изображения**:
- Используйте сверточную нейронную сеть (CNN) для извлечения визуальных признаков из входного изображения. CNN обычно состоит из нескольких сверточных слоев, за которыми следуют объединенные слои для получения иерархических визуальных представлений.
- Выходные данные CNN представляют собой вектор признаков, который представляет высокоуровневую визуальную информацию изображения. Давайте обозначим этот вектор признаков как V.

2. **Создание языка**:
- Используйте модель на основе трансформера для генерации тегов. Эта модель принимает вектор объектов V в качестве входных данных и генерирует заголовок слово за словом.
- На каждом временном шаге t модель предсказывает распределение вероятностей по словарному запасу, из которого отбирается следующее слово в заголовке.
- Модель обучается с использованием последовательности парных выборок (изображение, подпись), где особенности изображения служат исходными данными для модели генерации языка.
- Обозначим заголовок на временном шаге t как C_t, а условную вероятность следующего слова с учетом предыдущих слов и особенностей изображения как P(C_t+1 | V, C_1, C_2, ..., C_t).

3. **Цель обучения**:
- Цель обучения состоит в том, чтобы максимально увеличить вероятность создания правильных подписей на основе входных изображений.
- Обычно это формулируется как минимизация потери кросс-энтропии между предсказанными подписями и основными истинными подписями в обучающем наборе данных.


## **Обзор датасета**

1. Изображения представляют собой различные помещения отелей с разных углов. На некоторых фото много объектов, на некоторых - почти нет. 

2. Классы несбалансированны - ни по отелям, ни по гостиничным сетям.

3. Размер фотографий - примерно 250х350. Разрешение очень низкое и видны артефакты.

# **Часть 3** **Обогащение датасета описаниями**

1. В качестве предобработки используем SwinIR-Large - он из коробки и хорошо работает. 

Upd. В AUTOMATIC1111 встроен SwinIR, так что изображения там предобрабатываются, даже автоматически.

2. Тегов много по сравнению с необработанными изображениями. Много тегов конкретных объектов + теги стилистики интерьера. В целом достаточно информативные кейворды, насколько хорошо получится генерировать подходящие инопланетянам изображения, если добавить интересующие их теги, посмотрим далее.

3. В случае небольшой выборки непохожих фотографий число кластеров получается равно числу классов(отелей). Однако:

> 1. На выборке размера 10 даже критерий независимости не проверишь (там через критерий Пирсона сложной гипотезы требуется не менее 50 объектов), так что о том, принимается ли гипотеза на всей тренировочной выборке, ничего сказать нельзя.

> 2. Выборка была из максимально разных фотографий, может если взять все фотографии из одного отеля, то и кластер получится единственный.

> 3. Отдельные теги кластеризуются лучше, и для них число классов отличается.

# **Часть 4** **Diffusion Filters**

1. Colab не справляется с AUTOMATIC1111, которая работает лучше, чем StableDiffusionMagic, так что пробуем вторую.

2. Результаты так себе. Пришось ставить локальный AUTOMATIC1111 и сверх него [Inpaint Anything](https://github.com/Uminosachi/sd-webui-inpaint-anything). Там много возможностей для работы с масками в режиме Inpaint - и вот тогда изображения преображаются как нужно.

# **Выводы**

1. Полностью автоматизировать процесс от загрузки датасета до выгрузки измененных изображений не получилось.

2. Diffusion Filters требуют deep dive на локалке, если не хочется вручную возиться с масками, хотя с ними добавление тегов довольно точно (хоть и не без артефактов) меняет картинку в желаемую сторону. Во всяком случае если в каждую маску прописать запрос по отдельному объекту то получется именно то, что мы и хотели.