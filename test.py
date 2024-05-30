from zipfile import ZipFile

filename = 'test.kmz'

kmz = ZipFile(filename, 'r')
kml = kmz.open('doc.kml', 'r').read()
print(kml)
