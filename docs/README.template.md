# base-template

Esta es una template para empezar cualquier proyecto.

## Configuración inicial

Cambiar el nombre de este archivo a README.template.md

```bash
mv README.md README.template.md
```

### Iniciamos la app de NodeJS y de Husky e instalamos las extensiones de VSCode

```bash
npm install
npm run prepare
```

- Hay que instalar las siguientes extensiones:

[Conventional Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
[Git-Emoji](https://marketplace.visualstudio.com/items?itemName=git-emoji.vscode-git-emoji)

### Actualizamos package.json

```json
{
  "name": "cambiar-nombre",
  "version": "0.0.1",
  "description": "cambiar descripción"
}
```

## Uso

### Commits:

Para realizar un commit utilizaremos la sección de git del VSCode y en el repositorio utilizado apretaremos el botón de conventional commits que es un circulo. Este nos abrira un menu con un pequeño formulario de con opciones para poder hacer el commit con la convención de manera correcta.

Otra forma es por la terminal ejecutando el comando `npm run commit` que abrira un interfaz en la ter minal para realizar el commit de manera correcta-

### Release

Utilizamos el comando `npm run release` para realizar la creación de una versión y que se actualice la versión del archivo ***"package.json"*** además de la creación del archivo ***"CHAGENLOG.md"*** donde se visualizaran los cambios. Luego de esto también se creara un commit con la convención de commits donde se agregara las tags al repositorio de git.

```bash
npm run release
git push --follow-tags origin main # subir las tags nuevas al repositorio
```