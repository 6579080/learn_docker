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

//подключиться к процесу в контейнере
docker run -d ngnix
docker exec -it 38bf99e5da71 bash

//запуск контейнера с указанием своего имени
docker run -d --name my_nginx nginx

//открыть порт  8080 - внешний : 80 - внутренний
docker run -d -p 8080:80 nginx

http://localhost:8080/

//меппинг томовdo
docker run -v ${PWD}:/usr/share/nginx/html nginx

 docker run -v ${PWD}:/usr/share/nginx/html -d -p 8080:80 nginx
 docker run -v .:/usr/share/nginx/html -d -p 8080:80 nginx
docker run -v C:\Users\Ulad\WebstormProjects\learn_docker\docker\nginx:/usr/share/nginx/html -d -p 8081:80 nginx

docker run -v C:\Users\Ulad\WebstormProjects\learn_docker\docker\nginx:/usr/share/nginx/html -d -p 8081:80 nginx
docker run -v /usr/share/html:/usr/share/nginx/html -d -p 80:80 nginx

docker exec -it 042ae930914e bash
ls -la
cat index.html

//удаление контейнера после завершения
docker run -it --rm busybox


"docker run \
--name my_nginx \
-v .:/usr/share/nginx/html \
-p 8080:80 \
-d \
--rm \
nginx"


//попасть в контейнер если он запущен
docker exec -it 042ae930914e sh


docker run -it --name my-node-app my-node








