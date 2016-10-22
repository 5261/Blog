# Blog

A Blog made by myself for practicing my coding skills.

It's built by Python, using Django.

The theme is modeled after [Concise](https://github.com/huangjunhui/concise).

## Run
It can run in local, starting by following commands:

```bash
sh ./Profile
```

It is running on `http://0.0.0.0:8000` by default.

Visit the site to preview it.

By now, you can only change the runnning port by modifying the `Procfile`.

## Generate
We can generate static site of the Blog, which can be shown in `Github Pages`

```bash
cd ./static-generator
sh ./generate.sh
```
The result will be in `public` folder.

Tips: Run server before generating.

## Deploy
Make a git repository in `public` folder before first deploying, like this:

```bash
cd ./static-generator/public
git init
git remote add origin "https://github.com/USERNAME/USERNAME.github.io"
```

After it, you can just run following commands to deploy site to `Github Pages`.
```bash
sh ./deploy
```

Tips: Generate it before deploying

## Footer
However, it's not a perfect Blog Manager.

It is mainly used by myself.
