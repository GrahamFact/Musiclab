# 🎵 MusicLab  

MusicLab — это REST API для управления базой данных артистов и их информации. Проект построен на **Django REST Framework (DRF)** и поддерживает основные CRUD-операции для работы с музыкальными исполнителями.  

##  Функциональность  
-  **Создание, получение, обновление и удаление** артистов  
-  **API-интерфейс** на основе Django REST Framework  
-  **Гибкая система прав доступа** (можно настраивать доступ к API)  
- **Быстрое развертывание с Docker (по желанию)** (сделаю позже) 

## ️ Установка и запуск  

###  Установка зависимостей  
Убедитесь, что у вас установлен **Python 3.12** и **pip**:  

```sh
git clone https://github.com/GrahamFact/Musiclab.git  
cd Musiclab  
python -m venv venv  
source venv/bin/activate  # Для Windows: venv\Scripts\activate  
pip install -r requirements.txt  
```

### Применение миграций и запуск сервера

```sh 
python manage.py migrate  
python manage.py runserver  
```

