from die import Die
import pygal

#创建一个D6
die=Die()

#掷几次骰子，并将结果保存在一个列表中
results = []
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

# print(results)

#计算点数出现的频率
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

print(frequencies)

#对结果进行可视化
hist=pygal.Bar()

hist.title = "Result of rolling one D6 to 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


