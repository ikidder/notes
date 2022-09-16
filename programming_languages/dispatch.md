# Dispatch
Dispatch is the process of selecting which implementation of a polymorphic operation (method or function) to call.

## Static vs Dynamic 
* Static dispatch means that the selection is made at compile time.
* Dynamic means that the selection is made at runtime.

## Single vs Multiple
* Single dispatch means that the selection is made based on a single object. `dividend.divide(divisor)` -> here, the selection is made based on the type of `dividend`. Think of it as sending a message called `divide` with param `divisor` to `dividend`. C++, Java, Swift, Javascript, and Python are all single dispatch.
* Multiple dispatch means that the selection is made based on the combination of operands. In the above example, the types of `dividend` and `divisor` together determine which `divide` operation will be called. Common LISP, and Julia are multiple dispatch languages.