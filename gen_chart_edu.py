#!/usr/bin/env python
# -*- coding: utf-8 -*-

import array
import sys
import csv
#   We using python2.7

#   DECORATOR FOR THE MAIN 
def printHTMLHead(original_function):
    def new_function():
        print '\n'.join([
            '<head>',
            '   <title>Chemestry charts</title>',
            '   <script src=\".\\Chart.bundle.min.js\"></script>',
            '   <script src=\".\\chartjs-plugin-datalabels\"></script>',
            '   <script src=\".\\jquery.min.js\"></script>',
            '   <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">',
            '   <style type="text/css">',
            '       #canvas1 {',
            '           height: 400px;',
            '           width: 800px;',
            '       }',
            '       #canvas2 {',
            '           height: 800px;',
            '           width: 800px;',
            '       }',
            '       #canvas3 {',
            '           height: 400px;',
            '           width: 800px;',
            '       }',
            '   </style>',
            '</head>',
            '<body>',
            '   <div id="canvas1"><canvas id="chart1" width="800" height="400"></canvas></div>',
            '   <div id="canvas2"><canvas id="chart2" width="800" height="700"></canvas></div>',
            '   <div id="canvas3"><canvas id="chart3" width="800" height="400"></canvas></div>',
            '   <script>',

        ])

        original_function()

        
        print '\n'.join([
            '   </script>',
            '</body>'
        ])
    return new_function

# GLOBAL VARIABLES / RESULTS
chart1_labels = ["0 - 10", "11 - 20", "21 - 30", "31 - 40", "41 - 50", "51 - 60", "61 - 70", "71 - 80", "81 - 90", "91 - 100"]
chart1_results = array.array('i',(0 for i in range(0,len(chart1_labels))))
chart1_colors = [ 
        '\'rgba(255, 99, 132, 0.6)\'',
        '\'rgba(54, 162, 235, 0.6)\'',
        '\'rgba(255, 206, 86, 0.6)\'',
        '\'rgba(75, 192, 192, 0.6)\'',
        '\'rgba(153, 102, 255, 0.6)\'',
        '\'rgba(255, 159, 64, 0.6)\'',
        '\'rgba(255, 99, 132, 0.6)\'',
        '\'rgba(54, 162, 235, 0.6)\'',
        '\'rgba(255, 206, 86, 0.6)\'',
        '\'rgba(75, 192, 192, 0.6)\'',
]

chart2_labels = ["ЭЛИСТА", "Городовиковский район", "Кетченеровская район", "Лаганский район", "Малодербетовский район", "Октябрьский район", "Приютненский район", "Сарпинский район", "Целинный район", "Черноземельский район", "Юстинский район", "Яшалтинский район", "Яшкульский район", "Ики-Бурульский район"]
chart2_ou_names = ["Elista", "Gorodov", "Ketch", "Lagan", "Derbet", "Oktyabr", "Priut", "Sarpin", "Celin", "Chernoz", "Yustin", "Yashalta", "Yashkul", "IkiBurul"]
chart2_results_bal = array.array('i',(0 for i in range(0,len(chart2_labels))))
chart2_results_count = array.array('i',(0 for i in range(0,len(chart2_labels))))
chart2_results = array.array('f',(0 for i in range(0,len(chart2_labels))))
chart2_colors = [ 
        '\'rgba(255, 99, 132, 0.6)\'',
        '\'rgba(54, 162, 235, 0.6)\'',
        '\'rgba(255, 206, 86, 0.6)\'',
        '\'rgba(75, 192, 192, 0.6)\'',
        '\'rgba(153, 102, 255, 0.6)\'',
        '\'rgba(255, 159, 64, 0.6)\'',
        '\'rgba(255, 99, 132, 0.6)\'',
        '\'rgba(54, 162, 235, 0.6)\'',
        '\'rgba(255, 206, 86, 0.6)\'',
        '\'rgba(75, 192, 192, 0.6)\'',
        '\'rgba(123, 99, 132, 0.6)\'',
        '\'rgba(156, 162, 235, 0.6)\'',
        '\'rgba(178, 206, 86, 0.6)\'',
        '\'rgba(234, 192, 192, 0.6)\''
]

chart3_labels = ["Задание 1", "Задание 2", "Задание 3", "Задание 4", "Задание 5", "Задание 6"]
chart3_score_0 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_score_1 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_score_2 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_score_3 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_score_4 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_score_5 = array.array('i', (0 for i in range(0, len(chart3_labels))))
chart3_max_score = 6 # Cause + score 0 also 
chart3_colors = [ 
        '\"rgba(255, 99, 132, 0.6)\"',
        '\"rgba(54, 162, 235, 0.6)\"',
        '\"rgba(255, 206, 86, 0.6)\"',
        '\"rgba(75, 192, 192, 0.6)\"',
        '\"rgba(153, 102, 255, 0.6)\"',
        '\"rgba(255, 159, 64, 0.6)\"'
]

# CALCULATIONS
def calculation(file_obj, ou_file_obj):
    reader = csv.DictReader(file_obj, fieldnames=['OU', 'Kratkiy_otver', 'Razvernutiy_otvet', 'Pervichniy_bal', 'Bal'], delimiter=';')
    ou_reader = csv.DictReader(ou_file_obj, delimiter=';')
    
    calculation_for_chart1(reader, file_obj)
    calculation_for_chart2(reader, ou_reader, file_obj, ou_file_obj)
    calculation_for_chart3(reader, file_obj)

# CALCULATION CHART 1 
def calculation_for_chart1(csv_reader, f_obj):
    f_obj.seek(0)
    for line in csv_reader:
        bal = int(line["Bal"])
        if bal >= 0 and bal <= 10: 
            chart1_results[0] += 1
        if bal > 10 and bal <= 20: 
            chart1_results[1] += 1
        if bal > 20 and bal <= 30: 
            chart1_results[2] += 1
        if bal > 30 and bal <= 40: 
            chart1_results[3] += 1
        if bal > 40 and bal <= 50: 
            chart1_results[4] += 1
        if bal > 50 and bal <= 60: 
            chart1_results[5] += 1
        if bal > 60 and bal <= 70: 
            chart1_results[6] += 1
        if bal > 70 and bal <= 80: 
            chart1_results[7] += 1
        if bal > 80 and bal <= 90: 
            chart1_results[8] += 1
        if bal > 90 and bal <= 100: 
            chart1_results[9] += 1

# CALCULATION CHART 2
def calculation_for_chart2(csv_reader, ou_reader, f_obj, ou_obj):
    for i in range(len(chart2_ou_names)):
        calculation_for_chart2_ou_count(csv_reader, ou_reader, f_obj, ou_obj, i)
        chart2_results[i] = float(chart2_results_bal[i]) / chart2_results_count[i]

def calculation_for_chart2_ou_count(csv_reader, ou_reader, f_obj, ou_obj, ou_index):
    f_obj.seek(0)
    for line in csv_reader:
        f_ou = line["OU"]
        ou_obj.seek(0)
        for ou_line in ou_reader:
            ou = ou_line[chart2_ou_names[ou_index]]
            if len(ou) == 6:
                if f_ou == ou: 
                    chart2_results_bal[ou_index] += int(line["Bal"])
                    chart2_results_count[ou_index] += 1
        
# CALCULATION CHART 3
def calculation_for_chart3(csv_reader, f_obj):
    f_obj.seek(0)
    for line in csv_reader:
        razvernutiy_otvet = line["Razvernutiy_otvet"]
        chart3_score_0[int(razvernutiy_otvet[0])] += 1
        chart3_score_1[int(razvernutiy_otvet[4])] += 1
        chart3_score_2[int(razvernutiy_otvet[8])] += 1
        chart3_score_3[int(razvernutiy_otvet[12])] += 1
        chart3_score_4[int(razvernutiy_otvet[16])] += 1
        chart3_score_5[int(razvernutiy_otvet[20])] += 1

# DRAW RESULTS
def draw():
    draw_chart1()
    draw_chart2()
    draw_chart3()

def draw_chart1():
    print '\n'.join([
        '       var popCanvas1 =  document.getElementById("chart1").getContext("2d");',
        '       var barChart1 = new Chart(popCanvas1, {',
        '           type: \'bar\',',
        '           data: {'
    ])
    sys.stdout.write("               labels: [ \"")
    sys.stdout.write(chart1_labels[0])
    sys.stdout.write("\"")
    for string in chart1_labels[1:]:
        sys.stdout.write(", \"")
        sys.stdout.write(string)
        sys.stdout.write("\"")
    sys.stdout.write(" ],\n")

    print '\n'.join([
        '               datasets: [{'
    ])
    
    sys.stdout.write("                   data: [")
    sys.stdout.write(str(chart1_results[0]))
    for num in chart1_results[1:]:
        sys.stdout.write(", ")
        sys.stdout.write(str(num))
    sys.stdout.write("],\n")

    
    sys.stdout.write("                   backgroundColor: [")
    sys.stdout.write(str(chart1_colors[0]))
    for color in chart1_colors[1:]:
        sys.stdout.write(", ")
        sys.stdout.write(color)
    sys.stdout.write("],\n")

    print '\n'.join([
        '               }]',
        '           },',
        '           options: {',
        '               title: {',
        '                   display: true,',
        '                   text: \'Распределение участников по баллам.\'',
        '               },',
        '               legend: {',
        '                   display: false',
        '               },',
        '               scales: {',
        '                   yAxes: [{',
        '                       ticks: {',
        '                           beginAtZero: true',
        '                       }',
        '                   }]',
        '               },',
        '               plugins: {',
        '                   datalabels: {',
        '                       anchor: "end",',
        '                       formatter: function(value, context) {',
        '                           return context.chart.data[context.dataIndex];',
        '                       }',
        '                   }',
        '               },',
        '           }',
        '       });'
    ])
    
def draw_chart2():
    print '\n'.join([
        '       var popCanvas2 =  document.getElementById("chart2").getContext("2d");',
        '       var barChart2 = new Chart(popCanvas2, {',
        '           type: \'horizontalBar\',',
        '           data: {'
    ])
    sys.stdout.write("               labels: [ \"")
    sys.stdout.write(chart2_labels[0])
    sys.stdout.write("\"")
    for string in chart2_labels[1:]:
        sys.stdout.write(", \"")
        sys.stdout.write(string)
        sys.stdout.write("\"")
    sys.stdout.write(" ],\n")

    print '\n'.join([
        '               datasets: [{'
    ])
    
    sys.stdout.write("                   data: [")
    sys.stdout.write("%.1f" % chart2_results[0])
    for num in chart2_results[1:]:
        sys.stdout.write(", ")
        sys.stdout.write("%.1f" % num)
    sys.stdout.write("],\n")

    sys.stdout.write("                   backgroundColor: [")
    sys.stdout.write(str(chart2_colors[0]))
    for color in chart2_colors[1:]:
        sys.stdout.write(", ")
        sys.stdout.write(color)
    sys.stdout.write("],\n")

    print '\n'.join([
        '               }]',
        '           },',
        '           options: {',
        '               title: {',
        '                   display: true,',
        '                   text: \'Распределение баллов по районам.\'',
        '               },',
        '               legend: {',
        '                   display: false',
        '               },',
        '               scales: {',
        '                   yAxes: [{',
        '                       ticks: {',
        '                           beginAtZero: true',
        '                       }',
        '                   }]',
        '               },',
        '               plugins: {',
        '                   datalabels: {',
        '                       anchor: "end",',
        '                       formatter: function(value, context) {',
        '                           return context.chart.data[context.dataIndex];',
        '                       }',
        '                   }',
        '               },',
        '           }',
        '       });'
    ])

def draw_chart3():
    print '\n'.join([
        '       var popCanvas3 =  document.getElementById("chart3").getContext("2d");',
        '       var barChart3 = new Chart(popCanvas3, {',
        '           type: \'bar\',',
        '           data: {'
    ])
    sys.stdout.write("               labels: [ \"")
    sys.stdout.write(chart3_labels[0])
    sys.stdout.write("\"")
    for string in chart3_labels[1:]:
        sys.stdout.write(", \"")
        sys.stdout.write(string)
        sys.stdout.write("\"")
    sys.stdout.write(" ],\n")

    print '\n'.join([
        '               datasets: [',
    ])
    for i in range(0, chart3_max_score):
        sys.stdout.write("                   {\n")

        sys.stdout.write("                       label: \"")
        sys.stdout.write(str(i))
        sys.stdout.write(" балл")
        if i == 0 or i == 5:
            sys.stdout.write("ов")
        if i >= 2 and i <= 4:
            sys.stdout.write("а")
        sys.stdout.write("\",\n")
        
        sys.stdout.write("                       backgroundColor: ")
        sys.stdout.write(chart3_colors[i])
        sys.stdout.write(",\n")
        sys.stdout.write("                       data: [")
        sys.stdout.write(str(chart3_score_0[i]))
        sys.stdout.write(", ")
        sys.stdout.write(str(chart3_score_1[i]))
        sys.stdout.write(", ")
        sys.stdout.write(str(chart3_score_2[i]))
        sys.stdout.write(", ")
        sys.stdout.write(str(chart3_score_3[i]))
        sys.stdout.write(", ")
        sys.stdout.write(str(chart3_score_4[i]))
        sys.stdout.write(", ")
        sys.stdout.write(str(chart3_score_5[i]))
        sys.stdout.write("]\n")
        sys.stdout.write("                   },\n")

    print("               ],")

    print '\n'.join([
        '           },',
        '           options: {',
        '               title: {',
        '                   display: true,',
        '                   text: \'Распределение баллов по участникам.\'',
        '               },',
        '               legend: {',
        '                   display: true',
        '               },',
        '               scales: {',
        '                   yAxes: [{',
        '                       ticks: {',
        '                           beginAtZero: true',
        '                       }',
        '                   }]',
        '               },',
        '               plugins: {',
        '                   datalabels: {',
        '                       anchor: "end",',
        '                       formatter: function(value, context) {',
        '                           return context.chart.data[context.dataIndex];',
        '                       }',
        '                   }',
        '               },',
        '           }',
        '       });'
    ])
    
@printHTMLHead
def main():
    draw()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f_obj:
            with open("Spravochnik_OU_RK.csv", "r") as ou_f_obj:
                calculation(f_obj, ou_f_obj)
    else: 
        print("- No csv file presented!")
        exit()
    main()
