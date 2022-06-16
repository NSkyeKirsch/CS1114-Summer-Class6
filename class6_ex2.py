# Flow of Control for Try-Except

"""

1. Control enters a try-suite (block)

2. if an error occurs within the try, stop executing the try-suite at the point where the error occurred and
abandon the rest of the suite. (Unexcused lines of try-suite are ignored)

3. Raise the exception (automatically)

4. Look for an except-suite that can handle the exception (matches the types or is a related type (OOP))

5. If the except-suite matches a raised error types, move control to the beginning of the matching except-suite.
Once the suite is done, move control to after try-except and continue the normal python execution

6. If an error is raised and no except-suite matches the error type, Python handles it (prints error, stops program)

7. If no error occurs in the try-suite, the suite finishes, the except suites are skipped and python continues with
normal execution after the try-except construct

"""

# Exception Else and Finally

"""

- else - a suite of statements that follow try-except that is ONLY executed if the try-suite does not encounter an error

- finally - a suite of statements that follow the try-except (and else) that run no matter whether an error occurred or
not. This is the place where code that absolutely must be executed can go. File closings may be good to put here

"""

