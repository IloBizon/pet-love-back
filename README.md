Установите MongoDB и mongosh

https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

https://www.mongodb.com/docs/mongodb-shell/install/  

Используйте строку mongodb://localhost:27017 для подключения  

Выполните команды 
mongosh //открытие mongosh

use main //Создание бд main

db.createCollection("products") //Создание коллекции products

Создайте файл .env:
MONGODB_URL=mongodb://localhost:27017/products

Установите зависимости из requirements.txt

запустите файл main.py


