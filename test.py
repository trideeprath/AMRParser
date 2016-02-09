import sys
import xml.etree.ElementTree as ET
import re


def main():
    """Main entry point for the script."""
    
    count =0
    amrDictionary= getSentenceAndAMRFromXML()
    
    #Get the words and the indentation
    for sentence, amr in amrDictionary.iteritems():
        
        list = getAllEdgesFromAMR(amr)
        print list
        
        '''
        wordsIndentList = []
        print sentence 
        print amr
        variableMap = {}
        
        for line in solve(amr).splitlines():
            pair = []
            indentCount = len(line) - len(line.lstrip())
            sense = None
            relation = None
            variable = None
            variableValue = None
            #Extracting the word from the line
            if line.find("/")!= -1:
                newLine = line.split("/")[1].strip(")")
                variableLine = line.split("/")[0].strip(")")
                if(variableLine.find("(") != -1):
                    variable = variableLine.split("(")[1].strip()
                line = newLine
                
            elif line.find(":") != -1:
                line = line.split()[1].strip().lstrip()
            
                
            #Removing the sense of the word from the string
            if(bool(re.search('[a-z]', line, re.IGNORECASE)) and bool(re.search('[0-9]', line, re.IGNORECASE)) 
               and not bool(re.search('value', line, re.IGNORECASE)) and not bool(re.search('quant', line, re.IGNORECASE))
                and not bool(re.search('quantity', line, re.IGNORECASE)) ):
                line = line.strip("0123456789")
                line = line.strip("-")
                
            #Removing the wiki/name/op ...
            if ":" in line:
                #print line
                if len(re.findall(r'"([^"]*)"', line))> 0:
                    line = re.findall(r'"([^"]*)"', line)[0]
                    #print line
                
            line = line.strip() 
            line = line.strip(")")
            
            if line in variableMap:
                print ">>>>",  line , variableMap.get(line)
                line = variableMap.get(line)
            #create variable map
            variableMap[variable] = line
            pair = [line,indentCount]
            wordsIndentList.append(pair)
            edges = []
        
        
        print variableMap
        print wordsIndentList
        #Returns all the edges from the List containing word with indentation
        edges = getAllEdges(wordsIndentList)
        print edges
        # To do tommorow fetch the pairs
        print "========================"
    
        '''
       
    pass 

def getAllEdges(list):
    edgeList = []
    for i in range(1, len(list)):
       # print list[i]
        pair = []
        pair = list[i]
        word = pair[0]
        index = pair[1]
        #print (pair[0] , index)
        for j in range(i-1, -1 , -1):
            previous = list[j]
            if(previous[1] < index):
                #print (word, previous[0])
                edgeList.append([word,previous[0]])
                break;
    return edgeList
    pass 


def getAllEdgesFromAMR(amr):
    wordsIndentList = []
    #print amr
    variableMap = {}
    
    for line in solve(amr).splitlines():
        pair = []
        indentCount = len(line) - len(line.lstrip())
        sense = None
        relation = None
        variable = None
        variableValue = None
        #Extracting the word from the line
        if line.find("/")!= -1:
            newLine = line.split("/")[1].strip(")")
            variableLine = line.split("/")[0].strip(")")
            if(variableLine.find("(") != -1):
                variable = variableLine.split("(")[1].strip()
            line = newLine
            
        elif line.find(":") != -1:
            line = line.split()[1].strip().lstrip()
        
            
        #Removing the sense of the word from the string
        if(bool(re.search('[a-z]', line, re.IGNORECASE)) and bool(re.search('[0-9]', line, re.IGNORECASE)) 
           and not bool(re.search('value', line, re.IGNORECASE)) and not bool(re.search('quant', line, re.IGNORECASE))
            and not bool(re.search('quantity', line, re.IGNORECASE)) ):
            line = line.strip("0123456789")
            line = line.strip("-")
            
        #Removing the wiki/name/op ...
        if ":" in line:
            #print line
            if len(re.findall(r'"([^"]*)"', line))> 0:
                line = re.findall(r'"([^"]*)"', line)[0]
                #print line
            
        line = line.strip() 
        line = line.strip(")")
        
        if line in variableMap:
            #print ">>>>",  line , variableMap.get(line)
            line = variableMap.get(line)
        '''create variable map'''
        variableMap[variable] = line
        pair = [line,indentCount]
        wordsIndentList.append(pair)
        edges = []
    
    
    #print variableMap
    #print wordsIndentList
    #Returns all the edges from the List containing word with indentation
    edges = getAllEdges(wordsIndentList)
    #print edges
    # To do tommorow fetch the pairs
    #print "========================"
    return edges
    
    pass

def getSentenceAndAMRFromXML():
    amrDictionary = {}
    
    filename = "/home/trideep/Downloads/amrBankXMLFile.xml"
    tree = ET.parse(filename)
    root = tree.getroot()
    #print root.tag
    
    for amrData in root.findall('sntamr'):
        sentence = amrData.find('sentence').text
        amrGraph = amrData.find('amr').text
        amrDictionary[sentence] = amrGraph
        #print(sentence)
        #print(amrGraph)
        #print("===============")
    
    return amrDictionary


def solve(s):
    """Returns a list of the lines in a sentence"""
    s = s.split('\n', 1)[-1]
    if s.find('\n') == -1:
        return ''
    return s.rsplit('\n', 1)[0]

if __name__ == '__main__':
    sys.exit(main())