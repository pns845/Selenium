"""
absolute and relative xpath
absolute-->starts from the parent
relative->xpath is relative
/ looks at the immediate child
// looks for all the nested children
syntax for xpath
//tag[@attribute='value']
//tag[contains(attribute,'value')]
//div[@id='blocks']//a[contains(text(),'Enroll now')]
//div[@id='blocks']//a[starts-with(@class,'btn-primary')]
//a[@href='/pages/practice']
//a[contains(@href,'practice')]
parent
xpathtosomeelemet//parent::<tag>
preceding sibling
xpathto somelemet//preceding sibling::<tag>
following sibling
xpathtosomelement//following sibling::<tag>
//a[@href='/sign_in']//parent::li//following-sibling::li//preceding-sibling::li[2]
"""
