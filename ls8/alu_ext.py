from alu import ALU
from typing import Callable


class ALU_EXT(ALU):
    """Extended ALU with more operations"""

    def immediate_operation(self, alu_operation: Callable):
        """
        Build an ALU operation that uses a register and immediate
        and sets the register to the result of the operation
        """

        def operation(register: int, immediate: int):
            reg_value = self.cpu.registers[register]
            self.cpu.registers[register] = alu_operation(reg_value, immediate)

            return 1

        return operation

    def ADDI(self):
        """
        `ADDI registerA immediate`

        Add the value in a registers to an integer and store the
        result in the register.

        Machine code:
        ```byte
        10110000 000000rr iiiiiiii
        B0 0r ii
        ```
        """
        return self.immediate_operation(lambda a, b: a + b)
