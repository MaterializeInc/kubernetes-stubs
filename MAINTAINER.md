# Maintainer instructions

1. Update the `kubernetes-client-python` submodule if necessary.

2. Do code generation:

   ```
   poetry run python codegen
   ```

3. Format:

   ```
   bin/fmt
   ```

4. Update the version in pyproject.toml and then add and push a corresponding
   tag, if a new release is desired.

   ```
   git commit -a && git tag -a $VERSION -m $VERSION && git push --tags
   ```
