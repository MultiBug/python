```rootsql
61.1 Анализатор текста
# На примере тестового проекта рассмотрим программу, 
которая анализирует некоторый файл и определяет какой процент текста приходится на каждый символ.
В этом разделе показано, как файл может быть открыт и прочитан.
```
```rootsql
61.2 Анализатор текста
# В этой части программы определяется функция, которая подсчитывает, сколько раз символ встречается в строке.
# В качестве аргументов этой функции присвоены текст файла и один символ; функция затем возвращает число упоминаний символа в тексте.
Теперь мы можем использовать ее для нашего файла.
# Символ "r" встречается в файле 83 раза
```
```rootsql
61.3 Анализатор текста
# Следующая часть программы находит какой процент текста приходится на каждый из символов алфавита.
# Давайте соберем все фрагменты вместе и запустим программу:
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
```
