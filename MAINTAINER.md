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

4. Ignore changes to the submodule:

   ```
   cd kubernetes-client-python && git checkout .
   ```

5. Update the version in pyproject.toml and then add and push a corresponding,
   if a new release is desired.

   ```
   git tag -a $VERSION -m $VERSION && git push --tags
   ```
