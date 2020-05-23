## Param Cleaner
Program that takes in a file with one URL per line and removes all lines with duplicate parameters
Do note, that these are not considered duplicates and both versions will be in the output:
1. http://example.com?a=1
2. https://example.com?a=1
\

1. http://example.com?a=1&b=2
2. http://example.com?a=1&b=2&c=3


# Usage:
`$ python3 clean.py <filepath>`

# Output:
`$ <original_file_name>_clean<original_file_extenstion>`
