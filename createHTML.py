import xml.etree.ElementTree as ET
def main():
    tree=ET.parse('PrettyPeopleList.xml')
    root=tree.getroot()
    people = [{'firstName':person.find('FirstName').text,'lastName':person.find('LastName').text,'job':person.find('Job').text,'path':person.find('Path').text} for person in root]
    
    s=""
    s+="<!DOCTYPE html>\n<html>\n<body>\n"
    for i in range(len(people)):
        colNum=i%3
        assert colNum in [0,1,2]
        person=people[i]
        personName = person['firstName']+" "+person['lastName']
        innerString="\t\t\t\t<img src=\""+person['path']+"\" style=\"width: 200px; height: 200px;\" />\n\t\t\t\t<p />\n\t\t\t\t<p>"+personName+"</p>\n\t\t\t\t<p>"+person['job']+"</p>\n"
        if colNum==0:
            s+="\t<div class=\"row\">\n\t\t<div class=\"col-md-12\">\n\t\t\t<div style=\"float: left; width: 33%;\">\n"
        elif colNum==1:
            s+="\t\t\t<div style=\"float: right; width: 33%;\">\n"
        else:
            s+="\t\t\t<div style=\"display: inline-block; width: 33%;\">\n"
        s+=innerString
        s+="\t\t\t</div>\n"
        if colNum==2 or i==len(people)-1:
            s+="\t\t</div>\n\t</div>\n</body>\n</html>\n"
    file=open("htmlPeople.html","w")
    file.write(s)
    file.close()
    
main()