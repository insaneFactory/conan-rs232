Issues:
- The library uses file scope variables (e.g. `Cport`, `error`). Those do make problems in shared objects (*.so) on linux.
  Fix: Make them `static`.
  Fix: Use other names and maybe a "Context" struct instead of global variables.
