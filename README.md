# Семместровый проект
## Описание
Данный проект предсталяет собой систему компьютерного зрения, принимающего изображения и определяющее на нём лица людей их пол, вохраст и настроение, на основе чего воспроизводит
видеоррлик направленный на целевую аудиторию находяющеся в поле зрения камеры.
## Используемые технологии
Язык программирования: Python
Python выбран в качестве языка для написания проекта ввиду его гибкости и наличия полного и разнообразного инструментария для выполнения поставленных задач

Фреймворк: OpenVINO
Проект базируется на фреймворке OpenVINO, ввиду скорости его работы и наличия полного спектар нужных предъобученных модлей 

Основная библиотека: OpenCV
Для работы с изображением используется библиотека OpenCV, так как она предоставляется возможность оптимально работать с изображениям

Используемое ПО: VLC
Данное ПО используется для качесвенного кроссплатформенного приёма и воспроизведения видеопотока


## Запуск и установка
1. Установка и компиляци фреймворка OpenVINO
2. Установка и компиляция OpenCV
3. Установка VLC, нужно указать путь к VLC в файле config
4. Установка библиотек из requirments 


## Примечания
1. В репозитории находиться готовые к вопроизведению видеоролики, если они будут отсутсвовать, система загрузит новые
2. В репозитории находяться предъобученные модели, их можно заменить на любые другие аналогичные, предварительно конвертирвав их под формат OpenVINO
3. Настройки системы производиться в файле Config, там можно настроить различные параметры приёма и обработки видеопотка для оптимизации работы системы
4. В проекте предполагается реализация выбора видеоролика для показа на стороннем сервере, который отправляет ответ ввиде json файла, для простоты работы, в репозитории лежит предзаготовленный ответ
