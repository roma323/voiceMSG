Этот скрипт может с помощью vk api отправлять голосовые сообщения, созданные с помощью модуля gtts 
В файле config.py надо указать login , пароль от своего аккаунта в Вконтакте и язык ru,en,fr и т.д.
Голосовое сообщение можно отослать  группе, беседе , пользователю
1) Чтобы отправить голос. сообщение группе , надо написать знак ^ и далее написать название группы (объязательно надо быть подписанным на группу ) 
    Второй вариант : узнать id группы и добавить знак - перед числом
Пример :
^๖ۣۜХауди ๖ۣۜХо™ - Просто о мире IT!


-84392011


2) Чтобы отправить голос. сообщение  в беседе надо узнать ее id: Допустим есть ссылка https://vk.com/im?sel=c2 . В этой ссылке id беседы будет 2   . Далее надо прибавить к этому числу 2000000000
  Пример: 20000000002
  
  Как вариант написать peer_id
3) Чтобы отправить сообщение человеку надо быть у него в друзьях и знать его имя и фамилию. Надо перед именем написать '/'

Пример :

/Имя Фамилия    или   /Фамилия Имя

  Еще как вариант написать id пользователя




Как это работает?
1) Сначала узнается url куда надо отсылать файл
2) Далее генерируется файл с речью 
3) После этот mp3 отсылается на тот самый url.
4)Далее узнается название документа . 
5) И финалом будет отправка этого документа
Орентировался по этой статье https://habrahabr.ru/post/327280/
