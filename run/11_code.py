import yaml
from collections import deque

class Monkey( ):

    def __init__( self, data ) -> None:
        self.name = list(data)[0]
        _monkey_data = data[ self.name ]
        self.items = self._parse_starting_items( _monkey_data )
        self.test_func = self._parse_test( _monkey_data )
        self.operation = self._parse_operation( _monkey_data['Operation'])
        self.inspect_count = 0

    def _parse_starting_items( self, monkey_data ):
        try:
            si = monkey_data["Starting items"].split(',')
            si = [ int(s.strip()) for s in si]
        except AttributeError:
            si = [monkey_data["Starting items"]]
        return deque(si)

    def _parse_test( self, monkey_data ):
        div_by = int(monkey_data['Test'].split()[-1])
        t_target = monkey_data['If true'].split()[-2].capitalize() + ' ' + monkey_data['If true'].split()[-1]
        f_target = monkey_data['If false'].split()[-2].capitalize() + ' ' + monkey_data['If false'].split()[-1]

        def test_func( x ):
            if (x % div_by == 0):
                return t_target
            else:
                return f_target
        return test_func

    def _parse_operation( self, operation ):
        
        op = operation.split()
        def make_value( valuestr, x ):
            if valuestr == 'old':
                return x
            return int(valuestr)

        def operation_func( x ):
            
            val2 = make_value( op[2], x )
            val4 = make_value( op[4], x )
            if op[3] == '+':
                return val2 + val4
            if op[3] == '*':
                return val2 * val4

        return operation_func

    def inspect_item( self, item ):
        item_new = self.operation( item ) // 3
        self.inspect_count += 1
        return item_new
    
    def throw_item( self, item, monkeys ):
        """
        monkeys - dict of named monkey instances 
        """
        target = self.test_func( item )
        
        monkeys[target].items.append( item )

        return target

    def take_turn( self, monkeys ):

        while self.items:
            it = self.items.popleft()
            it = self.inspect_item( it )
            self.throw_item( it, monkeys )

def play_round( monkeys ):

    for name in sorted(monkeys):

        monkeys[name].take_turn( monkeys )
    
    return 0

def calc_monkey_business( monkeys ):

    inspections = [ m.inspect_count for _,m in monkeys.items()]
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
    #     print(m.operation(it))
    #     print(m.inspect_item( it ))
    #     print((m.throw_item( it, monkeys )))
    
    # for name in sorted(monkeys):
    #     print(name)
    #     print(monkeys[name].items)

    for i in range(1000):
        # print("==")
        play_round( monkeys )
        
        # for name in sorted(monkeys):
        #     print(name)
        #     print(monkeys[name].items)
    
    calc_monkey_business( monkeys )