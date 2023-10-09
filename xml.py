import xml.etree.ElementTree as ET
data = '''
<person1>

<name>ahmed</name>

<email>ahmed@gmail.com</email>
<phone>02837744</phone>

<birthday>23/02/2003</birthday>
<country>egypt</country>


</person1>


'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text   )
print('Email:',tree.find('email').text   )
print('Phone',tree.find('phone').text   )
print('Birthday',tree.find('birthday').text   )
print('Country',tree.find('country').text   )