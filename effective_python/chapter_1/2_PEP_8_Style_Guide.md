https://peps.python.org/pep-0008/

(PEP = Python Enhancement Proposal)

# Whitespace

* Use spaces instead of tabs
* Use four spaces for each level
* Lines should be 79 chars or less
* In a file, functions and classes should be separated by two blank lines.
* In a class, methods should be sparated by one blank line.
* Dictionary: put no whitespace between key and colon
* One and only one space before and after =


# Naming

* Functions, variables, and attributes should be in lowercase_underscore format
* Protected instance attributes should be in _leading_underscore format
* Private instance attributes should be in __double_leading_underscore format
* Classes should be in CapitalizedWord format
* Module-level constants should be in ALL_CAPS
* instance methods should use 'self' as the first parameter
* Class methods should use 'cls' as the name of the first parameter.

# Expressions and Statements
* Use inline negation `if a is not b` rather than `if not a is b`
* Use `if not somelist` to check for empy list
* Use `if somelist` to check for non-empty
* Avoid single line `if`, `for`, and `while`
* Prefer multiline expressions with parens over using the \ line continuation char

# imports
* Always put imports at the top of a file
* Always use absolute names for modules when importing them. `from bar import foo` rather than `import foo`
* Imports should be in the following order: standard lib modules, third-party modules, own modules. Within each of those sections, use alphabetical order.