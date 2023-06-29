import subprocess
from time import sleep

repos = [
            ['nibalog', '', 'balogNicholas'],
            # ['elibrowne', 'js-basics', 'browneEli'],
            # ['matthew-erdman', 'first-js', 'erdmanMatthew'],
            # ['anniefanggg', 'javascript_website', 'fangAnnie'],
            # ['daxtongute', 'input-demo', 'gutekunstDax'],
            # ['athenachernandez', 'first-js', 'hernandezAthena'],
            # ['ashirkashyap', 'javascript', 'kashyapAshir'],
            # ['chiarakenagy', 'js2', 'kenagyChiara'],
            # ['willkessler7', 'stringmanipjs', 'kesslerWill'],
            # ['jkorn123', 'justin-korn-q.3-work', 'kornJustin'],
            # ['nicolemen', 'jsexercise', 'menNicole'],
            # ['hewittw', 'js2', 'watkinsHewitt'],
            # ['tastychickenmmm', 'firstjs', 'xuDaniel'],
            # ['shirleytxu', 'jsproject', 'xuShirley'],
            # ['sydneybold', 'javascript-ii', 'boldSidney'],
            # ['anderooc', 'js', 'changAndrew'],
            # ['georgeellis123', 'first-js', 'ellisGeorge'],
            # ['jah05', 'js_2', 'houJames'],
            # ['alexhuynh23', 'javascriptunit', 'huynhAlex'],
            # ['akhaz', 'html-and-js', 'khazeniAiden'],
            # ['willilai', 'javascript2', 'laiWilliam'],
            # ['emma-l810', 'ccsearch', 'liEmma'],
            # ['eddieqiao23', 'surveyjs', 'qiaoEddie'],
            # ['isabelreynoso', 'to-do-list', 'reynosoIsabel'],
            # ['hausen-wu-23', 'jsinput', 'wuHausen'],
            # ['emilyzhu23', 'js-html-hw', 'zhuEmily'],
        ]

for repo in repos:
    argList = ['git', 'clone', 'https://github.com/' + repo[0] + '/' + repo[1] + '.git', repo[2]]
    result = subprocess.run(argList, capture_output = True)
