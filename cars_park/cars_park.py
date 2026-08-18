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
        n = 0

        for i in range(len(position)):

            min_pos = position.index(min(position[i:]))
            position.insert(0, position.pop(min_pos))
            speed.insert(0, speed.pop(min_pos))

        print('start pos', position)
        print('start speed', speed)
        while position[-1] < target:

            new_position = []
            for i in range(len(position)):
                new_position.append(position[i] + speed[i])
                if new_position[i] >= target:
                     new_position[i] = target

            # проверка на ноль машинок
            
            while new_position[n] == 0 and speed[n] == 0 and n < len(position)-1:
                #print(n, new_position[n], speed[n])
                n += 1
                

            stack = [[position[n], new_position[n], speed[n], n]]
            print(new_position)
            for i in range(n, len(new_position)):
                if new_position[i] < stack[-1][1] and new_position[i] != 0 and speed[i] != 0: # и новая позиция ровна нулю
                    stack.append([position[i], new_position[i], speed[i], i]) # проверка на ноль машинок
                elif new_position[i] >= stack[-1][1]: # зануляем либо тут 
                    if position[i] < stack[-1][0] and position[i] != new_position[i] and stack[-1][0] != stack[-1][1] and stack[-1][1] <= target: # зануляем либо тут 
                        stick_nums += 1
                        new_position[stack[-1][3]], speed[stack[-1][3]] = 0, 0
                        stack.append([position[i], new_position[i], speed[i], i])
                        print(i)
                    speed[i], new_position[i] = stack[-1][2], stack[-1][1]
            print(new_position)
            position = new_position

        return len(speed) - stick_nums


abs = Solution()

# target=10
# position=[8,3,7,4,6,5]
# speed=[4,4,4,4,4,4]

# target=100
# position=[45,43,32,25,3]
# speed=[1,2,4,6,7]

# target=12
# position=[10,8,0,5,3]
# speed=[2,4,1,1,3]

# target=100
# position=[3, 2, 0]
# speed=[1, 2, 3]

# target=100
# position=[0,2,4]
# speed=[4,2,1]

# target = 100
# position = [11, 14, 7, 12]
# speed = [3, 2, 4, 1]

# target = 10
# position = [1, 4]
# speed = [3, 2]

# target = 10
# position = [4,1,0,7]
# speed = [2,2,1,1]

# target=13
# position=[10,2,5,7,4,6,11]
# speed=[7,5,10,5,9,4,1]

target=21
position=[1,15,6,8,18,14,16,2,19,17,3,20,5]
speed=[8,5,5,7,10,10,7,9,3,4,4,10,2] 

print(abs.carFleet(target, position, speed))