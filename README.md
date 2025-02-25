 Essa é uma versão adaptada do projeto, visando a geração de dados para cidades Brasileiras

[Há um notebook para rodar os Scripts no Google Colab](https://colab.research.google.com/gist/mapeadoreslivresufpr/d28aa5a55850ca89c9e2920ded9a755d/las_calles_de_las_mujeres_processing_part1.ipynb) 

-------------------------------------------------------------------------------

# SCRIPTS de generación de datos para #LasCallesDeLasMujeres

Visita la web del proyecto: [#LasCallesDeLasMujeres](https://geochicasosm.github.io/lascallesdelasmujeres/) ( Versión beta ) de [GEOCHICAS](https://geochicas.org/)

## Getting Started

Los datos que se visualizan en el proyecto [#LasCallesDeLasMujeres](https://geochicasosm.github.io/lascallesdelasmujeres/) se generan ejecutando los scripts contenidos en este proyecto. A continuación se detallan las instrucciones para reproducir el proceso y poder generar datos para cualquier ciudad.

### Instalación y preparación de entorno

Para poder decargar el proyecto y ejecutar los scripts, es necesario tener instalado:

- GIT (Descargar [AQUí](https://git-scm.com/downloads))
- Node.js versión >=12 (Descargar [AQUí](https://nodejs.org/download/release/v0.12.0/))

Descargar el proyecto:

```
git clone https://github.com/geochicasosm/data_scripts_lascallesdelasmujeres.git
```

Instalación de paquetes:

```
npm install
```

# Instrucciones

### _Paso 1_

Buscar [AQUÍ](https://www.openstreetmap.org/relation/11) el ID de OSM de la ciudad a tratar.

Crear una carpeta dentro de la carpeta "data" del proyecto, con el nombre de la ciudad a tratar, en minúsculas y sin espacios. Ejemplos:

**barcelona**

**sanjose**

**buenosaires**

### _Paso 2_

Ejecutar:

```
npm run initial-step -- --city=nombreciudad --relation=relationID
```

- Ejemplo: **npm run initial-step -- --area=[2.0875,41.2944,2.2582,41.4574] --city=barcelona --relation=347950**

Se generan los ficheros:

- nombreciudad_streets.geojson
- list.csv
- list_genderize.csv

### _Paso 3_

Aplicar el script que elimina las calles clasificadas como "unknown" (ni de mujer, ni de hombre) y búsqueda de los articulos de Wikipedia para las calles con nombre de mujer:

```
npm run wikipedia-step -- --city=nombreciudad
```

_\*Para deshabilitar el descarte automático de calles "Unknown" usar el flag `--keepUnknown`_

Se genera el fichero 'list_genderize_wikipedia.csv'.

### _Paso 5_

Revisar manualmente el fichero anterior:

- Eliminar calles que no son de persona
- Corregir errores en la clasificación male/female. El factor de fiabilidad es 2,-2 (Mujer,Hombre).
- Corregir y añadir enlaces de Wikipedia (las calles con nombre de hombre no necesitan enlace)

---

#### Criterios para eliminar o mantener calles:

Se _ELIMINA_ si:

- Hace alusión a flora o fauna
- Hace alusión a momentos históricos (La Batalla de Pavón)
- Hace alusión a objetos inanimados (Esmeralda = Buque Argentino)

Se _MANTIENE_ si:

- Lleva el nombre de una santa
- Lleva el nombre de una deidad femenina con representación de mujer (Venus)

---

Guardar el fichero corregido en la misma carpeta del proyecto, con el nombre:

**nombreciudad_finalCSV.csv**

_ATENCIÓN_: Es muy importante que el separador de campos utilizado en el CSV sea el ";", en caso contrario no funcionará.

### _Paso 6_

Ejecutar:

```
npm run final-step -- --city=nombreciudad
```

Se generan tres ficheros:

- **final_tile.geojson** Fichero final que se cargará en el mapa
- **stats.txt** fichero con estadísticas de los datos
- **noLinkList.txt** Fichero con el listado de calles sin artículo en wikipedia

## Para acabar

Haznos llegar los tres ficheros generados y añadiremos tu ciudad al mapa!

---

## Contribuir con el proyecto

Únete a nuestro canal de slack [#lascallesdelasmujeres](https://join.slack.com/t/geochicas-osm/shared_invite/enQtMzIzMzUyMDQyNjczLTU0YjYzNTQ2ZWRkOWQwZGJlNGY4NjhmODY4Y2M2M2Y2MDM3M2EyZTg4NWI0ODY2ZWRhZGIyN2JjMDc0ZDdlODE) si te interesa contribuir.

## Coordinadora Técnica

- **Jessica Sena** (_España_) - [@jsenag](https://jessisena.github.io/myprofile-cra/)
  Ingeniera informática, desarrolladora web/móvil en ámbito geo.

## Licencia

This project is licensed under _CC BY-SA_ License - see the [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) file for details

## Reconocimientos

- [Proyecto](https://blog.mapbox.com/mapping-female-versus-male-street-names-b4654c1e00d5) _Mapping female versus male street names_ de Mapbox por [Aruna Sankaranarayanan](https://www.mapbox.com/about/team/aruna-sankaranarayanan/)

- [Open Street Map](https://www.openstreetmap.org/)

- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page/es)

