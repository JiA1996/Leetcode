First put your input file in this directory. Let's say it is "test.txt"

First run 

python frontEnd.py test.txt

This will generate front_clauses.txt and front_out.txt, which are the clauses and the output from front end.
Then run 

python dpll.py

This will generate dpll_out.txt, which is the output from Davis-Putnam.
Finally run 

python backEnd.py

If there is no solution, nothing will be generated and a message will be printed to standard output.
If there is a solution, answer.txt will be generated.