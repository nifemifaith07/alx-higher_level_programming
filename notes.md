<strong> LINE CONTINUATION IN PYTHON</strong>
<details>
  <summary><i><b>PEP8's E128: continuation line under-indented for visual indent?</b></i></summary>
<b>Two ways to continue lines with opening parenthesis

e.g

urlpatterns = patterns(' ', url(r'^$', listing, name='investment-listing')
print('\n'.join([" ".join(["{:d}".format(item) for item in row]) for row in matrix])) too long right?
1. indenting to the opening bracket
- print('\n'.join([" ".join(["{:d}".format(item)\
  _____________________for item in row]) for row in matrix]))
2. no arguments on starting line, then indenting to a uniform level(if no other opening parethesis is present before breaking))
- urlpatterns = patterns(\
    _____' ',\
    _____url(r'^$', listing, name='investment-listing')\
 OR(if other parenthesis are opened before breaking follow rule 1 with rule 2)
 
print(\
___'\n'.join([" ".join(["{:d}".format(item)[normal indentation of 4 spaces here]\
___________for item in row]) for row in matrix]))[indent o parenthesis)</b>\
Note: backslash \ can also be used for line breaks or continuation
</details>
