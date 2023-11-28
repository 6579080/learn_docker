docker version

//все запущенные  и осттановленые контейнеры
docker ps -a

//просмотреть одразы локально
docker images

//запущеные контейнеры
docker ps

//все локальные img
docker images

//скачивает(если нет ) и запускает контейнер
docker run hello-world

//удалить контейнер
docker rm epic_rubin(names)
docker rm d180ebe454b6(id)
docker rm d180ebe454b6, f0cbf4e596dd (id, id)

//удалить все контейнеры
docker container prune


//удаление образов
docker rmi  d180ebe454b6

//запуск и подключение к shell контейнера
docker run -i -t busybox
docker run -it ubuntu root@d8e1140989525:/#

//показать имя контейнера
hostname

//показать ip адрес контейнера
hostname -i

//запуск контейнера фоном
docker run -d nginx

//остановка контейнера
docker stop 38bf99e5da71
docker kill

//инфа о контейнере
docker container inspect 38bf99e5da71

docker container inspect 38bf99e5da71 | grep IPAddress

