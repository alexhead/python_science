with open('../files/multiplication_table_a.html', 'w') as f:
    f.write('<html>'+'\n'+'<body>'+'\n')
    f.write('<table>'+'\n')
    for i in range(1, 11):
        f.write('<tr>'+'\n')
        for x in range(1, 11):
            y = i*x
            y = str(y)
            f.write('<td>'+'<a href=http://'+y+'.ru>'+y+'</a>'+'</td>'+'\n')
        f.write('</tr>'+'\n')
    f.write('</table>'+'\n')
    f.write('</body>'+'\n'+'</html>')
