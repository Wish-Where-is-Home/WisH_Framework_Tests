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
- **Email**: ``` dmin@example.com ```
- **Password**: ``` password ```

Depois de fazer login, clicar em **Add New Server** e preencher os campos com as seguintes credenciais:
- **Host name/address**: ``` db ```
- **Port**: ``` 5432 ```
- **Maintenance database**: ``` wish ```
- **Username**: ``` test ```
- **Password**: ``` password ```

    
Em relacao ao **QGIS**, vamos usar a versao download do site.
