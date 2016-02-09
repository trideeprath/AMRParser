# AMRParser 
[AMR Documentation](http://amr.isi.edu/)
Python Script to parse the AMR graph and return the list of all edges. 

####Input is the AMR graph:
(a / and
      :op1 (e / enter-01
            :ARG0 (p / person
                  :ARG0-of (l / light-04
                        :ARG1 (l2 / lamp))
                  :source (a2 / and
                        :op1 (c / country :wiki "China"
                              :name (n2 / name :op1 "China"))
                        :op2 (c2 / country-region :wiki "Siberia"
                              :name (n3 / name :op1 "Siberia"))))
            :time (n / next)
            :purpose (s / step
                  :poss p
                  :part-of (d2 / dance-01)))
      :op2 (w / wave-02
            :ARG1 p
            :ARG2 (b / back
                  :direction (i / into
                        :op1 (w2 / wing)))
            :time (t / then)
            :degree (t2 / too)))

####Output:
[['enter', 'and'], ['person', 'enter'], ['light', 'person'], ['lamp', 'light'], ['and', 'person'], ['China', 'and'], ['China', 'China'], ['Siberia', 'and'], ['Siberia', 'Siberia'], ['next', 'enter'], ['step', 'enter'], ['person', 'step'], ['dance', 'step'], ['wave', 'and'], ['person', 'wave'], ['back', 'wave'], ['into', 'back'], ['wing', 'into'], ['then', 'wave'], ['too', 'wave']]

####Method call eg.
list = getAllEdgesFromAMR(amr)

###Steps
1. Import the python script 
2. Run the method getAllEdgesFromAMR

