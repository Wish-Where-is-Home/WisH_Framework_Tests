# WisH - Where is Home 

## Frameworks Tests

### Database

No projeto **Wish** irao ser usadas base dados espaciais uma vez que a aplicacao tem como objectivo a localizacao de pontos de interesse. A base de dados espaciais escolhida foi a **PostGIS** que e uma extensao do **PostgreSQL**. Vamos usar o **pgAdmin** para gerir a base de dados, atraves de uma interface grafica. Utilizaremos ainda o **QGIS** para visualizar a base de dados espaciais.

- [Link para o PostgreSQL](https://www.postgresql.org/)
- [Link para o PostGIS](https://postgis.net/)
- [Link para o pgAdmin](https://www.pgadmin.org/)
- [Link para o QGIS](https://qgis.org/pt_PT/site/)


A base dados ira ser corrida em um ambiente **Docker**. Para isso, vamos usar o **Docker Compose** para criar um ambiente com o **PostGis**, o **pgAdmin** e o **PostgreSQL**.

Em relaçao ao **QGIS**, vamos usar a versao download do site.
- [Link para o QGIS](https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu)


```yml

version: '3.1'

services:
    db:
        image: postgis/postgis:15-3.3
        restart: "no"
        environment:
            POSTGRES_DB: wish
            POSTGRES_USER: test
            POSTGRES_PASSWORD: password
        ports:
            - "5432:5432"
        volumes:
            - ./data:/var/lib/postgresql/data

    pgadmin:
        image: dpage/pgadmin4
        restart: "no"
        environment:
            PGADMIN_DEFAULT_EMAIL: admin@example.com
            PGADMIN_DEFAULT_PASSWORD: password
            PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION: 'True'
        ports:
            - "5050:80"

volumes:
    data:
        name: wish_data

```

Com o ficheiro **docker-compose.yml** criado, vamos correr o ambiente com o seguinte comando:

```bash
docker-compose up -d
```

Aceder ao **pgAdmin** atraves do link [http://localhost:5050](http://localhost:5050) e fazer login com as credenciais:
- **Email**: ``` admin@example.com ```
- **Password**: ``` password ```

Depois de fazer login, clicar em **Add New Server** e preencher os campos com as seguintes credenciais:
- **Host name/address**: ``` db ```
- **Port**: ``` 5432 ```
- **Maintenance database**: ``` wish ```
- **Username**: ``` test ```
- **Password**: ``` password ```

    
Em relacao ao **QGIS**, vamos usar a versao download do site. É necessario criar uma nova ligação a base de dados espaciais. Para isso, clicar em **Add PostGIS Layers** e preencher os campos com as seguintes credenciais:
- **Name**: ``` wish ```
- **Host**: ``` localhost ```
- **Port**: ``` 5432 ```
- **Database**: ``` wish ```
- **Username**: ``` test ```
- **Password**: ``` password ```
- **SSL mode**: ``` disable ```
- **Save username and password**: ``` yes ```


Para conectares ao **PostGis Docker** atraves da linha de comandos, podes usar o seguinte comando:

```bash
docker exec -it wish_framework_tests_db_1 psql -U test -d wish 
```

Para inserir dados na base de dados, podes usar o seguinte comando:

```bash
shp2pgsql -s 4326 ../../Transferências/portugal-latest-free.shp/gis_osm_buildings_a_free_1.shp public.geo_buildings_free | docker exec -i wish_framework_tests_db_1 psql -U test -d wish
```

### API

A API do projeto **Wish** ira ser desenvolvida em **GeoDjango** que e uma extensao do **Django**. Vamos usar o **Django Rest Framework** para criar uma API REST. Vamos usar o **Postman** para testar a API.

- [Link para o Django](https://www.djangoproject.com/)
- [Link para o GeoDjango](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/)
- [Link para o Django Rest Framework](https://www.django-rest-framework.org/)
- [Link para o Postman](https://www.postman.com/)
- [Tutorial para o GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/tutorial/)
- [Tutorial Youtube](https://www.youtube.com/watch?v=L3YoX9wrGDc&list=PL7amXK4vKqATa_KrfQ3_tEF_ywAgAqWeJ&index=2&ab_channel=WanjohiKibui)

Começa por criar um ambiente virtual e instalar os requerimentos do projeto:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Depois de instalar os requerimentos, cria um novo projeto **Django**:

```bash
django-admin startproject wish
```

Depois de criar o projeto, cria uma nova aplicacao **Django**:

```bash
python manage.py startapp api
```

Com o techo de codigo abaixo, lemos todas as tabelas da base de dados e criamos os modelos **Django** automaticamente:
```bash
python manage.py inspectdb > models.py
```


### GeoServer


Pull da imagem do **GeoServer**:

```bash
docker pull docker.osgeo.org/geoserver:2.24.1
```

Correr o **GeoServer**:

```bash
docker run -it -p 8080:8080 \
  --mount src="./data/",target=/opt/geoserver_data/,type=bind \
  docker.osgeo.org/geoserver:2.24.1
```

Aceder ao **GeoServer** atraves do link [http://localhost:8080/geoserver/web](http://localhost:8080/geoserver/web) e fazer login com as credencias por defeito
- **Username**: ``` admin ```
- **Password**: ``` geoserver ```


aceder ao post gis atraves do geoserver:
