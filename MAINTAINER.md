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

4. Update the version in pyproject.toml.

5. Add and push a corresponding tag:

   ```
   git commit -a && git tag -a $VERSION -m $VERSION && git push --tags
   ```
