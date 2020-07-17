# Instructions

## To run site locally

```
npm run setup
npm run local
```

## To build and publish site

1. First confirm the default branch to be `development` (any branch other than `master`) using
```
git branch
```

2. Commit and push the changes to the same
```
git add .
git commit -m 'initial commit'
git push origin development
```

3. Run the following to build the site from local and automagically push the compiled site to `master`
```
npm run publish
```

