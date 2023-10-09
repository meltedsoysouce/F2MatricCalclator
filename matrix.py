import pandas as pd
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class F2Matrix:
    """
    F2空間内の行列

    Parameters
    ---
    - content : pandas.core.DataFrame : 行列本体
    """
    content: pd.DataFrame

    @staticmethod
    def __int_to_binary(binary_list: list[bool]) -> int:
        """
        list[bool]から二進数に変換する

        Parameters
        ---
        - binary_list : list[bool] : 二進数化対象のboolのリスト

        Returns
        ---
        - int : 二進数に変換した結果
        """
        binary_str = ''.join(str(bit) for bit in binary_list)
        binary_int = int(binary_str, 2)
        return binary_int

    def __mul__(self, other: 'F2Matrix') -> 'F2Matrix':
        """
        F2Matrix*F2Matrixの定義
        行と列を取り出して、ビットandを取ったのち、1である桁の数を計上している。

        Parameters
        ---
        - other : F2Matrix : オペレーターの右側にあるF2Matrix

        Returns
        ---
        - F2Matrix : 積
        """
        row_num, _ = self.content.shape
        _, col_num = other.content.shape
        result = pd.DataFrame(np.zeros((row_num, col_num)))
        for i in range(row_num):
            row = F2Matrix.__int_to_binary(self.content.astype(int).iloc[i])
            for j in range(col_num):
                col = F2Matrix.__int_to_binary(other.content.astype(int)[f'{j}'])
                calc_result = bin(row&col).count('1') % 2
                result.iloc[i, j] = calc_result
        
        return result
