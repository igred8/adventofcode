import yaml
from collections import deque


### Part 2 unsolved.........


class Monkey( ):

    def __init__( self, data ) -> None:
        self.name = list(data)[0]
        # self.div_by = 1
        _monkey_data = data[ self.name ]
        self.items = self._parse_starting_items( _monkey_data )
        # self.oper = _monkey_data['Operation'].split()[3]
        self.operation_test = self._parse_operation_test( _monkey_data)
        self.inspect_count = 0

    def _parse_starting_items( self, monkey_data ):
        try:
            si = monkey_data["Starting items"].split(',')
            si = [ [int(s.strip()), 0] for s in si]
        except AttributeError:
            si = [[monkey_data["Starting items"], 0]]
        return deque(si)

    def _parse_operation_test( self, monkey_data ):
        
        div_by = int(monkey_data['Test'].split()[-1])
        t_target = monkey_data['If true'].split()[-2].capitalize() + ' ' + monkey_data['If true'].split()[-1]
        f_target = monkey_data['If false'].split()[-2].capitalize() + ' ' + monkey_data['If false'].split()[-1]

        def test( it, c, n, op ):
            if op == '+':
                x = (it%div_by) + (c*n)%div_by
            elif op == '*':
                x = (it%div_by) * (c**n)%div_by
            
            if (x % div_by == 0):
                return t_target
            else:
                return f_target
        
        op = monkey_data['Operation'].split()
        
        def make_value( valuestr, x ):
            if valuestr == 'old':
                return x
            return int(valuestr)

        def operation_test_func( item ):
            x, num_of_inspect = item
            val2 = make_value( op[2], x )
            val4 = make_value( op[4], x )
            
            target = test( val2, val4, num_of_inspect, op[3])
            item[1] = num_of_inspect + 1
            
            return target

        return operation_test_func
    
    def throw_item( self, item, monkeys ):
        """
        monkeys - dict of named monkey instances 
        """
        target = self.operation_test( item )
        # item_new = item_new // 3
        self.inspect_count += 1
        monkeys[target].items.append( item )

        return target

    def take_turn( self, monkeys ):

        while self.items:
            it = self.items.popleft()
            
            self.throw_item( it, monkeys )

def play_round( monkeys ):

    for name in sorted(monkeys):
        
        # print(f"{name}: {monkeys[name].items}")

        monkeys[name].take_turn( monkeys )
        
    
    return 0

def calc_monkey_business( monkeys ):

    inspections = [ m.inspect_count for _,m in monkeys.items()]
    print(inspections)
    inspections.sort()
    print(inspections[-2]*inspections[-1])

if __name__ == "__main__":
    # filename = "E:/Dropbox/py_projects/adventofcode/inputs/11_input.yaml"
    filename = "E:/Dropbox/py_projects/adventofcode/inputs/11.1_input.yaml"
    
    monkeys = {}

    with open(filename) as file:
        for mdata in yaml.safe_load_all( file ):
            name = list(mdata)[0]

            # print(mdata[name])

            monkeys[name] = Monkey(mdata)

    # for name in sorted(monkeys):
    # for name in list((monkeys)):
        # print(name)

    # it = 7
    # for name, m in monkeys.items():
    #     print(m.name)
    #     print(m.operation_test(it))
    #     # print(m.inspect_item( it ))
    #     print((m.throw_item( it, monkeys )))
    
    # for name in sorted(monkeys):
    #     print(name)
    #     print(monkeys[name].items)

    for i in range(20):
        play_round( monkeys )
        
        # print("==")
        # for name in sorted(monkeys):
        #     print(name)
        #     print(monkeys[name].items)
    
    calc_monkey_business( monkeys )