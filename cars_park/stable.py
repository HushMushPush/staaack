# упорядочиваем позиции(от большей к меньшей) машин, скорости располагаем в порядке позиций
# работаем циклом до тех пор пока последняя машинка не доедет до финиша
# на каждой иттерации цикла обновляем все предпологаемые позиции машин (новая позиция это старая позиция + скорость)
# для того чтобы разобратся со слипанием пользуемся стэком: 
# - на стэк кладем машины по старшинству их позиций
# - если стэк пустой машину кладем
# - если предпологаемая позиция очередной машинки(которую мы хотим положить на стэк) больше чем на верху стэка - 'машинки слипаются' -
# чистим данные за слипшимися машинками, берем минимальную из скоростей, убираем данные слипшихся машинок(убираем заднии машины оставляем передюю)

# после того как нашли место слипания 
# проверяем их позиции, старую и новую: 
# - если их старые позиции различаются (<) а новые позиции (>=), кроме того что передняя машинка двигалась - то тогда слипаемся
# проблема:
# - лишних слипаний у таргета когда каждая машинка автопарка слипается с уже приехавшой машинкой, 
# предпологаемое решение:
# - зануление слипшихся машинок для исскринение проблемы с повторным слипанием

class Solution:
    def carFleet(self, target, position, speed): # int List[int] List[int] -> int:
        stick_nums = 0

        for i in range(len(position)):
            min_pos = position.index(min(position[i:]))
            position.insert(0, position.pop(min_pos))
            speed.insert(0, speed.pop(min_pos))

        while position[-1] < target:

            new_position = []
            for i in range(len(position)):
                new_position.append(position[i] + speed[i])
                if new_position[i] >= target:
                    new_position[i] = target


            stack = [[position[0], new_position[0], speed[0]]]
            for i in range(1, len(new_position)):
                if new_position[i] < stack[-1][1]: # и новая позиция ровна нулю
                    stack.append([position[i], new_position[i], speed[i]])
                elif new_position[i] >= stack[-1][1]: # зануляем либо тут 
                    speed[i], new_position[i] = stack[-1][2], stack[-1][1]

                    if position[i] < stack[-1][0] and position[i] != new_position[i] and stack[-1][0] != stack[-1][1]: # зануляем либо тут 
                        stick_nums += 1
                        print(position, new_position, stick_nums, i)
 
            position = new_position

        return len(speed) - stick_nums


abs = Solution()

target=100
position=[0,2,4]
speed=[4,2,1]

# target = 100
# position = [11, 14, 7, 12]
# speed = [3, 2, 4, 1]

# target = 10
# position = [1, 4]
# speed = [3, 2]

# target = 10
# position = [4,1,0,7]
# speed = [2,2,1,1]

print(abs.carFleet(target, position, speed))