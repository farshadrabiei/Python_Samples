from string import Template


def main():
    print('ok {0}'.format('farshad rabiei'))

    #template by place holder
    templ = Template("Youre watching ${title} by ${author}")

    #جایگزین == substitute
    str2 = templ.substitute(title='book',author='farshad') 

    print(str2)

    #Dictonary استفاده از دیکشنری در تمپلیت

    data = {
            "title":"TV",
            "author" :"Na"
    }
    str3 = templ.substitute(data)
    print(str3)

if __name__ == '__main__':
    main()
    