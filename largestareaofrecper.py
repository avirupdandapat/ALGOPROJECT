class Solution():

    def solve(self, array):

        if not array:
            return 0

        no_row = len(array)
        no_column = len(array[0])

        new_array = []
        max_area = None
        for row_index, value_1 in enumerate(array):

            new_array.append([])
            for column_index, value_2 in enumerate(array[row_index]):

                if row_index == 0:
                    new_array[row_index].append(value_2)

                elif value_2 == 0:
                    new_array[row_index].append(0)

                else:
                    new_array[row_index].append(value_2 + new_array[row_index - 1][column_index])

        for row_index, value_1 in enumerate(new_array):

            new_array[row_index].sort(reverse=True)

            for column_index, value_2 in enumerate(new_array[row_index]):

                if value_2 == 0:
                    break

                else:
                    if value_2 * (column_index + 1) > max_area:
                        max_area = value_2 * (column_index + 1)

        return max_area
